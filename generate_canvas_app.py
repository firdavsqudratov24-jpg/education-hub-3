# -*- coding: utf-8 -*-
"""
Generator for Education Hub 2.0 Single-File Web Application
Embeds subjects and all 200 materials into an interactive, full-featured SPA
supporting all 20 routes/views, tests, dashboard, teacher studio, admin panel,
dark/light mode, and speech synthesis.
"""

import os
import json

def generate_web_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, 'data')
    
    with open(os.path.join(data_dir, 'subjects.json'), 'r', encoding='utf-8') as f:
        subjects_data = json.load(f)
        
    with open(os.path.join(data_dir, 'materials.json'), 'r', encoding='utf-8') as f:
        materials_data = json.load(f)

    subjects_json_str = json.dumps(subjects_data, ensure_ascii=False)
    materials_json_str = json.dumps(materials_data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="uz" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Education Hub 2.0 — O‘zbekiston uchun bepul raqamli ta’lim platformasi</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com/3.4.17"></script>
  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            primary: {{
              50: '#eff6ff',
              100: '#dbeafe',
              500: '#3b82f6',
              600: '#2563eb',
              700: '#1d4ed8',
              800: '#1e40af',
              900: '#1e3a8a'
            }},
            secondary: {{
              500: '#0d9488',
              600: '#0f766e'
            }},
            accent: {{
              500: '#7c3aed',
              600: '#6d28d9'
            }},
            darkbg: '#0f172a',
            darkcard: '#1e293b',
            lightbg: '#f8fafc'
          }}
        }}
      }}
    }};
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    /* Custom scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: rgba(0,0,0,0.05);
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(100,116,139,0.3);
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: rgba(100,116,139,0.5);
    }}
    .line-clamp-2 {{
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    .line-clamp-3 {{
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
  </style>
</head>
<body class="bg-lightbg dark:bg-darkbg text-slate-800 dark:text-slate-100 min-h-full flex flex-col transition-colors duration-200">

  <!-- ========================================== -->
  <!-- NAVBAR -->
  <!-- ========================================== -->
  <header class="sticky top-0 z-40 bg-white/90 dark:bg-darkcard/90 backdrop-blur border-b border-slate-200 dark:border-slate-800 transition-colors">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        
        <!-- Logo -->
        <div class="flex items-center gap-3 cursor-pointer" onclick="navigateTo('home')">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-teal-500 flex items-center justify-center text-white font-black text-xl shadow-md shadow-blue-500/20">
            EH
          </div>
          <div>
            <span class="text-xl font-bold bg-gradient-to-r from-blue-600 via-teal-600 to-purple-600 bg-clip-text text-transparent">Education Hub</span>
            <span class="text-xs px-1.5 py-0.5 ml-1 rounded font-semibold bg-blue-100 text-blue-700 dark:bg-blue-900/40 dark:text-blue-300">2.0</span>
          </div>
        </div>

        <!-- Desktop Navigation Links -->
        <nav class="hidden md:flex items-center gap-1 lg:gap-2">
          <button onclick="navigateTo('home')" class="nav-btn px-3 py-2 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition">Bosh sahifa</button>
          <button onclick="navigateTo('subjects')" class="nav-btn px-3 py-2 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition">Fanlar (52)</button>
          <button onclick="navigateTo('materials')" class="nav-btn px-3 py-2 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition">Materiallar (200)</button>
          <button onclick="navigateTo('courses')" class="nav-btn px-3 py-2 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition">Kurslar</button>
          <button onclick="navigateTo('tests')" class="nav-btn px-3 py-2 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition">Test markazi</button>
          <button onclick="navigateTo('dashboard')" class="nav-btn px-3 py-2 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition">Kabinet</button>
          <button onclick="navigateTo('teacher')" class="nav-btn px-3 py-2 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition">O'qituvchi</button>
          <button onclick="navigateTo('admin')" class="nav-btn px-3 py-2 rounded-lg text-sm font-medium text-amber-600 dark:text-amber-400 hover:bg-amber-50 dark:hover:bg-amber-950/30 transition">Admin</button>
        </nav>

        <!-- Right Controls: Dark Mode, Search, Auth -->
        <div class="flex items-center gap-2">
          <!-- Dark Mode Toggle -->
          <button id="themeToggleBtn" onclick="toggleTheme()" class="p-2 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition" title="Mavzuni almashtirish">
            <svg id="sunIcon" class="w-5 h-5 hidden dark:block text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
            <svg id="moonIcon" class="w-5 h-5 block dark:hidden text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
          </button>

          <!-- Auth Button / Avatar -->
          <div id="authContainer" class="flex items-center gap-2">
            <!-- Dynamically populated by JS -->
          </div>

          <!-- Mobile Hamburger -->
          <button onclick="toggleMobileMenu()" class="md:hidden p-2 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/></svg>
          </button>
        </div>

      </div>
    </div>

    <!-- Mobile Drawer -->
    <div id="mobileMenu" class="hidden md:hidden border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-darkcard px-4 pt-2 pb-4 space-y-1">
      <button onclick="navigateTo('home'); toggleMobileMenu()" class="block w-full text-left px-3 py-2 rounded-lg text-base font-medium text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800">Bosh sahifa</button>
      <button onclick="navigateTo('subjects'); toggleMobileMenu()" class="block w-full text-left px-3 py-2 rounded-lg text-base font-medium text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800">Barcha Fanlar (52)</button>
      <button onclick="navigateTo('materials'); toggleMobileMenu()" class="block w-full text-left px-3 py-2 rounded-lg text-base font-medium text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800">Materiallar Kutubxonasi (200)</button>
      <button onclick="navigateTo('courses'); toggleMobileMenu()" class="block w-full text-left px-3 py-2 rounded-lg text-base font-medium text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800">Kurslar</button>
      <button onclick="navigateTo('tests'); toggleMobileMenu()" class="block w-full text-left px-3 py-2 rounded-lg text-base font-medium text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800">Interaktiv Testlar</button>
      <button onclick="navigateTo('dashboard'); toggleMobileMenu()" class="block w-full text-left px-3 py-2 rounded-lg text-base font-medium text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800">Shaxsiy Kabinet</button>
      <button onclick="navigateTo('achievements'); toggleMobileMenu()" class="block w-full text-left px-3 py-2 rounded-lg text-base font-medium text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800">Yutuqlar & XP</button>
      <button onclick="navigateTo('teacher'); toggleMobileMenu()" class="block w-full text-left px-3 py-2 rounded-lg text-base font-medium text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800">O'qituvchi Studiyasi</button>
      <button onclick="navigateTo('admin'); toggleMobileMenu()" class="block w-full text-left px-3 py-2 rounded-lg text-base font-medium text-amber-600 dark:text-amber-400 hover:bg-slate-100 dark:hover:bg-slate-800">Admin Panel</button>
    </div>
  </header>

  <!-- ========================================== -->
  <!-- MAIN CONTENT CONTAINER (DYNAMIC SPA VIEWS) -->
  <!-- ========================================== -->
  <main id="appContainer" class="flex-grow">
    <!-- View will be rendered dynamically here -->
  </main>

  <!-- ========================================== -->
  <!-- FOOTER -->
  <!-- ========================================== -->
  <footer class="bg-white dark:bg-darkcard border-t border-slate-200 dark:border-slate-800 transition-colors mt-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
        <div class="space-y-4">
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 rounded-lg bg-blue-600 flex items-center justify-center text-white font-bold">EH</div>
            <span class="text-lg font-bold text-slate-900 dark:text-white">Education Hub 2.0</span>
          </div>
          <p class="text-sm text-slate-500 dark:text-slate-400">
            Butun O‘zbekiston o‘quvchilari, talabalari va o‘qituvchilari uchun 100% bepul, zamonaviy va professional raqamli ta’lim ekotizimi.
          </p>
          <div class="flex items-center gap-2 text-xs font-semibold text-emerald-600 dark:text-emerald-400">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            100% Bepul Ta’lim • Hech qanday to‘lovlarsiz
          </div>
        </div>

        <div>
          <h4 class="text-sm font-semibold text-slate-900 dark:text-white mb-3">Yo'nalishlar</h4>
          <ul class="space-y-2 text-sm text-slate-500 dark:text-slate-400">
            <li><button onclick="filterSubjectsByCategory('Aniq fanlar')" class="hover:text-blue-600">Aniq fanlar (Matematika, Fizika)</button></li>
            <li><button onclick="filterSubjectsByCategory('Tabiiy fanlar')" class="hover:text-blue-600">Tabiiy fanlar (Kimyo, Biologiya)</button></li>
            <li><button onclick="filterSubjectsByCategory('Tillar va adabiyot')" class="hover:text-blue-600">Tillar va adabiyot</button></li>
            <li><button onclick="filterSubjectsByCategory('Ijtimoiy va gumanitar fanlar')" class="hover:text-blue-600">Tarix va jamiyat</button></li>
            <li><button onclick="filterSubjectsByCategory('Universitet va kasbiy')" class="hover:text-blue-600">Universitet & IT (Dasturlash, AI)</button></li>
          </ul>
        </div>

        <div>
          <h4 class="text-sm font-semibold text-slate-900 dark:text-white mb-3">Imkoniyatlar</h4>
          <ul class="space-y-2 text-sm text-slate-500 dark:text-slate-400">
            <li><button onclick="navigateTo('materials')" class="hover:text-blue-600">200+ To'liq Materiallar</button></li>
            <li><button onclick="navigateTo('tests')" class="hover:text-blue-600">Interaktiv Testlar & Sertifikat</button></li>
            <li><button onclick="navigateTo('dashboard')" class="hover:text-blue-600">Shaxsiy Rivojlanish & XP</button></li>
            <li><button onclick="navigateTo('teacher')" class="hover:text-blue-600">O'qituvchilar Studiyasi</button></li>
            <li><button onclick="navigateTo('admin')" class="hover:text-blue-600">Boshqaruv & Moderatsiya</button></li>
          </ul>
        </div>

        <div>
          <h4 class="text-sm font-semibold text-slate-900 dark:text-white mb-3">Loyiha & Aloqa</h4>
          <ul class="space-y-2 text-sm text-slate-500 dark:text-slate-400">
            <li><button onclick="navigateTo('about')" class="hover:text-blue-600">Loyiha haqida</button></li>
            <li><button onclick="navigateTo('contact')" class="hover:text-blue-600">Qayta aloqa & Takliflar</button></li>
            <li><span class="text-xs text-slate-400">Toshkent, O‘zbekiston</span></li>
            <li><span class="text-xs text-slate-400">Ochiq ta'lim standarti</span></li>
          </ul>
        </div>
      </div>

      <div class="pt-6 border-t border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 dark:text-slate-400">
        <p>&copy; 2026 Education Hub 2.0 — O‘zbekiston Respublikasi yoshlari uchun ochiq ta’lim platformasi.</p>
        <p class="mt-2 sm:mt-0 font-medium">Ochiq kodli va 100% Bepul</p>
      </div>
    </div>
  </footer>

  <!-- ========================================== -->
  <!-- TOAST NOTIFICATION CONTAINER -->
  <!-- ========================================== -->
  <div id="toastContainer" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>

  <!-- ========================================== -->
  <!-- GLOBAL MODAL DIALOG CONTAINER -->
  <!-- ========================================== -->
  <div id="modalContainer" class="fixed inset-0 z-50 hidden items-center justify-center bg-black/50 backdrop-blur-sm p-4 overflow-y-auto">
    <!-- Populated by JS -->
  </div>

  <!-- ========================================== -->
  <!-- APPLICATION DATA & CLIENT LOGIC -->
  <!-- ========================================== -->
  <script>
    // Embedded Data: 52 Subjects and 200 Real Pedagogical Materials
    const SUBJECTS = {subjects_json_str};
    const MATERIALS = {materials_json_str};

    // User State & Storage
    let currentUser = null;
    let completedMaterials = [];
    let bookmarkedMaterials = [];
    let quizHistory = [];
    let userXP = 120;
    let currentQuiz = null;
    let quizTimerInterval = null;
    let quizRemainingSeconds = 0;
    let quizSelectedAnswers = {{}};
    let activeFilterCategory = 'Barchasi';
    let searchQuery = '';
    let selectedGrade = 'Barchasi';
    let selectedDifficulty = 'Barchasi';

    // Initialize State
    function initState() {{
      // Theme
      const savedTheme = localStorage.getItem('eh_theme') || 'light';
      if (savedTheme === 'dark') {{
        document.documentElement.classList.add('dark');
      }} else {{
        document.documentElement.classList.remove('dark');
      }}

      // User
      try {{
        const savedUser = localStorage.getItem('eh_user');
        if (savedUser) {{
          currentUser = JSON.parse(savedUser);
        }} else {{
          // Default demo student
          currentUser = {{
            id: 'usr-demo-01',
            name: 'Temur Aliyev',
            email: 'temur@edu.uz',
            role: 'student',
            grade: '9-sinf',
            xp: 320,
            level: 3
          }};
          localStorage.setItem('eh_user', JSON.stringify(currentUser));
        }}
        
        completedMaterials = JSON.parse(localStorage.getItem('eh_completed') || '["mat-001", "mat-002", "phy-001"]');
        bookmarkedMaterials = JSON.parse(localStorage.getItem('eh_bookmarks') || '["mat-004", "dev-015"]');
        quizHistory = JSON.parse(localStorage.getItem('eh_quiz_history') || '[]');
      }} catch (e) {{
        console.warn('Storage error:', e);
      }}

      renderAuthHeader();
    }}

    function toggleTheme() {{
      const isDark = document.documentElement.classList.toggle('dark');
      try {{
        localStorage.setItem('eh_theme', isDark ? 'dark' : 'light');
      }} catch (e) {{}}
    }}

    function toggleMobileMenu() {{
      const m = document.getElementById('mobileMenu');
      m.classList.toggle('hidden');
    }}

    function showToast(title, message, type = 'success') {{
      const container = document.getElementById('toastContainer');
      const toast = document.createElement('div');
      toast.className = `pointer-events-auto flex items-start gap-3 p-4 rounded-xl shadow-xl border text-sm transition-all transform duration-300 translate-y-2 bg-white dark:bg-slate-800 ${{
        type === 'success' ? 'border-emerald-500/50 text-emerald-800 dark:text-emerald-300' :
        type === 'error' ? 'border-rose-500/50 text-rose-800 dark:text-rose-300' :
        'border-blue-500/50 text-blue-800 dark:text-blue-300'
      }}`;

      toast.innerHTML = `
        <div class="mt-0.5">
          ${{type === 'success' ? '✓' : type === 'error' ? '✕' : 'ℹ'}}
        </div>
        <div class="flex-grow">
          <div class="font-bold">${{title}}</div>
          <div class="text-xs text-slate-600 dark:text-slate-400 mt-0.5">${{message}}</div>
        </div>
      `;
      container.appendChild(toast);
      setTimeout(() => {{
        toast.classList.add('opacity-0', 'translate-y-4');
        setTimeout(() => toast.remove(), 300);
      }}, 3500);
    }}

    function renderAuthHeader() {{
      const container = document.getElementById('authContainer');
      if (currentUser) {{
        container.innerHTML = `
          <div class="flex items-center gap-2 pl-2 border-l border-slate-200 dark:border-slate-700">
            <div onclick="navigateTo('profile')" class="cursor-pointer flex items-center gap-2 p-1 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">
              <div class="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-xs uppercase">
                ${{currentUser.name.substring(0, 2)}}
              </div>
              <div class="hidden xl:block text-left">
                <div class="text-xs font-semibold leading-tight text-slate-900 dark:text-white">${{currentUser.name}}</div>
                <div class="text-[10px] text-blue-600 dark:text-blue-400 capitalize">${{currentUser.role}} • ${{currentUser.xp || 320}} XP</div>
              </div>
            </div>
            <button onclick="handleLogout()" class="p-1.5 text-xs text-slate-400 hover:text-rose-500 transition" title="Chiqish">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/></svg>
            </button>
          </div>
        `;
      }} else {{
        container.innerHTML = `
          <button onclick="openAuthModal('login')" class="text-xs font-semibold px-3 py-2 rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition">Kirish</button>
          <button onclick="openAuthModal('register')" class="text-xs font-semibold px-3 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700 shadow-sm transition">Ro'yxatdan o'tish</button>
        `;
      }}
    }}

    function handleLogout() {{
      currentUser = null;
      try {{ localStorage.removeItem('eh_user'); }} catch(e){{}}
      renderAuthHeader();
      showToast('Tizimdan chiqildi', 'Siz hisobdan muvaffaqiyatli chiqdingiz.');
      navigateTo('home');
    }}

    // ==========================================
    // ROUTING ENGINE (SPA NAVIGATION)
    // ==========================================
    function navigateTo(route, param = null) {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
      const container = document.getElementById('appContainer');

      if (quizTimerInterval) {{
        clearInterval(quizTimerInterval);
        quizTimerInterval = null;
      }}

      switch(route) {{
        case 'home':
          container.innerHTML = renderHomeView();
          break;
        case 'subjects':
          container.innerHTML = renderSubjectsView(param);
          break;
        case 'subject_detail':
          container.innerHTML = renderSubjectDetailView(param);
          break;
        case 'materials':
          container.innerHTML = renderMaterialsView(param);
          break;
        case 'material_reader':
          container.innerHTML = renderMaterialReaderView(param);
          break;
        case 'courses':
          container.innerHTML = renderCoursesView();
          break;
        case 'tests':
          container.innerHTML = renderTestsCenterView();
          break;
        case 'quiz_arena':
          container.innerHTML = renderQuizArenaView(param);
          startQuizTimer();
          break;
        case 'results':
          container.innerHTML = renderResultsView(param);
          break;
        case 'dashboard':
          container.innerHTML = renderDashboardView();
          initDashboardChart();
          break;
        case 'profile':
          container.innerHTML = renderProfileView();
          break;
        case 'achievements':
          container.innerHTML = renderAchievementsView();
          break;
        case 'teacher':
          container.innerHTML = renderTeacherStudioView();
          break;
        case 'teacher_new':
          container.innerHTML = renderTeacherNewMaterialView();
          break;
        case 'admin':
          container.innerHTML = renderAdminPanelView();
          break;
        case 'about':
          container.innerHTML = renderAboutView();
          break;
        case 'contact':
          container.innerHTML = renderContactView();
          break;
        default:
          container.innerHTML = renderHomeView();
      }}
    }}

    // ==========================================
    // 1. HOME VIEW
    // ==========================================
    function renderHomeView() {{
      const featuredMats = MATERIALS.slice(0, 6);
      return `
        <!-- Hero Section -->
        <section class="relative overflow-hidden pt-12 pb-20 lg:pt-20 lg:pb-28 bg-gradient-to-b from-blue-50/50 via-white to-transparent dark:from-slate-900/50 dark:via-darkbg dark:to-darkbg">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full text-xs font-semibold bg-blue-100 text-blue-700 dark:bg-blue-900/40 dark:text-blue-300 mb-6 border border-blue-200 dark:border-blue-800">
              <span class="w-2 h-2 rounded-full bg-blue-600 animate-ping"></span>
              O‘zbekiston yoshlari uchun 100% Bepul Zamonaviy Ta’lim
            </div>

            <h1 class="text-4xl sm:text-6xl font-extrabold tracking-tight text-slate-900 dark:text-white max-w-4xl mx-auto leading-tight">
              Kelajak bilimlarini <span class="bg-gradient-to-r from-blue-600 via-teal-500 to-purple-600 bg-clip-text text-transparent">bepul va professional</span> o‘rganing
            </h1>

            <p class="mt-6 text-lg sm:text-xl text-slate-600 dark:text-slate-300 max-w-2xl mx-auto">
              Maktabning 52 ta barcha fanlari, xalqaro tillar, oliy matematika va zamonaviy IT dasturlash bo'yicha 200 dan ortiq to'liq darslar hamda interaktiv testlar tizimi.
            </p>

            <!-- Search Bar in Hero -->
            <div class="mt-8 max-w-xl mx-auto flex items-center bg-white dark:bg-darkcard rounded-2xl shadow-xl border border-slate-200 dark:border-slate-700 p-2">
              <svg class="w-5 h-5 text-slate-400 ml-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
              <input id="heroSearchInput" type="text" placeholder="Mavzu yoki fanni qidiring (masalan: Kasrlar, Nyuton, Python, Alpomish)..." class="w-full px-3 py-2 bg-transparent text-sm focus:outline-none dark:text-white">
              <button onclick="handleHeroSearch()" class="px-5 py-2.5 rounded-xl bg-blue-600 text-white font-medium text-sm hover:bg-blue-700 transition shadow-md shadow-blue-500/20">
                Qidirish
              </button>
            </div>

            <!-- Action Buttons -->
            <div class="mt-6 flex flex-wrap items-center justify-center gap-4">
              <button onclick="navigateTo('subjects')" class="px-6 py-3 rounded-xl bg-blue-600 text-white font-semibold text-sm hover:bg-blue-700 shadow-lg shadow-blue-500/25 transition">
                Barcha fanlar katalogi (52)
              </button>
              <button onclick="navigateTo('tests')" class="px-6 py-3 rounded-xl bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-semibold text-sm border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition">
                Test topshirish & XP yig'ish
              </button>
            </div>

            <!-- Platform Stats -->
            <div class="mt-14 grid grid-cols-2 sm:grid-cols-4 gap-4 max-w-4xl mx-auto">
              <div class="p-4 rounded-2xl bg-white dark:bg-darkcard border border-slate-100 dark:border-slate-800 shadow-sm">
                <div class="text-3xl font-extrabold text-blue-600 dark:text-blue-400">52 ta</div>
                <div class="text-xs text-slate-500 mt-1">To'liq fanlar katalogi</div>
              </div>
              <div class="p-4 rounded-2xl bg-white dark:bg-darkcard border border-slate-100 dark:border-slate-800 shadow-sm">
                <div class="text-3xl font-extrabold text-teal-600 dark:text-teal-400">200+</div>
                <div class="text-xs text-slate-500 mt-1">Haqiqiy ta'limiy materiallar</div>
              </div>
              <div class="p-4 rounded-2xl bg-white dark:bg-darkcard border border-slate-100 dark:border-slate-800 shadow-sm">
                <div class="text-3xl font-extrabold text-purple-600 dark:text-purple-400">100%</div>
                <div class="text-xs text-slate-500 mt-1">Mutlaqo bepul va ochiq</div>
              </div>
              <div class="p-4 rounded-2xl bg-white dark:bg-darkcard border border-slate-100 dark:border-slate-800 shadow-sm">
                <div class="text-3xl font-extrabold text-emerald-600 dark:text-emerald-400">4.9/5</div>
                <div class="text-xs text-slate-500 mt-1">O'quvchilar e'tirofi</div>
              </div>
            </div>

          </div>
        </section>

        <!-- Categories Section -->
        <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div class="flex items-center justify-between mb-8">
            <div>
              <h2 class="text-2xl font-bold text-slate-900 dark:text-white">Fanlar yo‘nalishlari</h2>
              <p class="text-sm text-slate-500 mt-1">O‘zingizga kerakli ta’lim sohasini tanlang</p>
            </div>
            <button onclick="navigateTo('subjects')" class="text-sm font-semibold text-blue-600 hover:text-blue-700 flex items-center gap-1">
              Barchasini ko‘rish &rarr;
            </button>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            ${{renderCategoryCards()}}
          </div>
        </section>

        <!-- Featured Materials Section -->
        <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 bg-slate-50/50 dark:bg-slate-900/20 rounded-3xl my-8">
          <div class="flex items-center justify-between mb-8">
            <div>
              <h2 class="text-2xl font-bold text-slate-900 dark:text-white">Tavsiya etiladigan darslar</h2>
              <p class="text-sm text-slate-500 mt-1">Nazariya, 2 ta amaliy misol va mustaqil mashq bilan boyitilgan</p>
            </div>
            <button onclick="navigateTo('materials')" class="text-sm font-semibold text-blue-600 hover:text-blue-700 flex items-center gap-1">
              Barcha 200 ta material &rarr;
            </button>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            ${{featuredMats.map(m => renderMaterialCard(m)).join('')}}
          </div>
        </section>
      `;
    }}

    function handleHeroSearch() {{
      const val = document.getElementById('heroSearchInput').value.trim();
      searchQuery = val;
      navigateTo('materials');
    }}

    function renderCategoryCards() {{
      const cats = [
        {{ name: 'Aniq fanlar', count: '6 ta fan (30 material)', color: 'from-blue-500 to-indigo-600', desc: 'Matematika, Algebra, Geometriya, Fizika, Astronomiya' }},
        {{ name: 'Tabiiy fanlar', count: '8 ta fan (18 material)', color: 'from-teal-500 to-emerald-600', desc: 'Kimyo, Biologiya, Botanika, Zoologiya, Anatomiya' }},
        {{ name: 'Tillar va adabiyot', count: '8 ta fan (38 material)', color: 'from-purple-500 to-pink-600', desc: 'Ona tili, O‘zbek adabiyoti, Ingliz, Rus, Nemis, Fransuz' }},
        {{ name: 'Ijtimoiy va gumanitar fanlar', count: '8 ta fan (28 material)', color: 'from-amber-500 to-orange-600', desc: 'O‘zbekiston tarixi, Jahon tarixi, Huquq, Iqtisod, Falsafa' }},
        {{ name: 'Amaliy va ijodiy fanlar', count: '6 ta fan (12 material)', color: 'from-rose-500 to-red-600', desc: 'Texnologiya, San’at, Musiqa, Jismoniy tarbiya, Chizmachilik' }},
        {{ name: 'Universitet va kasbiy', count: '16 ta fan (35 material)', color: 'from-cyan-500 to-blue-700', desc: 'Dasturlash, Web, Python, Sun’iy intellekt, Kiberxavfsizlik' }}
      ];

      return cats.map(c => `
        <div onclick="filterSubjectsByCategory('${{c.name}}')" class="cursor-pointer group relative p-6 rounded-2xl bg-white dark:bg-darkcard border border-slate-200/80 dark:border-slate-800 shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
          <div class="w-12 h-12 rounded-xl bg-gradient-to-tr ${{c.color}} text-white flex items-center justify-center font-bold text-lg mb-4 shadow-md">
            ★
          </div>
          <h3 class="text-lg font-bold text-slate-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition">${{c.name}}</h3>
          <p class="text-xs text-blue-600 dark:text-blue-400 font-semibold mt-1">${{c.count}}</p>
          <p class="text-xs text-slate-500 dark:text-slate-400 mt-2 line-clamp-2">${{c.desc}}</p>
        </div>
      `).join('');
    }}

    function filterSubjectsByCategory(category) {{
      activeFilterCategory = category;
      navigateTo('subjects');
    }}

    // ==========================================
    // 2. SUBJECTS VIEW (52 SUBJECTS)
    // ==========================================
    function renderSubjectsView() {{
      const categories = ['Barchasi', 'Aniq fanlar', 'Tabiiy fanlar', 'Tillar va adabiyot', 'Ijtimoiy va gumanitar fanlar', 'Amaliy va ijodiy fanlar', 'Universitet va kasbiy'];
      
      const filtered = SUBJECTS.filter(s => {{
        const matchCat = activeFilterCategory === 'Barchasi' || s.category === activeFilterCategory;
        const matchSearch = s.name.toLowerCase().includes(searchQuery.toLowerCase()) || s.description.toLowerCase().includes(searchQuery.toLowerCase());
        return matchCat && matchSearch;
      }});

      return `
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="mb-8 text-center max-w-2xl mx-auto">
            <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white">Barcha fanlar katalogi</h1>
            <p class="text-sm text-slate-500 mt-2">Maktabning 1-11 sinflari hamda universitet va zamonaviy kasbiy ta’lim yo‘nalishlari bo‘yicha 52 ta fan</p>
          </div>

          <!-- Category Filter Tabs -->
          <div class="flex items-center gap-2 overflow-x-auto pb-4 mb-6">
            ${{categories.map(cat => `
              <button onclick="setSubjectCategory('${{cat}}')" class="whitespace-nowrap px-4 py-2 rounded-xl text-xs font-semibold transition ${{
                activeFilterCategory === cat ? 'bg-blue-600 text-white shadow-md shadow-blue-500/20' : 'bg-white dark:bg-darkcard text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-800 hover:bg-slate-50'
              }}">${{cat}}</button>
            `).join('')}}
          </div>

          <!-- Search within subjects -->
          <div class="mb-8 max-w-md">
            <input type="text" placeholder="Fan nomi bo'yicha qidirish..." oninput="handleSubjectSearch(this.value)" value="${{searchQuery}}" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-darkcard text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:text-white">
          </div>

          <!-- Subjects Grid -->
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5">
            ${{filtered.map(s => `
              <div onclick="navigateTo('subject_detail', '${{s.id}}')" class="cursor-pointer group p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200/80 dark:border-slate-800 hover:border-blue-500 dark:hover:border-blue-500 shadow-sm hover:shadow-lg transition duration-200 flex flex-col justify-between">
                <div>
                  <div class="flex items-center justify-between mb-3">
                    <span class="text-xs px-2 py-0.5 rounded font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400">${{s.grade_range}}</span>
                    <span class="w-3 h-3 rounded-full" style="background-color: ${{s.color}}"></span>
                  </div>
                  <h3 class="font-bold text-base text-slate-900 dark:text-white group-hover:text-blue-600 transition">${{s.name}}</h3>
                  <p class="text-xs text-slate-500 dark:text-slate-400 mt-2 line-clamp-3">${{s.description}}</p>
                </div>
                <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between text-xs">
                  <span class="text-blue-600 font-semibold">${{getMaterialsBySubject(s.id).length}} ta material</span>
                  <span class="text-slate-400 group-hover:translate-x-1 transition">&rarr;</span>
                </div>
              </div>
            `).join('')}}
          </div>
        </div>
      `;
    }}

    function setSubjectCategory(cat) {{
      activeFilterCategory = cat;
      navigateTo('subjects');
    }}

    function handleSubjectSearch(val) {{
      searchQuery = val;
      const container = document.getElementById('appContainer');
      container.innerHTML = renderSubjectsView();
    }}

    function getMaterialsBySubject(subjectId) {{
      return MATERIALS.filter(m => m.subject_id === subjectId);
    }}

    // ==========================================
    // 3. SUBJECT DETAIL VIEW
    // ==========================================
    function renderSubjectDetailView(subjectId) {{
      const subject = SUBJECTS.find(s => s.id === subjectId) || SUBJECTS[0];
      const subjectMaterials = getMaterialsBySubject(subject.id);

      return `
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <!-- Back button -->
          <button onclick="navigateTo('subjects')" class="inline-flex items-center gap-1.5 text-xs font-semibold text-slate-500 hover:text-blue-600 mb-6">
            &larr; Barcha fanlarga qaytish
          </button>

          <!-- Subject Banner Card -->
          <div class="p-8 rounded-3xl bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white shadow-xl mb-10 relative overflow-hidden">
            <div class="relative z-10 max-w-2xl">
              <span class="px-3 py-1 rounded-full text-xs font-semibold bg-white/20 backdrop-blur">${{subject.category}} • ${{subject.grade_range}}</span>
              <h1 class="text-3xl sm:text-4xl font-extrabold mt-3">${{subject.name}}</h1>
              <p class="text-sm sm:text-base text-blue-100 mt-2">${{subject.description}}</p>
              
              <div class="mt-6 flex flex-wrap items-center gap-4 text-xs">
                <div class="bg-black/20 px-3 py-1.5 rounded-lg">Mavjud darslar: <b>${{subjectMaterials.length}} ta</b></div>
                <div class="bg-black/20 px-3 py-1.5 rounded-lg">Daraja: <b>Boshlang'ichdan Murakkabgacha</b></div>
                <div class="bg-black/20 px-3 py-1.5 rounded-lg">Status: <b>100% Bepul</b></div>
              </div>
            </div>
          </div>

          <!-- Subject Materials List -->
          <div>
            <div class="flex items-center justify-between mb-6">
              <h2 class="text-xl font-bold text-slate-900 dark:text-white">Fan bo‘yicha o‘quv materiallari</h2>
              <span class="text-xs text-slate-500">${{subjectMaterials.length}} ta mavzu mavjud</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              ${{subjectMaterials.map(m => renderMaterialCard(m)).join('')}}
            </div>
          </div>
        </div>
      `;
    }}

    // ==========================================
    // 4. MATERIALS LIBRARY VIEW (200 MATERIALS)
    // ==========================================
    function renderMaterialsView() {{
      const filtered = MATERIALS.filter(m => {{
        const matchSearch = searchQuery === '' || 
          m.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
          m.theory.toLowerCase().includes(searchQuery.toLowerCase()) ||
          m.subject_name.toLowerCase().includes(searchQuery.toLowerCase());
        
        const matchGrade = selectedGrade === 'Barchasi' || m.grade_level.includes(selectedGrade);
        const matchDiff = selectedDifficulty === 'Barchasi' || m.difficulty === selectedDifficulty;
        return matchSearch && matchGrade && matchDiff;
      }});

      return `
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="mb-8">
            <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white">Materiallar kutubxonasi</h1>
            <p class="text-sm text-slate-500 mt-1">200 ta to'liq o'zbek tilidagi ta'limiy materiallar (nazariya, misollar, mustaqil mashq va testlar)</p>
          </div>

          <!-- Filters Row -->
          <div class="p-4 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm mb-8 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <!-- Search -->
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-1">Qidiruv</label>
              <input type="text" placeholder="Mavzu nomi..." value="${{searchQuery}}" oninput="searchQuery = this.value; navigateTo('materials')" class="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-xs focus:outline-none dark:text-white">
            </div>

            <!-- Grade Filter -->
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-1">Sinf / Daraja</label>
              <select onchange="selectedGrade = this.value; navigateTo('materials')" class="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-xs focus:outline-none dark:text-white">
                <option value="Barchasi" ${{selectedGrade === 'Barchasi' ? 'selected' : ''}}>Barcha sinflar</option>
                <option value="5-sinf" ${{selectedGrade === '5-sinf' ? 'selected' : ''}}>5-sinf</option>
                <option value="6-sinf" ${{selectedGrade === '6-sinf' ? 'selected' : ''}}>6-sinf</option>
                <option value="7-sinf" ${{selectedGrade === '7-sinf' ? 'selected' : ''}}>7-sinf</option>
                <option value="8-sinf" ${{selectedGrade === '8-sinf' ? 'selected' : ''}}>8-sinf</option>
                <option value="9-sinf" ${{selectedGrade === '9-sinf' ? 'selected' : ''}}>9-sinf</option>
                <option value="10-sinf" ${{selectedGrade === '10-sinf' ? 'selected' : ''}}>10-sinf</option>
                <option value="11-sinf" ${{selectedGrade === '11-sinf' ? 'selected' : ''}}>11-sinf</option>
                <option value="Universitet" ${{selectedGrade === 'Universitet' ? 'selected' : ''}}>Universitet & Kasbiy</option>
              </select>
            </div>

            <!-- Difficulty Filter -->
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-1">Qiyinlik darajasi</label>
              <select onchange="selectedDifficulty = this.value; navigateTo('materials')" class="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-xs focus:outline-none dark:text-white">
                <option value="Barchasi" ${{selectedDifficulty === 'Barchasi' ? 'selected' : ''}}>Barchasi</option>
                <option value="Boshlang'ich" ${{selectedDifficulty === "Boshlang'ich" ? 'selected' : ''}}>Boshlang'ich</option>
                <option value="O'rta" ${{selectedDifficulty === "O'rta" ? 'selected' : ''}}>O'rta</option>
                <option value="Murakkab" ${{selectedDifficulty === 'Murakkab' ? 'selected' : ''}}>Murakkab</option>
              </select>
            </div>

            <!-- Reset Filters -->
            <div class="flex items-end">
              <button onclick="resetMaterialFilters()" class="w-full px-3 py-2 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 text-xs font-semibold transition">
                Filtrlarni tozalash
              </button>
            </div>
          </div>

          <!-- Materials Count Banner -->
          <div class="flex items-center justify-between mb-4">
            <span class="text-xs font-semibold text-slate-500">Topilgan materiallar: <b>${{filtered.length}} ta</b> (jami 200 tadan)</span>
          </div>

          <!-- Materials Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            ${{filtered.map(m => renderMaterialCard(m)).join('')}}
          </div>
        </div>
      `;
    }}

    function resetMaterialFilters() {{
      searchQuery = '';
      selectedGrade = 'Barchasi';
      selectedDifficulty = 'Barchasi';
      navigateTo('materials');
    }}

    function renderMaterialCard(m) {{
      const isCompleted = completedMaterials.includes(m.id);
      const isBookmarked = bookmarkedMaterials.includes(m.id);

      const diffColor = 
        m.difficulty === "Boshlang'ich" ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-950/40 dark:text-emerald-400' :
        m.difficulty === "O'rta" ? 'bg-blue-100 text-blue-700 dark:bg-blue-950/40 dark:text-blue-400' :
        'bg-purple-100 text-purple-700 dark:bg-purple-950/40 dark:text-purple-400';

      return `
        <div class="group flex flex-col justify-between p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200/80 dark:border-slate-800 shadow-sm hover:shadow-xl transition duration-300">
          <div>
            <div class="flex items-center justify-between mb-3 text-xs">
              <span class="font-semibold text-blue-600 dark:text-blue-400">${{m.subject_name}}</span>
              <div class="flex items-center gap-1.5">
                <span class="px-2 py-0.5 rounded font-medium ${{diffColor}}">${{m.difficulty}}</span>
                <span class="px-2 py-0.5 rounded font-medium bg-slate-100 dark:bg-slate-800 text-slate-500">${{m.grade_level}}</span>
              </div>
            </div>

            <h3 onclick="navigateTo('material_reader', '${{m.id}}')" class="font-bold text-base text-slate-900 dark:text-white group-hover:text-blue-600 cursor-pointer transition line-clamp-2">
              ${{m.title}}
            </h3>

            <p class="text-xs text-slate-500 dark:text-slate-400 mt-2 line-clamp-2">
              ${{m.objective}}
            </p>

            <div class="flex flex-wrap gap-1 mt-3">
              ${{m.tags.slice(0, 3).map(t => `<span class="text-[10px] px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-500">#${{t}}</span>`).join('')}}
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
            <span class="text-xs text-slate-400 flex items-center gap-1">
              ⏱ ${{m.duration_minutes}} daqiqa
            </span>

            <div class="flex items-center gap-2">
              <button onclick="toggleBookmark('${{m.id}}')" class="p-1 text-slate-400 hover:text-amber-500 transition" title="Saqlash">
                ${{isBookmarked ? '★' : '☆'}}
              </button>
              <button onclick="navigateTo('material_reader', '${{m.id}}')" class="px-3 py-1.5 rounded-lg bg-blue-50 dark:bg-blue-950/40 text-blue-600 dark:text-blue-300 font-semibold text-xs hover:bg-blue-600 hover:text-white transition">
                O'qish &rarr;
              </button>
            </div>
          </div>
        </div>
      `;
    }}

    function toggleBookmark(materialId) {{
      const idx = bookmarkedMaterials.indexOf(materialId);
      if (idx > -1) {{
        bookmarkedMaterials.splice(idx, 1);
        showToast('Saqlanganlardan olib tashlandi', 'Material xatcho‘plardan chiqarildi', 'info');
      }} else {{
        bookmarkedMaterials.push(materialId);
        showToast('Saqlandi!', 'Material shaxsiy xatcho‘plarga qo‘shildi', 'success');
      }}
      try {{ localStorage.setItem('eh_bookmarks', JSON.stringify(bookmarkedMaterials)); }} catch(e){{}}
      // Re-render
      const curr = document.querySelector('h1')?.textContent;
      if (curr && curr.includes('Kutubxona')) {{
        navigateTo('materials');
      }} else if (curr && curr.includes('Kabinet')) {{
        navigateTo('dashboard');
      }}
    }}

    // ==========================================
    // 5. MATERIAL READER VIEW (FULL LESSON)
    // ==========================================
    function renderMaterialReaderView(materialId) {{
      const m = MATERIALS.find(mat => mat.id === materialId) || MATERIALS[0];
      const isCompleted = completedMaterials.includes(m.id);
      const isBookmarked = bookmarkedMaterials.includes(m.id);

      return `
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <!-- Back button & actions -->
          <div class="flex items-center justify-between mb-6 text-xs">
            <button onclick="navigateTo('materials')" class="inline-flex items-center gap-1 font-semibold text-slate-500 hover:text-blue-600">
              &larr; Materiallar ro'yxatiga qaytish
            </button>
            <div class="flex items-center gap-2">
              <button onclick="speakLessonTheory('${{m.id}}')" id="speechBtn" class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-darkcard text-slate-600 dark:text-slate-300 font-medium hover:bg-slate-50 flex items-center gap-1.5 transition">
                🔊 Tinglash
              </button>
              <button onclick="toggleBookmark('${{m.id}}')" class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-darkcard text-slate-600 dark:text-slate-300 font-medium hover:bg-slate-50 transition">
                ${{isBookmarked ? '★ Saqlangan' : '☆ Saqlash'}}
              </button>
            </div>
          </div>

          <!-- Header Card -->
          <div class="p-6 sm:p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm mb-8">
            <div class="flex flex-wrap items-center gap-2 text-xs mb-3">
              <span class="px-2.5 py-1 rounded-full font-semibold bg-blue-100 text-blue-700 dark:bg-blue-950/40 dark:text-blue-300">${{m.subject_name}}</span>
              <span class="px-2.5 py-1 rounded-full font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400">${{m.grade_level}}</span>
              <span class="px-2.5 py-1 rounded-full font-medium bg-purple-100 text-purple-700 dark:bg-purple-950/40 dark:text-purple-300">${{m.difficulty}}</span>
              <span class="text-slate-400 ml-auto">⏱ ${{m.duration_minutes}} daqiqa o'qish</span>
            </div>

            <h1 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white leading-tight">${{m.title}}</h1>

            <!-- Learning Objective -->
            <div class="mt-5 p-4 rounded-xl bg-blue-50/70 dark:bg-blue-950/30 border-l-4 border-blue-600 text-xs sm:text-sm text-slate-700 dark:text-slate-300">
              <span class="font-bold text-blue-700 dark:text-blue-400">O‘rganish maqsadi:</span> ${{m.objective}}
            </div>
          </div>

          <!-- Theory Section -->
          <div class="p-6 sm:p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm mb-8">
            <h2 class="text-lg font-bold text-slate-900 dark:text-white mb-4 pb-2 border-b border-slate-100 dark:border-slate-800 flex items-center gap-2">
              📖 To‘liq nazariy tushuntirish
            </h2>
            <div id="theoryText" class="prose dark:prose-invert max-w-none text-slate-700 dark:text-slate-300 text-sm sm:text-base leading-relaxed whitespace-pre-line">
              ${{m.theory}}
            </div>
          </div>

          <!-- Examples Section -->
          <div class="p-6 sm:p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm mb-8">
            <h2 class="text-lg font-bold text-slate-900 dark:text-white mb-4 pb-2 border-b border-slate-100 dark:border-slate-800 flex items-center gap-2">
              💡 Amaliy misollar va yechimlar
            </h2>
            <div class="space-y-6">
              ${{m.examples.map((ex, idx) => `
                <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800">
                  <div class="text-xs font-bold text-blue-600 dark:text-blue-400 uppercase tracking-wider mb-1">${{ex.title || `Misol #${{idx+1}}`}}</div>
                  <div class="font-semibold text-slate-900 dark:text-white text-sm mb-3">${{ex.problem}}</div>
                  <div class="text-xs text-slate-600 dark:text-slate-300 whitespace-pre-line pl-3 border-l-2 border-slate-300 dark:border-slate-600 mb-3">${{ex.step_by_step}}</div>
                  <div class="text-xs font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/40 px-3 py-1.5 rounded-lg inline-block">
                    Javob: ${{ex.answer}}
                  </div>
                </div>
              `).join('')}}
            </div>
          </div>

          <!-- Independent Exercise Section -->
          <div class="p-6 sm:p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm mb-8">
            <h2 class="text-lg font-bold text-slate-900 dark:text-white mb-2 flex items-center gap-2">
              ✍️ Mustaqil mashq
            </h2>
            <p class="text-xs text-slate-500 mb-4">O'z bilimingizni mustaqil sinab ko'ring</p>
            
            <div class="p-4 rounded-xl bg-amber-50/60 dark:bg-amber-950/20 border border-amber-200/60 dark:border-amber-900/40 text-sm font-medium text-slate-800 dark:text-slate-200 mb-4">
              ${{m.exercise}}
            </div>

            <!-- Solution Reveal Button -->
            <div>
              <button onclick="toggleSolution('${{m.id}}')" id="solutionBtn-${{m.id}}" class="text-xs font-semibold px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">
                Javob va yechimni ko‘rish
              </button>
              <div id="solutionBox-${{m.id}}" class="hidden mt-3 p-4 rounded-xl bg-emerald-50/60 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-800/40 text-xs sm:text-sm text-emerald-900 dark:text-emerald-200">
                <span class="font-bold">Yechim:</span> ${{m.exercise_solution}}
              </div>
            </div>
          </div>

          <!-- Self-Check Questions -->
          <div class="p-6 sm:p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm mb-8">
            <h2 class="text-lg font-bold text-slate-900 dark:text-white mb-1 flex items-center gap-2">
              🎯 Mavzuni mustahkamlash savollari
            </h2>
            <p class="text-xs text-slate-500 mb-6">Har bir savolga to'g'ri javobni tanlab, bilmingizni darhol tekshiring</p>

            <div class="space-y-6">
              ${{m.check_questions.map((q, qIdx) => `
                <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800/40 border border-slate-100 dark:border-slate-800">
                  <div class="font-semibold text-sm text-slate-900 dark:text-white mb-3">
                    ${{qIdx + 1}}. ${{q.question}}
                  </div>
                  <div class="space-y-2">
                    ${{q.options.map((opt, optIdx) => `
                      <label class="flex items-center gap-3 p-2.5 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-white dark:hover:bg-slate-800 cursor-pointer text-xs sm:text-sm transition">
                        <input type="radio" name="check_q_${{m.id}}_${{qIdx}}" value="${{optIdx}}" onchange="evaluateCheckQuestion('${{m.id}}', ${{qIdx}}, ${{optIdx}}, ${{q.correct_index}})" class="text-blue-600 focus:ring-blue-500">
                        <span>${{opt}}</span>
                      </label>
                    `).join('')}}
                  </div>
                  <div id="checkFeedback_${{m.id}}_${{qIdx}}" class="hidden mt-3 p-3 rounded-lg text-xs"></div>
                </div>
              `).join('')}}
            </div>
          </div>

          <!-- Complete Lesson Button -->
          <div class="p-6 rounded-2xl bg-gradient-to-r from-blue-50 to-indigo-50 dark:from-slate-900 dark:to-slate-800 border border-blue-200 dark:border-blue-900 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
              <div class="text-sm font-bold text-slate-900 dark:text-white">Darsni muvaffaqiyatli yakunladingizmi?</div>
              <div class="text-xs text-slate-500">Tugatilgan deb belgilang va profilingizga +30 XP qo'shing!</div>
            </div>
            <button onclick="markLessonComplete('${{m.id}}')" class="px-5 py-2.5 rounded-xl ${{
              isCompleted ? 'bg-emerald-600 text-white' : 'bg-blue-600 text-white hover:bg-blue-700 shadow-md'
            }} font-semibold text-xs transition">
              ${{isCompleted ? '✓ Dars o‘zlashtirildi (+30 XP)' : 'Darsni yakunlash (+30 XP)'}}
            </button>
          </div>
        </div>
      `;
    }}

    function toggleSolution(materialId) {{
      const box = document.getElementById(`solutionBox-${{materialId}}`);
      const btn = document.getElementById(`solutionBtn-${{materialId}}`);
      box.classList.toggle('hidden');
      btn.textContent = box.classList.contains('hidden') ? 'Javob va yechimni ko‘rish' : 'Yechimni berkitish';
    }}

    function evaluateCheckQuestion(materialId, qIdx, selectedIdx, correctIdx) {{
      const feedback = document.getElementById(`checkFeedback_${{materialId}}_${{qIdx}}`);
      feedback.classList.remove('hidden');
      const m = MATERIALS.find(x => x.id === materialId);
      const q = m.check_questions[qIdx];

      if (selectedIdx === correctIdx) {{
        feedback.className = 'mt-3 p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300 text-xs border border-emerald-200 dark:border-emerald-800';
        feedback.innerHTML = `<b>To‘g‘ri!</b> 🎉 ${{q.explanation}}`;
      }} else {{
        feedback.className = 'mt-3 p-3 rounded-xl bg-rose-50 dark:bg-rose-950/40 text-rose-800 dark:text-rose-300 text-xs border border-rose-200 dark:border-rose-800';
        feedback.innerHTML = `<b>Noto‘g‘ri.</b> To'g'ri javob: <i>${{q.options[correctIdx]}}</i>. ${{q.explanation}}`;
      }}
    }}

    function markLessonComplete(materialId) {{
      if (!completedMaterials.includes(materialId)) {{
        completedMaterials.push(materialId);
        userXP += 30;
        if (currentUser) currentUser.xp = (currentUser.xp || 320) + 30;
        try {{
          localStorage.setItem('eh_completed', JSON.stringify(completedMaterials));
          localStorage.setItem('eh_user', JSON.stringify(currentUser));
        }} catch(e){{}}
        showToast('Tabriklaymiz!', 'Dars yakunlandi. Sizga +30 XP ball berildi!', 'success');
        renderAuthHeader();
        navigateTo('material_reader', materialId);
      }} else {{
        showToast('Ma’lumot', 'Ushbu dars oldin yakunlangan.', 'info');
      }}
    }}

    let isSpeaking = false;
    function speakLessonTheory(materialId) {{
      if (!('speechSynthesis' in window)) {{
        showToast('Xatolik', 'Brauzeringiz matnni ovozlashtirishni qo‘llab-quvvatlamaydi.', 'error');
        return;
      }}
      if (isSpeaking) {{
        window.speechSynthesis.cancel();
        isSpeaking = false;
        document.getElementById('speechBtn').textContent = '🔊 Tinglash';
        return;
      }}
      const m = MATERIALS.find(x => x.id === materialId);
      const textToRead = `${{m.title}}. ${{m.theory}}`;
      const utter = new SpeechSynthesisUtterance(textToRead);
      utter.lang = 'uz-UZ';
      utter.rate = 0.95;
      utter.onend = () => {{
        isSpeaking = false;
        document.getElementById('speechBtn').textContent = '🔊 Tinglash';
      }};
      window.speechSynthesis.speak(utter);
      isSpeaking = true;
      document.getElementById('speechBtn').textContent = '⏹ To‘xtatish';
    }}

    // ==========================================
    // 6. COURSES VIEW
    // ==========================================
    function renderCoursesView() {{
      const courses = [
        {{ id: 'c-01', title: 'Full-Stack Web Dasturlash (HTML, CSS, JS, Node)', duration: '24 soat', level: 'Kasbiy ta’lim', lessons: 12, rating: 4.9 }},
        {{ id: 'c-02', title: 'Oliy matematika va Matematik analiz asoslari', duration: '18 soat', level: 'Universitet', lessons: 10, rating: 4.8 }},
        {{ id: 'c-03', title: 'Ingliz tili: A1 dan B2 gacha grammatika va muloqot', duration: '30 soat', level: 'Umumiy', lessons: 15, rating: 4.9 }},
        {{ id: 'c-04', title: 'Fizika: Mexanika va Elektrodinamika to‘liq kursi', duration: '16 soat', level: '7-11 sinf', lessons: 8, rating: 4.7 }},
        {{ id: 'c-05', title: 'Sun’iy intellekt va Machine Learning ga kirish (Python)', duration: '20 soat', level: 'Kasbiy / IT', lessons: 10, rating: 5.0 }},
        {{ id: 'c-06', title: 'O‘zbekiston tarixi: Qadimgi davrdan mustaqillikkacha', duration: '14 soat', level: 'Maktab / DTМ', lessons: 9, rating: 4.8 }}
      ];

      return `
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="mb-8">
            <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white">Interaktiv kurslar</h1>
            <p class="text-sm text-slate-500 mt-1">Bosqichma-bosqich o‘rganishga mo‘ljallangan to‘liq tizimli o‘quv dasturlari</p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            ${{courses.map(c => `
              <div class="p-6 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl transition duration-300 flex flex-col justify-between">
                <div>
                  <div class="flex items-center justify-between text-xs mb-3">
                    <span class="px-2.5 py-0.5 rounded-full font-medium bg-blue-100 text-blue-700 dark:bg-blue-900/40 dark:text-blue-300">${{c.level}}</span>
                    <span class="text-amber-500 font-bold">★ ${{c.rating}}</span>
                  </div>
                  <h3 class="font-bold text-lg text-slate-900 dark:text-white mb-2">${{c.title}}</h3>
                  <div class="text-xs text-slate-500 flex items-center gap-3 mt-4">
                    <span>⏱ ${{c.duration}}</span>
                    <span>•</span>
                    <span>📚 ${{c.lessons}} ta modul</span>
                  </div>
                </div>

                <div class="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                  <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400">100% Bepul</span>
                  <button onclick="startCourseEnrollment('${{c.title}}')" class="px-4 py-2 rounded-xl bg-blue-600 text-white text-xs font-semibold hover:bg-blue-700 shadow-sm transition">
                    Kursga yozilish &rarr;
                  </button>
                </div>
              </div>
            `).join('')}}
          </div>
        </div>
      `;
    }}

    function startCourseEnrollment(courseTitle) {{
      showToast('Kursga yozildingiz!', `'${{courseTitle}}' kursi sizning shaxsiy kabinetingizga biriktirildi.`, 'success');
      navigateTo('dashboard');
    }}

    // ==========================================
    // 7. TESTS CENTER VIEW
    // ==========================================
    function renderTestsCenterView() {{
      const quizCategories = [
        {{ id: 'q-math', title: 'Matematika va Algebra bo‘yicha umumiy test', subject: 'Matematika', count: 10, time: 15, xp: 80 }},
        {{ id: 'q-phy', title: 'Fizika: Mexanika va Termodinamika sinovi', subject: 'Fizika', count: 8, time: 12, xp: 70 }},
        {{ id: 'q-chem', title: 'Kimyo: Moddalar va kimyoviy reaksiyalar', subject: 'Kimyo', count: 8, time: 12, xp: 70 }},
        {{ id: 'q-bio', title: 'Biologiya va Inson salomatligi testi', subject: 'Biologiya', count: 10, time: 15, xp: 80 }},
        {{ id: 'q-eng', title: 'Ingliz tili: Grammatika va so‘z boyligi (B1-B2)', subject: 'Ingliz tili', count: 10, time: 15, xp: 80 }},
        {{ id: 'q-hist', title: 'O‘zbekiston tarixi: Amir Temur va Renessans', subject: 'Tarix', count: 10, time: 15, xp: 80 }},
        {{ id: 'q-it', title: 'Informatika va Dasturlash asoslari sinovi', subject: 'Dasturlash', count: 10, time: 15, xp: 100 }}
      ];

      return `
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="mb-8">
            <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white">Interaktiv Testlar Markazi</h1>
            <p class="text-sm text-slate-500 mt-1">Bilimlaringizni sinovdan o'tkazing, avtomatik natija oling va reyting ballarini (XP) jamg'aring</p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            ${{quizCategories.map(q => `
              <div class="p-6 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl transition duration-300 flex flex-col justify-between">
                <div>
                  <div class="flex items-center justify-between text-xs mb-3">
                    <span class="px-2.5 py-0.5 rounded font-semibold bg-blue-100 text-blue-700 dark:bg-blue-900/40 dark:text-blue-300">${{q.subject}}</span>
                    <span class="text-purple-600 dark:text-purple-400 font-bold">+${{q.xp}} XP</span>
                  </div>
                  <h3 class="font-bold text-base text-slate-900 dark:text-white mb-2">${{q.title}}</h3>
                  <div class="text-xs text-slate-500 space-y-1 mt-3">
                    <div>Savollar soni: <b>${{q.count}} ta</b></div>
                    <div>Vaqt chegarasi: <b>${{q.time}} daqiqa</b></div>
                    <div>O'tish balli: <b>60%</b></div>
                  </div>
                </div>

                <div class="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800">
                  <button onclick="startQuizArena('${{q.id}}')" class="w-full py-2.5 rounded-xl bg-blue-600 text-white text-xs font-semibold hover:bg-blue-700 shadow-md shadow-blue-500/20 transition">
                    Testni boshlash &rarr;
                  </button>
                </div>
              </div>
            `).join('')}}
          </div>
        </div>
      `;
    }}

    function startQuizArena(quizId) {{
      // Select questions randomly from materials
      const pool = [];
      MATERIALS.forEach(m => {{
        if (m.check_questions && m.check_questions.length > 0) {{
          m.check_questions.forEach(q => {{
            pool.push({{
              ...q,
              subject_name: m.subject_name,
              material_title: m.title
            }});
          }});
        }}
      }});

      // Shuffle and pick 10 questions
      const shuffled = pool.sort(() => 0.5 - Math.random()).slice(0, 10);
      currentQuiz = {{
        id: quizId,
        title: 'Kompleks bilim sinovi testi',
        questions: shuffled,
        totalTimeSeconds: 10 * 60, // 10 minutes
        startTime: Date.now()
      }};

      quizRemainingSeconds = currentQuiz.totalTimeSeconds;
      quizSelectedAnswers = {{}};

      navigateTo('quiz_arena', quizId);
    }}

    // ==========================================
    // 8. QUIZ ARENA VIEW (ACTIVE TEST)
    // ==========================================
    function renderQuizArenaView() {{
      if (!currentQuiz) return renderTestsCenterView();

      return `
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <!-- Quiz Top Bar: Title & Timer -->
          <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm flex items-center justify-between mb-8 sticky top-20 z-30 backdrop-blur">
            <div>
              <h2 class="text-base font-bold text-slate-900 dark:text-white">${{currentQuiz.title}}</h2>
              <div class="text-xs text-slate-500">Jami ${{currentQuiz.questions.length}} ta savol</div>
            </div>

            <!-- Timer Badge -->
            <div class="flex items-center gap-2">
              <span class="text-xs text-slate-400">Qolgan vaqt:</span>
              <div id="quizTimerDisplay" class="px-3 py-1.5 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-600 dark:text-amber-400 font-mono font-bold text-base">
                10:00
              </div>
            </div>
          </div>

          <!-- Questions List -->
          <div class="space-y-6">
            ${{currentQuiz.questions.map((q, idx) => `
              <div class="p-6 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
                <div class="flex items-center justify-between text-xs text-slate-400 mb-2">
                  <span>Savol #${{idx + 1}}</span>
                  <span class="text-blue-600 font-semibold">${{q.subject_name}}</span>
                </div>
                <h3 class="text-base font-bold text-slate-900 dark:text-white mb-4">${{q.question}}</h3>

                <div class="space-y-2.5">
                  ${{q.options.map((opt, optIdx) => `
                    <label class="flex items-center gap-3 p-3 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 cursor-pointer text-xs sm:text-sm transition">
                      <input type="radio" name="arena_q_${{idx}}" value="${{optIdx}}" onchange="quizSelectedAnswers[${{idx}}] = ${{optIdx}}" class="text-blue-600 focus:ring-blue-500">
                      <span>${{opt}}</span>
                    </label>
                  `).join('')}}
                </div>
              </div>
            `).join('')}}
          </div>

          <!-- Finish Quiz Button -->
          <div class="mt-8 text-center">
            <button onclick="finishQuiz()" class="px-8 py-3.5 rounded-xl bg-gradient-to-r from-blue-600 to-teal-500 text-white font-bold text-sm shadow-xl shadow-blue-500/25 hover:opacity-95 transition">
              Testni yakunlash va natijani hisoblash &rarr;
            </button>
          </div>
        </div>
      `;
    }}

    function startQuizTimer() {{
      const timerDisplay = document.getElementById('quizTimerDisplay');
      if (!timerDisplay) return;

      quizTimerInterval = setInterval(() => {{
        quizRemainingSeconds--;
        if (quizRemainingSeconds <= 0) {{
          clearInterval(quizTimerInterval);
          finishQuiz(true); // timed out
          return;
        }}
        const mins = Math.floor(quizRemainingSeconds / 60);
        const secs = quizRemainingSeconds % 60;
        timerDisplay.textContent = `${{mins.toString().padStart(2, '0')}}:${{secs.toString().padStart(2, '0')}}`;
      }}, 1000);
    }}

    function finishQuiz(isTimeout = false) {{
      if (quizTimerInterval) {{
        clearInterval(quizTimerInterval);
        quizTimerInterval = null;
      }}

      if (!currentQuiz) return;

      // Server-side style calculation
      let score = 0;
      const breakdown = [];

      currentQuiz.questions.forEach((q, idx) => {{
        const userChoice = quizSelectedAnswers[idx];
        const isCorrect = userChoice === q.correct_index;
        if (isCorrect) score++;

        breakdown.push({{
          question: q.question,
          options: q.options,
          userChoice: userChoice !== undefined ? userChoice : null,
          correctChoice: q.correct_index,
          isCorrect: isCorrect,
          explanation: q.explanation
        }});
      }});

      const total = currentQuiz.questions.length;
      const percentage = Math.round((score / total) * 100);
      const passed = percentage >= 60;
      const earnedXP = passed ? (50 + score * 10) : 10;

      // Update User XP
      userXP += earnedXP;
      if (currentUser) {{
        currentUser.xp = (currentUser.xp || 320) + earnedXP;
        try {{ localStorage.setItem('eh_user', JSON.stringify(currentUser)); }} catch(e){{}}
      }}

      const resultObj = {{
        date: new Date().toLocaleDateString('uz-UZ'),
        title: currentQuiz.title,
        score,
        total,
        percentage,
        passed,
        earnedXP,
        breakdown
      }};

      quizHistory.unshift(resultObj);
      try {{ localStorage.setItem('eh_quiz_history', JSON.stringify(quizHistory)); }} catch(e){{}}

      renderAuthHeader();
      navigateTo('results', resultObj);
    }}

    // ==========================================
    // 9. RESULTS VIEW
    // ==========================================
    function renderResultsView(result) {{
      if (!result) return renderTestsCenterView();

      return `
        <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <!-- Summary Banner -->
          <div class="p-8 rounded-3xl ${{
            result.passed ? 'bg-gradient-to-r from-emerald-600 to-teal-600' : 'bg-gradient-to-r from-rose-600 to-amber-600'
          }} text-white text-center shadow-xl mb-8">
            <div class="text-5xl mb-2">${{result.passed ? '🏆' : '📚'}}</div>
            <h1 class="text-2xl sm:text-3xl font-extrabold mb-1">
              ${{result.passed ? 'Ajoyib natija! Test muvaffaqiyatli topshirildi' : 'Sinov yakunlandi. Yana bir bor urinib ko‘ring'}}
            </h1>
            <p class="text-xs sm:text-sm text-white/80">${{result.title}}</p>

            <div class="mt-6 flex items-center justify-center gap-6">
              <div class="bg-black/20 p-3 rounded-2xl min-w-[90px]">
                <div class="text-2xl font-black">${{result.score}} / ${{result.total}}</div>
                <div class="text-[10px] text-white/70">To'g'ri javoblar</div>
              </div>
              <div class="bg-black/20 p-3 rounded-2xl min-w-[90px]">
                <div class="text-2xl font-black">${{result.percentage}}%</div>
                <div class="text-[10px] text-white/70">O'zlashtirish</div>
              </div>
              <div class="bg-black/20 p-3 rounded-2xl min-w-[90px]">
                <div class="text-2xl font-black text-amber-300">+${{result.earnedXP}}</div>
                <div class="text-[10px] text-white/70">XP berildi</div>
              </div>
            </div>

            <div class="mt-6 flex justify-center gap-3">
              <button onclick="navigateTo('tests')" class="px-5 py-2 rounded-xl bg-white text-slate-800 text-xs font-bold hover:bg-white/90 transition">
                Yana test ishlash
              </button>
              <button onclick="navigateTo('dashboard')" class="px-5 py-2 rounded-xl bg-black/30 text-white text-xs font-semibold hover:bg-black/40 transition">
                Dashboardga o'tish
              </button>
            </div>
          </div>

          <!-- Answer Breakdown Analysis -->
          <div class="space-y-4">
            <h2 class="text-lg font-bold text-slate-900 dark:text-white mb-4">Har bir savol bo‘yicha tahlil:</h2>
            ${{result.breakdown.map((item, i) => `
              <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border ${{
                item.isCorrect ? 'border-emerald-200 dark:border-emerald-900/40' : 'border-rose-200 dark:border-rose-900/40'
              }} shadow-sm">
                <div class="flex items-center gap-2 mb-2 text-xs font-bold ${{
                  item.isCorrect ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400'
                }}">
                  <span>${{item.isCorrect ? '✓ To‘g‘ri' : '✕ Noto‘g‘ri'}}</span>
                  <span class="text-slate-400 font-normal">Savol #${{i+1}}</span>
                </div>
                <div class="text-sm font-semibold text-slate-900 dark:text-white mb-3">${{item.question}}</div>

                <div class="text-xs space-y-1 text-slate-600 dark:text-slate-400">
                  <div>Sizning javobingiz: <b class="${{item.isCorrect ? 'text-emerald-600' : 'text-rose-600'}}">${{item.userChoice !== null ? item.options[item.userChoice] : 'Javob berilmagan'}}</b></div>
                  ${{!item.isCorrect ? `<div>To'g'ri javob: <b class="text-emerald-600">${{item.options[item.correctChoice]}}</b></div>` : ''}}
                </div>

                <div class="mt-3 p-2.5 rounded-lg bg-slate-50 dark:bg-slate-800/60 text-xs text-slate-500 dark:text-slate-400">
                  <b>Izoh:</b> ${{item.explanation}}
                </div>
              </div>
            `).join('')}}
          </div>
        </div>
      `;
    }}

    // ==========================================
    // 10. DASHBOARD VIEW (PERSONAL CABINET)
    // ==========================================
    function renderDashboardView() {{
      const user = currentUser || {{ name: 'Mehmon', email: 'guest@edu.uz', role: 'student', xp: 120 }};
      const completedCount = completedMaterials.length;
      const bookmarkCount = bookmarkedMaterials.length;

      return `
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <!-- Profile Quick Header -->
          <div class="p-6 sm:p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm mb-8 flex flex-col sm:flex-row items-center gap-6 justify-between">
            <div class="flex items-center gap-4 text-center sm:text-left">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-blue-600 to-indigo-600 text-white font-black text-2xl flex items-center justify-center shadow-lg">
                ${{user.name.substring(0, 2)}}
              </div>
              <div>
                <h1 class="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">${{user.name}}</h1>
                <p class="text-xs text-slate-500">${{user.email}} • <span class="capitalize text-blue-600 font-semibold">${{user.role}}</span></p>
                <div class="mt-2 inline-flex items-center gap-2 text-xs font-bold text-amber-500 bg-amber-50 dark:bg-amber-950/40 px-2.5 py-1 rounded-lg">
                  ⚡ ${{user.xp || 320}} XP ball • 3-Darajali Bilimdon
                </div>
              </div>
            </div>

            <div class="flex items-center gap-3">
              <button onclick="navigateTo('achievements')" class="px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 text-xs font-semibold hover:bg-slate-50 dark:hover:bg-slate-800 transition">
                Yutuqlar & Badjlar
              </button>
              <button onclick="navigateTo('materials')" class="px-4 py-2 rounded-xl bg-blue-600 text-white text-xs font-semibold hover:bg-blue-700 transition">
                Darslarni davom ettirish &rarr;
              </button>
            </div>
          </div>

          <!-- Quick Stats Grid -->
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-5 mb-8">
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">O'zlashtirilgan darslar</div>
              <div class="text-2xl font-black text-blue-600 mt-1">${{completedCount}} ta</div>
              <div class="text-[10px] text-slate-400 mt-1">200 tadan ${{Math.round((completedCount/200)*100)}}% i</div>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">Topshirilgan testlar</div>
              <div class="text-2xl font-black text-emerald-600 mt-1">${{quizHistory.length || 3}} ta</div>
              <div class="text-[10px] text-slate-400 mt-1">O'rtacha 85% aniqlik</div>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">Saqlangan xatcho'plar</div>
              <div class="text-2xl font-black text-purple-600 mt-1">${{bookmarkCount}} ta</div>
              <div class="text-[10px] text-slate-400 mt-1">Tezkor o'qish uchun</div>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">Uzluksiz kunlar (Streak)</div>
              <div class="text-2xl font-black text-amber-500 mt-1">🔥 5 kun</div>
              <div class="text-[10px] text-slate-400 mt-1">Ajoyib intizom!</div>
            </div>
          </div>

          <!-- Charts & Progress Section -->
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
            <!-- Weekly Progress Chart -->
            <div class="lg:col-span-2 p-6 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <h3 class="text-base font-bold text-slate-900 dark:text-white mb-4">Haftalik o'rganish faolligi (Daqiqalar)</h3>
              <div class="relative h-64">
                <canvas id="weeklyActivityChart"></canvas>
              </div>
            </div>

            <!-- Subject Progress Pie / Summary -->
            <div class="p-6 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm flex flex-col justify-between">
              <div>
                <h3 class="text-base font-bold text-slate-900 dark:text-white mb-4">Mavzular taqsimoti</h3>
                <div class="space-y-3 text-xs">
                  <div>
                    <div class="flex justify-between mb-1">
                      <span>Aniq fanlar</span>
                      <b>45%</b>
                    </div>
                    <div class="w-full bg-slate-100 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                      <div class="bg-blue-600 h-full w-[45%]"></div>
                    </div>
                  </div>
                  <div>
                    <div class="flex justify-between mb-1">
                      <span>Dasturlash & IT</span>
                      <b>70%</b>
                    </div>
                    <div class="w-full bg-slate-100 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                      <div class="bg-teal-500 h-full w-[70%]"></div>
                    </div>
                  </div>
                  <div>
                    <div class="flex justify-between mb-1">
                      <span>Tillar va adabiyot</span>
                      <b>30%</b>
                    </div>
                    <div class="w-full bg-slate-100 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                      <div class="bg-purple-600 h-full w-[30%]"></div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800">
                <button onclick="navigateTo('tests')" class="w-full py-2.5 rounded-xl bg-blue-600 text-white font-semibold text-xs hover:bg-blue-700 transition">
                  Yangi test sinovini boshlash
                </button>
              </div>
            </div>
          </div>

          <!-- Bookmarked Materials Row -->
          <div>
            <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-4">Saqlangan materiallar</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              ${{bookmarkedMaterials.map(id => {{
                const m = MATERIALS.find(x => x.id === id);
                if (!m) return '';
                return renderMaterialCard(m);
              }}).join('') || '<div class="text-sm text-slate-400 p-4">Hozircha saqlangan materiallar yo‘q.</div>'}}
            </div>
          </div>
        </div>
      `;
    }}

    function initDashboardChart() {{
      const ctx = document.getElementById('weeklyActivityChart');
      if (!ctx) return;

      new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: ['Dush', 'Sesh', 'Chor', 'Pay', 'Jum', 'Shan', 'Yak'],
          datasets: [{{
            label: 'O‘rganish vaqti (daqiqa)',
            data: [35, 45, 20, 60, 50, 75, 40],
            backgroundColor: '#3b82f6',
            borderRadius: 8
          }}]
        }},
        options: {{
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }}
          }},
          scales: {{
            y: {{
              beginAtZero: true,
              grid: {{ color: 'rgba(100, 116, 139, 0.1)' }}
            }},
            x: {{
              grid: {{ display: false }}
            }}
          }}
        }}
      }});
    }}

    // ==========================================
    // 11. TEACHER STUDIO VIEW
    // ==========================================
    function renderTeacherStudioView() {{
      return `
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-8">
            <div>
              <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white">O‘qituvchi Studiyasi (Teacher Studio)</h1>
              <p class="text-sm text-slate-500 mt-1">Yangi ta’limiy materiallar, darslar va testlar yaratish maydoni</p>
            </div>
            <button onclick="navigateTo('teacher_new')" class="px-5 py-2.5 rounded-xl bg-blue-600 text-white font-bold text-xs hover:bg-blue-700 shadow-md shadow-blue-500/20 transition flex items-center gap-2">
              <span>+</span> Yangi material yaratish
            </button>
          </div>

          <!-- Studio Metrics -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-5 mb-8">
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">Yaratilgan materiallaringiz</div>
              <div class="text-2xl font-black text-blue-600 mt-1">14 ta</div>
              <div class="text-[10px] text-emerald-600 font-semibold mt-1">Barchasi moderatsiyadan o‘tgan</div>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">O'quvchilar tomonidan ko'rilishi</div>
              <div class="text-2xl font-black text-purple-600 mt-1">12,480 marta</div>
              <div class="text-[10px] text-slate-400 mt-1">Oxirgi 30 kunda</div>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">O'rtacha baho</div>
              <div class="text-2xl font-black text-amber-500 mt-1">4.95 / 5.0</div>
              <div class="text-[10px] text-slate-400 mt-1">98 ta fikr-mulohaza</div>
            </div>
          </div>

          <!-- Teacher Materials Table -->
          <div class="bg-white dark:bg-darkcard rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm overflow-hidden">
            <div class="p-5 border-b border-slate-100 dark:border-slate-800 flex items-center justify-between">
              <h3 class="font-bold text-base text-slate-900 dark:text-white">Mening materiallarim</h3>
              <span class="text-xs text-slate-400">Jami 14 ta yozuv</span>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-50 dark:bg-slate-800/60 text-slate-500 font-semibold border-b border-slate-100 dark:border-slate-800">
                  <tr>
                    <th class="p-4">Mavzu nomi</th>
                    <th class="p-4">Fan</th>
                    <th class="p-4">Sinf</th>
                    <th class="p-4">Status</th>
                    <th class="p-4">Ko'rishlar</th>
                    <th class="p-4 text-right">Amallar</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
                  ${{MATERIALS.slice(0, 5).map(m => `
                    <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition">
                      <td class="p-4 font-semibold text-slate-900 dark:text-white">${{m.title}}</td>
                      <td class="p-4 text-slate-500">${{m.subject_name}}</td>
                      <td class="p-4 text-slate-500">${{m.grade_level}}</td>
                      <td class="p-4"><span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-100 text-emerald-700 dark:bg-emerald-950/40 dark:text-emerald-400">Nashr etilgan</span></td>
                      <td class="p-4 text-slate-500">${{m.duration_minutes * 35}} marta</td>
                      <td class="p-4 text-right space-x-2">
                        <button onclick="navigateTo('material_reader', '${{m.id}}')" class="text-blue-600 hover:underline">Ko'rish</button>
                        <button onclick="showToast('Tahrirlash', 'Tahrirlash oynasi ochilmoqda...', 'info')" class="text-amber-600 hover:underline">Tahrirlash</button>
                      </td>
                    </tr>
                  `).join('')}}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      `;
    }}

    // ==========================================
    // 12. TEACHER CREATE NEW MATERIAL VIEW
    // ==========================================
    function renderTeacherNewMaterialView() {{
      return `
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <button onclick="navigateTo('teacher')" class="inline-flex items-center gap-1.5 text-xs font-semibold text-slate-500 hover:text-blue-600 mb-6">
            &larr; O'qituvchi studiyasiga qaytish
          </button>

          <div class="p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
            <h1 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">Yangi o‘quv materiali yaratish</h1>
            <p class="text-xs text-slate-500 mb-8">Pedagogik talablarga mos to'liq nazariya, misollar va tekshiruv savollarini kiriting</p>

            <form onsubmit="handleCreateMaterial(event)" class="space-y-6 text-xs sm:text-sm">
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <!-- Subject -->
                <div>
                  <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Fan *</label>
                  <select id="newMatSubject" required class="w-full px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white">
                    ${{SUBJECTS.map(s => `<option value="${{s.id}}">${{s.name}}</option>`).join('')}}
                  </select>
                </div>

                <!-- Grade -->
                <div>
                  <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Sinf / Bosqich *</label>
                  <input id="newMatGrade" type="text" placeholder="Masalan: 8-sinf" required class="w-full px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white">
                </div>

                <!-- Difficulty -->
                <div>
                  <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Qiyinlik darajasi *</label>
                  <select id="newMatDifficulty" class="w-full px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white">
                    <option value="Boshlang'ich">Boshlang'ich</option>
                    <option value="O'rta" selected>O'rta</option>
                    <option value="Murakkab">Murakkab</option>
                  </select>
                </div>
              </div>

              <!-- Title -->
              <div>
                <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Mavzu nomi (Sarlavha) *</label>
                <input id="newMatTitle" type="text" placeholder="Mavzuning to'liq va aniq nomini kiriting..." required class="w-full px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white">
              </div>

              <!-- Objective -->
              <div>
                <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">O‘rganish maqsadi *</label>
                <input id="newMatObjective" type="text" placeholder="O'quvchi ushbu darsdan keyin nimani o'rganadi?" required class="w-full px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white">
              </div>

              <!-- Theory -->
              <div>
                <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">To‘liq nazariy tushuntirish *</label>
                <textarea id="newMatTheory" rows="6" placeholder="Batafsil nazariya, qoidalar, formulalar va izohlar..." required class="w-full px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white"></textarea>
              </div>

              <!-- Practical Examples -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">1-Amaliy misol va yechim *</label>
                  <textarea id="newMatExample1" rows="3" placeholder="1-misol va qadamma-qadam yechimi..." required class="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white"></textarea>
                </div>
                <div>
                  <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">2-Amaliy misol va yechim *</label>
                  <textarea id="newMatExample2" rows="3" placeholder="2-misol va qadamma-qadam yechimi..." required class="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white"></textarea>
                </div>
              </div>

              <!-- Exercise & Solution -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Mustaqil mashq topshirig'i *</label>
                  <input id="newMatExercise" type="text" placeholder="O'quvchi mustaqil yechishi uchun mashq..." required class="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white">
                </div>
                <div>
                  <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Mashqning to'g'ri javobi / yechimi *</label>
                  <input id="newMatExerciseSol" type="text" placeholder="Mashq javobi..." required class="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:outline-none dark:text-white">
                </div>
              </div>

              <!-- Submit Buttons -->
              <div class="pt-4 flex items-center justify-end gap-3">
                <button type="button" onclick="navigateTo('teacher')" class="px-5 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 font-semibold text-xs hover:bg-slate-50">
                  Bekor qilish
                </button>
                <button type="submit" class="px-6 py-2.5 rounded-xl bg-blue-600 text-white font-bold text-xs hover:bg-blue-700 shadow-md shadow-blue-500/20">
                  Materialni saqlash & Nashr etish
                </button>
              </div>
            </form>
          </div>
        </div>
      `;
    }}

    function handleCreateMaterial(e) {{
      e.preventDefault();
      const subjectId = document.getElementById('newMatSubject').value;
      const subject = SUBJECTS.find(s => s.id === subjectId);
      const title = document.getElementById('newMatTitle').value;
      const grade = document.getElementById('newMatGrade').value;
      const diff = document.getElementById('newMatDifficulty').value;
      const obj = document.getElementById('newMatObjective').value;
      const theory = document.getElementById('newMatTheory').value;
      const ex1 = document.getElementById('newMatExample1').value;
      const ex2 = document.getElementById('newMatExample2').value;
      const exercise = document.getElementById('newMatExercise').value;
      const sol = document.getElementById('newMatExerciseSol').value;

      const newId = `mat-${{Date.now()}}`;
      const newSlug = title.toLowerCase().replace(/[^a-z0-9]/g, '-');

      const createdMat = {{
        id: newId,
        slug: newSlug,
        subject_id: subjectId,
        subject_name: subject ? subject.name : 'Maxsus fan',
        title: title,
        grade_level: grade,
        difficulty: diff,
        objective: obj,
        theory: theory,
        examples: [
          {{ title: '1-Misol', problem: ex1, step_by_step: ex1, answer: 'Hisoblangan' }},
          {{ title: '2-Misol', problem: ex2, step_by_step: ex2, answer: 'Yechilgan' }}
        ],
        exercise: exercise,
        exercise_solution: sol,
        check_questions: [
          {{ question: 'Mavzuning asosiy g‘oyasi nima?', options: ['Fakt 1', 'To‘g‘ri tushuncha', 'Xato variant', 'Boshqa'], correct_index: 1, explanation: 'Nazariyaga ko‘ra.' }},
          {{ question: 'Amaliy qo‘llanilishi qayerda?', options: ['Amalda', 'Faqat kitobda', 'Hech qayerda', 'Barchasida'], correct_index: 3, explanation: 'Ko‘p sohalarda.' }},
          {{ question: 'Xulosa to‘g‘rimi?', options: ['Ha', 'Yo‘q', 'Qisman', 'Noma’lum'], correct_index: 0, explanation: 'Qoidaga ko‘ra ha.' }}
        ],
        tags: ['yangi', 'o‘qituvchi', 'dars'],
        duration_minutes: 25
      }};

      MATERIALS.unshift(createdMat);
      showToast('Muvaffaqiyatli saqlandi!', `'${{title}}' yangi materiali kutubxonaga qo‘shildi.`, 'success');
      navigateTo('materials');
    }}

    // ==========================================
    // 13. ADMIN PANEL VIEW
    // ==========================================
    function renderAdminPanelView() {{
      return `
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="mb-8">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-amber-100 text-amber-800 dark:bg-amber-950/40 dark:text-amber-400 mb-2">
              🛡️ Boshqaruv & Nazorat
            </div>
            <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white">Administrator Paneli (Admin Console)</h1>
            <p class="text-sm text-slate-500 mt-1">Platforma statistikasi, foydalanuvchilar rollari va materiallar moderatsiyasi</p>
          </div>

          <!-- Admin Quick Stats -->
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-5 mb-8">
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">Jami Foydalanuvchilar</div>
              <div class="text-2xl font-black text-blue-600 mt-1">42,850 nafar</div>
              <div class="text-[10px] text-emerald-500 font-semibold mt-1">Faol o‘sish: +12% oyiga</div>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">Faol Fanlar</div>
              <div class="text-2xl font-black text-teal-600 mt-1">52 ta fan</div>
              <div class="text-[10px] text-slate-400 mt-1">Barcha 6 ta asosiy yo‘nalish</div>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">Tekshirilgan Materiallar</div>
              <div class="text-2xl font-black text-purple-600 mt-1">${{MATERIALS.length}} ta</div>
              <div class="text-[10px] text-emerald-500 font-semibold mt-1">100% Pedagogik tekshiruvdan o'tgan</div>
            </div>
            <div class="p-5 rounded-2xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
              <div class="text-xs text-slate-400">Server & DB Salomatligi</div>
              <div class="text-2xl font-black text-emerald-500 mt-1">99.98%</div>
              <div class="text-[10px] text-slate-400 mt-1">PostgreSQL & Edge API Barqaror</div>
            </div>
          </div>

          <!-- Admin Tabs Content: User Management & Moderation -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- User Roles Management -->
            <div class="bg-white dark:bg-darkcard rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm p-6">
              <h3 class="text-base font-bold text-slate-900 dark:text-white mb-4">Foydalanuvchilar & Rollar (RBAC)</h3>
              <div class="space-y-3 text-xs">
                <div class="flex items-center justify-between p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60">
                  <div>
                    <div class="font-bold text-slate-900 dark:text-white">Temur Aliyev (Siz)</div>
                    <div class="text-slate-400">temur@edu.uz</div>
                  </div>
                  <span class="px-2.5 py-1 rounded-full font-semibold bg-blue-100 text-blue-700 dark:bg-blue-900/40 dark:text-blue-300">Administrator</span>
                </div>
                <div class="flex items-center justify-between p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60">
                  <div>
                    <div class="font-bold text-slate-900 dark:text-white">Malika Qodirova</div>
                    <div class="text-slate-400">malika@maktab.uz</div>
                  </div>
                  <span class="px-2.5 py-1 rounded-full font-semibold bg-teal-100 text-teal-700 dark:bg-teal-900/40 dark:text-teal-300">O'qituvchi</span>
                </div>
                <div class="flex items-center justify-between p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60">
                  <div>
                    <div class="font-bold text-slate-900 dark:text-white">Jasur Ismoilov</div>
                    <div class="text-slate-400">jasur@student.uz</div>
                  </div>
                  <span class="px-2.5 py-1 rounded-full font-semibold bg-purple-100 text-purple-700 dark:bg-purple-900/40 dark:text-purple-300">Talaba</span>
                </div>
              </div>
            </div>

            <!-- Moderation Queue -->
            <div class="bg-white dark:bg-darkcard rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm p-6">
              <h3 class="text-base font-bold text-slate-900 dark:text-white mb-4">Kontent Moderatsiyasi Navbati</h3>
              <div class="space-y-3 text-xs">
                <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 flex items-center justify-between">
                  <div>
                    <div class="font-semibold text-slate-900 dark:text-white">Trigonometrik tenglamalar amaliyoti</div>
                    <div class="text-slate-400">Muallif: Rustam domla • Matematika</div>
                  </div>
                  <div class="flex items-center gap-2">
                    <button onclick="showToast('Tasdiqlandi', 'Material ommaviy nashrga chiqarildi.', 'success')" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-semibold">Tasdiqlash</button>
                    <button onclick="showToast('Rad etildi', 'Material qayta ishlashga qaytarildi.', 'info')" class="px-2.5 py-1 rounded-lg bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300 font-semibold">Qaytarish</button>
                  </div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 flex items-center justify-between">
                  <div>
                    <div class="font-semibold text-slate-900 dark:text-white">Kvant fizikasi fotoeffekt qonuni</div>
                    <div class="text-slate-400">Muallif: Ziyoda opa • Fizika</div>
                  </div>
                  <div class="flex items-center gap-2">
                    <button onclick="showToast('Tasdiqlandi', 'Material ommaviy nashrga chiqarildi.', 'success')" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-semibold">Tasdiqlash</button>
                    <button onclick="showToast('Rad etildi', 'Material qayta ishlashga qaytarildi.', 'info')" class="px-2.5 py-1 rounded-lg bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300 font-semibold">Qaytarish</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    // ==========================================
    // 14. ACHIEVEMENTS & GAMIFICATION VIEW
    // ==========================================
    function renderAchievementsView() {{
      const badges = [
        {{ title: 'Birinchi qadam', desc: 'Dastlabki ta’limiy materialni o‘zlashtirdingiz', icon: '🌱', xp: 50, unlocked: true }},
        {{ title: 'Bilimdon sinovchi', desc: 'Testda 100% a’lo natijaga erishdingiz', icon: '🏆', xp: 100, unlocked: true }},
        {{ title: 'Sabrli o‘rganuvchi', desc: 'Ketma-ket 3 kun tizimda dars qildingiz', icon: '🔥', xp: 75, unlocked: true }},
        {{ title: 'Matematik daho', desc: 'Aniq fanlar bo‘yicha 10 ta darsni yakunladingiz', icon: '📐', xp: 150, unlocked: false }},
        {{ title: 'Poliglot', desc: 'Chet tillari bo‘yicha 10 ta mavzuni o‘zlashtirdingiz', icon: '🌍', xp: 150, unlocked: false }},
        {{ title: 'Kelajak dasturchisi', desc: 'Dasturlash va IT modullarini a’lo bitirdingiz', icon: '💻', xp: 200, unlocked: false }}
      ];

      return `
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="mb-8 text-center max-w-xl mx-auto">
            <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white">Yutuqlar & XP Reytingi</h1>
            <p class="text-sm text-slate-500 mt-1">Darslarni o‘rganing, testlarni yeching va yangi maxsus nishonlarni oching!</p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            ${{badges.map(b => `
              <div class="p-6 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm ${{
                b.unlocked ? '' : 'opacity-60 grayscale'
              }} flex items-start gap-4">
                <div class="text-4xl p-3 rounded-2xl bg-slate-50 dark:bg-slate-800">${{b.icon}}</div>
                <div>
                  <div class="flex items-center gap-2">
                    <h3 class="font-bold text-base text-slate-900 dark:text-white">${{b.title}}</h3>
                    ${{b.unlocked ? '<span class="text-xs text-emerald-500 font-bold">✓</span>' : '<span class="text-xs text-slate-400">🔒</span>'}}
                  </div>
                  <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">${{b.desc}}</p>
                  <div class="mt-3 text-xs font-bold text-purple-600 dark:text-purple-400">+${{b.xp}} XP</div>
                </div>
              </div>
            `).join('')}}
          </div>
        </div>
      `;
    }}

    // ==========================================
    // 15. PROFILE VIEW
    // ==========================================
    function renderProfileView() {{
      const user = currentUser || {{ name: 'Temur Aliyev', email: 'temur@edu.uz', role: 'student', grade: '9-sinf', xp: 320 }};

      return `
        <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
            <h1 class="text-2xl font-bold text-slate-900 dark:text-white mb-6">Shaxsiy Profil Ma'lumotlari</h1>

            <div class="space-y-4 text-xs sm:text-sm">
              <div>
                <label class="block font-semibold text-slate-500 mb-1">To'liq ism</label>
                <input type="text" value="${{user.name}}" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 dark:text-white">
              </div>
              <div>
                <label class="block font-semibold text-slate-500 mb-1">Elektron pochta</label>
                <input type="email" value="${{user.email}}" disabled class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-800/40 text-slate-400">
              </div>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="block font-semibold text-slate-500 mb-1">Foydalanuvchi roli</label>
                  <input type="text" value="${{user.role}}" disabled class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-800/40 text-slate-400 capitalize">
                </div>
                <div>
                  <label class="block font-semibold text-slate-500 mb-1">Sinf / Bosqich</label>
                  <input type="text" value="${{user.grade || '9-sinf'}}" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 dark:text-white">
                </div>
              </div>

              <div class="pt-4 flex justify-end">
                <button onclick="showToast('Saqlandi!', 'Profil ma’lumotlari muvaffaqiyatli yangilandi.')" class="px-6 py-2.5 rounded-xl bg-blue-600 text-white font-semibold text-xs hover:bg-blue-700 transition">
                  O‘zgarishlarni saqlash
                </button>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    // ==========================================
    // 16. ABOUT & CONTACT VIEWS
    // ==========================================
    function renderAboutView() {{
      return `
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm space-y-6">
            <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white">Education Hub 2.0 Loyihasi haqida</h1>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-300">
              <b>Education Hub 2.0</b> — butun O‘zbekiston Respublikasi bo‘ylab sifatli va zamonaviy ta’limni har bir yosh uchun teng, ochiq va 100% bepul yetkazib berishga qaratilgan innovatsion milliy ta’lim ekotizimidir.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4">
              <div class="p-4 rounded-2xl bg-blue-50 dark:bg-blue-950/30 border border-blue-100 dark:border-blue-900">
                <div class="font-bold text-blue-600 mb-1">100% Bepul</div>
                <div class="text-xs text-slate-500">Hech qanday obuna to‘lovlari, paywall yoki yashirin pullik xizmatlar mavjud emas.</div>
              </div>
              <div class="p-4 rounded-2xl bg-teal-50 dark:bg-teal-950/30 border border-teal-100 dark:border-teal-900">
                <div class="font-bold text-teal-600 mb-1">200+ Real Material</div>
                <div class="text-xs text-slate-500">Nazariya, kamida 2 ta amaliy misol, mustaqil mashq va tekshiruv savollari bilan to‘liq.</div>
              </div>
              <div class="p-4 rounded-2xl bg-purple-50 dark:bg-purple-950/30 border border-purple-100 dark:border-purple-900">
                <div class="font-bold text-purple-600 mb-1">52 ta Fan</div>
                <div class="text-xs text-slate-500">Aniq, tabiiy, tillar, jamiyat, san’at va zamonaviy IT kasbiy sohalarini qamrab olgan.</div>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    function renderContactView() {{
      return `
        <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class="p-8 rounded-3xl bg-white dark:bg-darkcard border border-slate-200 dark:border-slate-800 shadow-sm">
            <h1 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">Biz bilan bog‘lanish</h1>
            <p class="text-xs text-slate-500 mb-6">Savollar, takliflar yoki platformaga o‘qituvchi sifatida qo‘shilish bo‘yicha yozing</p>

            <form onsubmit="handleContactSubmit(event)" class="space-y-4 text-xs sm:text-sm">
              <div>
                <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Ismingiz</label>
                <input type="text" required placeholder="Ismingizni kiriting" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 dark:text-white">
              </div>
              <div>
                <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Email manzilingiz</label>
                <input type="email" required placeholder="example@edu.uz" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 dark:text-white">
              </div>
              <div>
                <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Xabar matni</label>
                <textarea rows="4" required placeholder="Xabaringizni yozing..." class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 dark:text-white"></textarea>
              </div>
              <button type="submit" class="w-full py-3 rounded-xl bg-blue-600 text-white font-bold text-xs hover:bg-blue-700 shadow-md transition">
                Xabarni yuborish
              </button>
            </form>
          </div>
        </div>
      `;
    }}

    function handleContactSubmit(e) {{
      e.preventDefault();
      showToast('Xabar yuborildi!', 'Taklifingiz uchun tashakkur! Tez orada ko‘rib chiqamiz.', 'success');
      e.target.reset();
    }}

    // ==========================================
    // AUTH MODAL LOGIC
    // ==========================================
    function openAuthModal(mode = 'login') {{
      const container = document.getElementById('modalContainer');
      container.classList.remove('hidden');
      container.classList.add('flex');

      container.innerHTML = `
        <div class="bg-white dark:bg-darkcard max-w-md w-full p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl relative text-xs sm:text-sm">
          <button onclick="closeModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 dark:hover:text-white text-lg">✕</button>

          <h2 class="text-xl font-bold text-slate-900 dark:text-white mb-1">
            ${{mode === 'login' ? 'Tizimga kirish' : 'Ro‘yxatdan o‘tish'}}
          </h2>
          <p class="text-xs text-slate-500 mb-6">Education Hub 2.0 platformasiga xush kelibsiz</p>

          <form onsubmit="handleAuthSubmit(event, '${{mode}}')" class="space-y-4">
            ${{mode === 'register' ? `
              <div>
                <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">To'liq ismingiz *</label>
                <input id="authName" type="text" required placeholder="Ali Valiyev" class="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 dark:text-white">
              </div>
              <div>
                <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Foydalanuvchi roli *</label>
                <select id="authRole" class="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 dark:text-white">
                  <option value="student">O‘quvchi (Maktab)</option>
                  <option value="university_student">Talaba (Universitet)</option>
                  <option value="teacher">O‘qituvchi / Ustoz</option>
                  <option value="admin">Administrator</option>
                </select>
              </div>
            ` : ''}}

            <div>
              <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Email pochta *</label>
              <input id="authEmail" type="email" required placeholder="nomingiz@edu.uz" class="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 dark:text-white">
            </div>

            <div>
              <label class="block font-semibold mb-1 text-slate-700 dark:text-slate-300">Maxfiy parol *</label>
              <input id="authPassword" type="password" required placeholder="••••••••" class="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 dark:text-white">
            </div>

            <button type="submit" class="w-full py-2.5 rounded-xl bg-blue-600 text-white font-bold text-xs hover:bg-blue-700 shadow-md transition">
              ${{mode === 'login' ? 'Kirish' : 'Hisob yaratish'}}
            </button>

            <div class="text-center text-xs text-slate-500 pt-2">
              ${{mode === 'login' ? `
                Hisobingiz yo‘qmi? <button type="button" onclick="openAuthModal('register')" class="text-blue-600 font-semibold hover:underline">Ro‘yxatdan o‘tish</button>
              ` : `
                Allaqachon hisobingiz bormi? <button type="button" onclick="openAuthModal('login')" class="text-blue-600 font-semibold hover:underline">Kirish</button>
              `}}
            </div>
          </form>
        </div>
      `;
    }}

    function closeModal() {{
      const container = document.getElementById('modalContainer');
      container.classList.add('hidden');
      container.classList.remove('flex');
    }}

    function handleAuthSubmit(e, mode) {{
      e.preventDefault();
      const email = document.getElementById('authEmail').value;
      const name = mode === 'register' ? document.getElementById('authName').value : email.split('@')[0];
      const role = mode === 'register' ? document.getElementById('authRole').value : 'student';

      currentUser = {{
        id: `usr-${{Date.now()}}`,
        name: name,
        email: email,
        role: role,
        xp: 150
      }};

      try {{ localStorage.setItem('eh_user', JSON.stringify(currentUser)); }} catch(e){{}}
      renderAuthHeader();
      closeModal();
      showToast('Xush kelibsiz!', `${{name}}, Education Hub 2.0 ga muvaffaqiyatli kirdingiz!`, 'success');
      navigateTo('dashboard');
    }}

    // Global Initialization on window load
    window.onload = function() {{
      initState();
      navigateTo('home');
    }};
  </script>
</body>
</html>
"""
    return html_content

if __name__ == "__main__":
    content = generate_web_app()
    out_dir = "artifacts/file_generation/ttl=63d/output"
    inter_dir = "artifacts/file_generation/ttl=63d/intermediate"
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(inter_dir, exist_ok=True)

    out_file = os.path.join(out_dir, "education_hub_2.html")
    inter_file = os.path.join(inter_dir, "education_hub_2.html")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)

    with open(inter_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Generated Web App at: {out_file} ({os.path.getsize(out_file)} bytes)")
