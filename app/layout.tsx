import './globals.css';
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
