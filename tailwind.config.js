/** @type {import('tailwindcss').Config} */
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
