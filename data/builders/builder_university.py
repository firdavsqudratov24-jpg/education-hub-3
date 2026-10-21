# -*- coding: utf-8 -*-
"""
Builder for Universitet va kasbiy fanlar (15 materials: uni-001 to uni-015)
- sub-41: Sun’iy intellekt (uni-001)
- sub-42: Ma’lumotlar tahlili (uni-002)
- sub-43: Kiberxavfsizlik (uni-003)
- sub-44: Oliy matematika (uni-004)
- sub-45: Statistika (uni-005)
- sub-46: Muhandislik (uni-006)
- sub-47: Pedagogika (uni-007)
- sub-48: Tibbiyot asoslari (uni-008)
- sub-49: Moliya (uni-009)
- sub-50: Buxgalteriya (uni-010)
- sub-51: Menejment (uni-011)
- sub-52: Marketing (uni-012)
- sub-28: Falsafa (uni-013)
- sub-29: Psixologiya (uni-014)
- sub-30: Mantiq (uni-015)
"""

def get_university_materials():
    materials = [
        {
            "id": "uni-001",
            "slug": "suniy-intellekt-mashinali-organish-asoslari",
            "subject_id": "sub-41",
            "subject_name": "Sun’iy intellekt",
            "title": "Sun’iy intellekt va Machine Learning: Nazorat ostidagi va nazoratsiz o'rganish",
            "grade_level": "Universitet",
            "difficulty": "Murakkab",
            "objective": "Sun'iy intellekt (AI), Machine Learning (ML), Deep Learning, Nazorat ostidagi (Supervised) va Nazoratsiz (Unsupervised) o'rganish hamda neyron to'rlar arxitekturasini o'rganish.",
            "theory": "Sun'iy intellekt (AI) — inson aqliy faoliyatini (o'rganish, xulosa chiqarish, ko'rish, tushunish) kompyuter tizimlarida modellashtirishdir. Machine Learning (ML) — qat'iy dasturlashtirilmagan holda ma'lumotlar (data) asosida o'rganuvchi algoritmlar sohasidir. 3 ta asosiy turi: 1) Supervised Learning (Nazorat ostidagi o'rganish) — modelga kiruvchi ma'lumotlar va ularning to'g'ri javoblari (labels) beriladi. Masalalar: Regressiya (sonli qiymat bashorati — uy narxi) va Klassifikatsiya (toifaga ajratish — spam/not spam); 2) Unsupervised Learning (Nazoratsiz o'rganish) — javoblar (labels) yo'q, model ma'lumotlar ichidagi yashirin qonuniyatlarni topadi. Masalalar: Klasterlash (mijozlarni guruhlash — K-Means) va o'lchamni qisqartirish (PCA); 3) Reinforcement Learning (Mustahkamlash orqali o'rganish) — agent mukofot (reward) va jazo tizimi asosida atrof-muhit bilan sinab-ko'rib o'rganadi. Neyron to'rlar (Neural Networks) — inson miyasi neyronlari analogi bo'lib, kirish, yashirin va chiqish qatlamlaridan iborat.",
            "examples": [
                {
                    "title": "Klassifikatsiya va Regressiya farqi",
                    "problem": "1) Bemorning MRT suratiga qarab unda o'sma bor-yo'qligini aniqlash; 2) Mashinaning yili va probegiga qarab uning bozor narxini baholash. Bular ML ning qaysi turiga kiradi?",
                    "step_by_step": "1) O'sma bor/yo'qligi — toifaga ajratish (Klassifikatsiya);\n2) Mashina narxi — uzluksiz sonli qiymatni bashorat qilish (Regressiya). Ikkalasi ham Nazorat ostidagi o'rganish (Supervised) hisoblanadi.",
                    "answer": "1 - Klassifikatsiya, 2 - Regressiya"
                },
                {
                    "title": "Overfitting (Qayta moslashuv) muammosi",
                    "problem": "ML modeli o'rgatish ma'lumotlarida 100% aniqlik ko'rsatib, yangi real ma'lumotlarda juda yomon natija bersa bu qanday hodisa?",
                    "step_by_step": "Bu Overfitting (qayta moslashuv / yodlab olish) deyiladi. Model umumiy qonuniyatni o'rganmasdan, o'quv ma'lumotlaridagi shovqinlarni yodlab olgan. Buni yechish uchun regularizatsiya, Dropout yoki ko'proq ma'lumot kerak.",
                    "answer": "Overfitting (qayta moslashuv)"
                }
            ],
            "exercise": "Spam-filtrlarda xatning spam yoki oddiy ekanligini aniqlashda qaysi mashhur ehtimollik algoritmi qo'llaniladi?",
            "exercise_solution": "Naive Bayes (Sodda Bayes) klassifikatori matndagi so'zlarning uchrash ehtimolligi asosida juda samarali ishlaydi.",
            "check_questions": [
                {
                    "question": "Javoblari (labels) belgilanmagan ma'lumotlarni o'xshashlik bo'yicha guruhlash nima deyiladi?",
                    "options": ["Regressiya", "Klasterlash (Clustering)", "Klassifikatsiya", "Random Forest"],
                    "correct_index": 1,
                    "explanation": "Klasterlash (masalan, K-Means) nazoratsiz o'rganish usuli bo'lib, o'xshash obyektlarni guruhlarga ajratadi."
                },
                {
                    "question": "Deep Learning (Chuqur o'rganish) nima asosida qurilgan?",
                    "options": ["Ko'p qatlamli sun'iy neyron to'rlari (Artificial Neural Networks)", "Faqat chiziqli tenglamalar", "Qidiruv algoritmlari", "SQL so'rovlar"],
                    "correct_index": 0,
                    "explanation": "Deep Learning ko'p sonli yashirin qatlamlarga ega murakkab neyron to'rlariga tayanadi."
                },
                {
                    "question": "Agent mukofot va jazo asosida o'yinlarda (shaxmat, Go) o'rganishi qaysi yo'nalishga kiradi?",
                    "options": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning (Mustahkamlash orqali)", "Data Mining"],
                    "correct_index": 2,
                    "explanation": "Reinforcement Learning agentning rag'batlantirish orqali optimal strategiyani tanlashini o'rganadi."
                }
            ],
            "tags": ["sun'iy intellekt", "machine learning", "neyron to'rlar", "supervised", "deep learning", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-002",
            "slug": "malumotlar-tahlili-pandas-va-eda",
            "subject_id": "sub-42",
            "subject_name": "Ma’lumotlar tahlili",
            "title": "Ma’lumotlar tahlili (Data Analytics): Pandas, Ma'lumotlarni tozalash va EDA",
            "grade_level": "Universitet",
            "difficulty": "O'rta",
            "objective": "Data Analytics bosqichlari, Python Pandas kutubxonasida DataFrame bilan ishlash, yo'qolgan qiymatlarni (NaN) tozalash va dastlabki tahlil (EDA) o'tkazish.",
            "theory": "Ma'lumotlar tahlili (Data Analytics) — xom ma'lumotlarni tozalash, o'zgartirish va biznes qarorlar qabul qilish uchun foydali xulosalar chiqarish jarayonidir. Asosiy vosita — Python Pandas kutubxonasi. Asosiy tuzilmalar: Series (bir o'lchamli massiv) va DataFrame (ikki o'lchamli elektron jadval). Tahlil bosqichlari: 1) Ma'lumotlarni yuklash (pd.read_csv, pd.read_sql); 2) EDA (Exploratory Data Analysis — Dastlabki tahlil): df.info(), df.describe(), df.head(); 3) Ma'lumotlarni tozalash (Data Cleaning): yo'qolgan qiymatlarni to'ldirish (df.fillna) yoki o'chirish (df.dropna), dublikatlarni tozalash (df.drop_duplicates); 4) Guruhlash va agregatsiya: df.groupby('city')['salary'].mean(); 5) Vizuallashtirish: Matplotlib va Seaborn orqali gistogrammalar va korrelyatsiya issiqlik xaritalari (heatmap) tuzish.",
            "examples": [
                {
                    "title": "Pandas da guruhlash (GroupBy)",
                    "problem": "Har bir fan bo'yicha materiallarning o'rtacha ko'rilishlar sonini (views) hisoblang.",
                    "step_by_step": "import pandas as pd\n\ndf = pd.read_csv('materials.csv')\nresult = df.groupby('subject_name')['views'].mean().reset_index()\nprint(result)",
                    "answer": "df.groupby('subject_name')['views'].mean()"
                },
                {
                    "title": "Yo'qolgan qiymatlarni (Missing values) to'ldirish",
                    "problem": "'age' ustunida bo'sh (NaN) qiymatlar bor. Ularni o'rtacha yosh (mean) bilan to'ldiring.",
                    "step_by_step": "mean_age = df['age'].mean()\ndf['age'] = df['age'].fillna(mean_age)",
                    "answer": "df['age'].fillna(df['age'].mean())"
                }
            ],
            "exercise": "Ikkita sonli o'zgaruvchi orasidagi chiziqli bog'liqlik darajasini aniqlovchi koeffitsiyent nima deyiladi?",
            "exercise_solution": "Pirson korrelyatsiya koeffitsiyenti (Correlation, r) bo'lib, -1 dan +1 gacha oraliqda o'zgaradi.",
            "check_questions": [
                {
                    "question": "Pandas da ikki o'lchamli ustun va qatorlardan iborat asosiy jadval tuzilmasi nima deyiladi?",
                    "options": ["Series", "DataFrame", "Matrix", "Dictionary"],
                    "correct_index": 1,
                    "explanation": "DataFrame — Pandas da ma'lumotlar bilan ishlashning asosiy jadval shaklidir."
                },
                {
                    "question": "Sonli ustunlarning soni, o'rtacha qiymati, min, max va kvartillarini chiqaruvchi metod qaysi?",
                    "options": ["df.head()", "df.describe()", "df.info()", "df.count()"],
                    "correct_index": 1,
                    "explanation": "df.describe() tavsifiy statistika ko'rsatkichlarini bir zumda hisoblab beradi."
                },
                {
                    "question": "Tahlilda 'anomaliya' (outlier) deganda nima tushuniladi?",
                    "options": ["Barcha to'g'ri qiymatlar", "Umumiy taqsimotdan keskin ajralib turuvchi favqulodda chekka xato yoki noodatiy qiymatlar", "Nol qiymatlar", "Matnli ma'lumotlar"],
                    "correct_index": 1,
                    "explanation": "Outliers — umumiy qonuniyatdan juda uzoqda yotgan, o'rtacha ko'rsatkichni buzishi mumkin bo'lgan chekka nuqtalardir."
                }
            ],
            "tags": ["ma'lumotlar tahlili", "pandas", "data analytics", "EDA", "dataframe", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-003",
            "slug": "tarmoq-kiberxavfsizligi-va-kriptografiya",
            "subject_id": "sub-43",
            "subject_name": "Kiberxavfsizlik",
            "title": "Kiberxavfsizlik: CIA triadası, Asimmetrik kriptografiya (RSA) va Tarmoq xavfsizligi",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Murakkab",
            "objective": "Axborot xavfsizligining CIA modeli (Konfidentsiallik, Yaxlitlik, Foydalanish imkoniyati), Simmetrik va Asimmetrik shifrlash (RSA, AES) hamda xavfsizlik devorlari (Firewall)ni o'rganish.",
            "theory": "Kiberxavfsizlikning poydevori — CIA triadasi: 1) Confidentiality (Maxfiylik) — ma'lumot faqat ruxsati bor shaxslarga ko'rinishi (shifrlash); 2) Integrity (Yaxlitlik) — ma'lumot uzatishda o'zgartirilmasligi yoki buzilmasligi (xesh-funksiyalar: SHA-256); 3) Availability (Foydalanish imkoniyati) — vakolatli foydalanuvchi istalgan paytda tizimdan foydalana olishi (DDoS himoyasi). Kriptografiya asoslari:\n- Simmetrik shifrlash (AES): bitta maxfiy kalit bilan shifrlanadi va ochiladi (juda tez, katta hajmlar uchun);\n- Asimmetrik shifrlash (RSA): ikkita kalit ishlatiladi — ochiq kalit (Public key — hamma ko'radi, faqat shifrlaydi) va yopiq kalit (Private key — faqat egasida saqlanadi, shifrni ochadi). Raqamli imzo (Digital Signature) — xat jo'natuvchining shaxsini va hujjat o'zgarmaganini isbotlaydi. Tarmoq xavfsizligi: Firewall (Xavfsizlik devori) tarmoq trafigini filtrlaydi; VPN (Virtual Private Network) shifrlangan xavfsiz tunnel yaratadi.",
            "examples": [
                {
                    "title": "Asimmetrik shifrlash ishlashi",
                    "problem": "Ali Valiga maxfiy xabar yubormoqchi. U xabarni kimning qaysi kaliti bilan shifrlashi kerak?",
                    "step_by_step": "1) Ali Valining Ochiq kalitini (Public key) oladi;\n2) Xabarni Valining ochiq kaliti bilan shifrlaydi;\n3) Bu shifrni faqat Valining o'zidagina bor bo'lgan Yopiq kalit (Private key) ochishi mumkin.",
                    "answer": "Valining ochiq kaliti (Public key) bilan shifrlaydi"
                },
                {
                    "title": "DDoS hujumi nima?",
                    "problem": "DDoS (Distributed Denial of Service) hujumi qanday amalga oshiriladi va u CIA ning qaysi bo'g'inini buzadi?",
                    "step_by_step": "Xakerlar minglab zararlangan botnet kompyuterlaridan serverga bir vaqtda millionlab soxta so'rovlar yuboradi. Server bardosh bera olmay o'chadi. Bu CIA ning Availability (Foydalanish imkoniyati) bo'g'inini buzadi.",
                    "answer": "Serverni ortiqcha yuklama bilan qulatadi; Availability buziladi"
                }
            ],
            "exercise": "SHA-256 xesh funksiyasining qaytmaslik (bir tomonlama) xossasi nimani anglatadi?",
            "exercise_solution": "Berilgan xesh kodidan (masalan, e3b0c442...) dastlabki matnni qaytarib tiklash matematik jihatdan imkonsiz ekanligini anglatadi.",
            "check_questions": [
                {
                    "question": "CIA xavfsizlik modelining 3 ta komponenti qaysi?",
                    "options": ["Code, Internet, Access", "Confidentiality, Integrity, Availability", "CPU, IP, Antivirus", "Control, Identity, Audit"],
                    "correct_index": 1,
                    "explanation": "Maxfiylik (Confidentiality), Yaxlitlik (Integrity) va Foydalanish imkoniyati (Availability) axborot xavfsizligi asosidir."
                },
                {
                    "question": "Asimmetrik kriptografiyada (masalan RSA) nechta kalitdan foydalaniladi?",
                    "options": ["1 ta umumiy kalit", "2 ta kalit (Ochiq va Yopiq kalit juftligi)", "3 ta kalit", "Kalitsiz"],
                    "correct_index": 1,
                    "explanation": "Asimmetrik shifrlash Public va Private key juftligi orqali ishlaydi."
                },
                {
                    "question": "Tarmoq paketlarini qoidalarga asosan tekshirib, ruxsatsiz ulanishlarni to'suvchi dastur yoki qurilma nima deyiladi?",
                    "options": ["Router", "Firewall (Xavfsizlik devori)", "Switch", "Modem"],
                    "correct_index": 1,
                    "explanation": "Firewall tarmoq trafigini tahlil qilib xavfli kirishlarni to'xtatadi."
                }
            ],
            "tags": ["kiberxavfsizlik", "kriptografiya", "RSA", "CIA triadasi", "firewall", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-004",
            "slug": "oliy-matematika-chiziqli-algebra-va-matritsalar",
            "subject_id": "sub-44",
            "subject_name": "Oliy matematika",
            "title": "Oliy matematika: Matritsalar algebrasi, determinantlar va Kramer qoidasi",
            "grade_level": "Universitet",
            "difficulty": "Murakkab",
            "objective": "Matritsalar ustida amallar (qo'shish, songa ko'paytirish, matritsalar ko'paytmasi), 2- va 3-tartibli determinantlar va chiziqli tenglamalar sistemasini Kramer usulida yechish.",
            "theory": "Oliy matematika muhandislik va iqtisodiyotning poydevoridir. Matritsa — m ta qator va n ta ustundan iborat to'g'ri to'rtburchakli sonlar jadvaldir. Matritsalarni ko'paytirish qoidasi: birinchi matritsaning ustunlar soni ikkinchi matritsaning qatorlar soniga teng bo'lishi shart ('qatorni ustunga ko'paytirish'). Kvadrat matritsaning determinanti (aniqlovchisi): 2x2 uchun det(A) = a11*a22 - a12*a21; 3x3 uchun uchburchak yoki Sarryus qoidasi ishlatiladi. Chiziqli tenglamalar sistemasini yechishning Kramer qoidasi: x_i = Delta_i / Delta (bu yerda Delta - asosiy determinant != 0, Delta_i esa i-ustun o'rniga ozod hadlar qo'yilgan determinant). Teskari matritsa: A^(-1) = (1 / det(A)) * A^T_adj (det(A) != 0 bo'lganda mavjud).",
            "examples": [
                {
                    "title": "2x2 determinantni hisoblash",
                    "problem": "A = [[3, 5], [2, 4]] matritsasining determinantini toping.",
                    "step_by_step": "det(A) = 3 * 4 - 5 * 2 = 12 - 10 = 2.",
                    "answer": "2"
                },
                {
                    "title": "Kramer qoidasi bilan tenglama yechish",
                    "problem": "Sistemani yeching: { 2x + y = 7; x - 3y = -7 }",
                    "step_by_step": "1) Asosiy determinant: Delta = 2*(-3) - 1*1 = -6 - 1 = -7.\n2) Delta_x = 7*(-3) - 1*(-7) = -21 + 7 = -14 => x = -14 / -7 = 2.\n3) Delta_y = 2*(-7) - 7*1 = -14 - 7 = -21 => y = -21 / -7 = 3.",
                    "answer": "x = 2, y = 3"
                }
            ],
            "exercise": "Matritsalar ko'paytmasida A * B har doim B * A ga teng bo'ladimi (kommutativlik)?",
            "exercise_solution": "Umumiy holda yo'q: matritsalar ko'paytmasida kommutativlik xossasi o'rinli emas (A * B != B * A).",
            "check_questions": [
                {
                    "question": "Qachon matritsaning teskari matritsasi (A^-1) mavjud bo'lmaydi?",
                    "options": ["Barcha elementlari musbat bo'lganda", "Determinanti nolga teng bo'lganda (det(A) = 0)", "Faqat toq o'lchamli bo'lganda", "Hech qachon"],
                    "correct_index": 1,
                    "explanation": "Determinanti 0 bo'lgan xos matritsaning teskarisi mavjud emas (nolga bo'lish mumkin emas)."
                },
                {
                    "question": "A(2x3) va B(3x4) matritsalari ko'paytirilsa, hosil bo'lgan C matritsasining o'lchami qanday bo'ladi?",
                    "options": ["2x3", "3x4", "2x4", "Ko'paytirib bo'lmaydi"],
                    "correct_index": 2,
                    "explanation": "(m x k) va (k x n) ko'paytmasi (m x n) o'lchamli matritsani beradi, ya'ni 2x4."
                },
                {
                    "question": "Bosh diagonali 1 lardan, qolgan elementlari 0 lardan iborat kvadrat matritsa nima deyiladi?",
                    "options": ["Nol matritsa", "Birlik matritsa (E)", "Transponirlangan", "Diagonal"],
                    "correct_index": 1,
                    "explanation": "Birlik matritsa (I yoki E) oddiy arifmetikadagi 1 soni vazifasini o'taydi: A * E = A."
                }
            ],
            "tags": ["oliy matematika", "chiziqli algebra", "matritsa", "determinant", "kramer", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-005",
            "slug": "statistika-tavsifiy-va-ehtimollar-taqsimoti",
            "subject_id": "sub-45",
            "subject_name": "Statistika",
            "title": "Amaliy statistika: O'rta arifmetik, Mediana, Dispersiya va Normal taqsimot (Gausian)",
            "grade_level": "Universitet",
            "difficulty": "O'rta",
            "objective": "Tavsifiy statistika ko'rsatkichlari (Mean, Median, Mode, Variance, Standard Deviation) va Gauss normal taqsimoti qoidasini (68-95-99.7 qoidasi) bilish.",
            "theory": "Statistika — ommaviy ma'lumotlarni yig'ish, tizimlashtirish, tahlil qilish va xulosalar chiqarish fanidir. Asosiy o'lchovlar:\n1) Markaziy tendensiya o'lchovlari: O'rta arifmetik (Mean — barcha qiymatlar yig'indisi / soni); Mediana (Median — tartiblangan qatorning qoq o'rtasidagi qiymat, anomaliyalarga chidamli); Moda (Mode — eng ko'p takrorlangan qiymat);\n2) Tarqoqlik o'lchovlari: Qamrov (Range = Max - Min); Dispersiya (Variance, sigma^2 — qiymatlarning o'rtachadan chetlanishlari kvadratlarining o'rtachasi); O'rtacha kvadratik chetlanish (Standard Deviation, sigma = sqrt(dispersiya));\n3) Normal taqsimot (Gauss qo'ng'irog'i): tabiat va jamiyatdagi ko'plab tasodifiy miqdorlar qo'ng'iroqsimon simmetrik egri chiziq bo'ylab taqsimlanadi. 'Uch sigma' qoidasi (68-95-99.7%): barcha qiymatlarning ~68% i mu +- 1*sigma oraliqda, ~95% i mu +- 2*sigma oraliqda, ~99.7% i mu +- 3*sigma oraliqda yotadi.",
            "examples": [
                {
                    "title": "Mediana va o'rtacha qiymat farqi",
                    "problem": "Kompaniyada 4 nafar ishchi 3 mln so'mdan, 1 nafar rahbar 48 mln so'm maosh oladi. O'rtacha maosh va medianani toping.",
                    "step_by_step": "1) O'rtacha maosh = (3*4 + 48) / 5 = 60 / 5 = 12 million so'm;\n2) Qator: 3, 3, 3, 3, 48. Qoq o'rtadagi son (Mediana) = 3 million so'm.\nAnomaliya (rahbar maoshi) tufayli o'rtacha ko'rsatkich buzilgan, mediana esa haqiqiy holatni (3 mln) aks ettiradi.",
                    "answer": "O'rtacha: 12 mln, Mediana: 3 mln"
                },
                {
                    "title": "Standart chetlanish hisobi",
                    "problem": "Sonlar: 2, 4, 6. O'rtacha kvadratik chetlanishni (sigma) toping.",
                    "step_by_step": "1) O'rtacha = (2+4+6)/3 = 4;\n2) Kvadratlar ayirmasi: (2-4)^2 + (4-4)^2 + (6-4)^2 = 4 + 0 + 4 = 8;\n3) Dispersiya = 8 / 3 = 2.67;\n4) Standart chetlanish sigma = sqrt(2.67) ~ 1.63.",
                    "answer": "sigma ~ 1.63"
                }
            ],
            "exercise": "Normal taqsimotda ma'lumotlarning taxminan necha foizi o'rtacha qiymatdan ikkita standart chetlanish (mu +- 2*sigma) oralig'iga to'g'ri keladi?",
            "exercise_solution": "Taqsimot qoidasiga ko'ra taxminan 95.4% ma'lumotlar mu +- 2*sigma oralig'ida yotadi.",
            "check_questions": [
                {
                    "question": "Anomaliyalarga (outliers) nisbatan eng chidamli markaziy ko'rsatkich qaysi?",
                    "options": ["O'rta arifmetik", "Mediana", "Dispersiya", "Standart chetlanish"],
                    "correct_index": 1,
                    "explanation": "Mediana o'rtadagi tartib bo'yicha aniqlangani sababli chekka haddan tashqari katta/kichik sonlarga ta'sirlanmaydi."
                },
                {
                    "question": "Standart chetlanish (sigma) nimani ko'rsatadi?",
                    "options": ["Eng katta sonni", "Ma'lumotlarning o'rtacha qiymat atrofida qanchalik tarqoq yoki zich joylashganligini", "Qatordagi elementlar sonini", "Foydani"],
                    "correct_index": 1,
                    "explanation": "Standart chetlanish ma'lumotlar tarqoqligi va tebranish ko'lamini ifodalaydi."
                },
                {
                    "question": "Eng ko'p takrorlangan qiymat nima deyiladi?",
                    "options": ["Mediana", "Moda", "Kvantil", "Gistogramma"],
                    "correct_index": 1,
                    "explanation": "Moda — qatorda eng yuqori chastota bilan uchraydigan qiymatdir."
                }
            ],
            "tags": ["statistika", "mediana", "o'rtacha arifmetik", "dispersiya", "normal taqsimot", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-006",
            "slug": "muhandislik-loyihalash-va-materialshunoslik",
            "subject_id": "sub-46",
            "subject_name": "Muhandislik",
            "title": "Muhandislik asoslari: Muhandislik dizayni sikli va materialshunoslik asoslari",
            "grade_level": "Universitet",
            "difficulty": "O'rta",
            "objective": "Muhandislik loyihalash bosqichlari, materiallarning mexanik xossalari (mustahkamlik, qattiqlik, plastiklik) va xavfsizlik koeffitsiyentini o'rganish.",
            "theory": "Muhandislik — ilmiy va matematik bilimlarni insoniyat manfaati uchun inshootlar, mashinalar, qurilmalar va tizimlarni yaratishda amaliy qo'llash san'atidir. Muhandislik loyihalash sikli (Engineering Design Process): 1) Muammoni aniqlash; 2) Tadqiq qilish va cheklovlarni belgilash; 3) Yechimlarni miya hujumi (brainstorming) qilish; 4) Eng maqbul konsepsiyani tanlash; 5) Prototip (tajriba nusxasi) yaratish; 6) Sinovdan o'tkazish va optimallashtirish; 7) Yakuniy ishlab chiqarish. Materialshunoslik asoslari: 1) Mustahkamlik (kuch ta'sirida buzilmaslik); 2) Elastiklik (kuch to'xtagach o'z shakliga qaytish — Guk qonuni); 3) Plastiklik (qoldiq deformatsiyani saqlash); 4) Qattiqlik (chizilish va botishga qarshilik — Brinell, Rokvell shkalalari); 5) Mo'rtlik. Xavfsizlik koeffitsiyenti (Factor of Safety, n = sigma_ruxsat / sigma_ishchi) inshootlarning kutilmagan favqulodda yuklamalarga bardosh berishini ta'minlaydi (odatda n = 1.5 - 3).",
            "examples": [
                {
                    "title": "Xavfsizlik koeffitsiyentini hisoblash",
                    "problem": "Po'lat kabel 60 kN yuklamada uziladi. Agar ruxsat etilgan xavfsiz yuklama 20 kN bo'lsa, xavfsizlik koeffitsiyenti nechaga teng?",
                    "step_by_step": "n = Buzuvchi kuch / Ruxsat etilgan kuch = 60 kN / 20 kN = 3. Kabel uch barobar xavfsizlik zaxirasiga ega.",
                    "answer": "n = 3"
                },
                {
                    "title": "Prototip yaratishning maqsadi",
                    "problem": "Nima sababdan mahsulotni ommaviy ishlab chiqarishdan oldin prototip yaratiladi?",
                    "step_by_step": "Kompyuter simulyatsiyasi ko'rmagan real kamchiliklarni amalda sinab ko'rish, ergonomikasini tekshirish va xatolarni zavod konveyeriga chiqmasdan arzon narxda bartaraf etish uchun.",
                    "answer": "Haqiqiy kamchiliklarni erta aniqlash va xavfni kamaytirish uchun"
                }
            ],
            "exercise": "Materialning charchashi (Fatigue) nima va nima uchun reaktiv samolyotlarda u juda xavfli?",
            "exercise_solution": "Ko'p marotaba takrorlanuvchi o'zgaruvchan tebranishlar natijasida materialda mikro-darzlar paydo bo'lib, ruxsat etilgan me'yordan ancha past yuklamada ham to'satdan sinib ketish hodisasi charchash deyiladi.",
            "check_questions": [
                {
                    "question": "Tashqi kuch ta'siri to'xtagach, jismning o'z dastlabki o'lcham va shaklini to'liq tiklash xossasi nima?",
                    "options": ["Plastiklik", "Elastiklik", "Mo'rtlik", "Suyuqlanish"],
                    "correct_index": 1,
                    "explanation": "Elastiklik deformatsiyadan so'ng asl holatga qaytish qobiliyatidir."
                },
                {
                    "question": "Muhandislik loyihalashida 'Xavfsizlik koeffitsiyenti' (Factor of Safety) 1 dan kichik bo'lishi mumkinmi?",
                    "options": ["Ha, arzon bo'lishi uchun", "Yo'q, 1 dan kichik bo'lsa inshoot ishchi yuklamada qulaydi (xavfli)", "Ixtiyoriy", "Faqat ko'priklarda"],
                    "correct_index": 1,
                    "explanation": "n < 1 bo'lsa inshoot oddiy ish sharoitining o'zidayoq buziladi, shuning uchun n har doim 1 dan katta bo'ladi."
                },
                {
                    "question": "Materialning o'ziga boshqa qattiqroq jismning botishiga qarshilik ko'rsatish qobiliyati nima?",
                    "options": ["Qattiqlik", "Mustahkamlik", "Og'irlik", "Issiqlik o'tkazuvchanlik"],
                    "correct_index": 0,
                    "explanation": "Qattiqlik — yuzaga botishga qarshilik ko'rsatish xossasidir."
                }
            ],
            "tags": ["muhandislik", "materialshunoslik", "prototip", "mustahkamlik", "xavfsizlik koeffitsiyenti", "universitet"],
            "duration_minutes": 30
        },
        {
            "id": "uni-007",
            "slug": "pedagogika-talim-nazariyasi-va-zamonaviy-metodlar",
            "subject_id": "sub-47",
            "subject_name": "Pedagogika",
            "title": "Pedagogika va ta'lim texnologiyalari: Didaktika tamoyillari va Blum taksonomiyasi",
            "grade_level": "Universitet",
            "difficulty": "O'rta",
            "objective": "Didaktika qonuniyatlari, Y.A. Komenskiyning ko'rsatmalilik tamoyili, zamonaviy interfaol metodlar hamda bilish darajalarining Blum taksonomiyasini o'rganish.",
            "theory": "Pedagogika — insonni tarbiyalash, unga ta'lim va ma'lumot berish qonuniyatlarini o'rganadigan fandir. Ilmiy asoschisi — Yan Amos Komenskiy ('Buyuk didaktika', sinf-dars tizimi asoschisi). Didaktika — ta'lim va o'qitish nazariyasi. Asosiy didaktik tamoyillar: ko'rsatmalilik (ko'rib tushunish), onglilik va faollik, tizimlilik va ketma-ketlik, tushunarlilik, mustahkamlik. Benjamin Blum taksonomiyasi (Bloom's Taxonomy) — bilish maqsadlarini 6 ta bosqichga ajratadi (pastdan yuqoriga): 1) Eslab qolish (Remembering — faktlarni aytib berish); 2) Tushunish (Understanding — o'z so'zlari bilan izohlash); 3) Qo'llash (Applying — yangi vaziyatda qoidani ishlatish); 4) Tahlil (Analyzing — qismlarga ajratib sabab-oqibatni topish); 5) Baholash (Evaluating — xulosa berish, himoya qilish); 6) Yaratish (Creating — yangi loyiha, mahsulot yoki nazariya ishlab chiqish).",
            "examples": [
                {
                    "title": "Blum taksonomiyasini amalda qo'llash",
                    "problem": "O'quvchiga 'Pifagor teoremasini yoddan ayt' va 'Pifagor teoremasidan foydalanib romb tomonini top' topshiriqlari Blum bo'yicha qaysi darajalarga kiradi?",
                    "step_by_step": "1) Yoddan aytish — quyi 1-daraja: Eslab qolish (Remembering);\n2) Masalada formulani amalda ishlatish — 3-daraja: Qo'llash (Applying).",
                    "answer": "1-topshiriq: Eslab qolish, 2-topshiriq: Qo'llash"
                },
                {
                    "title": "Interfaol metodlar samarasi",
                    "problem": "Nima sababdan noan'anaviy interfaol metodlar (klaster, aqliy hujum, FSMU) an'anaviy ma'ruzadan ko'ra samaraliroq?",
                    "step_by_step": "Chunki interfaol ta'limda o'quvchi passiv tinglovchi emas, balki bilimlarni mustaqil izlab topuvchi, tahlil qiluvchi va jamoada muhokama qiluvchi faol ishtirokchiga aylanadi.",
                    "answer": "O'quvchini darsning faol subyektiga aylantirgani uchun"
                }
            ],
            "exercise": "FSMU (Fikr, Sabab, Misol, Umumlashtirish) texnologiyasining 4 ta bosqichini yozing.",
            "exercise_solution": "F — Fikringizni bayon eting; S — Fikringiz sababini tushuntiring; M — Fikringizni isbotlovchi misol keltiring; U — Fikringizni umumlashtirib yakunlang.",
            "check_questions": [
                {
                    "question": "Sinf-dars tizimining asoschisi va 'Buyuk didaktika' asari muallifi kim?",
                    "options": ["Yan Amos Komenskiy", "Jan-Jak Russo", "Lev Vigotskiy", "Konfutsiy"],
                    "correct_index": 0,
                    "explanation": "Y.A. Komenskiy XVII asrda zamonaviy dars va sinf tizimiga poydevor qo'ygan."
                },
                {
                    "question": "Blum taksonomiyasining eng oliy, eng yuqori darajasi qaysi?",
                    "options": ["Eslab qolish", "Tushunish", "Tahlil", "Yaratish (Creating)"],
                    "correct_index": 3,
                    "explanation": "Blum piramidasining eng yuqori cho'qqisi yangi yechim va g'oyalarni Yaratish (Creating) darajasidir."
                },
                {
                    "question": "Didaktikaning 'oltin qoidasi' deb qaysi tamoyil atalgan?",
                    "options": ["Jazolash tamoyili", "Ko'rsatmalilik tamoyili (ko'rish, eshitish orqali his qilish)", "Faqat yodlash", "Tezlik"],
                    "correct_index": 1,
                    "explanation": "Komenskiy 'barcha narsani sezgi a'zolariga havola qilish'ni didaktikaning oltin qoidasi deb atagan."
                }
            ],
            "tags": ["pedagogika", "didaktika", "blum taksonomiyasi", "komenskiy", "ta'lim metodlari", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-008",
            "slug": "tibbiyot-asoslari-birinchi-yordam-va-klinik-belgilar",
            "subject_id": "sub-48",
            "subject_name": "Tibbiyot asoslari",
            "title": "Klinik tibbiyot asoslari: Hayotiy ko'rsatkichlar va Yurak-o'pka reanimatsiyasi (YOR/CPR)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Murakkab",
            "objective": "Insonning asosiy hayotiy ko'rsatkichlari (vital signs: puls, bosim, saturatsiya, harorat), hushdan ketish va to'satdan yurak to'xtaganda Yurak-o'pka reanimatsiyasini (CPR) xalqaro standartda bajarish.",
            "theory": "Klinik propedevtika inson organizmi hayotiy ko'rsatkichlarini (Vital Signs) baholashdan boshlanadi: 1) Puls (tomir urishi) — tinch holatda kattalarda 60-80 marta/minut; 2) Nafas chastotasi — 16-20 marta/minut; 3) Arterial qon bosimi — 120/80 mm sim.ust.; 4) SpO2 (kislorod saturatsiyasi) — 95-99%; 5) Tana harorati — 36.6 °C. Yurak-o'pka reanimatsiyasi (YOR / CPR — Cardiopulmonary Resuscitation): Jarohatlangan shaxs hushsiz, nafas olmayotgan va uyqu arteriyasida puls yo'q bo'lsa darhol boshlanadi. Ketma-ketlik (C-A-B): 1) Chest Compressions (ko'krak qafasini kompressiya qilish) — ko'krak suyagining o'rtasiga qo'llarni qulflab, 5-6 sm chuqurlikda, minutiga 100-120 marta tezlikda 30 marta bosiladi; 2) Airway (nafas yo'lini ochish — boshni orqaga engashtirish va jag'ni ko'tarish); 3) Breathing (sun'iy nafas berish — og'izdan og'izga 2 marta puflash). Standart nisbat: 30 ta bosishga 2 ta sun'iy nafas (30:2) tez yordam yetib kelguncha davom ettiriladi.",
            "examples": [
                {
                    "title": "CPR algoritmini qo'llash",
                    "problem": "Ko'chada to'satdan yiqilib hushini yo'qotgan odamga yordam berish qadamlari qanday?",
                    "step_by_step": "1) Atrof xavfsizligini tekshirish;\n2) Yelkalaridan ushlab ovoz chiqarib chaqirish (hushini tekshirish);\n3) 103 ga qo'ng'iroq qilishni atrofdagilarga buyurish;\n4) Nafas va pulsni 10 sekund ichida tekshirish;\n5) Nafas bo'lmasa, darhol 30:2 nisbatda ko'krak kompressiyasi va sun'iy nafasni boshlash.",
                    "answer": "Hushni tekshirish -> 103 ga qo'ng'iroq -> 30:2 CPR ni boshlash"
                },
                {
                    "title": "Anafilaktik shok belgilari",
                    "problem": "Dori vositasi yoki hasharot chaqqandan keyin yuzaga keladigan o'ta og'ir allergik holat — anafilaktik shokda qanday shoshilinch dori yuboriladi?",
                    "step_by_step": "Anafilaktik shokda nafas qisishi, tomoq shishi va qon bosimi keskin tushib ketishi kuzatiladi. Hayotni saqlab qoluvchi birinchi vosita — zudlik bilan mushak orasiga Adrenalin (Epinefrin) inyeksiyasidir.",
                    "answer": "Adrenalin (Epinefrin)"
                }
            ],
            "exercise": "Arterial qon ketishida qon to'xtatuvchi bog'lam (jgut) yozda va qishda ko'pi bilan necha soatga qo'yilishi mumkin?",
            "exercise_solution": "To'qimalar nekroziga yo'l qo'ymaslik uchun jgut yoz faslida ko'pi bilan 1 soatga, qish faslida esa 30-40 minutga qo'yiladi (vaqt yozilgan qog'oz qistirib qo'yilishi shart).",
            "check_questions": [
                {
                    "question": "Yurak-o'pka reanimatsiyasida (CPR) ko'krakni bosish va nafas berishning xalqaro standart nisbati qanday?",
                    "options": ["15 : 2", "30 : 2", "10 : 1", "50 : 5"],
                    "correct_index": 1,
                    "explanation": "Kattalar uchun xalqaro standart: 30 ta ko'krak kompressiyasi va 2 ta sun'iy nafas."
                },
                {
                    "question": "Sog'lom katta yoshli insonning normal pulsi minutiga nechta bo'ladi?",
                    "options": ["30-40", "60-80", "120-140", "90-110"],
                    "correct_index": 1,
                    "explanation": "Tinch holatda kattalarda me'yordagi yurak urishi 60-80 zarba/minut."
                },
                {
                    "question": "Hushsiz bemorning nafas yo'lini ochish uchun qanday harakat qilinadi?",
                    "options": ["Boshini ko'kragiga egish", "Boshini orqaga engashtirib, iyakni yuqoriga ko'tarish", "Uni o'tirg'izish", "Suv ichirish"],
                    "correct_index": 1,
                    "explanation": "Til orqaga ketib halqumni yopib qo'ymasligi uchun bosh orqaga engashtirilib jag' ko'tariladi."
                }
            ],
            "tags": ["tibbiyot", "birinchi yordam", "CPR", "reanimatsiya", "puls", "qon ketishi", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-009",
            "slug": "korporativ-moliya-va-investitsiya-tahlili",
            "subject_id": "sub-49",
            "subject_name": "Moliya",
            "title": "Korporativ moliya: Pulning vaqtdagi qiymati (TVM), NPV va IRR ko'rsatkichlari",
            "grade_level": "Universitet",
            "difficulty": "Murakkab",
            "objective": "Pulning vaqtdagi qiymati konsepsiyasi (Time Value of Money), Diskontlash, Sof joriy qiymat (NPV) va Ichki rentabellik stavkasi (IRR) orqali investitsiya loyihalarini baholash.",
            "theory": "Korporativ moliya kompaniyalarning moliyaviy resurslarini shakllantirish, kapital tuzilmasini boshqarish va foydali investitsiya qarorlarini qabul qilishni o'rganadi. Pulning vaqtdagi qiymati (TVM — Time Value of Money): bugungi 1 dollar kelajakdagi 1 dollardan qimmatroqdir (chunki bugungi pulni investitsiya qilib foiz daromadi olish mumkin va inflyatsiya pulni qadrsizlantiradi). Bo'lajak pul oqimlarini bugungi kunga keltirish diskontlash deyiladi: PV = FV / (1 + r)^t (bu yerda PV - joriy qiymat, FV - kelajakdagi qiymat, r - diskont stavkasi). Investitsiya loyihasini baholashning asosiy mezonlari:\n1) NPV (Net Present Value — Sof joriy qiymat): Kutilayotgan barcha diskontlangan pul tushumlari yig'indisi minus boshlang'ich investitsiya: NPV = Sum[CF_t / (1 + r)^t] - C_0. Qoida: Agar NPV > 0 bo'lsa, loyiha foydali va qabul qilinadi; NPV < 0 bo'lsa, loyiha rad etiladi;\n2) IRR (Internal Rate of Return — Ichki daromadlilik stavkasi): NPV ni roppa-rosa nolga aylantiradigan diskont stavkasidir. Agar IRR kapital narxidan (WACC) yuqori bo'lsa loyiha qabul qilinadi.",
            "examples": [
                {
                    "title": "Kelajakdagi pulning bugungi qiymatini (PV) topish",
                    "problem": "Agar diskont stavkasi r = 10% bo'lsa, 1 yildan keyin olinadigan 110 000 000 so'm pulning bugungi qiymati (PV) qancha?",
                    "step_by_step": "PV = FV / (1 + r)^1 = 110 000 000 / (1 + 0.10) = 110 000 000 / 1.1 = 100 000 000 so'm.",
                    "answer": "100 000 000 so'm"
                },
                {
                    "title": "NPV bo'yicha qaror qabul qilish",
                    "problem": "Loyiha uchun 50 000 dollar tikiladi. Kutilayotgan pul tushumlarining joriy qiymati 65 000 dollar bo'lsa, loyiha qabul qilinadimi?",
                    "step_by_step": "NPV = 65 000 - 50 000 = +15 000 dollar. NPV > 0 bo'lgani sababli kompaniya qiymati 15 000 dollarga oshadi, loyiha qabul qilinadi.",
                    "answer": "NPV = +15 000 $ (Loyiha qabul qilinadi)"
                }
            ],
            "exercise": "Agar ikkita o'zaro bir-birini inkor qiluvchi loyiha taqdim etilsa va A loyihaning NPV si 50 000 $, B loyihaniki 35 000 $ bo'lsa, qaysi biri tanlanadi?",
            "exercise_solution": "NPV qoidasiga ko'ra aksiyadorlar boyligini ko'proq oshiradigan A loyihasi (NPV = 50 000 $) tanlanadi.",
            "check_questions": [
                {
                    "question": "Investitsiya loyihasini qabul qilish uchun uning NPV ko'rsatkichi qanday bo'lishi shart?",
                    "options": ["NPV < 0", "NPV = 0", "NPV > 0 (musbat)", "Manfiy"],
                    "correct_index": 2,
                    "explanation": "NPV > 0 bo'lgandagina loyiha barcha xarajatlarni qoplab, kompaniyaga sof foyda keltiradi."
                },
                {
                    "question": "Kelajakdagi kutilayotgan pul oqimlarini bugungi qiymatga keltirish jarayoni nima deyiladi?",
                    "options": ["Inflyatsiya", "Diskontlash", "Kompaunding", "Amortizatsiya"],
                    "correct_index": 1,
                    "explanation": "Diskontlash (Discounting) kelajakdagi pul qiymatini vaqt va xavf omilini hisobga olib bugungi kunga kamaytirishdir."
                },
                {
                    "question": "NPV ni roppa-rosa nolga tenglashtiruvchi foiz stavkasi nima deb ataladi?",
                    "options": ["WACC", "IRR (Internal Rate of Return)", "ROI", "EBITDA"],
                    "correct_index": 1,
                    "explanation": "IRR loyihaning ichki rentabellik chegarasi bo'lib, unda NPV = 0 bo'ladi."
                }
            ],
            "tags": ["moliya", "korporativ moliya", "NPV", "IRR", "diskontlash", "TVM", "investitsiya", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-010",
            "slug": "buxgalteriya-hisobi-ikkilamchi-yozuv-va-balans",
            "subject_id": "sub-50",
            "subject_name": "Buxgalteriya",
            "title": "Buxgalteriya hisobi: Asosiy tenglama, Debet/Kredit, Provodkalar va Moliyaviy balans",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "O'rta",
            "objective": "Buxgalteriya hisobining bosh tenglamasi (Aktiv = Passiv), Ikkilamchi yozuv (Debet va Kredit), asosiy schotlar va buxgalteriya balansi tuzilishini o'rganish.",
            "theory": "Buxgalteriya hisobi — korxonaning barcha xo'jalik operatsiyalari, mablag'lari va majburiyatlarini uzluksiz, hujjatlashtirilgan holda pul ifodasida hisobga olish tizimidir. Buxgalteriya hisobining oltin tenglamasi: AKTIVLAR = MAJBURIYATLAR + XUSUSIY KAPITAL (Assets = Liabilities + Equity). Aktivlar — korxonaga tegishli bo'lgan barcha iqtisodiy boyliklar (bino, tovarlar, bank hisobidagi pul, kassa). Majburiyatlar — korxonaning qarzlaridir (kreditlar, yetkazib beruvchilarga qarz). Xususiy kapital — ta'sischilar ulushi va taqsimlanmagan sof foyda. Ikkilamchi yozuv (Double-entry bookkeeping — Luka Pacholi, 1494): har bir xo'jalik muomalasi bir vaqtning o'zida bitta schotning Debetiga va ikkinchi schotning Kreditiga teng summada yoziladi (D-t = K-t). Aktiv schotlarda: ko'payish Debetda (+), kamayish Kreditda (-); Passiv schotlarda: ko'payish Kreditda (+), kamayish Debetda (-).",
            "examples": [
                {
                    "title": "Xo'jalik muomalasini provodka qilish",
                    "problem": "Korxona bankdagi hisob raqamidan kassaga 5 000 000 so'm naqd pul oldi. Bu operatsiyaning provodkasini tuzing.",
                    "step_by_step": "1) Kassa (5010-schot) — Aktiv schot, naqd pul ko'paydi -> Debet 5010;\n2) Hisob-kitob raqami (5110-schot) — Aktiv schot, pul kamaydi -> Kredit 5110.\nProvodka: Debet 5010, Kredit 5110 — 5 000 000 so'm.",
                    "answer": "Debet 5010 / Kredit 5110 — 5 000 000 so'm"
                },
                {
                    "title": "Balans tengligi",
                    "problem": "Kompaniyaning jami aktivlari 100 000 dollar, qarz majburiyatlari 40 000 dollar bo'lsa, uning xususiy kapitali qancha?",
                    "step_by_step": "Aktiv = Majburiyat + Kapital => Kapital = Aktiv - Majburiyat = 100 000 - 40 000 = 60 000 dollar.",
                    "answer": "60 000 dollar"
                }
            ],
            "exercise": "Mol yetkazib beruvchidan 10 000 000 so'mlik xomashyo qarzga qabul qilindi. Ushbu operatsiyaning Debet va Kreditini yozing.",
            "exercise_solution": "Debet 1010 (Xomashyo va materiallar ko'paydi) / Kredit 6010 (Mol yetkazib beruvchilarga qarz majburiyati ko'paydi) — 10 000 000 so'm.",
            "check_questions": [
                {
                    "question": "Buxgalteriya hisobining fundamental asosiy tenglamasi qaysi?",
                    "options": ["Foyda = Daromad - Xarajat", "Aktivlar = Majburiyatlar + Xususiy kapital", "Debet = Kredit + QQS", "Aktiv = Majburiyat - Kapital"],
                    "correct_index": 1,
                    "explanation": "Buxgalteriya balansi har doim Aktivlar = Majburiyatlar + Kapital tengligiga asoslanadi."
                },
                {
                    "question": "Ikkilamchi yozuv (Debet/Kredit) qoidasini 1494-yilda fanga kiritgan olim kim?",
                    "options": ["Adam Smit", "Luka Pacholi", "Karl Marks", "Jon Meynard Keyns"],
                    "correct_index": 1,
                    "explanation": "Italiyalik matematik Luka Pacholi buxgalteriya hisobining otasi hisoblanadi."
                },
                {
                    "question": "Aktiv schotlarda mablag'ning ko'payishi qayerga yoziladi?",
                    "options": ["Debetga", "Kreditga", "Saldoma", "Faqat izohga"],
                    "correct_index": 0,
                    "explanation": "Aktiv schotlarda kirim (ko'payish) har doim Debet qismiga yoziladi."
                }
            ],
            "tags": ["buxgalteriya", "debet", "kredit", "balans", "aktiv", "provodka", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-011",
            "slug": "zamonaviy-menejment-va-agile-metodologiyalari",
            "subject_id": "sub-51",
            "subject_name": "Menejment",
            "title": "Zamonaviy menejment: Boshqaruv funksiyalari, Agile, Scrum va Loyihalarni boshqarish",
            "grade_level": "Universitet",
            "difficulty": "O'rta",
            "objective": "Menejmentning 4 ta klassik funksiyasi (rejalashtirish, tashkil etish, motivatsiya, nazorat), Liderlik uslublari hamda IT loyihalarda Agile va Scrum freymvorkini o'rganish.",
            "theory": "Menejment — tashkilotning qo'yilgan maqsadlariga erishishi uchun mavjud insoniy, moliyaviy va moddiy resurslarni samarali boshqarish jarayonidir (Anri Fayol). 4 ta klassik funksiya: 1) Rejalashtirish (maqsad va strategiyani belgilash); 2) Tashkil etish (tuzilma, vazifalar taqsimoti); 3) Motivatsiya (xodimlarni rag'batlantirish — Maslou ehtiyojlar piramidasi); 4) Nazorat (haqiqiy natijani reja bilan solishtirish). Zamonaviy loyihalarni boshqarish: An'anaviy Waterfall (kaskadli — qat'iy bosqichma-bosqich) modelidan Agile (chaqqon, moslashuvchan) metodologiyasiga o'tilmoqda. Scrum freymvorki: loyiha 1-4 haftalik qisqa sikllarga (Sprint) bo'linadi. Rollar: Product Owner (mahsulot egasi, vazifalar ustuvorligini belgilaydi), Scrum Master (jamoani to'siqlardan xalos qiluvchi murabbiy), Development Team (dasturchilar jamoasi). Tizimlar: Daily Standup (har kungi 15 minutlik uchrashuv), Kanban doskalari (To Do, In Progress, Done).",
            "examples": [
                {
                    "title": "Scrum da Sprint retrospektivasi",
                    "problem": "Har bir Sprint yakunida 'Sprint Retrospective' yig'ilishi nima maqsadda o'tkaziladi?",
                    "step_by_step": "Jamoa o'tgan 2 hafta davomida nimalar a'lo darajada ishladi, qayerda qiyinchilik bo'ldi va keyingi Sprintda jarayonni qanday yaxshilash mumkinligini ochiq muhokama qiladi (doimiy o'sish).",
                    "answer": "Jarayondagi xatolardan xulosa chiqarib, jamoaviy ishni yaxshilash uchun"
                },
                {
                    "title": "Maslou ehtiyojlar piramidasi",
                    "problem": "Xodimning maoshi past va xavfsizligi ta'minlanmagan bo'lsa, unga faqat maqtov yorlig'i berish motivatsiya beradimi?",
                    "step_by_step": "Maslou qoidasiga ko'ra, quyi ehtiyojlar (fiziologik oziq-ovqat va xavfsizlik) qondirilmaguncha, inson yuqori ijtimoiy ehtiyojlarga (e'tirof va o'zini namoyon qilishga) qiziqmaydi.",
                    "answer": "Yo'q, avval bazaviy moddiy va xavfsizlik ehtiyojlari qondirilishi shart"
                }
            ],
            "exercise": "Kanban doskasidagi WIP (Work In Progress) limiti nima uchun qo'yiladi?",
            "exercise_solution": "Bir vaqtning o'zida juda ko'p ishlarni boshlab qo'yib, hech birini oxiriga yetkaza olmaslikning oldini olish va diqqatni boshlangan ishni tezroq yakunlashga qaratish uchun.",
            "check_questions": [
                {
                    "question": "Menejmentning klassik 4 ta asosiy funksiyasi qaysi?",
                    "options": ["Sotish, sotib olish, reklama, ombor", "Rejalashtirish, tashkil etish, motivatsiya, nazorat", "Ishga olish, ishdan bo'shatish, jazolash, maosh", "Dizayn, dasturlash, testlash, reliz"],
                    "correct_index": 1,
                    "explanation": "Anri Fayol bo'yicha menejment: Rejalashtirish, Tashkil etish, Rag'batlantirish (motivatsiya) va Nazoratdan iborat."
                },
                {
                    "question": "Scrum freymvorkida 1-4 haftalik rejalashtirilgan ish sikli nima deb ataladi?",
                    "options": ["Deadline", "Sprint", "Backlog", "Milestone"],
                    "correct_index": 1,
                    "explanation": "Sprint — belgilangan vazifalarni bajarish uchun ajratilgan qat'iy vaqt oraliqidir."
                },
                {
                    "question": "Scrum da mahsulot vazifalari navbati va ustuvorligini (Backlog) kim boshqaradi?",
                    "options": ["Scrum Master", "Product Owner (Mahsulot egasi)", "Bosh direktor", "Dasturchi"],
                    "correct_index": 1,
                    "explanation": "Product Owner mijozlar va biznes ehtiyojlaridan kelib chiqib Product Backlog ga javobgardir."
                }
            ],
            "tags": ["menejment", "boshqaruv", "agile", "scrum", "sprint", "kanban", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-012",
            "slug": "raqamli-marketing-smm-seo-va-voronka",
            "subject_id": "sub-52",
            "subject_name": "Marketing",
            "title": "Marketing asoslari: 4P modeli, Raqamli marketing (SMM, SEO) va Savdo voronkasi (Sales Funnel)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "O'rta",
            "objective": "Klassik 4P marketing miksi (Product, Price, Place, Promotion), Savdo voronkasi (AIDA), Raqamli marketing (SEO, SMM, Kontekst reklama) va mijoz jalb qilish narxini (CAC, LTV) o'rganish.",
            "theory": "Marketing — iste'molchilar ehtiyojlarini aniqlash, ularni qondirish va korxonaga foyda keltirish san'atidir (Filip Kotler). Klassik Marketing miksi (4P): Product (mahsulot sifati va dizayni), Price (narxlash strategiyasi), Place (tarqatish kanallari va sotuv joyi), Promotion (reklama va targ'ibot). Raqamli marketing (Digital Marketing) tarmoqlari: 1) SEO (Search Engine Optimization) — saytni qidiruv tizimlarida (Google) organik (bepul) yuqori o'ringa olib chiqish; 2) SMM (Social Media Marketing) — Instagram, Telegram, TikTok, LinkedIn orqali auditoriya yig'ish va kontent yaratish; 3) Targetlangan va kontekstli reklama (PPC — Pay-Per-Click). Savdo voronkasi (AIDA modeli): Attention (Diqqatni jalb qilish) -> Interest (Qiziqish uyg'otish) -> Desire (Xohish uyg'otish) -> Action (Xarid amali). Asosiy metrikalar: CAC (Customer Acquisition Cost — bitta mijozni jalb qilish xarajati) va LTV (Lifetime Value — mijozning butun hayoti davomida keltiradigan jami daromadi). Sog'lom biznesda LTV kamida CAC dan 3 marta ko'p bo'lishi shart (LTV > 3*CAC).",
            "examples": [
                {
                    "title": "CAC va LTV tahlili",
                    "problem": "Kompaniya reklama kampaniyasiga 10 000 dollar sarflab 500 ta yangi xaridor jalb qildi. Bitta mijoz o'rtacha 80 dollar foyda keltiradi. Biznes modeli samaralimi?",
                    "step_by_step": "1) CAC = Reklama xarajati / Yangi mijozlar = 10 000 / 500 = 20 dollar;\n2) LTV = 80 dollar;\n3) LTV / CAC nisbati = 80 / 20 = 4 (bu 3 dan katta!). Demak, har 20 dollar kiritilib 80 dollar qaytmoqda — marketing o'ta samarali.",
                    "answer": "CAC = 20 $, LTV = 80 $. Marketing juda samarali (LTV/CAC = 4)"
                },
                {
                    "title": "SEO va Target farqi",
                    "problem": "Tezda bugunoq xaridor kerak bo'lsa SEO tanlanadimi yoki Target reklamami?",
                    "step_by_step": "SEO uzoq muddatli organik jarayon (natija 3-6 oyda ko'rinadi). Tezkor va darhol sotuvlar uchun pullik Target va kontekst reklama yoqiladi.",
                    "answer": "Tezkor natija uchun Target reklama tanlanadi"
                }
            ],
            "exercise": "AIDA formulasining 4 ta bosqichini o'zbekcha nomlang.",
            "exercise_solution": "A — Attention (Diqqat), I — Interest (Qiziqish), D — Desire (Xohish), A — Action (Harakat / Xarid).",
            "check_questions": [
                {
                    "question": "Klassik marketing miksining '4P' modeliga qaysi komponentlar kiradi?",
                    "options": ["People, Power, Profit, Plan", "Product, Price, Place, Promotion", "Plan, Process, Project, Platform", "Public, Phone, Post, Price"],
                    "correct_index": 1,
                    "explanation": "4P modeli: Product (Mahsulot), Price (Narx), Place (Tarqatish), Promotion (Targ'ibot) dan iborat."
                },
                {
                    "question": "Saytni qidiruv tizimlarida (Google) bepul tabiiy yo'l bilan yuqoriga chiqarish nima deyiladi?",
                    "options": ["SMM", "SEO (Search Engine Optimization)", "Spam", "Clickbait"],
                    "correct_index": 1,
                    "explanation": "SEO qidiruv tizimlari algoritmlariga moslashib organik trafigini oshirish san'atidir."
                },
                {
                    "question": "Bitta yangi xaridorni jalb qilish uchun sarflangan o'rtacha xarajat qanday ataladi?",
                    "options": ["ROI", "CAC (Customer Acquisition Cost)", "LTV", "CTR"],
                    "correct_index": 1,
                    "explanation": "CAC (Mijoz jalb qilish narxi) reklama byudjetining jalb qilingan xaridorlar soniga nisbatidir."
                }
            ],
            "tags": ["marketing", "SMM", "SEO", "savdo voronkasi", "4P", "AIDA", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-013",
            "slug": "falsafa-ontologiya-gnoseologiya-va-inson-mohiyati",
            "subject_id": "sub-28",
            "subject_name": "Falsafa",
            "title": "Falsafa asoslari: Borliq falsafasi (Ontologiya), Bilish nazariyasi (Gnoseologiya) va Etika",
            "grade_level": "Universitet",
            "difficulty": "Murakkab",
            "objective": "Falsafaning asosiy savollari, borliq va materiya (Ontologiya), bilish imkoniyatlari (Gnoseologiya: ratsionalizm va empirizm) hamda inson hayotining ma'nosi falsafasini tushunish.",
            "theory": "Falsafa (yunoncha 'philosophia' — donolikni sevish, Pifagor tomonidan kiritilgan) — inson, jamiyat va borliqning eng umumiy qonuniyatlari, mohiyati va ma'nosini o'rganuvchi fan va dunyoqarashdir. Falsafaning asosiy bo'limlari: 1) Ontologiya — borliq va mavjudlik haqidagi ta'limot (Materiya nima? Ruh nima? Dunyo birlamchimi yoki ongmi?); 2) Gnoseologiya — bilish nazariyasi (Inson olamni bila oladimi? Haqiqat nima? Empirizm — bilish manbai sezgilar va tajriba deb biladi / Jon Lokk; Ratsionalizm — bilish manbai aql va tafakkur deb biladi / Rene Dekart: 'Cogito, ergo sum' — 'Fikr yuritayapman, demak, mavjudman'); 3) Aksiologiya — qadriyatlar falsafasi; 4) Etika — axloq va ezgulik haqidagi ta'limot (Immanuil Kantning Kategorik imperativi: 'Boshqalarga o'zingga qilinishini xohlagan muomalada bo'l'). Falsafiy oqimlar: Materializm, Idealizm, Ekzistensializm (inson erkinligi va shaxsiy mas'uliyati).",
            "examples": [
                {
                    "title": "Rene Dekartning 'Cogito, ergo sum'",
                    "problem": "Rene Dekart nima sababdan har narsadan shubhalanib, oxirida 'Fikr qilyapman, demak mavjudman' xulosasiga keldi?",
                    "step_by_step": "Sezgilarimiz aldamchi bo'lishi mumkin (tush ko'rayotgandek). Ammo shubhalanayotganimning o'zi — mening fikrlayotganimni isbotlaydi. Fikrlovchi subyekt esa mavjud bo'lmasligi mumkin emas. Bu mutlaq ishonchli boshlang'ich haqiqatdir.",
                    "answer": "Shubhalanish va fikrlash inson mavjudligining eng oliy isbotidir"
                },
                {
                    "title": "Kantning kategorik imperativi",
                    "problem": "Kantning axloqiy qonuni odamlarni boshqalardan foydalanishdan qanday qaytaradi?",
                    "step_by_step": "'Har doim insonga (o'zingga ham, boshqaga ham) faqat maqsad deb qara, hech qachon uni vositaga (foydalanish quroliga) aylantirma'. Boshqa inson uning manfaatlari uchun vosita emas, oliy qadriyatdir.",
                    "answer": "Insonga vosita emas, oliy maqsad deb qarash talab qilinadi"
                }
            ],
            "exercise": "Agnostitsizm nima va u insonning bilish qobiliyatiga qanday baho beradi?",
            "exercise_solution": "Agnostitsizm — dunyoni va uning asl mohiyatini (Kant bo'yicha 'narsa o'zida') inson aqli va sezgilari bilan to'liq bilish imkonsiz deb hisoblovchi falsafiy yo'nalish.",
            "check_questions": [
                {
                    "question": "Borliq, mavjudlik va uning umumiy qonuniyatlarini o'rganuvchi falsafa bo'limi nima deyiladi?",
                    "options": ["Gnoseologiya", "Ontologiya", "Etika", "Estetika"],
                    "correct_index": 1,
                    "explanation": "Ontologiya — borliq haqidagi falsafiy ta'limotdir."
                },
                {
                    "question": "'Cogito, ergo sum' ('Fikr qilyapman, demak, mavjudman') aforizmi qaysi faylasufga tegishli?",
                    "options": ["Aristotel", "Rene Dekart", "Immanuil Kant", "Fridrix Nitsshe"],
                    "correct_index": 1,
                    "explanation": "Ratsionalizm asoschisi Rene Dekart ushbu mashhur fikr muallifidir."
                },
                {
                    "question": "Bilimlar manbai inson aqli va mantiqiy tafakkurida deb hisoblovchi oqim qaysi?",
                    "options": ["Empirizm", "Ratsionalizm", "Skeptitsizm", "Materializm"],
                    "correct_index": 1,
                    "explanation": "Ratsionalizm (lotincha ratio — aql) bilishning asosiy mezonini sof aql deb hisoblaydi."
                }
            ],
            "tags": ["falsafa", "ontologiya", "gnoseologiya", "dekart", "kant", "etika", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-014",
            "slug": "shaxs-psixologiyasi-temperament-va-hissiy-intellekt",
            "subject_id": "sub-29",
            "subject_name": "Psixologiya",
            "title": "Umumiy psixologiya: Temperament turlari, Shaxs xarakteri va Hissiy intellekt (EQ)",
            "grade_level": "Universitet",
            "difficulty": "O'rta",
            "objective": "Gippokratning 4 ta temperament tipi (sangvinik, xolerik, flegmatik, melanxolik), xarakter aksentuatsiyalari va Hissiy intellekt (EQ) komponentlarini o'rganish.",
            "theory": "Psixologiya — inson ruhiyati, xulq-atvori, ruhiy jarayonlari va shaxsiy xususiyatlarini o'rganuvchi fandir. Temperament — inson oliy asab faoliyatining tug'ma tipi bo'lib, emotsiyalarning tezligi va kuchi bilan belgilanadi (Gippokrat-Pavlov tasnifi): 1) Sangvinik (kuchli, muvozanatli, harakatchan) — quvnoq, kirishimli, tez moslashuvchan; 2) Xolerik (kuchli, muvozanatsiz) — jo'shqin, qiziqqon, tez jahli chiqadigan, faol kurashchi; 3) Flegmatik (kuchli, muvozanatli, kamharakat) — xotirjam, sabrli, his-tuyg'ularini oshkor qilmaydigan; 4) Melanxolik (kuchsiz asab tipi) — nozik ta'sirchan, tez xafa bo'ladigan, ichki kechinmalarga boy. Hissiy intellekt (EQ — Daniel Goleman): o'z his-tuyg'ularini tushunish va boshqarish, boshqalar his-tuyg'ularini his qilish (empatiya) va ijtimoiy munosabatlarni samarali qurish qobiliyatidir. Muvaffaqiyatda EQ ko'pincha oddiy IQ dan muhimroq hisoblanadi.",
            "examples": [
                {
                    "title": "To'rtta temperamentning shlyapa ustiga o'tirib qo'yilgandagi reaksiyasi",
                    "problem": "Mashhur psixologik latifada yangi shlyapasi ustiga birov o'tirib ezib qo'yganda 4 ta temperament qanday munosabat bildiradi?",
                    "step_by_step": "1) Xolerik — g'azablanib aybdorning yoqasiga yopishadi;\n2) Sangvinik — qah-qah urib kuladi va hazilga aylantiradi;\n3) Flegmatik — xotirjam cho'ntagiga solib ketadi ('baribir kiyib bo'lmaydi');\n4) Melanxolik — ko'z yosh to'kib chuqur qayg'uga botadi.",
                    "answer": "Xolerik g'azablanadi, Sangvinik kuladi, Flegmatik befarq, Melanxolik yig'laydi"
                },
                {
                    "title": "Empatiya nima?",
                    "problem": "Empatiya hissi nima va u professional muloqotda nega zarur?",
                    "step_by_step": "Empatiya — o'zini boshqa odamning o'rniga qo'yib, uning his-tuyg'ularini, dardini va nuqtai nazarini chin dildan his qila olishdir. Bu rahbarlar, o'qituvchilar va shifokorlar uchun eng muhim ko'nikmadir.",
                    "answer": "Boshqa insonning his-tuyg'ularini tushunish va unga sherik bo'lish"
                }
            ],
            "exercise": "Temperament va Xarakter orasidagi asosiy farq nimada?",
            "exercise_solution": "Temperament — tug'ma, biologik asab xususiyati bo'lib o'zgarmaydi; Xarakter esa hayot davomida tarbiya, muhit va iroda ta'sirida shakllanadi va o'zgarishi mumkin.",
            "check_questions": [
                {
                    "question": "Tez qo'zg'aluvchan, hissiyotli va ba'zan jizzaki bo'lgan kuchli, lekin muvozanatsiz temperament qaysi?",
                    "options": ["Sangvinik", "Xolerik", "Flegmatik", "Melanxolik"],
                    "correct_index": 1,
                    "explanation": "Xolerik asab tizimi kuchli, ammo tormozlanish va qo'zg'alish muvozanatlashmagan jizzaki xarakterdir."
                },
                {
                    "question": "O'z va o'zgalar hissiyotlarini tushunish va boshqarish qobiliyati nima deb ataladi?",
                    "options": ["IQ (Intellekt koeffitsiyenti)", "EQ (Hissiy intellekt)", "Ekstroversiya", "Konformizm"],
                    "correct_index": 1,
                    "explanation": "EQ (Emotional Quotient) his-tuyg'ularni anglash va boshqarish madaniyatidir."
                },
                {
                    "question": "Xotirjam, sabr-toqatli va hissiyotlarini namoyon qilmaydigan sokin temperament turi qaysi?",
                    "options": ["Sangvinik", "Flegmatik", "Xolerik", "Melanxolik"],
                    "correct_index": 1,
                    "explanation": "Flegmatik bosiq, mulohazali va xotirjam asab tizimiga egadir."
                }
            ],
            "tags": ["psixologiya", "temperament", "xarakter", "EQ", "hissiy intellekt", "empatiya", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "uni-015",
            "slug": "mantiq-tafakkur-shakllari-va-xatolar",
            "subject_id": "sub-30",
            "subject_name": "Mantiq",
            "title": "Mantiq ilmi: Tafakkur shakllari (Tushuncha, Hukm, Xulosa) va Mantiqiy qonunlar",
            "grade_level": "Universitet",
            "difficulty": "O'rta",
            "objective": "Tafakkurning 3 ta shakli, 4 ta asosiy mantiqiy qonun (ayaniylik, ziddiyatsizlik, uchinchisi istisno, yetarli asos) va sofistika/mantiqiy xatolarni fosh qilish.",
            "theory": "Mantiq (Logika — yunoncha 'logos' — so'z, fikr, qonun, Aristotel tomonidan asos solingan) — to'g'ri tafakkur yuritish qoidalari va shakllarini o'rganuvchi fandir. Tafakkurning 3 ta shakli:\n1) Tushuncha — narsa va hodisalarning eng muhim xossalarini umumlashtirib ifodalash (masalan, 'talaba', 'uchburchak');\n2) Hukm — biror narsa haqida biror narsani tasdiqlovchi yoki inkor etuvchi fikr ('Oltin metalldir' — rost hukm, 'Oy quyoshdan katta' — yolg'on hukm);\n3) Xulosa chiqarish (Sillogizm) — bir yoki bir nechta boshlang'ich hukmlardan (asoslardan) yangi hukm hosil qilish (Masalan: Barcha insonlar foniydir -> Suqrot insondir -> Demak, Suqrot foniydir).\n4 ta asosiy mantiqiy qonun:\n1) Ayniyat qonuni (A = A): fikr yuritish jarayonida har bir tushuncha o'z ma'nosida qat'iy saqlanishi kerak;\n2) Ziddiyatsizlik qonuni: Ikkita bir-biriga zid hukm bir vaqtda va bitta nisbatda birdek rost bo'la olmaydi;\n3) Uchinchisi istisno qonuni: Zid hukmlardan biri albatta rost, ikkinchisi yolg'on bo'ladi, uchinchi oraliq hukm bo'lishi mumkin emas;\n4) Yetarli asos qonuni (Leybnits): Har qanday to'g'ri fikr yetarli dalillar bilan asoslangan bo'lishi shart.",
            "examples": [
                {
                    "title": "Deduksiya va Induksiya",
                    "problem": "Deduktiv va Induktiv xulosa chiqarishning farqi nimada?",
                    "step_by_step": "Deduksiya — umumiy qoidadan xususiy holatga xulosa chiqarish (Barcha metallar elektr o'tkazadi -> Temir metall -> Temir elektr o'tkazadi);\nInduksiya — xususiy misollardan umumiy xulosaga borish (Temir o'tkazadi, mis o'tkazadi, oltin o'tkazadi -> Barcha metallar elektr o'tkazar ekan).",
                    "answer": "Deduksiya: umumiydan xususiyga; Induksiya: xususiydan umumiyga"
                },
                {
                    "title": "Mantiqiy xatoni aniqlash (Sofizm)",
                    "problem": "'Nimaniki yo'qotmagan bo'lsang, o'sha narsa senda bor. Sen shoxlaringni yo'qotmading. Demak, sening shoxlaring bor'. Bu xulosada qaysi mantiqiy qonun buzilgan?",
                    "step_by_step": "Bu yerda Ayniyat qonuni buzilgan. 'Yo'qotmagan narsa' tushunchasi dastlab inson mulkida bo'lgan narsalar haqida, keyin esa umuman bo'lmagan narsa haqida turlicha ma'noda ishlatilib, so'z o'yini (sofizm) qilingan.",
                    "answer": "Ayniyat qonuni buzilgan (so'z o'yini va soxta asos)"
                }
            ],
            "exercise": "Arastu yaratgan deduktiv xulosa chiqarish shakli (Sillogizm) nimalardan tashkil topgan?",
            "exercise_solution": "Katta asos (umumiy qoida), kichik asos (xususiy fakt) va ulardan kelib chiquvchi yakuniy Xulosadan tashkil topgan.",
            "check_questions": [
                {
                    "question": "Mantiq ilmining asoschisi deb qaysi antik faylasuf tan olingan?",
                    "options": ["Suqrot", "Aflotun (Platon)", "Aristotel (Arastu)", "Pifagor"],
                    "correct_index": 2,
                    "explanation": "Aristotel 'Organon' asarida to'g'ri tafakkur mantiqiy qonuniyatlarini tizimlashtirgan."
                },
                {
                    "question": "'Bir vaqtda va bir nisbatda narsa ham oq, ham qora bo'la olmaydi' qaysi mantiq qonuni?",
                    "options": ["Ayniyat qonuni", "Ziddiyatsizlik qonuni", "Yetarli asos qonuni", "Uchinchisi istisno qonuni"],
                    "correct_index": 1,
                    "explanation": "Ziddiyatsizlik qonuniga ko'ra ikkita qarama-qarshi hukm bir vaqtda haqiqat bo'la olmaydi."
                },
                {
                    "question": "Xususiy dalillardan umumiy xulosaga boruvchi tafakkur yo'li nima deyiladi?",
                    "options": ["Deduksiya", "Induksiya", "Abstraksiya", "Analogiya"],
                    "correct_index": 1,
                    "explanation": "Induksiya yakka holatlarni umumlashtirish orqali umumiy xulosaga olib boradi."
                }
            ],
            "tags": ["mantiq", "tafakkur", "aristotel", "sillogizm", "deduksiya", "induksiya", "universitet"],
            "duration_minutes": 30
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_university_materials()
    print(f"Generated {len(mats)} University materials.")
