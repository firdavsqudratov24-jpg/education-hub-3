# -*- coding: utf-8 -*-
"""
Builder for Informatika va Dasturlash (20 materials: dev-001 to dev-020)
- sub-04: Informatika (6: dev-001 to dev-006)
- sub-37: Dasturlash (4: dev-007 to dev-010)
- sub-38: Web Development (4: dev-011 to dev-014)
- sub-39: Python (3: dev-015 to dev-017)
- sub-40: JavaScript (3: dev-018 to dev-020)
"""

def get_cs_programming_materials():
    materials = [
        # INFORMATIKA (6)
        {
            "id": "dev-001",
            "slug": "axborot-olchov-birliklari-va-ikkilik-sanoq-tizimi",
            "subject_id": "sub-04",
            "subject_name": "Informatika",
            "title": "Axborot, uning o'lchov birliklari va ikkilik (binar) sanoq tizimi",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Axborot tushunchasi, bit, bayt, kilobayt, megabayt o'lchovlari hamda o'nlik sonlarni ikkilik sanoq tizimiga o'tkazishni o'rganish.",
            "theory": "Axborot — atrof-muhitdagi voqea-hodisalar, buyumlar haqidagi ma'lumotlar yig'indisidir. Kompyuterda barcha ma'lumotlar ikkilik sanoq tizimida (0 va 1 signallari orqali) ifodalanadi. Eng kichik axborot o'lchov birligi — bit (binary digit). 1 bayt = 8 bit (bitta harf yoki belgini xotirada saqlash uchun 1 bayt kerak bo'ladi). Axborot karrali birliklari (2 ning darajalari): 1 KB (Kilobayt) = 1024 bayt = 2^10 bayt; 1 MB (Megabayt) = 1024 KB = 2^20 bayt; 1 GB (Gigabayt) = 1024 MB; 1 TB (Terabayt) = 1024 GB. Sanoq tizimlari: O'nlik sonni ikkilik sanoq tizimiga o'tkazish uchun son 0 bo'lguncha ketma-ket 2 ga bo'linadi va qoldiqlar teskari tartibda (pastdan yuqoriga) yoziladi.",
            "examples": [
                {
                    "title": "O'nlik sonni ikkilikka o'tkazish",
                    "problem": "25 sonini ikkilik sanoq tizimiga o'tkazing.",
                    "step_by_step": "1) 25 : 2 = 12 (qoldiq 1)\n2) 12 : 2 = 6 (qoldiq 0)\n3) 6 : 2 = 3 (qoldiq 0)\n4) 3 : 2 = 1 (qoldiq 1)\n5) 1 : 2 = 0 (qoldiq 1)\nQoldiqlarni teskari yozamiz: 11001_2.",
                    "answer": "11001_2"
                },
                {
                    "title": "Axborot hajmini hisoblash",
                    "problem": "Matn 4 sahifadan iborat, har bir sahifada 32 ta qator, har bir qatorda 64 ta belgi bor (1 belgi = 1 bayt). Matn hajmini Kilobaytda toping.",
                    "step_by_step": "1) Jami belgilar: 4 * 32 * 64 = 2^2 * 2^5 * 2^6 = 2^13 bayt = 8192 bayt.\n2) Kilobaytga o'tkazish: 8192 / 1024 = 8 KB.",
                    "answer": "8 KB"
                }
            ],
            "exercise": "Ikkilik sanoq tizimidagi 10110_2 sonini o'nlik sanoq tizimiga o'tkazing.",
            "exercise_solution": "1*2^4 + 0*2^3 + 1*2^2 + 1*2^1 + 0*2^0 = 16 + 0 + 4 + 2 + 0 = 22.",
            "check_questions": [
                {
                    "question": "1 bayt necha bitga teng?",
                    "options": ["2 bit", "4 bit", "8 bit", "16 bit"],
                    "correct_index": 2,
                    "explanation": "Standart bo'yicha 1 bayt 8 ta bitdan iborat."
                },
                {
                    "question": "1 Megabaytda (MB) necha Kilobayt (KB) bor?",
                    "options": ["1000 KB", "1024 KB", "2048 KB", "1048576 KB"],
                    "correct_index": 1,
                    "explanation": "Axborot o'lchovida 2^10 = 1024 karrali qadam ishlatiladi: 1 MB = 1024 KB."
                },
                {
                    "question": "Kompyuter apparat ta'minotida mantiqiy 0 va 1 nimani anglatadi?",
                    "options": ["Ranglarni", "Elektr toki (kuchlanish) borligi va yo'qligini", "Klaviatura harflarini", "Tovush to'lqinlarini"],
                    "correct_index": 1,
                    "explanation": "Tranzistorlarda past kuchlanish 0, yuqori kuchlanish 1 deb qabul qilinadi."
                }
            ],
            "tags": ["informatika", "axborot o'lchovi", "bayt", "ikkilik tizim", "binary", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "dev-002",
            "slug": "kompyuter-arxitekturasi-protsessor-va-xotira",
            "subject_id": "sub-04",
            "subject_name": "Informatika",
            "title": "Kompyuter arxitekturasi: protsessor (CPU), operativ xotira (RAM) va tashqi qurilmalar",
            "grade_level": "6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Fon Neyman arxitekturasi, protsessor takt chastotasi, tezkor xotira (RAM va ROM) hamda kiritish-chiqarish qurilmalarini bilish.",
            "theory": "Zamonaviy kompyuterlar Jon fon Neyman tomonidan 1945-yilda taklif qilingan tamoyillar asosida ishlaydi (dasturning xotirada saqlanishi, ikkilik kodlash, ketma-ket bajarilish). Kompyuterning asosiy tugunlari: 1) Markaziy protsessor (CPU) — kompyuterning 'miyasi' bo'lib, arifmetik-mantiqiy qurilma (ALU), boshqaruv qurilmasi (CU) va registrlar xotirasidan iborat. Asosiy ko'rsatkichlari: yadro soni va takt chastotasi (Gigagerts, GHz); 2) Xotira: Ichki xotira — Operativ xotira (RAM — elektr toki o'chganda ma'lumot yo'qoladigan tezkor xotira) va Doimiy xotira (ROM/BIOS — zavod dasturlari saqlanadi, o'chmaydi). Kesh xotira (L1, L2, L3 — CPU va RAM orasidagi o'ta tez xotira); Tashqi xotira — qattiq disk (HDD) va tezkor yarimo'tkazgichli disklar (SSD, NVMe); 3) Kiritish qurilmalari: klaviatura, sichqoncha, skaner, mikrofon; 4) Chiqarish qurilmalari: monitor, printer, dinamik, proyektor.",
            "examples": [
                {
                    "title": "RAM va SSD farqi",
                    "problem": "Operativ xotira (RAM) va qattiq disk (SSD) o'rtasidagi asosiy funksional farq nimada?",
                    "step_by_step": "RAM — o'ta tez ishlaydi, ammo faqat ochiq turgan dasturlarni vaqtinchalik saqlaydi, kompyuter o'chirilganda tozalanadi. SSD — sekinroq, lekin kompyuter o'chsa ham ma'lumotlarni doimiy saqlaydi.",
                    "answer": "RAM vaqtinchalik tezkor, SSD doimiy uzoq muddatli xotira"
                },
                {
                    "title": "Protsessor takt chastotasi",
                    "problem": "Protsessorning 3.2 GHz chastotasi nimani anglatadi?",
                    "step_by_step": "1 Gerts = sekundiga 1 ta amal. 3.2 GHz (Gigagerts) protsessor bir sekund ichida 3 milliard 200 million ta taktli amalni bajara olishini anglatadi.",
                    "answer": "Sekundiga 3.2 milliard taktli amal"
                }
            ],
            "exercise": "Kompyuter yoqilganda eng birinchi ishga tushuvchi BIOS dasturi qayerda saqlanadi?",
            "exercise_solution": "Ona plata (motherboard) ustida joylashgan doimiy xotira mikrosxemasida (ROM / EEPROM) saqlanadi.",
            "check_questions": [
                {
                    "question": "Kompyuter o'chirilganda qaysi xotiradagi ma'lumotlar butunlay o'chib ketadi?",
                    "options": ["SSD disk", "Operativ xotira (RAM)", "ROM (Doimiy xotira)", "Flash xotira"],
                    "correct_index": 1,
                    "explanation": "RAM (Random Access Memory) uchuvchan xotira bo'lib, elektr ta'minoti to'xtashi bilan ma'lumot yo'qoladi."
                },
                {
                    "question": "Quyidagilardan qaysi biri faqat axborotni kiritish qurilmasi hisoblanadi?",
                    "options": ["Monitor", "Printer", "Skaner", "Karnay (dinamik)"],
                    "correct_index": 2,
                    "explanation": "Skaner qog'ozdagi tasvir va matnlarni kompyuterga kiritish qurilmasidir."
                },
                {
                    "question": "Zamonaviy kompyuterlarning fundamental arxitekturasi kimning nomi bilan ataladi?",
                    "options": ["Alan Tyuring", "Blez Paskal", "Jon fon Neyman", "Bill Geyts"],
                    "correct_index": 2,
                    "explanation": "Fon Neyman arxitekturasi 1945-yildan buyon barcha zamonaviy hisoblash mashinalari asosi hisoblanadi."
                }
            ],
            "tags": ["informatika", "kompyuter arxitekturasi", "protsessor", "RAM", "SSD", "fon neyman", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "dev-003",
            "slug": "algoritmlash-asoslari-va-blok-sxemalar",
            "subject_id": "sub-04",
            "subject_name": "Informatika",
            "title": "Algoritmlash asoslari, turlari va blok-sxemalar bilan tasvirlash",
            "grade_level": "7-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Algoritm ta'rifi va xossalari (diskretlik, tushunarlilik, aniqlik, ommaviylik, natijaviylik), chiziqli, tarmoqlanuvchi va takrorlanuvchi algoritmlar blok-sxemalarini chizish.",
            "theory": "Qo'yilgan maqsadga erishish yoki masalani yechish uchun bajaruvchiga berilgan buyruqlarning aniq va tartibli ketma-ketligi algoritm deyiladi. Algoritm xossalari: 1) Diskretlik (alohida qadamlardan iborat bo'lishi); 2) Tushunarlilik (bajaruvchining buyruqlar sistemasiga mos bo'lishi); 3) Aniqlik (har bir buyruq bir xil talqin qilinishi); 4) Ommaviylik (bir xil toifadagi barcha masalalar uchun yaroqli bo'lishi); 5) Natijaviylik (chekli qadamlardan so'ng aniq natija berishi yoki yechim yo'qligini ko'rsatishi). Blok-sxema elementlari: Oval — boshlanishi va tugashi; Parallelogramm — ma'lumotlarni kiritish va chiqarish; To'g'ri to'rtburchak — hisoblash jarayoni (amal); Romb — shartni tekshirish (ha/yo'q tarmoqlanishi). Algoritm turlari: Chiziqli (buyruqlar ketma-ket bajariladi), Tarmoqlanuvchi (shartga qarab u yoki bu yo'nalish tanlanadi), Takrorlanuvchi / Siklik (muayyan qadamlar bir necha marta takrorlanadi).",
            "examples": [
                {
                    "title": "Tarmoqlanuvchi algoritm",
                    "problem": "Berilgan sonning musbat yoki manfiyligini aniqlovchi algoritm qadami qanday bo'ladi?",
                    "step_by_step": "1) Boshlash; 2) x sonini kiritish; 3) Rombda shart: x >= 0? Agar 'Ha' bo'lsa -> 'Musbat' deb chiqarish; Agar 'Yo'q' bo'lsa -> 'Manfiy' deb chiqarish; 4) Tamom.",
                    "answer": "Shart blokida x >= 0 tekshiriladi"
                },
                {
                    "title": "Siklik (takrorlanuvchi) algoritm",
                    "problem": "1 dan 100 gacha bo'lgan sonlar yig'indisini hisoblash algoritmi qanday tuziladi?",
                    "step_by_step": "1) S = 0, i = 1; 2) S = S + i; 3) i = i + 1; 4) i <= 100? Agar 'Ha' bo'lsa 2-qadamga qaytish (sikil); Agar 'Yo'q' bo'lsa S ni chiqarish va tamom.",
                    "answer": "Sikl hisoblagichi (i) 100 ga yetguncha takrorlanadi"
                }
            ],
            "exercise": "Algoritmning 'natijaviylik' xossasi buzilishiga misol keltiring.",
            "exercise_solution": "Cheksiz sikl (infinite loop) — algoritm shartining noto'g'riligi sababli cheksiz aylanib to'xtamasligi va natija bermasligi natijaviylik xossasining buzilishidir.",
            "check_questions": [
                {
                    "question": "Blok-sxemada shartni tekshirish uchun qaysi geometrik shakl ishlatiladi?",
                    "options": ["To'g'ri to'rtburchak", "Oval", "Romb", "Parallelogramm"],
                    "correct_index": 2,
                    "explanation": "Shart bloklari har doim romb shaklida tasvirlanadi (ikkita chiqish: Ha va Yo'q)."
                },
                {
                    "question": "Algoritmning bitta emas, o'sha turdagi barcha masalalarni yecha olish qobiliyati qaysi xossasi?",
                    "options": ["Diskretlik", "Ommaviylik", "Aniqlik", "Natijaviylik"],
                    "correct_index": 1,
                    "explanation": "Ommaviylik — algoritm ixtiyoriy boshlang'ich berilganlar bilan ishlay olishidir."
                },
                {
                    "question": "Ma'lumotlarni kiritish va chiqarish blok-sxemada qanday shaklda chiziladi?",
                    "options": ["Parallelogramm", "Doira", "Uchburchak", "Kvadrat"],
                    "correct_index": 0,
                    "explanation": "Parallelogramm kiritish va chiqarish amallari uchun standart shartli belgi hisoblanadi."
                }
            ],
            "tags": ["informatika", "algoritm", "blok-sxema", "sikl", "tarmoqlanish", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "dev-004",
            "slug": "kompyuter-tarmoqlari-va-internet-protokollari",
            "subject_id": "sub-04",
            "subject_name": "Informatika",
            "title": "Kompyuter tarmoqlari: LAN, WAN, IP manzillar, DNS va OSI modeli",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Lokal (LAN) va global (WAN) tarmoqlar, tarmoq topologiyalari, IP manzillar (IPv4 va IPv6), DNS qanday ishlashi va mijoz-server arxitekturasini bilish.",
            "theory": "Kompyuter tarmog'i — axborot va resurslarni o'zaro almashish maqsadida birlashtirilgan kompyuterlar tizimidir. Masshtabiga ko'ra: LAN (Local Area Network — bitta xona yoki bino ichidagi lokal tarmoq) va WAN (Wide Area Network — butun dunyo bo'ylab global tarmoq, Internet). Asosiy tarmoq topologiyalari: yulduzsimon (star), shinaviy (bus), halqasimon (ring). Internetda har bir qurilma unikal IP-manzilga ega. IPv4 — 32 bitli (4 ta 0-255 gacha sonlar nuqta bilan: 192.168.1.1); IPv6 — 128 bitli o'n oltilik manzil (manzillar yetishmovchiligini hal qilgan). DNS (Domain Name System) — inson tushunadigan domen nomlarini (masalan, google.com) kompyuter tushunadigan raqamli IP-manzilga (masalan, 142.250.180.206) aylantiruvchi global ma'lumotlar bazasi. Asosiy protokollar: HTTP/HTTPS (veb-sahifalar), TCP/IP (ishonchli paket uzatish), FTP (fayllar uzatish).",
            "examples": [
                {
                    "title": "DNS qanday ishlaydi?",
                    "problem": "Brauzerga 'educationhub.uz' deb yozganimizda sahifa qanday topiladi?",
                    "step_by_step": "1) Kompyuter DNS serveriga murojaat qiladi: 'educationhub.uz ning IP si nima?';\n2) DNS server javob qaytaradi: 'IP: 185.196.220.50';\n3) Brauzer to'g'ridan-to'g'ri ushbu IP dagi veb-serverga HTTPS so'rov yuboradi va sahifani yuklab oladi.",
                    "answer": "Domen nomi DNS orqali IP-manzilga o'giriladi"
                },
                {
                    "title": "IPv4 manzil to'g'riligini tekshirish",
                    "problem": "'192.168.300.1' manzili nima sababdan haqiqiy IPv4 manzili bo'la olmaydi?",
                    "step_by_step": "IPv4 da har bir son 1 bayt (8 bit) dan iborat bo'lib, uning qiymati faqat 0 dan 255 gacha bo'lishi mumkin. 300 soni bu diapazondan tashqarida.",
                    "answer": "Har bir oktet 0 dan 255 gacha bo'lishi shart (300 noto'g'ri)"
                }
            ],
            "exercise": "Xavfsiz HTTPS protokoli oddiy HTTP dan nimasi bilan farq qiladi?",
            "exercise_solution": "HTTPS da ma'lumotlar SSL/TLS protokollari yordamida shifrlanadi (kriptografik himoyalanadi), uchinchi shaxslar parollar va shaxsiy ma'lumotlarni tutib o'g'irlay olmaydi.",
            "check_questions": [
                {
                    "question": "Domen nomlarini IP-manzillarga aylantirib beruvchi tizim nima deyiladi?",
                    "options": ["DHCP", "DNS (Domain Name System)", "FTP", "HTML"],
                    "correct_index": 1,
                    "explanation": "DNS internetning 'telefon kitobi' bo'lib, sayt nomlarini raqamli IP larga o'giradi."
                },
                {
                    "question": "Bitta bino yoki xona ichidagi kompyuterlarni birlashtiruvchi tarmoq qaysi?",
                    "options": ["WAN", "MAN", "LAN", "PAN"],
                    "correct_index": 2,
                    "explanation": "LAN (Local Area Network) lokal tarmoq hisoblanadi."
                },
                {
                    "question": "IPv4 manzili necha bitdan iborat?",
                    "options": ["16 bit", "32 bit", "64 bit", "128 bit"],
                    "correct_index": 1,
                    "explanation": "IPv4 32 bitdan (4 ta 8 bitlik baytdan) iborat."
                }
            ],
            "tags": ["informatika", "tarmoqlar", "internet", "IP manzil", "DNS", "HTTP", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "dev-005",
            "slug": "malumotlar-bazasi-va-sql-asoslari",
            "subject_id": "sub-04",
            "subject_name": "Informatika",
            "title": "Ma'lumotlar bazasi tushunchasi, Relyatsion modellar va SQL so'rovlar tili",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Relyatsion MB (jadvallar, Primary Key, Foreign Key), MBBT (DBMS) va asosiy SQL so'rovlarini (SELECT, INSERT, UPDATE, DELETE) yozish.",
            "theory": "Ma'lumotlar bazasi (MB) — ma'lum qoidalar asosida tartiblangan, o'zaro bog'langan ma'lumotlar to'plamidir. Ularni boshqarish dasturi MBBT (Ma'lumotlar Bazasini Boshqarish Tizimi — MySQL, PostgreSQL, SQLite, Oracle) deyiladi. Relyatsion MB ma'lumotlarni ikki o'lchamli jadvallarda (qatorlar — yozuv/record, ustunlar — maydon/field) saqlaydi. Primary Key (birlamchi kalit) — jadvaldagi har bir qatorni bir qiymatli identifikatsiyalovchi unikal ustun (id). Foreign Key (tashqi kalit) — ikkita jadvalni bir-biriga bog'lovchi kalit. SQL (Structured Query Language) — ma'lumotlar bazasi bilan muloqot qilish tili:\n- SELECT: ma'lumotlarni tanlash (SELECT * FROM users WHERE age > 18);\n- INSERT INTO: yangi ma'lumot qo'shish (INSERT INTO users (name, age) VALUES ('Ali', 20));\n- UPDATE: ma'lumotni tahrirlash (UPDATE users SET age = 21 WHERE id = 1);\n- DELETE: ma'lumotni o'chirish (DELETE FROM users WHERE id = 5).",
            "examples": [
                {
                    "title": "SELECT so'rovi va filtrlash",
                    "problem": "'Students' jadvalidan bahosi 5 bo'lgan o'quvchilarning ismi va familiyasini saralangan holda tanlab oling.",
                    "step_by_step": "SQL kodi:\nSELECT first_name, last_name \nFROM students \nWHERE grade = 5 \nORDER BY last_name ASC;",
                    "answer": "SELECT first_name, last_name FROM students WHERE grade = 5 ORDER BY last_name ASC;"
                },
                {
                    "title": "Primary Key ahamiyati",
                    "problem": "Nima sababdan odamning ism-familiyasi Primary Key qilib olinmaydi?",
                    "step_by_step": "Chunki bir xil ism-familiyali odamlar juda ko'p uchraydi. Primary Key esa mutlaqo takrorlanmas (unikal) bo'lishi shart, shu bois unikal raqamli ID ishlatiladi.",
                    "answer": "Ism takrorlanishi mumkin, Primary Key esa mutlaqo unikal bo'lishi shart"
                }
            ],
            "exercise": "'Users' jadvalidan 'status' ustuni 'banned' bo'lgan barcha yozuvlarni o'chiruvchi SQL so'rovini yozing.",
            "exercise_solution": "DELETE FROM users WHERE status = 'banned';",
            "check_questions": [
                {
                    "question": "Jadvaldagi har bir yozuvni unikal ajratib turuvchi kalit nima deyiladi?",
                    "options": ["Foreign Key", "Primary Key", "Index Key", "Super Key"],
                    "correct_index": 1,
                    "explanation": "Primary Key (birlamchi kalit) yozuvning yagona unikal identifikatoridir."
                },
                {
                    "question": "Ma'lumotlar bazasidan ma'lumotlarni o'qib olish (tanlash) uchun qaysi SQL buyrug'i ishlatiladi?",
                    "options": ["GET", "READ", "SELECT", "FETCH"],
                    "correct_index": 2,
                    "explanation": "SELECT ma'lumotlarni qidirish va olish uchun standart SQL komandasidir."
                },
                {
                    "question": "Ikkita jadval orasidagi aloqani bog'lovchi kalit nima deyiladi?",
                    "options": ["Primary Key", "Foreign Key (tashqi kalit)", "Unique Key", "Check Key"],
                    "correct_index": 1,
                    "explanation": "Foreign Key bir jadval ustunini ikkinchi jadvaldagi Primary Key ga bog'laydi."
                }
            ],
            "tags": ["informatika", "ma'lumotlar bazasi", "SQL", "select", "primary key", "database", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "dev-006",
            "slug": "kiberxavfsizlik-va-axborot-himoyasi-asoslari",
            "subject_id": "sub-04",
            "subject_name": "Informatika",
            "title": "Kiberxavfsizlik asoslari: viruslar, fishing, parollar xavfsizligi va shifrlash",
            "grade_level": "9-11-sinf",
            "difficulty": "O'rta",
            "objective": "Zararli dasturlar turlari (virus, troyan, ransomware), ijtimoiy muhandislik (fishing), ikki bosqichli autentifikatsiya (2FA) va shaxsiy ma'lumotlarni himoyalash.",
            "theory": "Kiberxavfsizlik — kompyuter tizimlari, tarmoqlar va ma'lumotlarni ruxsatsiz kirish, o'g'irlash yoki shikastlashdan himoya qilish sohasidir. Zararli dasturlar (Malware): 1) Kompyuter virusi — boshqa fayllarga yuqib ko'payuvchi kod; 2) Troyan (Trojan) — foydali dastur niqobi ostidagi josus dastur; 3) Ransomware (tovlamachi dastur) — kompyuterdagi barcha fayllarni shifrlab, pul talab qiluvchi virus (masalan, WannaCry). Kiberhujum usullari: Fishing (Phishing) — soxta bank yoki ijtimoiy tarmoq saytlari orqali foydalanuvchining login va parollarini aldab olish (ijtimoiy muhandislik). Himoya choralari: Kuchli parollar (kamida 12 ta belgi: katta-kichik harflar, raqamlar, maxsus belgilar), Ikki bosqichli autentifikatsiya (2FA / Two-Factor Authentication — parol + SMS kod), antivirus dasturlaridan foydalanish va shubhali havolalarni ochmaslik.",
            "examples": [
                {
                    "title": "Fishing xatini aniqlash",
                    "problem": "'Sizning bankingizdan xabar: Hisobingiz bloklandi! Qayta ochish uchun ushbu havolaga kiring: click-bank-security.xyz' xatiga qanday munosabat bildirish kerak?",
                    "step_by_step": "1) Domen nomi shubhali (.xyz, bankning rasmiy sayti emas);\n2) Banklar hech qachon shoshilinch parol kiritishni talab qiluvchi havolalar yubormaydi;\n3) Bu odatiy fishing hujumi. Havolani ochmaslik va xatni bloklash kerak.",
                    "answer": "Bu fishing hujumi, havolani ochmaslik kerak"
                },
                {
                    "title": "2FA (Ikki bosqichli tekshiruv) nima uchun kerak?",
                    "problem": "Agar xaker sizning parolingizni bilib olsa, 2FA sizni qanday himoya qiladi?",
                    "step_by_step": "Xaker parolni to'g'ri kiritgan taqdirda ham, tizimga kirish uchun sizning telefoningizga kelgan 6 xonali tasdiqlash kodi talab qilinadi. Telefoningiz o'zingizda bo'lgani uchun u akkauntga kira olmaydi.",
                    "answer": "Yot kishi parolni bilsa ham SMS kodi bo'lmasa kira olmaydi"
                }
            ],
            "exercise": "Qaysi parol xavfsizlik talablariga to'liq javob beradi: '12345678', 'iloveuzbekistan', 'T@shk3nt_2026#Ex'?",
            "exercise_solution": "'T@shk3nt_2026#Ex' — katta va kichik harflar, raqamlar va maxsus belgilar (@, _, #) qatnashgan kuchli parol.",
            "check_questions": [
                {
                    "question": "Foydalanuvchilarni aldab ularning parollarini o'g'irlashga qaratilgan kiberfiribgarlik nima deyiladi?",
                    "options": ["Spam", "Fishing (Phishing)", "DDoS", "Mining"],
                    "correct_index": 1,
                    "explanation": "Fishing — soxta havolalar va xatlar orqali ma'lumotlarni aldov yo'li bilan o'g'irlash usuli."
                },
                {
                    "question": "Fayllarni shifrlab qo'yib, ochish uchun pul (to'lov) talab qiladigan zararli dastur nima deb ataladi?",
                    "options": ["Shpion dastur", "Ransomware (tovlamachi dastur)", "Adware", "Rootkit"],
                    "correct_index": 1,
                    "explanation": "Ransomware fayllarni qulflab, kalit uchun kriptovalyutada to'lov talab qiladi."
                },
                {
                    "question": "2FA (Two-factor authentication) nimani ta'minlaydi?",
                    "options": ["Internet tezligini 2 barobar oshiradi", "Hisobga kirishda paroldan tashqari ikkinchi xavfsizlik kodi bilan qo'shimcha himoya beradi", "Fayllarni 2 marta siqadi", "Viruslarni avtomatik o'chiradi"],
                    "correct_index": 1,
                    "explanation": "2FA ikki bosqichli himoya vositasi bo'lib, xavfsizlikni bir necha barobar oshiradi."
                }
            ],
            "tags": ["kiberxavfsizlik", "fishing", "parol", "2FA", "axborot xavfsizligi", "ransomware", "11-sinf"],
            "duration_minutes": 35
        },

        # DASTURLASH (4)
        {
            "id": "dev-007",
            "slug": "dasturlash-paradigmalari-va-oop-asoslari",
            "subject_id": "sub-37",
            "subject_name": "Dasturlash",
            "title": "Dasturlash asoslari: Protsedurali va Obyektga Yo'naltirilgan Dasturlash (OOP)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "O'rta",
            "objective": "Dasturlash paradigmalari, OOP ning 4 ta asosiy ustuni: Enkapsulyatsiya, Vorislik, Polimorfizm va Abstraksiya prinsiplarini o'zlashtirish.",
            "theory": "Dasturlash paradigmasi — dastur kodini yozish va muammolarni yechish uslubidir. 1) Protsedurali dasturlash (C, Pascal) — dastur funksiyalar va buyruqlar ketma-ketligidan iborat; 2) Obyektga Yo'naltirilgan Dasturlash (OOP — C++, Java, Python, C#) — real hayotdagi obyektlarni modellashtirishga asoslangan. Sinf (Class) — bu shablon yoki qolip (masalan, 'Car'); Obyekt (Object) — sinfning aniq namunasi (masalan, 'myCar = Car('Cobalt', 'oq')'). OOP ning 4 ta ustuni:\n- Enkapsulyatsiya (Encapsulation): ma'lumotlar (maydonlar) va ularni boshqaruvchi metodlarni bitta sinf ichida birlashtirish hamda tashqi xavfli aralashuvdan yashirish (private, protected, public);\n- Vorislik (Inheritance): mavjud sinf xossalarini yangi sinfga meros qilib o'tkazish (masalan, Animal -> Dog);\n- Polimorfizm (Polymorphism): bir xil nomdagi metodlarning har xil sinflarda turlicha xatti-harakat qilishi (masalan, Dog.sound() -> 'Vov', Cat.sound() -> 'Miyov');\n- Abstraksiya (Abstraction): faqat muhim xususiyatlarni ko'rsatib, ichki murakkab detallarni yashirish (interface, abstract class).",
            "examples": [
                {
                    "title": "OOP vorisligi misoli (Python)",
                    "problem": "Animal umumiy sinfidan Dog sinfini meros qilib oling.",
                    "step_by_step": "class Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        pass\n\nclass Dog(Animal):\n    def speak(self):\n        return f'{self.name} vovulladi!'\n\ndog = Dog('Bobik')\nprint(dog.speak())",
                    "answer": "Bobik vovulladi!"
                },
                {
                    "title": "Enkapsulyatsiya va ma'lumotlarni himoyalash",
                    "problem": "Bank hisob raqamidagi balansni to'g'ridan-to'g'ri o'zgartirishdan qanday himoya qilinadi?",
                    "step_by_step": "Balans o'zgaruvchisi private (__balance) qilinadi. Unga faqat maxsus deposit() va withdraw() metodlari orqali, qat'iy tekshiruvdan so'ng qiymat kiritishga ruxsat beriladi.",
                    "answer": "Private maydonlar va getter/setter metodlari orqali"
                }
            ],
            "exercise": "Polimorfizm nima uchun kodni kengaytirishda qulaylik yaratadi?",
            "exercise_solution": "Yangi sinflar qo'shilganda asosiy dastur kodini o'zgartirmasdan, umumiy interfeys orqali barcha obyektlarni bir xilda boshqarish imkonini beradi.",
            "check_questions": [
                {
                    "question": "OOP ning qaysi ustuni ichki murakkablikni yashirib, faqat zarur interfeysni taqdim etadi?",
                    "options": ["Vorislik", "Abstraksiya", "Polimorfizm", "Sikl"],
                    "correct_index": 1,
                    "explanation": "Abstraksiya foydalanuvchiga faqat kerakli tugmalarni ko'rsatib, ichki murakkab ishlash mexanizmini yashiradi."
                },
                {
                    "question": "Sinf (Class) va Obyekt (Object) orasidagi farq nima?",
                    "options": ["Hech qanday farq yo'q", "Sinf — chizma/qolip, obyekt esa shu qolip asosida xotirada yaratilgan aniq nusxadir", "Obyekt faqat bitta bo'ladi", "Sinf ma'lumot saqlamaydi"],
                    "correct_index": 1,
                    "explanation": "Sinf barcha nusxalar uchun umumiy reja, obyekt esa o'sha rejadan yaratilgan real narsadir."
                },
                {
                    "question": "Meros olish (Inheritance) nima maqsadda ishlatiladi?",
                    "options": ["Dasturni sekinlashtirish uchun", "Kodni qayta yozmasdan (reusability) kengaytirish uchun", "Faqat xotirani tejash uchun", "Boshqa tildan kod ko'chirish uchun"],
                    "correct_index": 1,
                    "explanation": "Vorislik kodni qayta ishlatish (DRY - Don't Repeat Yourself) imkonini beradi."
                }
            ],
            "tags": ["dasturlash", "OOP", "enkapsulyatsiya", "vorislik", "polimorfizm", "abstraksiya", "universitet"],
            "duration_minutes": 35
        },
        {
            "id": "dev-008",
            "slug": "malumotlar-tuzilmalari-massiv-stack-queue",
            "subject_id": "sub-37",
            "subject_name": "Dasturlash",
            "title": "Ma'lumotlar tuzilmasi: Massivlar, Bog'langan ro'yxat, Stack (LIFO) va Queue (FIFO)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "O'rta",
            "objective": "Chiziqli ma'lumotlar tuzilmalari, xotirada joylashishi, LIFO va FIFO tamoyillari hamda amaliy qo'llanilish sohalarini bilish.",
            "theory": "Ma'lumotlar tuzilmasi (Data Structures) — ma'lumotlarni kompyuter xotirasida samarali saqlash va ular ustida tezkor amallar bajarish usulidir. Asosiy chiziqli tuzilmalar:\n1) Massiv (Array) — xotirada ketma-ket joylashgan, bir xil turdagi elementlar to'plami. Indeks orqali murojaat o'ta tez: O(1), lekin o'rtasiga element qo'shish O(n) vaqt oladi;\n2) Bog'langan ro'yxat (Linked List) — har bir tugun (node) qiymat va keyingi tugunga ko'rsatkich (pointer) saqlaydi. Xotirada tarqoq joylashishi mumkin, element qo'shish oson;\n3) Stack (Stek) — LIFO (Last In, First Out — 'Oxirgi kirgan — birinchi chiqadi') tamoyilida ishlaydi. Amallar: push() — qo'shish, pop() — oxirgisini olish. Misol: brauzerdagi 'Back' (orqaga) tugmasi, matn muharriridagi Undo (bekor qilish), funksiyalar chaqiruv steki;\n4) Queue (Navbat) — FIFO (First In, First Out — 'Birinchi kirgan — birinchi chiqadi') tamoyili. Amallar: enqueue() — navbatga qo'shish, dequeue() — navbatdan chiqarish. Misol: printerdagi hujjatlar navbati, serverga kelgan so'rovlar navbati.",
            "examples": [
                {
                    "title": "Stack (LIFO) amali",
                    "problem": "Bo'sh stekkaga ketma-ket push(10), push(20), push(30) amallari bajarildi. So'ngra pop() amali chaqirilsa qaysi son qaytadi?",
                    "step_by_step": "Stekkaga eng oxirgi kirgan element 30 bo'lgani uchun LIFO qoidasiga ko'ra pop() amali aynan 30 sonini olib tashlaydi va qaytaradi.",
                    "answer": "30"
                },
                {
                    "title": "Queue (FIFO) amali",
                    "problem": "Bo'sh navbatga enqueue('Ali'), enqueue('Vali') qo'shildi. Birinchi bo'lib dequeue() chaqirilsa kim chiqadi?",
                    "step_by_step": "Navbatga birinchi bo'lib 'Ali' kelgan (FIFO), shuning uchun birinchi bo'lib 'Ali' xizmat olib chiqadi.",
                    "answer": "Ali"
                }
            ],
            "exercise": "Qavslarning to'g'ri yopilganligini (masalan: '({[]})') tekshirish uchun qaysi ma'lumotlar tuzilmasidan foydalanish eng qulay?",
            "exercise_solution": "Stack (stek) tuzilmasi eng qulay: ochiq qavslar stekkaga kiritiladi, yopiq qavs kelganda stekkadan mos ochuvchi qavs bilan juftligi tekshirilib pop() qilinadi.",
            "check_questions": [
                {
                    "question": "LIFO (Last In, First Out) tamoyili asosida ishlovchi ma'lumotlar tuzilmasi qaysi?",
                    "options": ["Queue (Navbat)", "Stack (Stek)", "Massiv", "Daraxt (Tree)"],
                    "correct_index": 1,
                    "explanation": "Stek — oxirgi kiritilgan elementni birinchi bo'lib chiqaruvchi LIFO tizimidir."
                },
                {
                    "question": "FIFO (First In, First Out) tamoyili qaysi tizimga xos?",
                    "options": ["Stack", "Queue (Navbat)", "Graph", "HashTable"],
                    "correct_index": 1,
                    "explanation": "Navbat (Queue) har doim birinchi kelgan elementga birinchi xizmat ko'rsatish qoidasida ishlaydi."
                },
                {
                    "question": "Massivda n-indeksdagi elementni olish amali qanday vaqt murakkabligiga ega?",
                    "options": ["O(1) doimiy vaqt", "O(n) chiziqli vaqt", "O(log n)", "O(n^2)"],
                    "correct_index": 0,
                    "explanation": "Xotira manzili to'g'ridan-to'g'ri hisoblangani sababli massiv elementiga indeks orqali O(1) vaqtda murojaat qilinadi."
                }
            ],
            "tags": ["dasturlash", "ma'lumotlar tuzilmasi", "stack", "queue", "massiv", "LIFO", "FIFO"],
            "duration_minutes": 35
        },
        {
            "id": "dev-009",
            "slug": "qidirish-va-saralash-algoritmlari",
            "subject_id": "sub-37",
            "subject_name": "Dasturlash",
            "title": "Algoritmlar samaradorligi: Big O notatsiyasi, Binary Search va QuickSort",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Murakkab",
            "objective": "Vaqt va xotira murakkabligi (Big O), Chiziqli va Ikkilik qidirish (Binary Search), Pufaksimon va Tezkor saralash (QuickSort) algoritmlarini tushunish.",
            "theory": "Algoritm samaradorligi kiruvchi ma'lumotlar hajmi (n) ortishi bilan sarflanadigan vaqt va xotira o'sish tezligini ko'rsatuvchi Big O notatsiyasi bilan o'lchanadi:\n- O(1) — doimiy vaqt (eng tez);\n- O(log n) — logarifmik vaqt (juda samarali, masalan, Binary Search);\n- O(n) — chiziqli vaqt (Linear Search);\n- O(n log n) — optimal saralash (QuickSort, MergeSort);\n- O(n^2) — kvadratik vaqt (Bubble Sort, Selection Sort).\nQidirish algoritmlari:\n1) Linear Search (Chiziqli qidirish) — elementlarni boshidan oxirigacha bittalab tekshiradi, O(n);\n2) Binary Search (Ikkilik qidirish) — FAQAT saralangan massivda ishlaydi. Har bir qadamda massivni teng ikkiga bo'ladi, O(log n).\nSaralash algoritmlari:\n1) Bubble Sort (Pufaksimon saralash) — qo'shni elementlarni solishtirib o'rnini almashtiradi, O(n^2);\n2) QuickSort (Tezkor saralash) — tayanch element (pivot) tanlanadi, undan kichiklar chapga, kattalar o'ngga ajratiladi va rekursiv saralanadi, o'rtacha O(n log n).",
            "examples": [
                {
                    "title": "Binary Search samaradorligi",
                    "problem": "1 000 000 (bir million) ta saralangan elementdan iborat massivda qidirilayotgan sonni topish uchun Binary Search eng ko'pi bilan necha qadam sarflaydi?",
                    "step_by_step": "Har qadamda massiv teng ikkiga bo'linadi: 2^x >= 1 000 000. 2^20 = 1 048 576. Demak, eng ko'pi bilan atigi 20 ta taqqoslash kifoya (chiziqli qidiruv esa 1 million qadam sarflashi mumkin edi).",
                    "answer": "Eng ko'pi bilan 20 ta qadam"
                },
                {
                    "title": "Big O taqqoslash",
                    "problem": "1000 ta element uchun O(n^2) va O(n log n) algoritmlari taxminan nechtadan amal bajaradi?",
                    "step_by_step": "1) O(n^2): 1000^2 = 1 000 000 (bir million amal);\n2) O(n log n): 1000 * log2(1000) ~ 1000 * 10 = 10 000 amal (100 marta tezroq!).",
                    "answer": "O(n^2) ~ 1 000 000 amal, O(n log n) ~ 10 000 amal"
                }
            ],
            "exercise": "Binary Search algoritmini qo'llashning eng asosiy zaruriy sharti nima?",
            "exercise_solution": "Massiv elementlari oldindan o'sish yoki kamayish tartibida qat'iy saralangan (sorted) bo'lishi shart.",
            "check_questions": [
                {
                    "question": "Saralangan massivda qidirish uchun eng tezkor algoritm qaysi?",
                    "options": ["Linear Search", "Binary Search (Ikkilik qidirish)", "Bubble Search", "Brute Force"],
                    "correct_index": 1,
                    "explanation": "Binary Search O(log n) vaqt murakkabligi bilan eng samarali qidirish algoritmidir."
                },
                {
                    "question": "QuickSort algoritmining o'rtacha vaqt murakkabligi qanday?",
                    "options": ["O(n^2)", "O(n log n)", "O(1)", "O(n)"],
                    "correct_index": 1,
                    "explanation": "QuickSort va MergeSort ning o'rtacha samaradorligi O(n log n) ga teng."
                },
                {
                    "question": "Big O notatsiyasida eng sekin (eng yomon) o'sish darajasi qaysi?",
                    "options": ["O(1)", "O(log n)", "O(n)", "O(2^n) eksponensial"],
                    "correct_index": 3,
                    "explanation": "Eksponensial O(2^n) va faktorial O(n!) eng og'ir va qiyin murakkablik hisoblanadi."
                }
            ],
            "tags": ["dasturlash", "algoritmlar", "big O", "binary search", "quicksort", "murakkablik"],
            "duration_minutes": 35
        },
        {
            "id": "dev-010",
            "slug": "dasturiy-taminot-arxitekturasi-solid-va-clean-code",
            "subject_id": "sub-37",
            "subject_name": "Dasturlash",
            "title": "Dasturiy arxitektura tamoyillari: SOLID prinsiplari va Toza kod (Clean Code)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Murakkab",
            "objective": "Professional dastur tuzish madaniyati, Robert Martinning Clean Code tamoyillari va arxitekturaning 5 ta SOLID qoidasini o'rganish.",
            "theory": "Katta hajmli dasturiy ta'minotlarni kengaytiriladigan, sinovdan o'tkazish oson va barqaror qilish uchun SOLID prinsiplari qo'llaniladi (Robert C. Martin):\n1) S — Single Responsibility Principle (SRP): Har bir sinf faqat bitta vazifani bajarishi va uni o'zgartirish uchun faqat bitta sabab bo'lishi kerak;\n2) O — Open/Closed Principle (OCP): Dasturiy ta'minot kengayish uchun ochiq, o'zgartirish uchun yopiq bo'lishi kerak (yangi funksiya qo'shganda eski kodni buzmaslik);\n3) L — Liskov Substitution Principle (LSP): Voris sinflar asosiy ota sinf o'rnida uning xatti-harakatini buzmasdan bemalol ishlay olishi lozim;\n4) I — Interface Segregation Principle (ISP): Bitta katta, og'ir interfeysdan ko'ra bir nechta kichik, maxsus interfeyslar yaratish afzal;\n5) D — Dependency Inversion Principle (DIP): Yuqori darajali modullar quyi darajali modullarga to'g'ridan-to'g'ri bog'liq bo'lmasligi, ikkalasi ham abstraksiyalarga bog'lanishi kerak.\nClean Code: o'zgaruvchilarga mazmunli nom berish, ortiqcha izohlardan qochish, funksiyalar kichik bo'lishi va faqat 1 ishni qilishi kerak.",
            "examples": [
                {
                    "title": "Single Responsibility (Yagona javobgarlik) buzilishi",
                    "problem": "'User' sinfi ham foydalanuvchi ma'lumotlarini saqlasa, ham uni bazaga yozsa, ham email xabar yuborsa, bu to'g'rimi?",
                    "step_by_step": "Bu SRP prinsipining qo'pol buzilishidir. Buni 3 ga ajratish kerak: 1) User (ma'lumot modeli); 2) UserRepository (bazaga yozuvchi); 3) EmailService (xat yuboruvchi).",
                    "answer": "Xato. Vazifalar alohida sinflarga ajratilishi shart (SRP)"
                },
                {
                    "title": "Open/Closed tamoyilini qo'llash",
                    "problem": "Yangi to'lov tizimini (masalan, Payme, Click, Uzum) qo'shganda asosiy kodni buzmaslik uchun nima qilinadi?",
                    "step_by_step": "Umumiy 'PaymentProcessor' interfeysi yaratiladi. Har bir yangi tizim shu interfeysni amalga oshiradi (implements). Asosiy kod esa yangi sinfni to'g'ridan-to'g'ri qabul qilaveradi (kod kengayadi, lekin o'zgarmaydi).",
                    "answer": "Interfeys va polimorfizm orqali kengaytiriladi"
                }
            ],
            "exercise": "DRY (Don't Repeat Yourself) va KISS (Keep It Simple, Stupid) qoidalarining ma'nosi nima?",
            "exercise_solution": "DRY — kodni takrorlamaslik, umumiy funksiyalarga chiqarish; KISS — kodni keraksiz darajada murakkablashtirmasdan, imkon qadar sodda va tushunarli yozish.",
            "check_questions": [
                {
                    "question": "SOLID qoidalaridagi 'S' harfi nimani bildiradi?",
                    "options": ["Security Principle", "Single Responsibility Principle (Yagona javobgarlik)", "Speed Principle", "Simple Code"],
                    "correct_index": 1,
                    "explanation": "Single Responsibility — sinf faqat bitta vazifaga javobgar bo'lishi tamoyili."
                },
                {
                    "question": "Open/Closed prinsipi dastur kodiga nisbatan qanday talab qo'yadi?",
                    "options": ["Kodni hech qachon ochmaslik", "Kengayish uchun ochiq, o'zgartirish uchun yopiq bo'lishi kerak", "Faqat ochiq kodli (open source) bo'lishi kerak", "Faqat yopiq sinflar bilan ishlash"],
                    "correct_index": 1,
                    "explanation": "Yangi imkoniyatlarni eski kodni buzmasdan yangi modullar qo'shish orqali kiritish talab qilinadi."
                },
                {
                    "question": "Clean Code bo'yicha yaxshi funksiya qanday bo'lishi kerak?",
                    "options": ["Kamida 100 qator bo'lishi", "Kichik bo'lib, faqat bitta vazifani a'lo darajada bajarishi kerak", "Barcha parametrlarni bitta funksiyaga yig'ish", "Ko'p vazifali bo'lishi"],
                    "correct_index": 1,
                    "explanation": "Yaxshi funksiya kichik va bitta aniq ishni bajaruvchi bo'lishi shart."
                }
            ],
            "tags": ["dasturlash", "arxitektura", "SOLID", "clean code", "refactoring", "universitet"],
            "duration_minutes": 35
        },

        # WEB DEVELOPMENT (4)
        {
            "id": "dev-011",
            "slug": "html5-semantikasi-va-veb-sahifa-tuzilishi",
            "subject_id": "sub-38",
            "subject_name": "Web Development",
            "title": "HTML5 semantik teglari, veb-sahifa strukturasi va foydalanish qulayligi (Accessibility)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Boshlang'ich",
            "objective": "HTML5 ning semantik teglari (<header>, <nav>, <main>, <section>, <article>, <aside>, <footer>), formalar va qidiruv tizimlariga optimallashtirish (SEO).",
            "theory": "HTML (HyperText Markup Language) — veb-sahifalarning 'skeleti' bo'lib, uning tuzilishini belgilaydi. HTML5 zamonaviy semantik teglarni taqdim etdi. Semantik teglar nafaqat brauzerga, balki qidiruv tizimlari (Google, Yandex) va ko'zi ojizlar uchun ekran o'quvchi (screen reader) dasturlarga sahifaning ma'nosini tushuntiradi. Asosiy semantik teglar: <header> (sahifa yoki bo'lim sarlavhasi, logo), <nav> (asosiy navigatsiya menyusi), <main> (sahifaning yagona takrorlanmas asosiy kontenti), <article> (mustaqil ma'noga ega maqola, yangilik yoki post), <section> (mavzuli alohida bo'lim), <aside> (qo'shimcha yon panel / sidebar), <footer> (mualliflik huquqi, aloqa ma'lumotlari). Formalar: <form>, <input type='text|email|password'>, <button>, required va placeholder atributlari.",
            "examples": [
                {
                    "title": "Semantik sahifa skeleti",
                    "problem": "Veb-sayt bosh sahifasi uchun to'g'ri semantik HTML5 tuzilmasini yozing.",
                    "step_by_step": "<!DOCTYPE html>\n<html lang='uz'>\n<head><meta charset='UTF-8'><title>Education Hub</title></head>\n<body>\n  <header><nav>...</nav></header>\n  <main>\n    <section class='hero'>...</section>\n    <section class='courses'>...</section>\n  </main>\n  <footer><p>&copy; 2026 Education Hub</p></footer>\n</body>\n</html>",
                    "answer": "header, nav, main (sections), footer ketma-ketligi"
                },
                {
                    "title": "Rasm tegidagi 'alt' atributi ahamiyati",
                    "problem": "<img> tegida 'alt' atributini yozish nima uchun majburiy hisoblanadi?",
                    "step_by_step": "1) Agar rasm internet sekinligi tufayli yuklanmasa, uning o'rnida matnli tavsif chiqadi;\n2) Ko'zi ojizlar uchun ekran o'quvchi dasturlar 'alt' matnini o'qib beradi (Accessibility);\n3) Qidiruv tizimlari rasm nima haqida ekanligini bilib indekslaydi (SEO).",
                    "answer": "Accessibility, rasm yuklanmagandagi tushuntirish va SEO uchun"
                }
            ],
            "exercise": "Foydalanuvchidan email va parol so'rab, bo'sh qoldirishni taqiqlovchi oddiy login formasini yozing.",
            "exercise_solution": "<form><input type='email' placeholder='Email' required><input type='password' placeholder='Parol' required><button type='submit'>Kirish</button></form>",
            "check_questions": [
                {
                    "question": "Saytning asosiy menyusi qaysi semantik teg ichiga joylashtiriladi?",
                    "options": ["<menu>", "<nav>", "<links>", "<div>"],
                    "correct_index": 1,
                    "explanation": "<nav> (navigation) tegi saytning asosiy navigatsiya havolalari uchun mo'ljallangan."
                },
                {
                    "question": "Bitta veb-sahifada nechta <main> tegi bo'lishi mumkin?",
                    "options": ["Faqat 1 ta", "Cheksiz", "2 ta", "Bo'lishi shart emas"],
                    "correct_index": 0,
                    "explanation": "Qoidaga ko'ra veb-hujjatda faqat bitta yagona <main> tegi bo'lishi shart."
                },
                {
                    "question": "HTML faylida sahifa kodirovkasini UTF-8 deb ko'rsatish nega muhim?",
                    "options": ["Fayl hajmini kichraytirish uchun", "O'zbekcha (o', g') va xalqaro harflar buzilmasdan to'g'ri ko'rinishi uchun", "Tezroq yuklanishi uchun", "Rasmlar ochilishi uchun"],
                    "correct_index": 1,
                    "explanation": "UTF-8 dunyodagi barcha milliy alifbolarni (jumladan o'zbek lotin va kirill) to'g'ri aks ettirishni ta'minlaydi."
                }
            ],
            "tags": ["web development", "HTML5", "semantika", "SEO", "accessibility", "frontend"],
            "duration_minutes": 25
        },
        {
            "id": "dev-012",
            "slug": "css3-zamonaviy-dizayn-flexbox-va-grid",
            "subject_id": "sub-38",
            "subject_name": "Web Development",
            "title": "CSS3: Box Model, Responsive dizayn, Flexbox va CSS Grid tizimlari",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "O'rta",
            "objective": "CSS selektorlari, Box Model (content, padding, border, margin), moslashuvchan maketlar (Flexbox va CSS Grid) va media so'rovlar (@media) yordamida mobil dizayn yaratish.",
            "theory": "CSS (Cascading Style Sheets) — HTML elementlarining tashqi ko'rinishi, dizayni va joylashuvini boshqaradi. Box Model (blok modeli) har bir HTML elementini 4 qavatli quti deb qaraydi: Content (matn/rasm) -> Padding (ichki bo'shliq) -> Border (chegara hoshiyasi) -> Margin (tashqi masofa). box-sizing: border-box qoidasi element kengligiga padding va border qo'shilib ketishining oldini oladi. Zamonaviy tartiblash tizimlari: 1) Flexbox (display: flex) — bir o'lchamli (faqat qator yoki faqat ustun bo'yicha) elementlarni tekislash uchun juda qulay (justify-content, align-items, flex-direction); 2) CSS Grid (display: grid) — ikki o'lchamli (bir vaqtning o'zida ham qator, ham ustun) murakkab setkalar yaratish tizimi (grid-template-columns: repeat(3, 1fr), gap). Responsive (moslashuvchan) dizayn: @media (max-width: 768px) { ... } yordamida sayt smartfon, planshet va kompyuter ekranlariga moslashadi.",
            "examples": [
                {
                    "title": "Elementni markazga joylashtirish (Flexbox)",
                    "problem": "Elementni o'z ota blokining ham gorizontal, ham vertikal qoq o'rtasiga qanday joylashtiriladi?",
                    "step_by_step": ".parent {\n  display: flex;\n  justify-content: center; /* Gorizontal markaz */\n  align-items: center;     /* Vertikal markaz */\n  height: 100vh;\n}",
                    "answer": "display: flex; justify-content: center; align-items: center;"
                },
                {
                    "title": "Responsive CSS Grid",
                    "problem": "Ekran kengligiga qarab 1 tadan 3 tagacha ustun bo'ladigan kartalar qatori qanday tuziladi?",
                    "step_by_step": ".grid-container {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n  gap: 20px;\n}",
                    "answer": "grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));"
                }
            ],
            "exercise": "Padding va Margin o'rtasidagi asosiy farqni tushuntiring.",
            "exercise_solution": "Padding — elementning o'z chegarasi (border) ichidagi bo'shliq; Margin esa element chegarasidan tashqaridagi, qo'shni elementlargacha bo'lgan masofadir.",
            "check_questions": [
                {
                    "question": "Flexbox qaysi o'q bo'yicha elementlarni boshqaradi?",
                    "options": ["Faqat 3D fazoda", "Bir o'lchamli (asosiy o'q bo'ylab — qator yoki ustun)", "Har doim faqat vertikal", "Faqat diagonali"],
                    "correct_index": 1,
                    "explanation": "Flexbox bir o'lchamli tartib tizimi bo'lib, flex-direction ga qarab bir yo'nalishda ishlaydi."
                },
                {
                    "question": "Mobil telefonlar uchun maxsus uslub yozishda CSS ning qaysi qoidasi ishlatiladi?",
                    "options": ["@keyframes", "@media", "@import", "@font-face"],
                    "correct_index": 1,
                    "explanation": "@media (max-width: ...) ekran o'lchamiga qarab alohida dizayn berish vositasidir."
                },
                {
                    "question": "Nima sababdan CSS da 'box-sizing: border-box;' ishlatiladi?",
                    "options": ["Rangni o'zgartirish uchun", "Padding va border berilganda elementning umumiy kengligi o'zgarmasligi uchun", "Burchaklarni yumaloqlash uchun", "Shriftni kattalashtirish uchun"],
                    "correct_index": 1,
                    "explanation": "Border-box padding va chegara qalinligini berilgan kenglik (width) ichiga kiritadi."
                }
            ],
            "tags": ["web development", "CSS3", "flexbox", "grid", "responsive", "box model"],
            "duration_minutes": 35
        },
        {
            "id": "dev-013",
            "slug": "zamonaviy-frontend-react-va-komponentlar",
            "subject_id": "sub-38",
            "subject_name": "Web Development",
            "title": "Zamonaviy Frontend: React.js asoslari, JSX, Props va State (useState, useEffect)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Murakkab",
            "objective": "React kutubxonasi, Virtual DOM, deklarativ UI, funksional komponentlar, holat boshqaruvi (useState) va hayot sikli (useEffect)ni o'rganish.",
            "theory": "React — Meta (Facebook) tomonidan yaratilgan foydalanuvchi interfeyslarini (UI) qurish uchun mashhur JavaScript kutubxonasidir. SPA (Single Page Application) — sahifa qayta yuklanmasdan, faqat kerakli qismlar tezkor yangilanadi. Virtual DOM (VDOM) — React xotiradagi virtual nusxa orqali haqiqiy DOM ga minimal o'zgarishlarni kiritadi (tezlik oshadi). JSX (JavaScript XML) — JavaScript ichida to'g'ridan-to'g'ri HTML ga o'xshash kod yozish sintaksisi. Komponentlar — qayta ishlatiluvchi mustaqil UI bloklaridir. Asosiy tushunchalar: 1) Props (xususiyatlar) — ota komponentdan bola komponentga uzatiladigan o'zgarmas ma'lumotlar; 2) State (holat) — komponent ichida vaqt o'tishi bilan o'zgarishi mumkin bo'lgan ma'lumotlar (useState hook); 3) useEffect — tashqi dunyo bilan bog'lanish (API dan ma'lumot olish, hodisalarga obuna bo'lish).",
            "examples": [
                {
                    "title": "useState bilan oddiy hisoblagich (Counter)",
                    "problem": "Tugma bosilganda sonni 1 taga oshiruvchi React komponentini yozing.",
                    "step_by_step": "import { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n  return (\n    <div>\n      <p>Soni: {count}</p>\n      <button onClick={() => setCount(count + 1)}>Oshirish</button>\n    </div>\n  );\n}",
                    "answer": "useState orqali count holati boshqariladi"
                },
                {
                    "title": "Props uzatish",
                    "problem": "Bola komponentga foydalanuvchi ismini props orqali uzating.",
                    "step_by_step": "function Greeting({ name }) {\n  return <h2>Xush kelibsiz, {name}!</h2>;\n}\n\n// Ishlatilishi:\n<Greeting name='Sardor' />",
                    "answer": "<Greeting name='Sardor' />"
                }
            ],
            "exercise": "useEffect hookida bo'sh bog'liqliklar massivi '[]' (empty dependency array) berilsa, u qachon ishga tushadi?",
            "exercise_solution": "Faqat bir marta — komponent ekranda ilk bor paydo bo'lganda (mount bo'lganda) ishga tushadi.",
            "check_questions": [
                {
                    "question": "React da Virtual DOM qanday vazifani bajaradi?",
                    "options": ["Rasmlarni yuklaydi", "Haqiqiy DOM ga faqat o'zgargan joylarni kiritib ishlash tezligini oshiradi", "Xavfsizlikni tekshiradi", "CSS yozadi"],
                    "correct_index": 1,
                    "explanation": "Virtual DOM o'zgarishlarni solishtirib (diffing), haqiqiy brauzer DOM ini optimal yangilaydi."
                },
                {
                    "question": "React komponenti ichida dinamik holat saqlash uchun qaysi hook ishlatiladi?",
                    "options": ["useEffect", "useContext", "useState", "useRef"],
                    "correct_index": 2,
                    "explanation": "useState qiymat va uni o'zgartiruvchi funksiyani qaytaradi."
                },
                {
                    "question": "Props bola komponent ichida o'zgartirilishi mumkinmi?",
                    "options": ["Ha, bemalol", "Yo'q, props faqat o'qish uchun (read-only) bo'lib, o'zgarmaydi", "Faqat useState bilan", "Ixtiyoriy"],
                    "correct_index": 1,
                    "explanation": "Props yuqoridan pastga bir tomonlama uzatiladi va bola komponentda uni o'zgartirish qat'iyan man etiladi."
                }
            ],
            "tags": ["web development", "react", "frontend", "hooks", "useState", "useEffect", "JSX"],
            "duration_minutes": 35
        },
        {
            "id": "dev-014",
            "slug": "backend-arxitekturasi-rest-api-va-node-js",
            "subject_id": "sub-38",
            "subject_name": "Web Development",
            "title": "Backend asoslari: Node.js, Express.js va RESTful API arxitekturasi",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Murakkab",
            "objective": "Server tushunchasi, Node.js asinxron arxitekturasi, Express.js yordamida marshrutlash (routing) va HTTP metodlari (GET, POST, PUT, DELETE) orqali REST API yaratish.",
            "theory": "Backend (server qismi) — biznes mantiqni bajaruvchi, ma'lumotlar bazasi bilan ishlovchi va xavfsizlikni ta'minlovchi qismdir. Node.js — bu Chrome V8 dvigateliga asoslangan asinxron, bitta oqimli (single-threaded, Event Loop) JavaScript muhiti. Express.js — Node.js uchun eng mashhur yengil veb-freymvork. REST (Representational State Transfer) — klient va server o'rtasida ma'lumot almashish arxitekturasi (odatda JSON formatida). HTTP metodlari:\n- GET: ma'lumotlarni olish (/api/courses);\n- POST: yangi ma'lumot yaratish (/api/courses);\n- PUT / PATCH: mavjud ma'lumotni yangilash (/api/courses/12);\n- DELETE: ma'lumotni o'chirish (/api/courses/12).\nStatus kodlar: 200 (OK), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Internal Server Error).",
            "examples": [
                {
                    "title": "Oddiy Express.js GET marshruti",
                    "problem": "Barcha fanlar ro'yxatini qaytaruvchi oddiy Express.js API yo'lini yozing.",
                    "step_by_step": "const express = require('express');\nconst app = express();\n\nconst subjects = [\n  { id: 1, name: 'Matematika' },\n  { id: 2, name: 'Fizika' }\n];\n\napp.get('/api/subjects', (req, res) => {\n  res.status(200).json(subjects);\n});\n\napp.listen(3000, () => console.log('Server 3000-portda ishlamoqda'));",
                    "answer": "app.get('/api/subjects', ...)"
                },
                {
                    "title": "HTTP status kodlar",
                    "problem": "Foydalanuvchi so'ragan material bazada topilmasa, server qanday HTTP kod qaytarishi kerak?",
                    "step_by_step": "Resurs topilmaganda har doim 404 (Not Found) kodi qaytariladi. Agar server xatosi bo'lsa 500 bo'lardi.",
                    "answer": "404 Not Found"
                }
            ],
            "exercise": "Yangi material yaratish uchun mijoz serverga qaysi HTTP metodida va qanday formatda so'rov yuboradi?",
            "exercise_solution": "POST metodida va so'rov tanasida (request body) JSON formatida ma'lumot yuboradi.",
            "check_questions": [
                {
                    "question": "REST API da yangi resurs yaratish uchun qaysi HTTP metodi ishlatiladi?",
                    "options": ["GET", "POST", "PUT", "DELETE"],
                    "correct_index": 1,
                    "explanation": "POST metodi serverda yangi yozuv yaratish uchun xizmat qiladi."
                },
                {
                    "question": "So'rov muvaffaqiyatli bajarilganini bildiruvchi standart HTTP kodi qaysi?",
                    "options": ["200 OK", "404 Not Found", "500 Server Error", "301 Redirect"],
                    "correct_index": 0,
                    "explanation": "200 kodi so'rov muvaffaqiyatli bajarilganini bildiradi."
                },
                {
                    "question": "Node.js nima uchun yuqori yuklamalarda ham tez ishlaydi?",
                    "options": ["Ko'p oqimli bo'lgani uchun", "Asinxron va bloklamaydigan (non-blocking I/O) Event Loop modeli hisobiga", "Faqat kichik dasturlar uchun", "C++ da yozilgani uchun"],
                    "correct_index": 1,
                    "explanation": "Node.js asinxron Event Loop yordamida minglab so'rovlarni bitta oqimda to'xtab qolmasdan qayta ishlaydi."
                }
            ],
            "tags": ["web development", "backend", "node.js", "express", "REST API", "HTTP"],
            "duration_minutes": 35
        },

        # PYTHON (3)
        {
            "id": "dev-015",
            "slug": "python-sintaksisi-va-malumot-turlari",
            "subject_id": "sub-39",
            "subject_name": "Python",
            "title": "Python asoslari: Sintaksis, o'zgaruvchilar va ma'lumot turlari (List, Tuple, Dict, Set)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Boshlang'ich",
            "objective": "Python dinamik tiplash, shartlar (if-elif-else), sikllar (for, while) hamda 4 ta asosiy to'plam turi: ro'yxat (list), kortej (tuple), lug'at (dict) va to'plam (set) xossalarini bilish.",
            "theory": "Python — o'qilishi oson, o'rganishga qulay va qudratli yuqori darajali dasturlash tilidir (Gvido van Rossum, 1991). Asosiy ma'lumot turlari: int (butun son: 10), float (haqiqiy son: 3.14), str (matn: 'salom'), bool (True, False). To'plamlar:\n1) List (ro'yxat: [1, 2, 3]) — tartiblangan, o'zgaruvchan (mutable), dublikatlarga ruxsat beradi;\n2) Tuple (kortej: (1, 2, 3)) — tartiblangan, o'zgarmas (immutable — o'zgartirib bo'lmaydi);\n3) Set (to'plam: {1, 2, 3}) — tartiblanmagan, faqat unikal (takrorlanmas) elementlarni saqlaydi;\n4) Dictionary (lug'at: {'ism': 'Ali', 'yosh': 20}) — kalit-qiymat (key-value) juftliklari, kalitlar unikal bo'ladi. Pythonda bloklar qavslar bilan emas, balki qat'iy surilishlar (indentation — 4 ta bo'shliq) bilan belgilanadi.",
            "examples": [
                {
                    "title": "Lug'at (Dictionary) bilan ishlash",
                    "problem": "Talabaning baholari lug'atidan o'rtacha ballni hisoblang.",
                    "step_by_step": "grades = {'matematika': 5, 'fizika': 4, 'ona_tili': 5}\naverage = sum(grades.values()) / len(grades)\n# sum = 14, len = 3 -> 14 / 3 = 4.67\nprint(round(average, 2))",
                    "answer": "4.67"
                },
                {
                    "title": "Ro'yxatdan dublikatlarni tozalash",
                    "problem": "numbers = [1, 2, 2, 3, 4, 4, 5] ro'yxatidagi takrorlarni qanday olib tashlash mumkin?",
                    "step_by_step": "Ro'yxatni Set ga aylantiramiz, set faqat unikal qiymat saqlaydi: unique_numbers = list(set(numbers)). Natija: [1, 2, 3, 4, 5].",
                    "answer": "list(set(numbers))"
                }
            ],
            "exercise": "List comprehension yordamida 1 dan 10 gacha bo'lgan sonlarning kvadratlari ro'yxatini 1 qatorda hosil qiling.",
            "exercise_solution": "squares = [x**2 for x in range(1, 11)]",
            "check_questions": [
                {
                    "question": "Pythonda elementlarini o'zgartirib bo'lmaydigan (immutable) to'plam qaysi?",
                    "options": ["List (ro'yxat)", "Tuple (kortej)", "Dictionary (lug'at)", "Set"],
                    "correct_index": 1,
                    "explanation": "Tuple bir marta yaratilgach, unga element qo'shish yoki o'chirish mumkin emas."
                },
                {
                    "question": "Pythonda kod bloklari (if, for, funksiyalar) qanday ajratiladi?",
                    "options": ["Jingalak qavslar { } bilan", "begin ... end bilan", "Surilishlar (indentation / bo'shliqlar) bilan", "Nuqtali vergul bilan"],
                    "correct_index": 2,
                    "explanation": "Python sintaksisining asosiy belgisi — qat'iy bo'shliqlar (indentation) tizimidir."
                },
                {
                    "question": "Kalit-qiymat (key-value) juftligi asosida ishlovchi ma'lumot turi nima?",
                    "options": ["List", "Tuple", "Dictionary", "Float"],
                    "correct_index": 2,
                    "explanation": "Dictionary (dict) kalit bo'yicha qiymat saqlovchi ma'lumotlar tuzilmasidir."
                }
            ],
            "tags": ["python", "dasturlash", "list", "dict", "tuple", "sintaksis"],
            "duration_minutes": 30
        },
        {
            "id": "dev-016",
            "slug": "python-funksiyalar-fayllar-va-xatolar",
            "subject_id": "sub-39",
            "subject_name": "Python",
            "title": "Python: Funksiyalar, Fayllar bilan ishlash va Istisnolarni boshqarish (try-except)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "O'rta",
            "objective": "def va lambda funksiyalar, *args va **kwargs, fayllarni o'qish/yozish (with open), JSON bilan ishlash hamda try-except xatoliklar nazoratini o'rganish.",
            "theory": "Funksiya — ma'lum vazifani bajaruvchi nomlangan kod blokidir (def kalit so'zi). Argumentlar: pozitsion, kalitli va noaniq sonli argumentlar (*args — kortej, **kwargs — lug'at ko'rinishida oladi). Lambda — bir qatorli nomsiz funksiya (masalan, lambda x: x * 2). Fayllar bilan ishlash: matn va JSON fayllarni xavfsiz ochish uchun 'with open()' konstruksiyasi ishlatiladi (fayl avtomatik yopiladi): with open('data.txt', 'r', encoding='utf-8') as f: content = f.read(). Rejimlar: 'r' (o'qish), 'w' (qaytadan yozish), 'a' (oxiriga qo'shish). Istisnolarni boshqarish (Exception handling): dastur xato tufayli to'xtab qolmasligi uchun try-except bloklari ishlatiladi: try bloki tekshiradi, xato bo'lsa except ishga tushadi, finally har doim bajariladi.",
            "examples": [
                {
                    "title": "Xatoni ushlash (try-except)",
                    "problem": "Nolga bo'lish xatosini dasturni to'xtatmasdan ushlab qoling.",
                    "step_by_step": "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Xatolik: Nolga bo'lish mumkin emas!')\nfinally:\n    print('Dastur ishlashda davom etmoqda.')",
                    "answer": "ZeroDivisionError ushlanadi va xabar chiqadi"
                },
                {
                    "title": "JSON faylni o'qish",
                    "problem": "'users.json' faylini o'qib Python lug'atiga o'tkazing.",
                    "step_by_step": "import json\n\nwith open('users.json', 'r', encoding='utf-8') as f:\n    data = json.load(f)\nprint(data)",
                    "answer": "json.load(f) orqali o'qiladi"
                }
            ],
            "exercise": "Berilgan sonning faktorialini hisoblovchi rekursiv Python funksiyasini yozing.",
            "exercise_solution": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)",
            "check_questions": [
                {
                    "question": "Fayllar bilan ishlashda 'with open(...)' nima sababdan afzal?",
                    "options": ["Faylni shifrlaydi", "Amal tugagach faylni avtomatik va xavfsiz yopadi", "Faylni o'chiradi", "Faqat tezlik uchun"],
                    "correct_index": 1,
                    "explanation": "'with' kontekst menejeri bo'lib, xatolik yuz berganda ham faylni to'g'ri yopishni kafolatlaydi."
                },
                {
                    "question": "Ixtiyoriy sondagi pozitsion argumentlarni qabul qilish uchun nima ishlatiladi?",
                    "options": ["*args", "**kwargs", "&args", "lambda"],
                    "correct_index": 0,
                    "explanation": "*args funksiyaga istalgancha argumentlarni tuple sifatida uzatish imkonini beradi."
                },
                {
                    "question": "Nolga bo'lish paytida qaysi standart Python xatosi (Exception) yuzaga keladi?",
                    "options": ["ValueError", "TypeError", "ZeroDivisionError", "IndexError"],
                    "correct_index": 2,
                    "explanation": "Nolga bo'lishga uringanda ZeroDivisionError xatosi yuzaga keladi."
                }
            ],
            "tags": ["python", "funksiyalar", "fayllar", "try-except", "json", "lambda"],
            "duration_minutes": 35
        },
        {
            "id": "dev-017",
            "slug": "python-web-frameworklari-django-va-fastapi",
            "subject_id": "sub-39",
            "subject_name": "Python",
            "title": "Python Veb-texnologiyalari: Django ORM va Zamonaviy Asinxron FastAPI",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Murakkab",
            "objective": "Django arxitekturasi (MVT — Model-View-Template), Django ORM ma'lumotlar bazasi va zamonaviy tezyurar asinxron FastAPI freymvorkini o'rganish.",
            "theory": "Python veb-dasturlashda ikkita eng mashhur freymvork bor: 1) Django — 'Barcha batareyalari ichida' (batteries-included) bo'lgan to'liq quvvatli monolit freymvork. MVT (Model, View, Template) arxitekturasiga ega. Unda tayyor Admin panel, avtorizatsiya va eng kuchli Django ORM (Object-Relational Mapping — SQL yozmasdan Python klasslari orqali baza bilan ishlash) mavjud; 2) FastAPI — Python 3.8+ tiplashiga (type hints) asoslangan o'ta tez, asinxron (async/await) REST API freymvorki. Pydantic validatsiyasidan foydalanadi va avtomatik ravishda Swagger UI (/docs) interaktiv hujjatini yaratadi. Yuqori yuklamali mikroxizmatlar uchun ideal.",
            "examples": [
                {
                    "title": "Django ORM modeli",
                    "problem": "Djangoda Materiallar uchun oddiy model klassini yozing.",
                    "step_by_step": "from django.db import models\n\nclass Material(models.Model):\n    title = models.CharField(max_length=200)\n    content = models.TextField()\n    created_at = models.DateTimeField(auto_now_add=True)\n\n    def __str__(self):\n        return self.title",
                    "answer": "models.Model dan voris olingan klass"
                },
                {
                    "title": "FastAPI asinxron API yo'li",
                    "problem": "FastAPI da salomlashuvchi oddiy asinxron GET endpoint yarating.",
                    "step_by_step": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/api/hello')\nasync def say_hello(name: str = 'Foydalanuvchi'):\n    return {'message': f'Salom, {name}!'}",
                    "answer": "@app.get('/api/hello') async def say_hello..."
                }
            ],
            "exercise": "FastAPI da API hujjatlarini ko'rish uchun brauzerda qaysi manzil ochiladi?",
            "exercise_solution": "http://127.0.0.1:8000/docs (Swagger UI) yoki /redoc manzili ochiladi.",
            "check_questions": [
                {
                    "question": "Django da SQL yozmasdan Python kodlari orqali bazani boshqarish qaysi vosita orqali amalga oshiriladi?",
                    "options": ["Django Template", "Django ORM", "Django Forms", "Django Admin"],
                    "correct_index": 1,
                    "explanation": "Django ORM (Object-Relational Mapping) jadvallarni Python klasslariga bog'laydi."
                },
                {
                    "question": "FastAPI freymvorkining eng katta ustunligi nima?",
                    "options": ["O'yinlar yaratish", "O'ta yuqori tezlik, asinxronlik (async/await) va avtomatik Swagger hujjatlash", "Faqat SQLite da ishlash", "Grafik interfeys"],
                    "correct_index": 1,
                    "explanation": "FastAPI asinxron imkoniyatlari va avtomatik /docs hujjati bilan yetakchi API vositasidir."
                },
                {
                    "question": "Django ning standart arxitekturasi qanday nomlanadi?",
                    "options": ["MVC", "MVT (Model-View-Template)", "Flux", "Monolith"],
                    "correct_index": 1,
                    "explanation": "Django klassik MVC ni MVT (Model, View, Template) shaklida qo'llaydi."
                }
            ],
            "tags": ["python", "django", "fastapi", "ORM", "REST API", "backend", "universitet"],
            "duration_minutes": 35
        },

        # JAVASCRIPT (3)
        {
            "id": "dev-018",
            "slug": "javascript-asoslari-va-dom-manipulyatsiyasi",
            "subject_id": "sub-40",
            "subject_name": "JavaScript",
            "title": "JavaScript asoslari: o'zgaruvchilar (let, const), DOM bilan ishlash va hodisalar (Events)",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Boshlang'ich",
            "objective": "JavaScript sintaksisi, let va const farqi, funksiyalar, DOM elementlarini tanlash va hodisalarga quloq solish (addEventListener).",
            "theory": "JavaScript — veb-sahifalarga jonlilik, interaktivlik va dinamika beruvchi dasturlash tilidir. Brauzerda ishlaydi. O'zgaruvchilar: const (o'zgarmas qiymat), let (o'zgaruvchan blok ko'lamidagi qiymat). DOM (Document Object Model) — brauzer HTML hujjatini daraxtsimon obyektlar shaklida ko'radi va JavaScript yordamida har bir elementni o'zgartirish imkonini beradi. Elementlarni tanlash: document.getElementById(/* element ID */), document.querySelector('.myClass'). DOM manipulyatsiyasi: element.textContent (matnni o'zgartirish), element.style.color (rangini o'zgartirish), element.classList.add('active') (CSS klass qo'shish). Hodisalar (Events): foydalanuvchi harakatlari (click, input, submit, keydown). addEventListener('click', function) orqali tugma bosilganda funksiya chaqiriladi.",
            "examples": [
                {
                    "title": "Tugma bosilganda matnni o'zgartirish",
                    "problem": "Tugma bosilganda <p id='text'> matnini 'Salom, Dunyo!' ga o'zgartiruvchi JS kodini yozing.",
                    "step_by_step": "const btn = document.querySelector('button');\nconst text = document.querySelector('p');\n\nbtn.addEventListener('click', () => {\n  text.textContent = 'Salom, Dunyo!';\n  text.style.color = '#2563EB';\n});",
                    "answer": "btn.addEventListener('click', () => text.textContent = 'Salom, Dunyo!')"
                },
                {
                    "title": "Qorong'i rejim (Dark Mode) tugmasi",
                    "problem": "Bitta tugma orqali body ga 'dark' klassini yoqib-o'chirish qanday qilinadi?",
                    "step_by_step": "document.body.classList.toggle('dark');\n(toggle metodi agar klass bo'lsa o'chiradi, bo'lmasa qo'shadi).",
                    "answer": "document.body.classList.toggle('dark');"
                }
            ],
            "exercise": "Input maydoniga yozilgan matnni 'keyup' hodisasi orqali konsolga chiqaruvchi kod yozing.",
            "exercise_solution": "input.addEventListener('keyup', (e) => console.log(e.target.value));",
            "check_questions": [
                {
                    "question": "Qayta qiymat berib bo'lmaydigan (o'zgarmas) o'zgaruvchi qaysi kalit so'z bilan e'lon qilinadi?",
                    "options": ["var", "let", "const", "static"],
                    "correct_index": 2,
                    "explanation": "'const' o'zgarmas doimiy qiymatlar uchun ishlatiladi."
                },
                {
                    "question": "HTML elementiga hodisani (masalan chertishni) biriktirish uchun qaysi metod ishlatiladi?",
                    "options": ["addEventListener", "attachEvent", "setClick", "onClickAction"],
                    "correct_index": 0,
                    "explanation": "addEventListener zamonaviy va xavfsiz hodisa tinglovchisidir."
                },
                {
                    "question": "CSS klassini bor bo'lsa o'chirib, yo'q bo'lsa qo'shuvchi qulay metod qaysi?",
                    "options": ["classList.add", "classList.remove", "classList.toggle", "classList.switch"],
                    "correct_index": 2,
                    "explanation": "classList.toggle klass holatini o'zgartirib turadi."
                }
            ],
            "tags": ["javascript", "DOM", "events", "frontend", "addEventListener", "let const"],
            "duration_minutes": 30
        },
        {
            "id": "dev-019",
            "slug": "zamonaviy-javascript-es6-va-asinxron-dasturlash",
            "subject_id": "sub-40",
            "subject_name": "JavaScript",
            "title": "Modern JavaScript (ES6+): Arrow functions, Destructuring, Promises va async/await",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "O'rta",
            "objective": "ES6 yangiliklari (destrukturizatsiya, spread operatori, shablonli satrlar) hamda asinxronlik: Promise va async/await orqali API dan ma'lumot olish (fetch).",
            "theory": "2015-yilda chiqarilgan ECMAScript 6 (ES6) JavaScript tilini butunlay yangiladi: 1) Arrow functions (strelkali funksiyalar: const add = (a, b) => a + b); 2) Template literals (shablonli satrlar: `Ism: ${name}`); 3) Destructuring (obyekt va massivlarni oson ajratib olish: const { name, age } = user); 4) Spread/Rest operatori (...): massivlarni birlashtirish yoki parametrlarni yig'ish. Asinxron JavaScript: Veb-sayt qotib qolmasligi uchun uzoq davom etadigan amallar (serverdan ma'lumot olish) asinxron bajariladi. Promise (Va'da) 3 xil holatda bo'ladi: Pending (kutilmoqda), Fulfilled (muvaffaqiyatli), Rejected (xatolik). Zamonaviy async/await sintaksisi asinxron kodni xuddi sinxron koddek qulay o'qiladigan qiladi. fetch() funksiyasi orqali backend API lardan ma'lumot olinadi.",
            "examples": [
                {
                    "title": "fetch va async/await orqali API chaqirish",
                    "problem": "Backenddan ma'lumotlarni asinxron olib keluvchi to'g'ri funksiya yozing.",
                    "step_by_step": "async function loadMaterials() {\n  try {\n    const response = await fetch('https://api.educationhub.uz/materials');\n    if (!response.ok) throw new Error('Tarmoq xatosi');\n    const data = await response.json();\n    console.log(data);\n  } catch (error) {\n    console.error('Xatolik:', error);\n  }\n}",
                    "answer": "async/await va try-catch orqali xavfsiz yuklash"
                },
                {
                    "title": "Destrukturizatsiya va Spread operatori",
                    "problem": "Ikkita massivni yangi massivga birlashtiring.",
                    "step_by_step": "const arr1 = [1, 2, 3];\nconst arr2 = [4, 5, 6];\nconst combined = [...arr1, ...arr2]; // [1, 2, 3, 4, 5, 6]",
                    "answer": "[...arr1, ...arr2]"
                }
            ],
            "exercise": "Template literal (backtick `) yordamida 'Ali' va 'Toshkent' qiymatlaridan 'Salom, Ali! Siz Toshkent shahrida yashaysiz.' satrini hosil qiling.",
            "exercise_solution": "const str = `Salom, ${name}! Siz ${city} shahrida yashaysiz.`;",
            "check_questions": [
                {
                    "question": "Asinxron funksiyani e'lon qilish uchun qaysi kalit so'z ishlatiladi?",
                    "options": ["sync", "async", "await", "defer"],
                    "correct_index": 1,
                    "explanation": "Asinxron funksiyalar 'async' kalit so'zi bilan boshlanadi va ichida 'await' ishlatishga imkon beradi."
                },
                {
                    "question": "Promise muvaffaqiyatli yakunlanganda qaysi holatga (state) o'tadi?",
                    "options": ["Pending", "Fulfilled (Resolved)", "Rejected", "Finished"],
                    "correct_index": 1,
                    "explanation": "Muvaffaqiyatli yakun — Fulfilled holatidir."
                },
                {
                    "question": "ES6 da o'zgaruvchilarni matn ichiga ${...} orqali joylash uchun qaysi belgi ishlatiladi?",
                    "options": ["Oddiy qo'shtirnoq \" \"", "Bittalik tirnoq ' '", "Qiya tirnoq (backtick ` `)", "Qavslar ( )"],
                    "correct_index": 2,
                    "explanation": "Template literals har doim backtick (``) belgisi ichida yoziladi."
                }
            ],
            "tags": ["javascript", "ES6", "async await", "fetch", "promises", "destructuring"],
            "duration_minutes": 35
        },
        {
            "id": "dev-020",
            "slug": "typescript-asoslari-va-statik-tiplash",
            "subject_id": "sub-40",
            "subject_name": "JavaScript",
            "title": "TypeScript: Statik tiplash, Interfeyslar (Interface), Type va Generics",
            "grade_level": "Kasbiy / Universitet",
            "difficulty": "Murakkab",
            "objective": "Nima uchun TypeScript ishlatiladi, tiplash turlari (string, number, boolean, any, union), Interface va Type yaratish hamda Generics larni tushunish.",
            "theory": "TypeScript — Microsoft tomonidan yaratilgan, JavaScript ustiga qurilgan ochiq kodli til bo'lib, unga statik tiplash (static typing) imkoniyatini qo'shadi. TypeScript kodi to'g'ridan-to'g'ri brauzerda ishlamaydi, u avval toza JavaScript ga kompilyatsiya qilinadi (transpiled). Ustunligi: dasturchi kod yozish paytidayoq xatolarni aniqlaydi (runtime xatoliklar keskin kamayadi) va kodni avtomatik to'ldirish (IntelliSense) mukammal ishlaydi. Asosiy tushunchalar: 1) Tiplash: let age: number = 25; let name: string = 'Ali'; 2) Union types: let id: string | number; 3) Interface va Type: ma'lumotlar strukturasini qat'iy belgilash (interface User { id: number; name: string; email?: string }); 4) Generics (<T>): har qanday turdagi ma'lumotlar bilan xavfsiz ishlay oladigan universal komponentlar yaratish.",
            "examples": [
                {
                    "title": "Interface yaratish va foydalanish",
                    "problem": "Education Hub 2.0 da Material uchun TypeScript interfeysini yozing.",
                    "step_by_step": "interface Material {\n  id: string;\n  title: string;\n  subject_id: string;\n  difficulty: 'Boshlang\\'ich' | 'O\\'rta' | 'Murakkab';\n  views?: number; // ixtiyoriy maydon\n}\n\nconst lesson: Material = {\n  id: 'mat-001',\n  title: 'Kasrlar',\n  subject_id: 'sub-01',\n  difficulty: 'Boshlang\\'ich'\n};",
                    "answer": "interface Material { ... }"
                },
                {
                    "title": "Generics funksiya",
                    "problem": "Har qanday turdagi massivning birinchi elementini xavfsiz qaytaruvchi Generic funksiya yozing.",
                    "step_by_step": "function getFirstElement<T>(arr: T[]): T | undefined {\n  return arr[0];\n}\n\nconst num = getFirstElement([10, 20]); // num turi number\nconst str = getFirstElement(['olma', 'anor']); // str turi string",
                    "answer": "function getFirstElement<T>(arr: T[]): T | undefined"
                }
            ],
            "exercise": "TypeScriptda 'email?: string;' dagi so'roq belgisi (?) nimani anglatadi?",
            "exercise_solution": "Bu maydon ixtiyoriy (optional) ekanligini, ya'ni obyektda bo'lishi ham, bo'lmasligi ham mumkinligini bildiradi.",
            "check_questions": [
                {
                    "question": "TypeScript ning asosiy maqsadi nima?",
                    "options": ["HTML ni almashtirish", "JavaScriptga statik tiplash qo'shib xatolarni erta aniqlash", "Fayllar hajmini kichraytirish", "CSS yozish"],
                    "correct_index": 1,
                    "explanation": "TypeScript kodni kompilyatsiya vaqtida qat'iy tekshirib xatolarning oldini oladi."
                },
                {
                    "question": "O'zgaruvchi bir nechta turda (masalan yo son, yo matn) bo'lishi qanday yoziladi?",
                    "options": ["let x: string && number", "let x: string | number (Union type)", "let x: any[]", "let x: mixed"],
                    "correct_index": 1,
                    "explanation": "Tik chiziq (|) Union type bo'lib, o'zgaruvchi bir nechta turlardan biri bo'lishini bildiradi."
                },
                {
                    "question": "Brauzerlar TypeScript (.ts) fayllarini to'g'ridan-to'g'ri bajara oladimi?",
                    "options": ["Ha, barcha zamonaviy brauzerlar tushunadi", "Yo'q, u avval JavaScript (.js) ga kompilyatsiya qilinishi shart", "Faqat Chrome tushunadi", "Faqat Node.js da"],
                    "correct_index": 1,
                    "explanation": "Brauzerlar faqat JavaScriptni tushunadi, TypeScript esa kompilyatorda toza JS ga o'giriladi."
                }
            ],
            "tags": ["typescript", "javascript", "typing", "interface", "generics", "frontend", "universitet"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_cs_programming_materials()
    print(f"Generated {len(mats)} CS/Programming materials.")
