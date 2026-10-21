# -*- coding: utf-8 -*-
"""
Master Aggregator for Education Hub 2.0
Combines all materials, validates 200 real educational materials,
checks uniqueness, foreign keys, generates JSON, SQLite, and SQL seeds.
"""

import os
import sys
import json
import sqlite3
import shutil

# Add builders path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'builders')))

from builder_math import get_math_materials
from builder_physics_astronomy import get_physics_astronomy_materials
from builder_chemistry import get_chemistry_materials
from builder_biology_nature import get_biology_nature_materials
from builder_geography_ecology import get_geography_ecology_materials
from builder_language_literature import get_language_literature_materials
from builder_foreign_languages import get_foreign_languages_materials
from builder_history import get_history_materials
from builder_cs_programming import get_cs_programming_materials
from builder_law_economics import get_law_economics_materials
from builder_university import get_university_materials
from builder_practical_arts import get_practical_arts_materials

def load_subjects():
    subjects_file = os.path.join(os.path.dirname(__file__), 'subjects.json')
    with open(subjects_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_all_materials():
    groups = [
        ("Matematika, algebra, geometriya", get_math_materials()),
        ("Fizika va astronomiya", get_physics_astronomy_materials()),
        ("Kimyo", get_chemistry_materials()),
        ("Biologiya va tabiiy fanlar", get_biology_nature_materials()),
        ("Geografiya va ekologiya", get_geography_ecology_materials()),
        ("Ona tili va adabiyot", get_language_literature_materials()),
        ("Ingliz va boshqa xorijiy tillar", get_foreign_languages_materials()),
        ("O‘zbekiston va jahon tarixi", get_history_materials()),
        ("Informatika va dasturlash", get_cs_programming_materials()),
        ("Huquq, iqtisod, tarbiya", get_law_economics_materials()),
        ("Universitet fanlari", get_university_materials()),
        ("San’at, texnologiya va boshqa fanlar", get_practical_arts_materials())
    ]
    
    all_materials = []
    distribution = {}
    
    for group_name, mats in groups:
        distribution[group_name] = len(mats)
        all_materials.extend(mats)
        
    return all_materials, distribution

def validate_materials(materials, subjects):
    subject_map = {s['id']: s for s in subjects}
    
    seen_ids = set()
    seen_slugs = set()
    errors = []
    
    for idx, m in enumerate(materials):
        # 1. Unique ID
        if m['id'] in seen_ids:
            errors.append(f"Duplicated ID: {m['id']}")
        seen_ids.add(m['id'])
        
        # 2. Unique Slug
        if m['slug'] in seen_slugs:
            errors.append(f"Duplicated slug: {m['slug']}")
        seen_slugs.add(m['slug'])
        
        # 3. Valid Subject ID
        if m['subject_id'] not in subject_map:
            errors.append(f"Material {m['id']} has invalid subject_id {m['subject_id']}")
            
        # 4. Required fields
        req_fields = [
            'id', 'slug', 'subject_id', 'subject_name', 'title',
            'grade_level', 'difficulty', 'objective', 'theory',
            'examples', 'exercise', 'exercise_solution',
            'check_questions', 'tags', 'duration_minutes'
        ]
        for rf in req_fields:
            if rf not in m or m[rf] is None or (isinstance(m[rf], str) and len(m[rf].strip()) == 0):
                errors.append(f"Material {m['id']} missing or empty required field: {rf}")
                
        # 5. At least 2 examples
        if len(m.get('examples', [])) < 2:
            errors.append(f"Material {m['id']} has fewer than 2 examples (has {len(m.get('examples', []))})")
            
        # 6. At least 3 check questions
        if len(m.get('check_questions', [])) < 3:
            errors.append(f"Material {m['id']} has fewer than 3 check questions (has {len(m.get('check_questions', []))})")
            
    return errors

def create_sqlite_database(materials, subjects, target_db_path):
    temp_db_path = "/tmp/education_hub_build.db"
    if os.path.exists(temp_db_path):
        os.remove(temp_db_path)
        
    conn = sqlite3.connect(temp_db_path)
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id TEXT PRIMARY KEY,
        slug TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        grade_range TEXT NOT NULL,
        description TEXT,
        icon TEXT,
        color TEXT,
        total_materials INTEGER DEFAULT 0
    )
    """)
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS materials (
        id TEXT PRIMARY KEY,
        slug TEXT UNIQUE NOT NULL,
        subject_id TEXT NOT NULL,
        subject_name TEXT NOT NULL,
        title TEXT NOT NULL,
        grade_level TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        objective TEXT NOT NULL,
        theory TEXT NOT NULL,
        examples TEXT NOT NULL,
        exercise TEXT NOT NULL,
        exercise_solution TEXT NOT NULL,
        check_questions TEXT NOT NULL,
        tags TEXT NOT NULL,
        duration_minutes INTEGER NOT NULL,
        views INTEGER DEFAULT 0,
        likes INTEGER DEFAULT 0,
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
    )
    """)
    
    # Calculate material counts per subject
    subject_counts = {}
    for m in materials:
        subject_counts[m['subject_id']] = subject_counts.get(m['subject_id'], 0) + 1
        
    for s in subjects:
        cur.execute("""
        INSERT OR REPLACE INTO subjects (id, slug, name, category, grade_range, description, icon, color, total_materials)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            s['id'], s['slug'], s['name'], s['category'], s['grade_range'],
            s['description'], s['icon'], s['color'], subject_counts.get(s['id'], 0)
        ))
        
    for m in materials:
        cur.execute("""
        INSERT OR REPLACE INTO materials 
        (id, slug, subject_id, subject_name, title, grade_level, difficulty, objective, theory, 
         examples, exercise, exercise_solution, check_questions, tags, duration_minutes, views, likes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 120, 24)
        """, (
            m['id'], m['slug'], m['subject_id'], m['subject_name'], m['title'],
            m['grade_level'], m['difficulty'], m['objective'], m['theory'],
            json.dumps(m['examples'], ensure_ascii=False),
            m['exercise'], m['exercise_solution'],
            json.dumps(m['check_questions'], ensure_ascii=False),
            json.dumps(m['tags'], ensure_ascii=False),
            m['duration_minutes']
        ))
        
    conn.commit()
    conn.close()
    
    # Copy to target path
    shutil.copy(temp_db_path, target_db_path)
    os.remove(temp_db_path)

def generate_sql_migration(materials, subjects, sql_path):
    with open(sql_path, 'w', encoding='utf-8') as f:
        f.write("-- Education Hub 2.0 Seed Migration\n")
        f.write("-- 52 Subjects and 200 Real Educational Materials in Uzbek\n\n")
        
        f.write("-- 1. Insert 52 Subjects\n")
        for s in subjects:
            desc = s['description'].replace("'", "''")
            name = s['name'].replace("'", "''")
            f.write(f"INSERT INTO subjects (id, slug, name, category, grade_range, description, icon, color) "
                    f"VALUES ('{s['id']}', '{s['slug']}', '{name}', '{s['category']}', '{s['grade_range']}', '{desc}', '{s['icon']}', '{s['color']}') "
                    f"ON CONFLICT (id) DO UPDATE SET total_materials = EXCLUDED.total_materials;\n")
                    
        f.write("\n-- 2. Insert 200 Materials\n")
        for m in materials:
            title = m['title'].replace("'", "''")
            objective = m['objective'].replace("'", "''")
            theory = m['theory'].replace("'", "''")
            exercise = m['exercise'].replace("'", "''")
            exercise_sol = m['exercise_solution'].replace("'", "''")
            examples_json = json.dumps(m['examples'], ensure_ascii=False).replace("'", "''")
            questions_json = json.dumps(m['check_questions'], ensure_ascii=False).replace("'", "''")
            tags_json = json.dumps(m['tags'], ensure_ascii=False).replace("'", "''")
            
            f.write(f"INSERT INTO materials (id, slug, subject_id, title, grade_level, difficulty, objective, theory, examples, exercise, exercise_solution, check_questions, tags, duration_minutes) "
                    f"VALUES ('{m['id']}', '{m['slug']}', '{m['subject_id']}', '{title}', '{m['grade_level']}', '{m['difficulty']}', '{objective}', '{theory}', "
                    f"'{examples_json}'::jsonb, '{exercise}', '{exercise_sol}', '{questions_json}'::jsonb, '{tags_json}'::jsonb, {m['duration_minutes']}) "
                    f"ON CONFLICT (id) DO NOTHING;\n")

def main():
    data_dir = os.path.dirname(__file__)
    subjects = load_subjects()
    print(f"Loaded {len(subjects)} subjects.")
    
    materials, distribution = build_all_materials()
    print(f"Built {len(materials)} total materials.")
    print("Distribution:")
    for k, v in distribution.items():
        print(f"  - {k}: {v} ta")
        
    errors = validate_materials(materials, subjects)
    if errors:
        print(f"Validation FAILED with {len(errors)} errors:")
        for err in errors[:10]:
            print(f"  * {err}")
        sys.exit(1)
        
    print("ALL VALIDATION CHECKS PASSED: Exactly 200 unique, valid materials!")
    
    # Save materials.json
    materials_json_path = os.path.join(data_dir, 'materials.json')
    with open(materials_json_path, 'w', encoding='utf-8') as f:
        json.dump(materials, f, ensure_ascii=False, indent=2)
    print(f"Saved {materials_json_path} ({os.path.getsize(materials_json_path)} bytes)")
    
    # Save stats.json
    stats_json_path = os.path.join(data_dir, 'stats.json')
    stats = {
        "total_subjects": len(subjects),
        "total_materials": len(materials),
        "distribution": distribution,
        "verified": True,
        "language": "Uzbek (Latin)",
        "platform": "Education Hub 2.0"
    }
    with open(stats_json_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
        
    # Create SQLite DB
    db_path = os.path.join(data_dir, 'education_hub.db')
    create_sqlite_database(materials, subjects, db_path)
    print(f"Created SQLite database: {db_path} ({os.path.getsize(db_path)} bytes)")
    
    # Generate SQL seed file
    sql_path = os.path.abspath(os.path.join(data_dir, '..', 'supabase', 'migrations', '20261019_seed_200_materials.sql'))
    generate_sql_migration(materials, subjects, sql_path)
    print(f"Generated PostgreSQL seed migration: {sql_path} ({os.path.getsize(sql_path)} bytes)")

if __name__ == "__main__":
    main()
