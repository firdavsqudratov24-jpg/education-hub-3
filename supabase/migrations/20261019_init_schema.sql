-- ====================================================================
-- Education Hub 2.0 - Complete Supabase PostgreSQL Schema & RLS Policies
-- Tables: 16 core tables with indexes, foreign keys, triggers, and RLS
-- ====================================================================

-- 1. Create Enums
CREATE TYPE user_role_type AS ENUM ('student', 'university_student', 'teacher', 'admin');
CREATE TYPE material_difficulty AS ENUM ('Boshlang''ich', 'O''rta', 'Murakkab');
CREATE TYPE material_status AS ENUM ('draft', 'pending', 'published', 'rejected');

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. Profiles Table (linked to Supabase auth.users)
CREATE TABLE IF NOT EXISTS profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    avatar_url TEXT,
    bio TEXT,
    role user_role_type DEFAULT 'student',
    grade_or_course TEXT,
    xp_points INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    streak_days INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. User Roles Table (Role-based access control)
CREATE TABLE IF NOT EXISTS user_roles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    role user_role_type NOT NULL,
    granted_at TIMESTAMPTZ DEFAULT NOW(),
    granted_by UUID REFERENCES profiles(id),
    UNIQUE(user_id, role)
);

-- 4. Subjects Table
CREATE TABLE IF NOT EXISTS subjects (
    id TEXT PRIMARY KEY,
    slug TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    grade_range TEXT NOT NULL,
    description TEXT,
    icon TEXT,
    color TEXT,
    total_materials INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Materials Table (Core content: 200+ detailed materials)
CREATE TABLE IF NOT EXISTS materials (
    id TEXT PRIMARY KEY,
    slug TEXT UNIQUE NOT NULL,
    subject_id TEXT NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    author_id UUID REFERENCES profiles(id) ON DELETE SET NULL,
    title TEXT NOT NULL,
    grade_level TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    objective TEXT NOT NULL,
    theory TEXT NOT NULL,
    examples JSONB NOT NULL DEFAULT '[]'::jsonb,
    exercise TEXT NOT NULL,
    exercise_solution TEXT NOT NULL,
    check_questions JSONB NOT NULL DEFAULT '[]'::jsonb,
    tags JSONB NOT NULL DEFAULT '[]'::jsonb,
    duration_minutes INTEGER NOT NULL DEFAULT 30,
    status material_status DEFAULT 'published',
    views INTEGER DEFAULT 0,
    likes INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 6. Courses Table
CREATE TABLE IF NOT EXISTS courses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    slug TEXT UNIQUE NOT NULL,
    subject_id TEXT NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    instructor_id UUID REFERENCES profiles(id) ON DELETE SET NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    level TEXT NOT NULL,
    thumbnail TEXT,
    duration_hours NUMERIC(5, 1) DEFAULT 10.0,
    is_published BOOLEAN DEFAULT TRUE,
    enrolled_count INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 7. Lessons Table
CREATE TABLE IF NOT EXISTS lessons (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    material_id TEXT REFERENCES materials(id) ON DELETE SET NULL,
    title TEXT NOT NULL,
    order_num INTEGER NOT NULL,
    video_url TEXT,
    duration_minutes INTEGER DEFAULT 20,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 8. Enrollments Table
CREATE TABLE IF NOT EXISTS enrollments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    progress_percentage INTEGER DEFAULT 0,
    enrolled_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    UNIQUE(user_id, course_id)
);

-- 9. Quizzes Table (Interactive testing center)
CREATE TABLE IF NOT EXISTS quizzes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    subject_id TEXT NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    material_id TEXT REFERENCES materials(id) ON DELETE SET NULL,
    title TEXT NOT NULL,
    description TEXT,
    time_limit_minutes INTEGER DEFAULT 15,
    passing_score INTEGER DEFAULT 60,
    xp_reward INTEGER DEFAULT 50,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 10. Questions Table
CREATE TABLE IF NOT EXISTS questions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    quiz_id UUID NOT NULL REFERENCES quizzes(id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    options JSONB NOT NULL,
    correct_option_index INTEGER NOT NULL,
    explanation TEXT,
    points INTEGER DEFAULT 10,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 11. Quiz Attempts Table
CREATE TABLE IF NOT EXISTS quiz_attempts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    quiz_id UUID NOT NULL REFERENCES quizzes(id) ON DELETE CASCADE,
    score INTEGER NOT NULL,
    max_score INTEGER NOT NULL,
    percentage INTEGER NOT NULL,
    passed BOOLEAN NOT NULL,
    answers JSONB NOT NULL,
    started_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ DEFAULT NOW()
);

-- 12. Material Progress Table
CREATE TABLE IF NOT EXISTS material_progress (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    material_id TEXT NOT NULL REFERENCES materials(id) ON DELETE CASCADE,
    is_completed BOOLEAN DEFAULT TRUE,
    completed_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, material_id)
);

-- 13. Bookmarks Table
CREATE TABLE IF NOT EXISTS bookmarks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    material_id TEXT NOT NULL REFERENCES materials(id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, material_id)
);

-- 14. Achievements Table
CREATE TABLE IF NOT EXISTS achievements (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    icon TEXT NOT NULL,
    xp_reward INTEGER NOT NULL,
    category TEXT NOT NULL
);

-- 15. User Achievements Table
CREATE TABLE IF NOT EXISTS user_achievements (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    achievement_id TEXT NOT NULL REFERENCES achievements(id) ON DELETE CASCADE,
    unlocked_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, achievement_id)
);

-- 16. Notifications Table
CREATE TABLE IF NOT EXISTS notifications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    type TEXT DEFAULT 'info',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 17. Audit Logs Table
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES profiles(id) ON DELETE SET NULL,
    action TEXT NOT NULL,
    entity TEXT NOT NULL,
    entity_id TEXT,
    details JSONB,
    ip_address TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ====================================================================
-- INDEXES FOR PERFORMANCE
-- ====================================================================
CREATE INDEX IF NOT EXISTS idx_materials_subject ON materials(subject_id);
CREATE INDEX IF NOT EXISTS idx_materials_status ON materials(status);
CREATE INDEX IF NOT EXISTS idx_materials_slug ON materials(slug);
CREATE INDEX IF NOT EXISTS idx_materials_difficulty ON materials(difficulty);
CREATE INDEX IF NOT EXISTS idx_quiz_attempts_user ON quiz_attempts(user_id);
CREATE INDEX IF NOT EXISTS idx_material_progress_user ON material_progress(user_id);
CREATE INDEX IF NOT EXISTS idx_bookmarks_user ON bookmarks(user_id);
CREATE INDEX IF NOT EXISTS idx_notifications_user ON notifications(user_id, is_read);
CREATE INDEX IF NOT EXISTS idx_audit_logs_user ON audit_logs(user_id);

-- ====================================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- ====================================================================

ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_roles ENABLE ROW LEVEL SECURITY;
ALTER TABLE subjects ENABLE ROW LEVEL SECURITY;
ALTER TABLE materials ENABLE ROW LEVEL SECURITY;
ALTER TABLE courses ENABLE ROW LEVEL SECURITY;
ALTER TABLE lessons ENABLE ROW LEVEL SECURITY;
ALTER TABLE enrollments ENABLE ROW LEVEL SECURITY;
ALTER TABLE quizzes ENABLE ROW LEVEL SECURITY;
ALTER TABLE questions ENABLE ROW LEVEL SECURITY;
ALTER TABLE quiz_attempts ENABLE ROW LEVEL SECURITY;
ALTER TABLE material_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE bookmarks ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_achievements ENABLE ROW LEVEL SECURITY;
ALTER TABLE notifications ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_logs ENABLE ROW LEVEL SECURITY;

-- Helper function: is admin?
CREATE OR REPLACE FUNCTION is_admin(user_id UUID) 
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM profiles 
        WHERE id = user_id AND role = 'admin'
    );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Profiles: Public read, self-update only
CREATE POLICY "Public profiles are viewable by everyone" ON profiles FOR SELECT USING (true);
CREATE POLICY "Users can update own profile" ON profiles FOR UPDATE USING (auth.uid() = id);

-- Subjects & Materials: Public read for published
CREATE POLICY "Public subjects viewable by everyone" ON subjects FOR SELECT USING (true);
CREATE POLICY "Admin can modify subjects" ON subjects FOR ALL USING (is_admin(auth.uid()));

CREATE POLICY "Published materials are viewable by everyone" ON materials FOR SELECT USING (status = 'published' OR auth.uid() = author_id OR is_admin(auth.uid()));
CREATE POLICY "Teachers can create materials" ON materials FOR INSERT WITH CHECK (auth.uid() = author_id);
CREATE POLICY "Authors or admins can update materials" ON materials FOR UPDATE USING (auth.uid() = author_id OR is_admin(auth.uid()));
CREATE POLICY "Admins can delete materials" ON materials FOR DELETE USING (is_admin(auth.uid()));

-- Quizzes: Public read for active
CREATE POLICY "Quizzes are viewable by everyone" ON quizzes FOR SELECT USING (is_active = true OR is_admin(auth.uid()));
CREATE POLICY "Questions viewable by everyone" ON questions FOR SELECT USING (true);

-- Quiz Attempts: Users view own attempts
CREATE POLICY "Users can view own quiz attempts" ON quiz_attempts FOR SELECT USING (auth.uid() = user_id OR is_admin(auth.uid()));
CREATE POLICY "Users can insert own quiz attempts" ON quiz_attempts FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Material Progress & Bookmarks: Self only
CREATE POLICY "Users can view own progress" ON material_progress FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own progress" ON material_progress FOR ALL USING (auth.uid() = user_id);

CREATE POLICY "Users can view own bookmarks" ON bookmarks FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can manage own bookmarks" ON bookmarks FOR ALL USING (auth.uid() = user_id);

-- Notifications: Self only
CREATE POLICY "Users can view own notifications" ON notifications FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can update own notifications" ON notifications FOR UPDATE USING (auth.uid() = user_id);

-- Audit logs: Admin only
CREATE POLICY "Only admins can view audit logs" ON audit_logs FOR SELECT USING (is_admin(auth.uid()));

-- ====================================================================
-- SEED INITIAL ACHIEVEMENTS
-- ====================================================================
INSERT INTO achievements (id, title, description, icon, xp_reward, category) VALUES
('first-lesson', 'Birinchi qadam', 'Ilk ta''limiy materialni to''liq o''rgandingiz', 'BookOpen', 50, 'learning'),
('quiz-master', 'Bilimdon sinovchi', 'Testdan 100% natija qayd etdingiz', 'Trophy', 100, 'quiz'),
('streak-3', 'Sabrli o''rganuvchi', 'Ketma-ket 3 kun tizimda dars qildingiz', 'Flame', 75, 'streak'),
('math-pro', 'Matematik daho', 'Matematika bo''yicha 5 ta darsni yakunladingiz', 'Calculator', 150, 'subject'),
('polyglot', 'Xorijiy tillar ustasi', 'Ingliz yoki boshqa xorijiy tildan 5 ta dars o''tdingiz', 'Languages', 150, 'subject'),
('cyber-coder', 'Kelajak dasturchisi', 'Dasturlash va IT bo''yicha testlarni a''lo topshirdingiz', 'Code2', 200, 'tech')
ON CONFLICT (id) DO NOTHING;
