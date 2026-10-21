import Link from 'next/link';
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
