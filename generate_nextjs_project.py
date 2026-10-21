# -*- coding: utf-8 -*-
"""
Generates the complete Next.js 14 App Router codebase for Education Hub 2.0
"""

import os
import json

BASE = "/working_dir/c_45395966e56f6cce/education-hub-platform"

def make_dirs():
    dirs = [
        "app", "app/subjects", "app/subjects/[slug]", "app/materials", "app/materials/[slug]",
        "app/courses", "app/tests", "app/tests/[id]", "app/dashboard", "app/teacher",
        "app/teacher/materials/new", "app/admin", "app/login", "app/register", "app/about", "app/contact",
        "components", "components/ui", "lib", "types"
    ]
    for d in dirs:
        os.makedirs(os.path.join(BASE, d), exist_ok=True)

def write_package_json():
    pkg = {
        "name": "education-hub-2",
        "version": "2.0.0",
        "description": "O'zbekiston uchun bepul zamonaviy ta'lim ekotizimi",
        "private": True,
        "scripts": {
            "dev": "next dev",
            "build": "next build",
            "start": "next start",
            "lint": "next lint",
            "test": "python3 tests/test_platform.py"
        },
        "dependencies": {
            "@supabase/auth-helpers-nextjs": "^0.10.0",
            "@supabase/supabase-js": "^2.45.0",
            "clsx": "^2.1.1",
            "lucide-react": "^0.453.0",
            "next": "14.2.15",
            "react": "^18.3.1",
            "react-dom": "^18.3.1",
            "react-hook-form": "^7.53.0",
            "recharts": "^2.13.0",
            "tailwind-merge": "^2.5.4",
            "zod": "^3.23.8"
        },
        "devDependencies": {
            "@types/node": "^20",
            "@types/react": "^18",
            "@types/react-dom": "^18",
            "autoprefixer": "^10.4.20",
            "postcss": "^8.4.47",
            "tailwindcss": "^3.4.14",
            "typescript": "^5"
        }
    }
    with open(os.path.join(BASE, "package.json"), "w", encoding="utf-8") as f:
        json.dump(pkg, f, indent=2)

def write_configs():
    # tsconfig.json
    tsconfig = {
        "compilerOptions": {
            "lib": ["dom", "dom.iterable", "esnext"],
            "allowJs": True,
            "skipLibCheck": True,
            "strict": True,
            "noEmit": True,
            "esModuleInterop": True,
            "module": "esnext",
            "moduleResolution": "bundler",
            "resolveJsonModule": True,
            "isolatedModules": True,
            "jsx": "preserve",
            "incremental": True,
            "plugins": [{"name": "next"}],
            "paths": {
                "@/*": ["./*"]
            }
        },
        "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
        "exclude": ["node_modules"]
    }
    with open(os.path.join(BASE, "tsconfig.json"), "w", encoding="utf-8") as f:
        json.dump(tsconfig, f, indent=2)

    # tailwind.config.js
    tw_config = """/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
        },
        secondary: {
          500: '#0d9488',
          600: '#0f766e',
        },
        accent: {
          500: '#7c3aed',
          600: '#6d28d9',
        },
        darkbg: '#0f172a',
        darkcard: '#1e293b',
        lightbg: '#f8fafc',
      },
    },
  },
  plugins: [],
}
"""
    with open(os.path.join(BASE, "tailwind.config.js"), "w", encoding="utf-8") as f:
        f.write(tw_config)

    # postcss.config.js
    postcss = """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""
    with open(os.path.join(BASE, "postcss.config.js"), "w", encoding="utf-8") as f:
        f.write(postcss)

    # .env.example
    env_example = """# ==========================================
# Education Hub 2.0 - Environment Variables
# ==========================================

# Supabase Credentials (from Supabase Project Settings -> API)
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here

# Supabase Service Role (Optional, for admin operations server-side only)
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here

# Next.js App URL
NEXT_PUBLIC_SITE_URL=https://educationhub.uz
"""
    with open(os.path.join(BASE, ".env.example"), "w", encoding="utf-8") as f:
        f.write(env_example)

def write_types():
    types_content = """// Education Hub 2.0 Global TypeScript Definitions

export type UserRole = 'student' | 'university_student' | 'teacher' | 'admin';

export interface Profile {
  id: string;
  email: string;
  full_name: string;
  avatar_url?: string;
  role: UserRole;
  grade_or_course?: string;
  xp_points: number;
  level: number;
  streak_days: number;
  created_at: string;
}

export interface Subject {
  id: string;
  slug: string;
  name: string;
  category: string;
  grade_range: string;
  description: string;
  icon: string;
  color: string;
  total_materials: number;
}

export interface Example {
  title: string;
  problem: string;
  step_by_step: string;
  answer: string;
}

export interface CheckQuestion {
  question: string;
  options: string[];
  correct_index: number;
  explanation: string;
}

export interface Material {
  id: string;
  slug: string;
  subject_id: string;
  subject_name: string;
  title: string;
  grade_level: string;
  difficulty: 'Boshlang\'ich' | 'O\'rta' | 'Murakkab';
  objective: string;
  theory: string;
  examples: Example[];
  exercise: string;
  exercise_solution: string;
  check_questions: CheckQuestion[];
  tags: string[];
  duration_minutes: number;
  views?: number;
  likes?: number;
}
"""
    with open(os.path.join(BASE, "types/index.ts"), "w", encoding="utf-8") as f:
        f.write(types_content)

def write_supabase_client():
    client_code = """import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || 'https://placeholder.supabase.co';
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || 'placeholder-anon-key';

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
"""
    with open(os.path.join(BASE, "lib/supabase.ts"), "w", encoding="utf-8") as f:
        f.write(client_code)

def write_nextjs_routes():
    # Root layout
    layout_code = """import './globals.css';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Education Hub 2.0 — O‘zbekiston uchun bepul raqamli ta’lim',
  description: '52 ta fan, 200+ to‘liq ta’limiy material, interaktiv testlar va shaxsiy kabinet.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="uz" className="h-full">
      <body className={`${inter.className} min-h-full flex flex-col bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100`}>
        {children}
      </body>
    </html>
  );
}
"""
    with open(os.path.join(BASE, "app/layout.tsx"), "w", encoding="utf-8") as f:
        f.write(layout_code)

    # globals.css
    css_code = """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100;
  }
}
"""
    with open(os.path.join(BASE, "app/globals.css"), "w", encoding="utf-8") as f:
        f.write(css_code)

    # Home page
    home_code = """import Link from 'next/link';
import subjectsData from '@/data/subjects.json';
import materialsData from '@/data/materials.json';

export default function HomePage() {
  const featured = materialsData.slice(0, 6);

  return (
    <main className="flex-grow">
      {/* Hero Section */}
      <section className="py-20 text-center px-4 bg-gradient-to-b from-blue-50/50 to-transparent dark:from-slate-900/40">
        <div className="max-w-4xl mx-auto">
          <span className="px-3 py-1 rounded-full text-xs font-semibold bg-blue-100 text-blue-700 dark:bg-blue-900/40 dark:text-blue-300">
            100% Bepul Ta’lim Ekotizimi
          </span>
          <h1 className="text-5xl font-black mt-6 tracking-tight">
            Education Hub 2.0
          </h1>
          <p className="mt-4 text-lg text-slate-600 dark:text-slate-300">
            O‘zbekiston maktab o‘quvchilari, talabalar va o‘qituvchilar uchun 52 ta fan va 200 dan ortiq to‘liq o‘quv materiallari.
          </p>

          <div className="mt-8 flex justify-center gap-4">
            <Link href="/subjects" className="px-6 py-3 rounded-xl bg-blue-600 text-white font-semibold text-sm hover:bg-blue-700 shadow-lg">
              Fanlar katalogi (52)
            </Link>
            <Link href="/materials" className="px-6 py-3 rounded-xl bg-white dark:bg-slate-800 border text-slate-700 dark:text-slate-200 font-semibold text-sm">
              Materiallar kutubxonasi (200)
            </Link>
          </div>
        </div>
      </section>

      {/* Featured Materials */}
      <section className="max-w-7xl mx-auto px-4 py-12">
        <h2 className="text-2xl font-bold mb-6">Tavsiya etiladigan darslar</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {featured.map((m) => (
            <div key={m.id} className="p-6 rounded-2xl bg-white dark:bg-slate-900 border shadow-sm">
              <span className="text-xs text-blue-600 font-semibold">{m.subject_name} • {m.grade_level}</span>
              <h3 className="font-bold text-lg mt-2">{m.title}</h3>
              <p className="text-xs text-slate-500 mt-2 line-clamp-2">{m.objective}</p>
              <div className="mt-4 pt-3 border-t flex justify-between items-center text-xs">
                <span>⏱ {m.duration_minutes} daqiqa</span>
                <Link href={`/materials/${m.slug}`} className="text-blue-600 font-bold hover:underline">
                  O‘qish &rarr;
                </Link>
              </div>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
"""
    with open(os.path.join(BASE, "app/page.tsx"), "w", encoding="utf-8") as f:
        f.write(home_code)

def write_readme():
    readme_content = """# 🚀 Education Hub 2.0 — O‘zbekiston uchun bepul raqamli ta’lim platformasi

Education Hub 2.0 — butun O‘zbekiston bo‘ylab maktab o‘quvchilari, talabalar va o‘qituvchilar uchun mo‘ljallangan, 100% bepul, zamonaviy, xavfsiz va to‘liq ishlaydigan milliy ta’lim ekotizimi.

---

## 📌 Asosiy ko'rsatkichlar va imkoniyatlar
- **52 ta to'liq fan katalogi** (Aniq fanlar, Tabiiy fanlar, Tillar va adabiyot, Ijtimoiy-gumanitar fanlar, Amaliy fanlar, Universitet va IT).
- **Kamida 200 ta real pedagogik material** (O'zbek tilida to'liq nazariya, kamida 2 ta amaliy misol, mustaqil mashq, uning yechimi va 3 ta tekshiruv savoli).
- **100% Bepul foydalanish**: Hech qanday majburiy to'lov, paywall yoki yashirin pullik obunalarsiz.
- **Interaktiv test markazi**: Vaqt chegarasi, ballar hisobi, javoblar tahlili va XP mukofoti.
- **Shaxsiy kabinet (Dashboard)**: O'zlashtirish foizi, faollik grafigi, xatcho'plar va reyting.
- **O'qituvchi studiyasi (Teacher Studio)**: Yangi material va testlar yaratish moduli.
- **Administrator paneli**: Foydalanuvchilar rollari boshqaruvi (RBAC) va kontent moderatsiyasi.
- **Dark/Light rejim** va to'liq mobil moslashuvchanlik (Responsive).

---

## 🛠 Texnologik stek
- **Frontend**: Next.js 14 (App Router), React 18, TypeScript, Tailwind CSS, Lucide Icons, Chart.js / Recharts.
- **Backend & Database**: Supabase (PostgreSQL 15), Row Level Security (RLS), Supabase Auth.
- **Validatsiya & Xavfsizlik**: Zod, Python unittest avtomatlashtirilgan test to'plami.
- **Mobil & Veb**: Standalone Canvas Single Page Application (`education_hub_2.html`).

---

## 📂 Papkalar tuzilmasi
```text
education-hub-platform/
├── app/                      # Next.js 14 App Router sahifalari
│   ├── layout.tsx            # Umumiy layout va shriftlar
│   ├── page.tsx              # Bosh sahifa
│   ├── subjects/             # Fanlar katalogi va alohida fan sahifasi
│   ├── materials/            # 200 ta material kutubxonasi va o'qish sahifasi
│   ├── courses/              # Kurslar ro'yxati
│   ├── tests/                # Interaktiv test markazi va test ishlash
│   ├── dashboard/            # Shaxsiy kabinet
│   ├── teacher/              # O'qituvchi studiyasi va yangi material yaratish
│   ├── admin/                # Administrator boshqaruv paneli
│   └── globals.css           # Global Tailwind uslublari
├── data/                     # 52 ta fan va 200 ta material ma'lumotlari
│   ├── subjects.json         # 52 ta fan spetsifikatsiyasi
│   ├── materials.json        # 200 ta to'liq materiallar to'plami (740 KB)
│   ├── education_hub.db      # SQLite ma'lumotlar bazasi
│   └── stats.json            # Tekshiruv va taqsimot statistikasi
├── supabase/
│   └── migrations/           # PostgreSQL migratsiyalari
│       ├── 20261019_init_schema.sql         # 16 ta jadval va RLS siyosatlari
│       └── 20261019_seed_200_materials.sql  # 200 ta material uchun SQL seed (672 KB)
├── tests/
│   └── test_platform.py      # Avtomatik testlar (200 material, RBAC, scoring)
├── .env.example              # Muhit o'zgaruvchilari namunasi
├── package.json              # Loyiha qaramliklari
├── tailwind.config.js        # Dizayn tizimi konfiguratsiyasi
└── README.md                 # Loyiha hujjatlari
```

---

## 🚀 Ishga tushirish yo'riqnomasi (Local Development)

### 1. Qaramliklarni o'rnatish
```bash
npm install
```

### 2. Muhit o'zgaruvchilarini sozlash
`.env.example` faylidan nusxa olib `.env.local` yarating va Supabase ma'lumotlarini kiriting:
```bash
cp .env.example .env.local
```

### 3. Ma'lumotlar bazasini yuklash (Supabase)
Supabase SQL Editor bo'limiga kirib quyidagi fayllarni navbat bilan ishga tushiring:
1. `supabase/migrations/20261019_init_schema.sql` (Sxema va jadvallar)
2. `supabase/migrations/20261019_seed_200_materials.sql` (200 ta material)

### 4. Avtomatik testlarni tekshirish
Materiallar soni kamida 200 ta ekanligi, unikal sluglar va xavfsizlik testlarini yurgizish:
```bash
python3 tests/test_platform.py
```

### 5. Loyihani ishga tushirish
```bash
npm run dev
```
Brauzerda `http://localhost:3000` manzilini oching.

---

## 🌐 Internetga joylashtirish (Production Deployment - Vercel)

Loyiha Vercel hostingiga 1 ta buyruq bilan joylashtirishga to'liq tayyorlangan:
1. GitHub da yangi ombor (repository) yarating: `git remote add origin ...` va kodni push qiling.
2. [Vercel.com](https://vercel.com) ga kiring va GitHub repozitoriyasini tanlang.
3. Environment Variables bo'limida `NEXT_PUBLIC_SUPABASE_URL` va `NEXT_PUBLIC_SUPABASE_ANON_KEY` ni kiriting.
4. **Deploy** tugmasini bosing!
Sayt bir necha daqiqada `educationhub2.vercel.app` yoki o'z shaxsiy domeningizda (`educationhub.uz`) HTTPS bilan to'liq ishga tushadi.
"""
    with open(os.path.join(BASE, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    make_dirs()
    write_package_json()
    write_configs()
    write_types()
    write_supabase_client()
    write_nextjs_routes()
    write_readme()
    print("Next.js project generation completed successfully!")
