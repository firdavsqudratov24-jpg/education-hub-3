# -*- coding: utf-8 -*-
"""
Builder for Matematika, Algebra, Geometriya (30 materials)
- sub-01: Matematika (12 materials: mat-001 to mat-012)
- sub-02: Algebra (10 materials: mat-013 to mat-022)
- sub-03: Geometriya (8 materials: mat-023 to mat-030)
"""

def get_math_materials():
    materials = [
        # MATEMATIKA (12)
        {
            "id": "mat-001",
            "slug": "natural-sonlar-va-ular-ustida-amallar",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Natural sonlar va ular ustida to'rtta arifmetik amal",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Natural sonlar tushunchasi, sanoq tizimi va qo'shish, ayirish, ko'paytirish, bo'lish amallarining xossalarini to'liq o'zlashtirish.",
            "theory": "Sanoqda ishlatiladigan 1, 2, 3, ... sonlar natural sonlar to'plami deyiladi va N harfi bilan belgilanadi. 0 soni natural son emas, lekin natural sonlar bilan birga nomanfiy butun sonlar to'plamini hosil qiladi. Natural sonlar ustida amallar bajarishda xossalar muhim: o'rin almashtirish (a + b = b + a, a * b = b * a), guruhlash ((a + b) + c = a + (b + c)) va taqsimot qonuni (a * (b + c) = a * b + a * c). Bo'lish amali esa ko'paytirishga teskari amal bo'lib, nolga bo'lish mumkin emas.",
            "examples": [
                {
                    "title": "Taqsimot qonunini qo'llash",
                    "problem": "Hisoblang: 48 * 27 + 48 * 73",
                    "step_by_step": "1) Umumiy ko'paytuvchi 48 ni qavsdan tashqariga chiqaramiz: 48 * (27 + 73).\n2) Qavs ichidagi yig'indini hisoblaymiz: 27 + 73 = 100.\n3) Ko'paytirishni bajaramiz: 48 * 100 = 4800.",
                    "answer": "4800"
                },
                {
                    "title": "Qoldiqli bo'lish masalasi",
                    "problem": "358 sonini 14 ga bo'lgandagi to'liqsiz bo'linma va qoldiqni toping.",
                    "step_by_step": "1) 358 ni 14 ga bo'lamiz: 35 ning ichida 14 ikki marta bor (14 * 2 = 28).\n2) 35 - 28 = 7, 8 ni tushiramiz: 78. 78 ning ichida 14 besh marta bor (14 * 5 = 70).\n3) 78 - 70 = 8. Demak, 358 = 14 * 25 + 8.",
                    "answer": "Bo'linma: 25, Qoldiq: 8"
                }
            ],
            "exercise": "Taqsimot qonunidan foydalanib qulay usulda hisoblang: 125 * 64 * 8",
            "exercise_solution": "Guruhlash qonuniga ko'ra (125 * 8) * 64 = 1000 * 64 = 64 000.",
            "check_questions": [
                {
                    "question": "Qaysi son natural son hisoblanmaydi?",
                    "options": ["1", "100", "0", "9999"],
                    "correct_index": 2,
                    "explanation": "0 soni sanoqda buyumlarni sanashda ishlatilmaydi, shu sababli u natural son emas."
                },
                {
                    "question": "36 * (10 + 5) ifodaning qiymati qanday hisoblanadi?",
                    "options": ["360 + 5 = 365", "360 + 180 = 540", "36 * 15 = 480", "360 * 5 = 1800"],
                    "correct_index": 1,
                    "explanation": "Taqsimot qonuniga ko'ra 36*10 + 36*5 = 360 + 180 = 540."
                },
                {
                    "question": "a : b = c (qoldiq r) bo'lsa, qoldiq r qaysi oraliqda bo'ladi?",
                    "options": ["0 <= r < b", "r > b", "r = b", "r >= b"],
                    "correct_index": 0,
                    "explanation": "Qoldiq har doim noldan katta yoki teng va bo'luvchidan qat'iy kichik bo'lishi shart."
                }
            ],
            "tags": ["natural sonlar", "arifmetika", "qoldiqli bo'lish", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "mat-002",
            "slug": "bolinish-belgilari-tub-va-murakkab-sonlar",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Bo'linish belgilari, tub va murakkab sonlar",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "2, 3, 5, 9, 10 ga bo'linish belgilarini amalda qo'llash, tub sonlarni murakkab sonlardan ajrata olish va tub ko'paytuvchilarga ajratish.",
            "theory": "Faqat 1 ga va o'ziga bo'linadigan 1 dan katta sonlar tub sonlar deyiladi (2, 3, 5, 7, 11, ...). 2 soni yagona juft tub son hisoblanadi. Ikkitadan ortiq bo'luvchiga ega sonlar murakkab sonlar deyiladi. 1 soni na tub, na murakkab. Bo'linish belgilari: Oxirgi raqami juft sonlar 2 ga, oxirgi raqami 0 yoki 5 bo'lgan sonlar 5 ga, raqamlari yig'indisi 3 ga bo'linadigan sonlar 3 ga, raqamlari yig'indisi 9 ga bo'linadigan sonlar 9 ga qoldiqsiz bo'linadi.",
            "examples": [
                {
                    "title": "3 va 9 ga bo'linishni tekshirish",
                    "problem": "47 826 soni 3 ga va 9 ga bo'linadimi?",
                    "step_by_step": "1) Raqamlar yig'indisini topamiz: 4 + 7 + 8 + 2 + 6 = 27.\n2) 27 soni 3 ga bo'linadi (27:3=9), demak son 3 ga bo'linadi.\n3) 27 soni 9 ga bo'linadi (27:9=3), demak son 9 ga ham bo'linadi.",
                    "answer": "Ha, ikkalasiga ham bo'linadi"
                },
                {
                    "title": "Tub ko'paytuvchilarga ajratish",
                    "problem": "360 sonini tub ko'paytuvchilarga ajrating.",
                    "step_by_step": "360 : 2 = 180\n180 : 2 = 90\n90 : 2 = 45\n45 : 3 = 15\n15 : 3 = 5\n5 : 5 = 1.\nNatija: 360 = 2^3 * 3^2 * 5.",
                    "answer": "2^3 * 3^2 * 5"
                }
            ],
            "exercise": "504 sonini tub ko'paytuvchilarga ajrating.",
            "exercise_solution": "504 = 2 * 252 = 2 * 2 * 126 = 2 * 2 * 2 * 63 = 2^3 * 3^2 * 7.",
            "check_questions": [
                {
                    "question": "Yagona juft tub son qaysi?",
                    "options": ["0", "2", "4", "6"],
                    "correct_index": 1,
                    "explanation": "2 soni faqat 1 ga va 2 ga bo'linadi, boshqa barcha juft sonlar kamida 2 ga bo'lingani uchun murakkabdir."
                },
                {
                    "question": "Quyidagi sonlardan qaysi biri 9 ga bo'linadi?",
                    "options": ["1234", "5432", "7362", "8121"],
                    "correct_index": 2,
                    "explanation": "7+3+6+2 = 18. 18 soni 9 ga karrali, shuning uchun 7362 soni 9 ga bo'linadi."
                },
                {
                    "question": "1 soni qaysi guruhga kiradi?",
                    "options": ["Tub son", "Murakkab son", "Na tub, na murakkab", "Manfiy son"],
                    "correct_index": 2,
                    "explanation": "1 soni ta'rifga ko'ra na tub son, na murakkab son hisoblanadi."
                }
            ],
            "tags": ["tub sonlar", "bo'linish belgilari", "ko'paytuvchilar", "5-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-003",
            "slug": "ekub-va-ekuk-hisoblash-usullari",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Eng katta umumiy bo'luvchi (EKUB) va Eng kichik umumiy karrali (EKUK)",
            "grade_level": "5-sinf",
            "difficulty": "O'rta",
            "objective": "Sonlarning EKUB va EKUKini tub ko'paytuvchilarga ajratish orqali hamda Evklid algoritmi yordamida tezkor hisoblashni o'rganish.",
            "theory": "Ikki yoki undan ortiq natural sonlarning har biriga bo'linadigan eng katta son ularning Eng Katta Umumiy Bo'luvchisi (EKUB) deyiladi. Berilgan sonlarning har biriga bo'linadigan eng kichik natural son ularning Eng Kichik Umumiy Karralisi (EKUK) deyiladi. Sonlar tub ko'paytuvchilarga ajratilganda, EKUB uchun umumiy tub asoslarning eng kichik darajalari ko'paytiriladi, EKUK uchun esa barcha qatnashgan asoslarning eng katta darajalari ko'paytiriladi. Muhim qoida: EKUB(a, b) * EKUK(a, b) = a * b.",
            "examples": [
                {
                    "title": "EKUB va EKUKni topish",
                    "problem": "72 va 120 sonlarining EKUB va EKUKini toping.",
                    "step_by_step": "1) 72 = 2^3 * 3^2.\n2) 120 = 2^3 * 3 * 5.\n3) EKUB(72, 120) = 2^3 * 3^1 = 8 * 3 = 24.\n4) EKUK(72, 120) = 2^3 * 3^2 * 5 = 8 * 9 * 5 = 360.",
                    "answer": "EKUB = 24, EKUK = 360"
                },
                {
                    "title": "O'zaro tub sonlar",
                    "problem": "15 va 28 sonlarining EKUBi nechaga teng?",
                    "step_by_step": "15 = 3 * 5; 28 = 2^2 * 7. Umumiy tub ko'paytuvchi yo'q. Demak ularning yagona umumiy bo'luvchisi 1 dir.",
                    "answer": "1 (O'zaro tub sonlar)"
                }
            ],
            "exercise": "48 va 64 sonlarining EKUB va EKUKini toping.",
            "exercise_solution": "48 = 2^4 * 3, 64 = 2^6. EKUB = 2^4 = 16. EKUK = 2^6 * 3 = 192.",
            "check_questions": [
                {
                    "question": "O'zaro tub sonlarning EKUBi nechaga teng?",
                    "options": ["0", "1", "Ularning ko'paytmasiga", "Mavjud emas"],
                    "correct_index": 1,
                    "explanation": "O'zaro tub sonlar umumiy bo'luvchiga ega bo'lmagan (1 dan tashqari) sonlardir."
                },
                {
                    "question": "EKUB(a, b) = 12 va a * b = 1440 bo'lsa, EKUK(a, b) nimaga teng?",
                    "options": ["120", "144", "12", "720"],
                    "correct_index": 0,
                    "explanation": "EKUK(a, b) = (a * b) / EKUB(a, b) = 1440 / 12 = 120."
                },
                {
                    "question": "18 va 24 sonlarining EKUBi qaysi?",
                    "options": ["3", "6", "12", "72"],
                    "correct_index": 1,
                    "explanation": "18 = 2 * 3^2, 24 = 2^3 * 3. EKUB = 2 * 3 = 6."
                }
            ],
            "tags": ["EKUB", "EKUK", "bo'luvchilar", "5-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-004",
            "slug": "oddiy-kasrlar-va-ular-ustida-amallar",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Oddiy kasrlar va ular ustida amallar",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Oddiy kasrlarning asosiy xossasi, umumiy maxrajga keltirish, qisqartirish, qo'shish, ayirish, ko'paytirish va bo'lishni to'liq o'rganish.",
            "theory": "m/n ko'rinishidagi son oddiy kasr deyiladi, bu yerda m - kasr surati, n - kasr maxraji (n != 0). Kasrning surati maxrajidan kichik bo'lsa to'g'ri kasr, surat maxrajiga teng yoki undan katta bo'lsa noto'g'ri kasr deyiladi. Kasrning asosiy xossasi: agar kasrning surati va maxraji noldan farqli bitta songa ko'paytirilsa yoki bo'linsa, uning qiymati o'zgarmaydi. Kasrlarni qo'shish va ayirishda avval ularning maxrajlari umumiy maxrajga (EKUK) keltiriladi.",
            "examples": [
                {
                    "title": "Har xil maxrajli kasrlarni qo'shish",
                    "problem": "Hisoblang: 3/8 + 5/12",
                    "step_by_step": "1) 8 va 12 ning EKUKi = 24.\n2) Qo'shimcha ko'paytuvchilar: 24:8=3, 24:12=2.\n3) 3*3 / 24 + 5*2 / 24 = 9/24 + 10/24 = 19/24.",
                    "answer": "19/24"
                },
                {
                    "title": "Kasrlarni ko'paytirish va bo'lish",
                    "problem": "Hisoblang: (4/9) * (15/16) : (5/6)",
                    "step_by_step": "1) Ko'paytirish: (4 * 15) / (9 * 16) = (1 * 5) / (3 * 4) = 5/12.\n2) Bo'lish: ikkinchi kasrning teskarisiga ko'paytiramiz: (5/12) * (6/5) = (1 * 1) / (2 * 1) = 1/2.",
                    "answer": "1/2"
                }
            ],
            "exercise": "Hisoblang: 7/15 - 3/10 + 1/6",
            "exercise_solution": "Maxrajlar 15, 10, 6 uchun EKUK = 30. (14 - 9 + 5) / 30 = 10 / 30 = 1/3.",
            "check_questions": [
                {
                    "question": "Surati maxrajidan kichik bo'lgan kasr qanday kasr deyiladi?",
                    "options": ["Noto'g'ri kasr", "To'g'ri kasr", "Aralash son", "Cheksiz kasr"],
                    "correct_index": 1,
                    "explanation": "Surati maxrajidan kichik kasrlar to'g'ri kasr deb ataladi (masalan, 3/5 < 1)."
                },
                {
                    "question": "2/3 sonining teskari soni qaysi?",
                    "options": ["-2/3", "3/2", "1/3", "2/6"],
                    "correct_index": 1,
                    "explanation": "a/b sonining teskarisi b/a bo'lib, ularning ko'paytmasi 1 ga teng: (2/3)*(3/2)=1."
                },
                {
                    "question": "Kasrni qisqartirish nimani anglatadi?",
                    "options": ["Surat va maxrajni bir xil songa bo'lish", "Suratidan maxrajini ayirish", "Maxrajni nolga aylantirish", "Suratni 2 ga ko'paytirish"],
                    "correct_index": 0,
                    "explanation": "Kasrning surat va maxrajini ularning 1 dan katta umumiy bo'luvchisiga bo'lish qisqartirish deyiladi."
                }
            ],
            "tags": ["oddiy kasrlar", "umumiy maxraj", "qisqartirish", "5-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "mat-005",
            "slug": "onli-kasrlar-va-davriy-kasrlar",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "O'nli kasrlar va cheksiz davriy kasrlar",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "O'nli kasrlar ustida amallar, ularni oddiy kasrga aylantirish va cheksiz davriy kasrlarni oddiy kasrga o'tkazish formulalarini o'rganish.",
            "theory": "Maxraji 10, 100, 1000 kabi 10 ning darajalaridan iborat kasrlar o'nli kasrlar shaklida vergul yordamida yoziladi (masalan 0.75 = 75/100 = 3/4). Agar oddiy kasrning qisqarmaydigan maxrajida 2 va 5 dan boshqa tub ko'paytuvchilar bo'lsa, u cheksiz davriy o'nli kasrga aylanadi. Masalan 1/3 = 0.333... = 0.(3). Sof davriy kasrlarni oddiy kasrga aylantirishda davrdagi son suratga, davrdagi raqamlar sonicha 9 maxrajga yoziladi: 0.(a) = a/9.",
            "examples": [
                {
                    "title": "O'nli kasrlarni ko'paytirish",
                    "problem": "Hisoblang: 3.45 * 1.2",
                    "step_by_step": "1) Vergulni hisobga olmasdan ko'paytiramiz: 345 * 12 = 4140.\n2) Ikkala ko'paytuvchida verguldan keyin jami 2 + 1 = 3 ta raqam bor.\n3) Olingan natijadan o'ngdan 3 ta raqam ajratamiz: 4.140 = 4.14.",
                    "answer": "4.14"
                },
                {
                    "title": "Aralash davriy kasrni oddiy kasrga aylantirish",
                    "problem": "0.1(6) sonini oddiy kasrga aylantiring.",
                    "step_by_step": "Formula: 0.a(b) = (ab - a) / 90.\nBu yerda: (16 - 1) / 90 = 15 / 90 = 1/6.",
                    "answer": "1/6"
                }
            ],
            "exercise": "0.(27) sof davriy kasrini qisqarmas oddiy kasrga aylantiring.",
            "exercise_solution": "0.(27) = 27 / 99 = 3 / 11.",
            "check_questions": [
                {
                    "question": "0.25 sonining oddiy kasr ko'rinishi qaysi?",
                    "options": ["1/2", "1/4", "1/5", "2/5"],
                    "correct_index": 1,
                    "explanation": "0.25 = 25/100 = 1/4."
                },
                {
                    "question": "0.(7) davriy kasri qaysi oddiy kasrga teng?",
                    "options": ["7/10", "7/9", "7/99", "7/90"],
                    "correct_index": 1,
                    "explanation": "Sof davriy kasrda maxrajga davr xonalaricha 9 yoziladi, ya'ni 7/9."
                },
                {
                    "question": "12.4 : 0.04 amali qanday bajariladi?",
                    "options": ["12.4 : 4 = 3.1", "1240 : 4 = 310", "124 : 4 = 31", "1.24 : 4 = 0.31"],
                    "correct_index": 1,
                    "explanation": "Bo'luvchi butun son bo'lishi uchun ikkala sonni 100 ga ko'paytiramiz: 1240 : 4 = 310."
                }
            ],
            "tags": ["o'nli kasrlar", "davriy kasrlar", "arifmetika", "5-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-006",
            "slug": "nisbat-proporsiya-va-foizlar",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Nisbat, proporsiya va foiz hisoblash amaliyoti",
            "grade_level": "6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Proporsiyaning asosiy xossasini bilish, to'g'ri va teskari proporsional miqdorlarni farqlash hamda foizga doir 3 ta asosiy masalani yechish.",
            "theory": "Ikki sonning bo'linmasi ularning nisbati deyiladi. Ikki nisbatning tengligi proporsiya deyiladi: a : b = c : d yoki a/b = c/d. Proporsiyaning asosiy xossasi: chetki hadlar ko'paytmasi o'rta hadlar ko'paytmasiga teng (a * d = b * c). Sonning yuzdan bir qismi foiz (%) deyiladi (1% = 0.01 = 1/100). Foizga doir uchta asosiy masala: 1) Sonning foizini topish: b = a * (P/100); 2) Foiziga ko'ra sonni topish: a = b / (P/100); 3) Ikki sonning foiz nisbatini topish: (a/b) * 100%.",
            "examples": [
                {
                    "title": "Proporsiya noma'lum hadini topish",
                    "problem": "x : 18 = 5 : 6 tenglamadan x ni toping.",
                    "step_by_step": "1) Proporsiyaning asosiy xossasi bo'yicha: 6 * x = 18 * 5.\n2) 6x = 90.\n3) x = 90 / 6 = 15.",
                    "answer": "x = 15"
                },
                {
                    "title": "Tovarning yangi narxini hisoblash",
                    "problem": "Dastlabki narxi 240 000 so'm bo'lgan buyum narxi 15% ga arzonlashtirildi. Buyumning yangi narxi qancha?",
                    "step_by_step": "1) Chegirma summasini topamiz: 240 000 * 0.15 = 36 000 so'm.\n2) Yangi narxni hisoblaymiz: 240 000 - 36 000 = 204 000 so'm.",
                    "answer": "204 000 so'm"
                }
            ],
            "exercise": "Sinfdagi 30 nafar o'quvchidan 18 nafari a'lochi. A'lochilar sinf o'quvchilarining necha foizini tashkil qiladi?",
            "exercise_solution": "(18 / 30) * 100% = 0.6 * 100% = 60%.",
            "check_questions": [
                {
                    "question": "a : b = c : d proporsiyada to'g'ri munosabat qaysi?",
                    "options": ["a * c = b * d", "a * d = b * c", "a + d = b + c", "a : d = b : c"],
                    "correct_index": 1,
                    "explanation": "Proporsiyaning asosiy xossasiga ko'ra chetki hadlar ko'paytmasi o'rta hadlar ko'paytmasiga teng: a*d = b*c."
                },
                {
                    "question": "300 ning 20% i nechaga teng?",
                    "options": ["30", "50", "60", "150"],
                    "correct_index": 2,
                    "explanation": "300 * 0.20 = 60."
                },
                {
                    "question": "Qaysi bog'lanish teskari proporsional?",
                    "options": ["Tezlik o'zgarmaganda vaqt va masofa", "Masofa o'zgarmaganda tezlik va sarflangan vaqt", "Xarid miqdori va to'lanadigan summa", "Kvadrat tomoni va uning perimetri"],
                    "correct_index": 1,
                    "explanation": "Masofa doimiy bo'lganda tezlik qancha oshsa, vaqt shuncha kamayadi, ya'ni teskari proporsionaldir."
                }
            ],
            "tags": ["proporsiya", "foizlar", "nisbat", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-007",
            "slug": "butun-sonlar-va-ratsional-sonlar",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Butun sonlar, manfiy sonlar va ratsional sonlar to'plami",
            "grade_level": "6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Koordinata to'g'ri chizig'ida sonlarni tasvirlash, sonning moduli va manfiy sonlar ustida amallarni to'g'ri bajarish.",
            "theory": "Natural sonlar, ularga qarama-qarshi sonlar va 0 soni birgalikda butun sonlar to'plamini (Z) hosil qiladi: Z = {..., -3, -2, -1, 0, 1, 2, 3, ...}. Sonning moduli (|x|) deb sanoq boshidan berilgan nuqtagacha bo'lgan masofaga aytiladi va u doimo nomanfiy: |a| >= 0. Manfiy sonlarni qo'shganda ularning modullari qo'shilib, oldiga minus belgisi qo'yiladi: (-a) + (-b) = -(a+b). Ikkita manfiy sonni ko'paytirganda yoki bo'lganda musbat son hosil bo'ladi: (-) * (-) = (+).",
            "examples": [
                {
                    "title": "Turli ishorali sonlarni qo'shish va ayirish",
                    "problem": "Hisoblang: -15 + 23 - (-8) - 12",
                    "step_by_step": "1) -(-8) = +8 ekanligini hisobga olamiz: -15 + 23 + 8 - 12.\n2) Musbat sonlarni yig'amiz: 23 + 8 = 31.\n3) Manfiy sonlar yig'indisi: -15 + (-12) = -27.\n4) 31 - 27 = 4.",
                    "answer": "4"
                },
                {
                    "title": "Manfiy sonlar ko'paytmasi",
                    "problem": "Hisoblang: (-4) * (-2.5) * (-3)",
                    "step_by_step": "1) Dastlabki ikkita ko'paytuvchi: (-4) * (-2.5) = +10.\n2) Keyingi amal: 10 * (-3) = -30.",
                    "answer": "-30"
                }
            ],
            "exercise": "Hisoblang: |-18| - |12| + |-7| * (-2)",
            "exercise_solution": "18 - 12 + 7 * (-2) = 6 - 14 = -8.",
            "check_questions": [
                {
                    "question": "|-45| qiymati nechaga teng?",
                    "options": ["-45", "45", "0", "1/45"],
                    "correct_index": 1,
                    "explanation": "Har qanday sonning moduli nomanfiy masofani ifodalaydi, shuning uchun |-45| = 45."
                },
                {
                    "question": "(-6) * (-7) ko'paytmasining natijasi qanday?",
                    "options": ["-42", "42", "-13", "13"],
                    "correct_index": 1,
                    "explanation": "Ikkita manfiy son ko'paytmasi musbat songa teng: (-)*(-) = +."
                },
                {
                    "question": "-8 va -12 sonlaridan qaysi biri katta?",
                    "options": ["-12 katta", "-8 katta", "Ikkalasi teng", "Taqqoslab bo'lmaydi"],
                    "correct_index": 1,
                    "explanation": "Koordinata to'g'ri chizig'ida o'ngroqda joylashgan son katta bo'ladi. -8 > -12."
                }
            ],
            "tags": ["butun sonlar", "modul", "ratsional sonlar", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "mat-008",
            "slug": "chiziqli-tenglamalar-va-tengsizliklar-asoslari",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Bir noma'lumli sodda chiziqli tenglamalar",
            "grade_level": "6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Noma'lum qatnashgan sodda tenglamalarni yechish va tenglamaning ildizini tekshirish ko'nikmasini rivojlantirish.",
            "theory": "ax + b = 0 (a != 0) ko'rinishidagi tenglama bir noma'lumli chiziqli tenglama deyiladi. Tenglamaning ildizi deb, noma'lum o'rniga qo'yilganda uni to'g'ri tenglikka aylantiruvchi songa aytiladi. Tenglamani yechish qoidalari: 1) Tenglamaning istalgan hadini uning ishorasini qarama-qarshisiga o'zgartirib tenglikning bir tomonidan ikkinchi tomoniga o'tkazish mumkin. 2) Tenglamaning ikkala tomonini noldan farqli bir xil songa ko'paytirish yoki bo'lish mumkin.",
            "examples": [
                {
                    "title": "Chiziqli tenglamani yechish",
                    "problem": "5x - 14 = 2x + 7 tenglamani yeching.",
                    "step_by_step": "1) Noma'lumlarni chap tomonga, ma'lumlarni o'ng tomonga o'tkazamiz:\n   5x - 2x = 7 + 14.\n2) O'xshash hadlarni ixchamlaymiz: 3x = 21.\n3) x = 21 / 3 = 7.\n4) Tekshirish: 5*7 - 14 = 35 - 14 = 21; 2*7 + 7 = 14 + 7 = 21. Tenglik to'g'ri.",
                    "answer": "x = 7"
                },
                {
                    "title": "Qavsli tenglamani yechish",
                    "problem": "3(2x - 4) = 4x + 6 tenglamani yeching.",
                    "step_by_step": "1) Qavsni ochamiz: 6x - 12 = 4x + 6.\n2) 6x - 4x = 6 + 12.\n3) 2x = 18.\n4) x = 9.",
                    "answer": "x = 9"
                }
            ],
            "exercise": "Yeching: 7(x - 2) - 3(x + 1) = 9",
            "exercise_solution": "7x - 14 - 3x - 3 = 9 => 4x - 17 = 9 => 4x = 26 => x = 6.5.",
            "check_questions": [
                {
                    "question": "4x + 12 = 0 tenglamaning ildizi qanday?",
                    "options": ["3", "-3", "4", "-4"],
                    "correct_index": 1,
                    "explanation": "4x = -12 => x = -12 / 4 = -3."
                },
                {
                    "question": "Agar 0 * x = 5 bo'lsa, tenglama nechta yechimga ega?",
                    "options": ["1 ta", "Cheksiz ko'p", "Yechimga ega emas", "2 ta"],
                    "correct_index": 2,
                    "explanation": "0 ni har qanday songa ko'paytirganda 0 hosil bo'ladi, hech qachon 5 ga teng bo'la olmaydi. Yechim yo'q."
                },
                {
                    "question": "Tenglamaning hadini bir tomondan ikkinchi tomonga o'tkazganda nima o'zgaradi?",
                    "options": ["Moduli", "Ishorasi", "Darajasi", "Hech narsa"],
                    "correct_index": 1,
                    "explanation": "Tenglamaning hadlari tenglik orqali o'tkazilganda ishorasi qarama-qarshisiga almashadi."
                }
            ],
            "tags": ["tenglamalar", "chiziqli tenglama", "ildiz", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "mat-009",
            "slug": "matnli-masalalarni-tenglama-tuzib-yechish",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Matnli masalalarni tenglama tuzish yordamida yechish",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Harakatga, ish unumdorligiga va aralashmalarga oid amaliy matnli masalalarni matematik modelga aylantirish va yechish.",
            "theory": "Matnli masalalarni yechish bosqichlari: 1) Masala shartini tahlil qilish va noma'lumlardan birini x bilan belgilash; 2) Boshqa kattaliklarni x orqali ifodalash; 3) Masaladagi bog'lanish asosida tenglama tuzish; 4) Tenglamani yechish va ildizning masala ma'nosiga mosligini tekshirish. Harakat masalalarida asosiy formula: S = v * t (Masofa = tezlik * vaqt). Oqim bo'yicha tezlik: v_oqim = v_kater + v_daryo; oqimga qarshi tezlik: v_qarshi = v_kater - v_daryo.",
            "examples": [
                {
                    "title": "Harakatga doir masala",
                    "problem": "Ikki shahar orasidagi masofa 360 km. Ikki shahardan bir-biriga qarab ikki avtomobil yo'lga chiqdi va 3 soatdan keyin uchrashdi. Birinchi avtomobilning tezligi ikkinchisinikidan 20 km/soat ga ko'p bo'lsa, har birining tezligini toping.",
                    "step_by_step": "1) Ikkinchi avtomobil tezligi: x km/soat. Birinchi avtomobil: (x + 20) km/soat.\n2) Yaqinlashish tezligi: x + (x + 20) = 2x + 20.\n3) 3 soatdagi yo'l: 3 * (2x + 20) = 360.\n4) 2x + 20 = 120 => 2x = 100 => x = 50 km/soat.\n5) Birinchi avtomobil: 50 + 20 = 70 km/soat.",
                    "answer": "50 km/soat va 70 km/soat"
                },
                {
                    "title": "Yoshga doir masala",
                    "problem": "Otaning yoshi o'g'lining yoshidan 4 marta katta. 6 yildan keyin ota o'g'lidan 3 marta katta bo'lsa, hozir o'g'il necha yoshda?",
                    "step_by_step": "1) O'g'ilning yoshi: x, Otaning yoshi: 4x.\n2) 6 yildan so'ng: o'g'il (x + 6), ota (4x + 6).\n3) Tenglama: 4x + 6 = 3 * (x + 6).\n4) 4x + 6 = 3x + 18 => x = 12.",
                    "answer": "12 yoshda"
                }
            ],
            "exercise": "Katerning o'z tezligi 22 km/soat, daryo oqimi tezligi 3 km/soat. Kater oqim bo'yicha 4 soatda necha km masofani bosib o'tadi?",
            "exercise_solution": "v_oqim = 22 + 3 = 25 km/soat. S = 25 * 4 = 100 km.",
            "check_questions": [
                {
                    "question": "S = v * t formulasida t ni topish formulasi qaysi?",
                    "options": ["t = S * v", "t = S / v", "t = v / S", "t = S + v"],
                    "correct_index": 1,
                    "explanation": "Vaqt masofaning tezlikka bo'linganiga teng: t = S / v."
                },
                {
                    "question": "Kater daryo oqimiga qarshi suzganda uning tezligi qanday topiladi?",
                    "options": ["v_kater + v_oqim", "v_kater - v_oqim", "v_kater * v_oqim", "v_oqim - v_kater"],
                    "correct_index": 1,
                    "explanation": "Oqimga qarshi harakatda oqim tezligi kater tezligiga qarshilik ko'rsatadi: v = v_k - v_o."
                },
                {
                    "question": "Bir kishi ishni 6 kunda, ikkinchisi 3 kunda tugatsa, birgalikda necha kunda bajarishadi?",
                    "options": ["4.5 kunda", "2 kunda", "3 kunda", "1 kunda"],
                    "correct_index": 1,
                    "explanation": "Birgalikdagi unumdorlik: 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2. Jami vaqt: 1 / (1/2) = 2 kun."
                }
            ],
            "tags": ["matnli masalalar", "harakat", "tenglama", "6-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "mat-010",
            "slug": "darajalar-va-ularning-xossalari",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Natural va butun ko'rsatkichli daraja xossalari",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Daraja tushunchasini chuqur tushunish va bir xil asosli darajalarni ko'paytirish, bo'lish, darajani darajaga ko'tarish amallarini erkin bajarish.",
            "theory": "a sonining n-darajasi (a^n) deb har biri a ga teng bo'lgan n ta ko'paytuvchining ko'paytmasiga aytiladi. a^0 = 1 (a != 0), a^(-n) = 1 / (a^n). Asosiy xossalar: 1) a^m * a^n = a^(m+n); 2) a^m / a^n = a^(m-n); 3) (a^m)^n = a^(m*n); 4) (a * b)^n = a^n * b^n; 5) (a/b)^n = a^n / b^n.",
            "examples": [
                {
                    "title": "Darajali ifodani soddalashtirish",
                    "problem": "Hisoblang: (2^5 * 4^3) / 8^3",
                    "step_by_step": "1) Barcha asoslarni 2 ning darajasiga keltiramiz: 4 = 2^2, 8 = 2^3.\n2) 4^3 = (2^2)^3 = 2^6; 8^3 = (2^3)^3 = 2^9.\n3) Surat: 2^5 * 2^6 = 2^(5+6) = 2^11.\n4) Kasr: 2^11 / 2^9 = 2^(11-9) = 2^2 = 4.",
                    "answer": "4"
                },
                {
                    "title": "Manfiy ko'rsatkichli daraja",
                    "problem": "Hisoblang: (1/3)^(-2) + 5^(-1) * 20",
                    "step_by_step": "1) (1/3)^(-2) = 3^2 = 9.\n2) 5^(-1) = 1/5; (1/5) * 20 = 4.\n3) 9 + 4 = 13.",
                    "answer": "13"
                }
            ],
            "exercise": "Hisoblang: (3^7 * 9^(-2)) / 27",
            "exercise_solution": "3^7 * (3^2)^(-2) / 3^3 = 3^7 * 3^(-4) / 3^3 = 3^(7 - 4 - 3) = 3^0 = 1.",
            "check_questions": [
                {
                    "question": "Har qanday noldan farqli sonning 0-darajasi nimaga teng?",
                    "options": ["0", "1", "O'ziga", "Mavjud emas"],
                    "correct_index": 1,
                    "explanation": "Ta'rifga ko'ra a^0 = 1 (a != 0)."
                },
                {
                    "question": "2^(-3) ifodaning qiymati qanday?",
                    "options": ["-8", "-6", "1/8", "1/6"],
                    "correct_index": 2,
                    "explanation": "2^(-3) = 1 / (2^3) = 1/8."
                },
                {
                    "question": "(x^3)^4 ifoda qaysi biriga teng?",
                    "options": ["x^7", "x^12", "x^1", "x^(3/4)"],
                    "correct_index": 1,
                    "explanation": "Daraja darajaga ko'tarilganda ko'rsatkichlar ko'paytiriladi: 3 * 4 = 12."
                }
            ],
            "tags": ["darajalar", "ko'rsatkich", "arifmetika", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "mat-011",
            "slug": "sonli-ketma-ketliklar-va-qonuniyatlar",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Sonli ketma-ketliklar va ulardagi mantiqiy qonuniyatlar",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Sonlar qatoridagi qonuniyatni topish, ketma-ketlikning n-hadini ifodalash va mantiqiy fikrlashni rivojlantirish.",
            "theory": "Muayyan tartibda joylashgan sonlar to'plami sonli ketma-ketlik deyiladi. Ketma-ketlik elementlari uning hadlari deb ataladi va a_1, a_2, ..., a_n bilan belgilanadi. Masalan, juft sonlar ketma-ketligi: 2, 4, 6, 8, ... (umumiy hadi a_n = 2n). Toq sonlar ketma-ketligi: 1, 3, 5, 7, ... (a_n = 2n - 1). Fibonachchi ketma-ketligida har bir had o'zidan oldingi ikki hadning yig'indisiga teng: 1, 1, 2, 3, 5, 8, 13, ... (F_n = F_(n-1) + F_(n-2)).",
            "examples": [
                {
                    "title": "Qonuniyatni aniqlash va keyingi hadni topish",
                    "problem": "3, 7, 11, 15, 19, ... ketma-ketlikning keyingi ikkita hadini va 20-hadini toping.",
                    "step_by_step": "1) Har bir had oldingisiga 4 qo'shish orqali hosil bo'lmoqda: d = 4.\n2) Keyingi hadlar: 19 + 4 = 23, 23 + 4 = 27.\n3) Umumiy had: a_n = 3 + 4*(n - 1) = 4n - 1.\n4) 20-had: a_20 = 4*20 - 1 = 80 - 1 = 79.",
                    "answer": "Keyingi hadlar: 23, 27; 20-had: 79"
                },
                {
                    "title": "Kvadratlar ketma-ketligi",
                    "problem": "1, 4, 9, 16, 25, ... qatorining 12-hadi nechaga teng?",
                    "step_by_step": "1) Qonuniyat: a_n = n^2.\n2) a_12 = 12^2 = 144.",
                    "answer": "144"
                }
            ],
            "exercise": "2, 6, 18, 54, ... ketma-ketlikning 6-hadini toping.",
            "exercise_solution": "Har bir had 3 ga ko'paytirilmoqda. a_5 = 54 * 3 = 162, a_6 = 162 * 3 = 486.",
            "check_questions": [
                {
                    "question": "Fibonachchi sonlarida 8 dan keyingi son qaysi?",
                    "options": ["10", "11", "12", "13"],
                    "correct_index": 3,
                    "explanation": "Ketma-ketlik: 1, 1, 2, 3, 5, 8, 13... 5 + 8 = 13."
                },
                {
                    "question": "a_n = 3n + 2 ketma-ketlikning 5-hadi nechaga teng?",
                    "options": ["15", "17", "18", "20"],
                    "correct_index": 1,
                    "explanation": "a_5 = 3*5 + 2 = 15 + 2 = 17."
                },
                {
                    "question": "1, 8, 27, 64, ... ketma-ketlik nimani ifodalaydi?",
                    "options": ["Sonlar kvadratlarini", "Sonlar kublarini", "Tub sonlarni", "Tub ko'paytuvchilarni"],
                    "correct_index": 1,
                    "explanation": "1^3 = 1, 2^3 = 8, 3^3 = 27, 4^3 = 64 (natural sonlar kublari)."
                }
            ],
            "tags": ["ketma-ketlik", "mantiqiy qonuniyat", "fibonachchi", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "mat-012",
            "slug": "kombinatorika-va-ehtimollik-boshlangich-tushunchalari",
            "subject_id": "sub-01",
            "subject_name": "Matematika",
            "title": "Kombinatorika asoslari va klassik ehtimollik",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Ko'paytirish va qo'shish qoidalarini, o'rin almashtirishlar sonini va hodisaning klassik ehtimolligini hisoblashni o'rganish.",
            "theory": "Kombinatorika elementlarning turli joylashuv va birikmalar sonini hisoblaydi. Ko'paytirish qoidasi: agar A obyektni m usulda, uning har bir usuliga mos ravishda B obyektni n usulda tanlash mumkin bo'lsa, ikkala obyektni birgalikda m * n usulda tanlash mumkin. n ta elementning o'rin almashtirishlari soni faktorial bilan belgilanadi: P_n = n! = 1 * 2 * 3 * ... * n. Hodisaning klassik ehtimolligi P(A) = m / n formulasi bilan hisoblanadi, bu yerda m - hodisaga qulaylik yaratuvchi natijalar soni, n - barcha teng imkoniyatli natijalar soni (0 <= P(A) <= 1).",
            "examples": [
                {
                    "title": "Raqamlardan sonlar tuzish",
                    "problem": "1, 2, 3 raqamlaridan raqamlari takrorlanmaydigan nechta 3 xonali son tuzish mumkin?",
                    "step_by_step": "1) Yuzlar xonasiga 3 ta variant (1, 2, 3).\n2) O'nlar xonasiga qolgan 2 ta variant.\n3) Birlar xonasiga qolgan 1 ta variant.\n4) Ko'paytirish qoidasi: 3 * 2 * 1 = 3! = 6 ta.",
                    "answer": "6 ta"
                },
                {
                    "title": "O'yin suyagini tashlash",
                    "problem": "Oddiy o'yin suyagi tashlanganda juft ochko tushish ehtimolligini toping.",
                    "step_by_step": "1) Barcha natijalar: {1, 2, 3, 4, 5, 6}, jami n = 6.\n2) Qulay natijalar (juft sonlar): {2, 4, 6}, jami m = 3.\n3) P = m / n = 3 / 6 = 1/2 = 0.5 (yoki 50%).",
                    "answer": "0.5 (50%)"
                }
            ],
            "exercise": "Qutida 4 ta qizil va 6 ta oq shar bor. Tavakkaliga olingan sharning qizil bo'lish ehtimolligini toping.",
            "exercise_solution": "Jami sharlar: 4 + 6 = 10. Qizil sharlar: 4. Ehtimollik: P = 4/10 = 0.4.",
            "check_questions": [
                {
                    "question": "4! (to'rt faktorial) qiymati nechaga teng?",
                    "options": ["12", "16", "24", "48"],
                    "correct_index": 2,
                    "explanation": "4! = 1 * 2 * 3 * 4 = 24."
                },
                {
                    "question": "Mumkin bo'lmagan hodisaning ehtimolligi nimaga teng?",
                    "options": ["-1", "0", "0.5", "1"],
                    "correct_index": 1,
                    "explanation": "Hech qachon ro'y bermaydigan hodisa ehtimolligi 0 ga teng."
                },
                {
                    "question": "Tanga 1 marta tashlanganda gerb tushish ehtimolligi qancha?",
                    "options": ["1/4", "1/2", "1", "0"],
                    "correct_index": 1,
                    "explanation": "Tanganing 2 tomoni bor, gerb bitta natija: 1/2."
                }
            ],
            "tags": ["kombinatorika", "ehtimollik", "faktorial", "6-sinf"],
            "duration_minutes": 30
        },

        # ALGEBRA (10)
        {
            "id": "mat-013",
            "slug": "qisqa-kopaytirish-formulalari",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Qisqa ko'paytirish formulalari va ularning tatbiqi",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Kvadratlar ayirmasi, yig'indi va ayirmaning kvadrati hamda kubi formulalarini ifodalarni ko'paytuvchilarga ajratishda to'g'ri qo'llash.",
            "theory": "Qisqa ko'paytirish formulalari algebrada hisoblashlarni tezlashtirish va ko'phadlarni ko'paytuvchilarga ajratishda asosiy vositadir: 1) Kvadratlar ayirmasi: a^2 - b^2 = (a - b)(a + b); 2) Yig'indining kvadrati: (a + b)^2 = a^2 + 2ab + b^2; 3) Ayirmaning kvadrati: (a - b)^2 = a^2 - 2ab + b^2; 4) Kublar yig'indisi va ayirmasi: a^3 + b^3 = (a + b)(a^2 - ab + b^2), a^3 - b^3 = (a - b)(a^2 + ab + b^2); 5) Yig'indi va ayirmaning kubi: (a +- b)^3 = a^3 +- 3a^2b + 3ab^2 +- b^3.",
            "examples": [
                {
                    "title": "Kvadratlar ayirmasidan foydalanib hisoblash",
                    "problem": "Hisoblang: 73^2 - 27^2",
                    "step_by_step": "1) Formulani qo'llaymiz: (73 - 27) * (73 + 27).\n2) Qavslarni hisoblaymiz: 73 - 27 = 46; 73 + 27 = 100.\n3) 46 * 100 = 4600.",
                    "answer": "4600"
                },
                {
                    "title": "To'la kvadratni ajratish",
                    "problem": "x^2 + 6x + 9 ko'phadni ko'paytuvchilarga ajrating.",
                    "step_by_step": "x^2 + 2 * x * 3 + 3^2 = (x + 3)^2.",
                    "answer": "(x + 3)^2"
                }
            ],
            "exercise": "Soddalashtiring: (2x - 5)^2 - (2x + 5)^2",
            "exercise_solution": "Kvadratlar ayirmasi: [(2x - 5) - (2x + 5)][(2x - 5) + (2x + 5)] = (-10) * (4x) = -40x.",
            "check_questions": [
                {
                    "question": "(a - b)^2 ifodaning to'g'ri yoyilmasi qaysi?",
                    "options": ["a^2 - b^2", "a^2 - 2ab + b^2", "a^2 + 2ab + b^2", "a^2 - ab + b^2"],
                    "correct_index": 1,
                    "explanation": "Ikki son ayirmasining kvadrati birinchisining kvadrati minus ikkilangan ko'paytmasi plyus ikkinchisining kvadratiga teng."
                },
                {
                    "question": "x^2 - 49 ifodasi qanday ko'paytuvchilarga ajraladi?",
                    "options": ["(x - 7)^2", "(x + 7)^2", "(x - 7)(x + 7)", "(x - 49)(x + 1)"],
                    "correct_index": 2,
                    "explanation": "a^2 - b^2 = (a - b)(a + b) formulasi bo'yicha: x^2 - 7^2 = (x - 7)(x + 7)."
                },
                {
                    "question": "99^2 sonini qulay usulda hisoblash qaysi ifoda orqali bo'ladi?",
                    "options": ["(100 - 1)^2 = 10000 - 200 + 1", "(90 + 9)^2", "(100 + 1)(100 - 1)", "99 * 100 - 1"],
                    "correct_index": 0,
                    "explanation": "(100 - 1)^2 = 10000 - 200 + 1 = 9801."
                }
            ],
            "tags": ["qisqa ko'paytirish", "algebra", "ko'phadlar", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-014",
            "slug": "chiziqli-tenglamalar-sistemasi",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Ikki noma'lumli chiziqli tenglamalar sistemasi va yechish usullari",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Tenglamalar sistemasini o'rniga qo'yish, algebraik qo'shish va grafik usullarda to'liq yechish ko'nikmasini egallash.",
            "theory": "a_1*x + b_1*y = c_1 va a_2*x + b_2*y = c_2 ko'rinishidagi tenglamalar birgalikda ikki noma'lumli chiziqli tenglamalar sistemasini hosil qiladi. Sistemaning yechimi deb har ikkala tenglamani to'g'ri tenglikka aylantiruvchi (x; y) sonlar juftligiga aytiladi. Asosiy yechish usullari: 1) O'rniga qo'yish usuli (bir noma'lumni ikkinchisi orqali ifodalab, ikkinchi tenglamaga qo'yish); 2) Qo'shish usuli (noma'lumlardan birining koeffitsiyentlarini qarama-qarshi qilib, tenglamalarni hadma-had qo'shish); 3) Grafik usul (to'g'ri chiziqlarning kesishish nuqtasini topish).",
            "examples": [
                {
                    "title": "Qo'shish usulida yechish",
                    "problem": "Sistemani yeching: { 2x + 3y = 13; 5x - 3y = 8 }",
                    "step_by_step": "1) y ning oldidagi koeffitsiyentlar qarama-qarshi (+3 va -3). Tenglamalarni hadma-had qo'shamiz:\n   (2x + 5x) + (3y - 3y) = 13 + 8.\n2) 7x = 21 => x = 3.\n3) x = 3 ni birinchi tenglamaga qo'yamiz: 2*3 + 3y = 13 => 6 + 3y = 13 => 3y = 7 => y = 7/3.",
                    "answer": "(3; 7/3)"
                },
                {
                    "title": "O'rniga qo'yish usuli",
                    "problem": "Sistemani yeching: { x - 2y = 1; 3x + y = 10 }",
                    "step_by_step": "1) Birinchi tenglamadan x ni topamiz: x = 2y + 1.\n2) Ikkinchisiga qo'yamiz: 3(2y + 1) + y = 10 => 6y + 3 + y = 10 => 7y = 7 => y = 1.\n3) x = 2*1 + 1 = 3.",
                    "answer": "(3; 1)"
                }
            ],
            "exercise": "Sistemani yeching: { 3x + 2y = 12; 4x - y = 5 }",
            "exercise_solution": "Ikkinchi tenglamadan y = 4x - 5. Birinchisiga qo'yamiz: 3x + 2(4x - 5) = 12 => 3x + 8x - 10 = 12 => 11x = 22 => x = 2. y = 4*2 - 5 = 3. Javob: (2; 3).",
            "check_questions": [
                {
                    "question": "Chiziqli tenglamalar sistemasining to'g'ri chiziqlari parallel bo'lsa, nechta yechim bor?",
                    "options": ["1 ta", "2 ta", "Cheksiz ko'p", "Yechimga ega emas"],
                    "correct_index": 3,
                    "explanation": "Parallel to'g'ri chiziqlar hech qachon kesishmaydi, demak umumiy nuqtasi yo'q va sistema yechimga ega emas."
                },
                {
                    "question": "{ x + y = 10; x - y = 4 } sistemasidan x ni toping.",
                    "options": ["5", "6", "7", "8"],
                    "correct_index": 2,
                    "explanation": "Hadma-had qo'shsak: 2x = 14 => x = 7."
                },
                {
                    "question": "Tenglamalar sistemasi qachon cheksiz ko'p yechimga ega bo'ladi?",
                    "options": ["To'g'ri chiziqlar ustma-ust tushganda", "To'g'ri chiziqlar perpendikulyar bo'lganda", "To'g'ri chiziqlar kesishganda", "Hech qachon"],
                    "correct_index": 0,
                    "explanation": "Ikki to'g'ri chiziq ustma-ust tushsa (koeffitsiyentlar proporsional bo'lsa), umumiy nuqtalar cheksiz ko'p bo'ladi."
                }
            ],
            "tags": ["tenglamalar sistemasi", "algebra", "chiziqli sistema", "7-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "mat-015",
            "slug": "kvadrat-tenglamalar-va-diskriminant",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Kvadrat tenglamalar, diskriminant va Viyet teoremasi",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "ax^2 + bx + c = 0 tenglamani diskriminant orqali yechish, diskriminant ishorasiga qarab ildizlar sonini aniqlash va Viyet teoremasini qo'llash.",
            "theory": "ax^2 + bx + c = 0 (a != 0) tenglama kvadrat tenglama deyiladi. D = b^2 - 4ac kattalik kvadrat tenglamaning diskriminanti deyiladi. Diskriminant xossalari: 1) Agar D > 0 bo'lsa, tenglama ikkita haqiqiy ildizga ega: x_(1,2) = (-b +- sqrt(D)) / (2a); 2) Agar D = 0 bo'lsa, yagona karrali ildiz mavjud: x = -b / (2a); 3) Agar D < 0 bo'lsa, haqiqiy ildizlar mavjud emas. Viyet teoremasi: keltirilgan x^2 + px + q = 0 tenglamada x_1 + x_2 = -p va x_1 * x_2 = q.",
            "examples": [
                {
                    "title": "Kvadrat tenglamani yechish",
                    "problem": "2x^2 - 5x + 2 = 0 tenglamani yeching.",
                    "step_by_step": "1) Koeffitsiyentlar: a = 2, b = -5, c = 2.\n2) D = (-5)^2 - 4 * 2 * 2 = 25 - 16 = 9 > 0.\n3) sqrt(D) = 3.\n4) x_1 = (5 + 3) / (2 * 2) = 8 / 4 = 2.\n5) x_2 = (5 - 3) / (2 * 2) = 2 / 4 = 0.5.",
                    "answer": "x_1 = 2, x_2 = 0.5"
                },
                {
                    "title": "Viyet teoremasini qo'llash",
                    "problem": "x^2 - 7x + 12 = 0 tenglamaning ildizlarini Viyet teoremasi yordamida toping.",
                    "step_by_step": "1) x_1 + x_2 = 7.\n2) x_1 * x_2 = 12.\n3) Ko'paytmasi 12 va yig'indisi 7 bo'lgan butun sonlar: 3 va 4.",
                    "answer": "x_1 = 3, x_2 = 4"
                }
            ],
            "exercise": "x^2 + 2x - 15 = 0 tenglamani yeching.",
            "exercise_solution": "D = 4 - 4*1*(-15) = 64. x_1 = (-2 + 8)/2 = 3, x_2 = (-2 - 8)/2 = -5.",
            "check_questions": [
                {
                    "question": "Agar kvadrat tenglamada D < 0 bo'lsa, nechta haqiqiy ildiz bor?",
                    "options": ["2 ta", "1 ta", "0 ta (haqiqiy ildiz yo'q)", "Cheksiz ko'p"],
                    "correct_index": 2,
                    "explanation": "Manfiy sondan haqiqiy sonlar to'plamida kvadrat ildiz chiqarib bo'lmaydi, shuning uchun haqiqiy ildiz mavjud emas."
                },
                {
                    "question": "x^2 - 9x + 20 = 0 tenglamaning ildizlari yig'indisi nechaga teng?",
                    "options": ["-9", "9", "20", "-20"],
                    "correct_index": 1,
                    "explanation": "Viyet teoremasiga ko'ra keltirilgan kvadrat tenglamada ildizlar yig'indisi x_1 + x_2 = -p = -(-9) = 9."
                },
                {
                    "question": "3x^2 - 12 = 0 chala kvadrat tenglamaning ildizlari qaysilar?",
                    "options": ["x = 2", "x = -2", "x = +-2", "x = 4"],
                    "correct_index": 2,
                    "explanation": "3x^2 = 12 => x^2 = 4 => x = +-2."
                }
            ],
            "tags": ["kvadrat tenglama", "diskriminant", "viyet teoremasi", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "mat-016",
            "slug": "kvadrat-funksiya-va-uning-grafigi",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Kvadrat funksiya, parabola grafigi va xossalari",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "y = ax^2 + bx + c parabolaning uchi koordinatalarini topish, simmetriya o'qini chizish va funksiyaning o'sish/kamayish oraliqlarini tahlil qilish.",
            "theory": "y = ax^2 + bx + c (a != 0) funksiya kvadrat funksiya deyiladi, uning grafigi parabola deb ataladi. Agar a > 0 bo'lsa, parabolaning tarmoqlari yuqoriga qaragan bo'ladi va funksiya eng kichik qiymatga ega bo'ladi. Agar a < 0 bo'lsa, tarmoqlar pastga qaraydi va funksiya eng katta qiymatga erishadi. Parabola uchining koordinatalari: x_0 = -b / (2a), y_0 = y(x_0) = -(b^2 - 4ac) / (4a). x = x_0 to'g'ri chizig'i parabolaning simmetriya o'qi hisoblanadi.",
            "examples": [
                {
                    "title": "Parabola uchini topish",
                    "problem": "y = x^2 - 4x + 3 parabolaning uchi koordinatalarini toping.",
                    "step_by_step": "1) a = 1, b = -4, c = 3.\n2) x_0 = -(-4) / (2 * 1) = 4 / 2 = 2.\n3) y_0 = 2^2 - 4 * 2 + 3 = 4 - 8 + 3 = -1.\n4) Parabola uchi: (2; -1).",
                    "answer": "(2; -1)"
                },
                {
                    "title": "Parabolaning koordinata o'qlari bilan kesishish nuqtalari",
                    "problem": "y = -x^2 + 4 funksiyaning Ox va Oy o'qlari bilan kesishish nuqtalarini toping.",
                    "step_by_step": "1) Oy o'qi bilan: x = 0 => y = 4, nuqta (0; 4).\n2) Ox o'qi bilan: y = 0 => -x^2 + 4 = 0 => x^2 = 4 => x = +-2, nuqtalar (-2; 0) va (2; 0).",
                    "answer": "Oy: (0; 4); Ox: (-2; 0) va (2; 0)"
                }
            ],
            "exercise": "y = 2x^2 - 8x + 5 parabolaning simmetriya o'qi tenglamasini yozing.",
            "exercise_solution": "x = -b / (2a) = -(-8) / (2 * 2) = 8 / 4 = 2. Simmetriya o'qi: x = 2.",
            "check_questions": [
                {
                    "question": "y = -3x^2 + 5x - 1 parabolaning tarmoqlari qaysi tomonga yo'nalgan?",
                    "options": ["Yuqoriga", "Pastga", "O'ngga", "Chapga"],
                    "correct_index": 1,
                    "explanation": "Bosh koeffitsiyent a = -3 < 0 bo'lgani sababli parabolaning tarmoqlari pastga qaragan bo'ladi."
                },
                {
                    "question": "Parabola uchi x_0 abssissasini topish formulasi qaysi?",
                    "options": ["-b / a", "-b / (2a)", "b / (2a)", "c / a"],
                    "correct_index": 1,
                    "explanation": "Parabola uchining abssissasi x_0 = -b / (2a) formula orqali aniqlanadi."
                },
                {
                    "question": "y = (x - 3)^2 + 4 parabolaning uchi qaysi nuqtada joylashgan?",
                    "options": ["(-3; 4)", "(3; 4)", "(3; -4)", "(-3; -4)"],
                    "correct_index": 1,
                    "explanation": "Kanonik ko'rinish y = a(x - x_0)^2 + y_0 dan ko'rinib turibdiki, uchining koordinatalari (3; 4) dir."
                }
            ],
            "tags": ["kvadrat funksiya", "parabola", "grafik", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-017",
            "slug": "arifmetik-progressiya-va-yigindi",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Arifmetik progressiya: umumiy had va dastlabki n ta had yig'indisi",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Arifmetik progressiya ayirmasini, n-hadini va dastlabki n ta had yig'indisini hisoblash formulalarini amaliy masalalarda qo'llash.",
            "theory": "Ikkinchi hadidan boshlab har bir hadi o'zidan oldingi hadga bir xil d sonini qo'shish orqali hosil bo'ladigan ketma-ketlik arifmetik progressiya deyiladi. d soni arifmetik progressiyaning ayirmasi deyiladi: d = a_(n+1) - a_n. n-had formulasi: a_n = a_1 + (n - 1)d. Xossasi: har bir had o'ziga qo'shni hadlarning o'rta arifmetigiga teng: a_n = (a_(n-1) + a_(n+1)) / 2. Dastlabki n ta had yig'indisi formulalari: S_n = (a_1 + a_n) * n / 2 yoki S_n = [2a_1 + (n - 1)d] * n / 2.",
            "examples": [
                {
                    "title": "n-hadni va yig'indini hisoblash",
                    "problem": "a_1 = 5, d = 3 bo'lgan arifmetik progressiyaning 15-hadini va dastlabki 15 ta hadi yig'indisini toping.",
                    "step_by_step": "1) a_15 = a_1 + 14d = 5 + 14 * 3 = 5 + 42 = 47.\n2) S_15 = (a_1 + a_15) * 15 / 2 = (5 + 47) * 15 / 2 = 52 * 15 / 2 = 26 * 15 = 390.",
                    "answer": "a_15 = 47, S_15 = 390"
                },
                {
                    "title": "Natural sonlar yig'indisi",
                    "problem": "1 dan 100 gacha bo'lgan barcha natural sonlar yig'indisini toping.",
                    "step_by_step": "a_1 = 1, a_100 = 100, n = 100.\nS_100 = (1 + 100) * 100 / 2 = 101 * 50 = 5050.",
                    "answer": "5050"
                }
            ],
            "exercise": "Arifmetik progressiyada a_3 = 11, a_7 = 23 bo'lsa, a_1 va d ni toping.",
            "exercise_solution": "a_7 - a_3 = 4d => 23 - 11 = 12 => 4d = 12 => d = 3. a_1 = a_3 - 2d = 11 - 6 = 5.",
            "check_questions": [
                {
                    "question": "Arifmetik progressiyaning n-had formulasi qaysi?",
                    "options": ["a_n = a_1 * d^(n-1)", "a_n = a_1 + (n - 1)d", "a_n = a_1 + n*d", "a_n = (a_1 + d)*n"],
                    "correct_index": 1,
                    "explanation": "Arifmetik progressiyaning n-hadi a_n = a_1 + (n - 1)d formula orqali topiladi."
                },
                {
                    "question": "3, 7, 11, ... arifmetik progressiyada d ayirma nimaga teng?",
                    "options": ["2", "3", "4", "5"],
                    "correct_index": 2,
                    "explanation": "d = 7 - 3 = 4."
                },
                {
                    "question": "Dastlabki 10 ta toq sonlar yig'indisi nechaga teng?",
                    "options": ["50", "90", "100", "120"],
                    "correct_index": 2,
                    "explanation": "Dastlabki n ta toq sonlar yig'indisi n^2 ga teng. 10^2 = 100."
                }
            ],
            "tags": ["arifmetik progressiya", "ketma-ketlik", "yig'indi", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-018",
            "slug": "geometrik-progressiya-va-cheksiz-kamayuvchi",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Geometrik progressiya va cheksiz kamayuvchi geometrik progressiya",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Geometrik progressiyaning maxraji q, n-hadi, dastlabki n ta had yig'indisi hamda |q| < 1 bo'lganda cheksiz yig'indini hisoblashni o'zlashtirish.",
            "theory": "Birinchi hadi noldan farqli bo'lib, ikkinchisidan boshlab har bir hadi o'zidan oldingi hadni noldan farqli o'zgarmas q soniga ko'paytirish orqali hosil bo'ladigan ketma-ketlik geometrik progressiya deyiladi. q soni geometrik progressiya maxraji deyiladi: q = b_(n+1) / b_n. n-had formulasi: b_n = b_1 * q^(n-1). Dastlabki n ta had yig'indisi (q != 1): S_n = b_1 * (q^n - 1) / (q - 1). Agar |q| < 1 bo'lsa, cheksiz kamayuvchi geometrik progressiya yig'indisi formulasi: S = b_1 / (1 - q).",
            "examples": [
                {
                    "title": "Geometrik progressiya hadlarini topish",
                    "problem": "b_1 = 3 va q = 2 bo'lsa, progressiyaning 6-hadini va dastlabki 6 ta hadi yig'indisini toping.",
                    "step_by_step": "1) b_6 = b_1 * q^5 = 3 * 2^5 = 3 * 32 = 96.\n2) S_6 = 3 * (2^6 - 1) / (2 - 1) = 3 * (64 - 1) / 1 = 3 * 63 = 189.",
                    "answer": "b_6 = 96, S_6 = 189"
                },
                {
                    "title": "Cheksiz kamayuvchi progressiya yig'indisi",
                    "problem": "1 + 1/2 + 1/4 + 1/8 + ... cheksiz qator yig'indisini hisoblang.",
                    "step_by_step": "1) b_1 = 1, q = 1/2 (|q| < 1).\n2) S = b_1 / (1 - q) = 1 / (1 - 1/2) = 1 / (1/2) = 2.",
                    "answer": "2"
                }
            ],
            "exercise": "Cheksiz kamayuvchi geometrik progressiyada b_1 = 9, q = 1/3 bo'lsa, uning yig'indisini toping.",
            "exercise_solution": "S = 9 / (1 - 1/3) = 9 / (2/3) = 9 * 3 / 2 = 13.5.",
            "check_questions": [
                {
                    "question": "Geometrik progressiyaning n-had formulasi qaysi?",
                    "options": ["b_n = b_1 * (n - 1)q", "b_n = b_1 * q^(n-1)", "b_n = b_1 + q^n", "b_n = (b_1 * q)^n"],
                    "correct_index": 1,
                    "explanation": "b_n = b_1 * q^(n-1) geometrik progressiyaning umumiy had formulasidir."
                },
                {
                    "question": "|q| < 1 bo'lganda cheksiz kamayuvchi geometrik progressiya yig'indisi qaysi formula bilan topiladi?",
                    "options": ["b_1 / (q - 1)", "b_1 / (1 - q)", "b_1 * (1 - q)", "(1 - q) / b_1"],
                    "correct_index": 1,
                    "explanation": "S = b_1 / (1 - q) cheksiz yig'indi formulasidir."
                },
                {
                    "question": "5, 10, 20, 40, ... progressiyaning maxraji nechaga teng?",
                    "options": ["2", "5", "10", "4"],
                    "correct_index": 0,
                    "explanation": "q = 10 / 5 = 2."
                }
            ],
            "tags": ["geometrik progressiya", "cheksiz yig'indi", "maxraj", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-019",
            "slug": "trigonometrik-funksiyalar-va-asosiy-ayniyatlar",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Trigonometrik funksiyalar va asosiy trigonometrik ayniyatlar",
            "grade_level": "10-sinf",
            "difficulty": "Murakkab",
            "objective": "Birlik aylanada sin, cos, tg, ctg ta'riflari, choraklardagi ishoralari va asosiy ayniyatlar yordamida ifodalarni soddalashtirish.",
            "theory": "Birlik aylanada (radiusi R=1 bo'lgan aylana) markaziy burchak alfa ga mos nuqtaning ordinatasi sin(alfa), abssissasi cos(alfa) deyiladi. tg(alfa) = sin(alfa)/cos(alfa) (cos != 0), ctg(alfa) = cos(alfa)/sin(alfa) (sin != 0). Asosiy trigonometrik ayniyat: sin^2(alfa) + cos^2(alfa) = 1. Bundan tashqari: tg(alfa) * ctg(alfa) = 1; 1 + tg^2(alfa) = 1 / cos^2(alfa); 1 + ctg^2(alfa) = 1 / sin^2(alfa). Ikkilangan burchak formulalari: sin(2alfa) = 2*sin(alfa)*cos(alfa); cos(2alfa) = cos^2(alfa) - sin^2(alfa).",
            "examples": [
                {
                    "title": "Asosiy ayniyat orqali hisoblash",
                    "problem": "Agar sin(alfa) = 3/5 va alfa II chorakda bo'lsa, cos(alfa) va tg(alfa) ni toping.",
                    "step_by_step": "1) cos^2(alfa) = 1 - sin^2(alfa) = 1 - (3/5)^2 = 1 - 9/25 = 16/25.\n2) II chorakda kosinus manfiy bo'ladi: cos(alfa) = -sqrt(16/25) = -4/5.\n3) tg(alfa) = sin(alfa) / cos(alfa) = (3/5) / (-4/5) = -3/4.",
                    "answer": "cos(alfa) = -4/5, tg(alfa) = -3/4"
                },
                {
                    "title": "Trigonometrik ifodani soddalashtirish",
                    "problem": "Soddalashtiring: (1 - cos^2(x)) / sin(2x)",
                    "step_by_step": "1) Surat: 1 - cos^2(x) = sin^2(x).\n2) Maxraj: sin(2x) = 2*sin(x)*cos(x).\n3) Nisbat: sin^2(x) / (2*sin(x)*cos(x)) = sin(x) / (2*cos(x)) = 0.5 * tg(x).",
                    "answer": "0.5 * tg(x)"
                }
            ],
            "exercise": "Soddalashtiring: (sin^2(a) + cos^2(a)) + tg(a) * ctg(a)",
            "exercise_solution": "1 + 1 = 2.",
            "check_questions": [
                {
                    "question": "sin^2(x) + cos^2(x) ifoda har doim nimaga teng?",
                    "options": ["0", "1", "2", "tg(x)"],
                    "correct_index": 1,
                    "explanation": "Asosiy pifagor trigonometrik ayniyatiga ko'ra yig'indi har doim 1 ga teng."
                },
                {
                    "question": "sin(90 gradus) qiymati nechaga teng?",
                    "options": ["0", "1/2", "sqrt(2)/2", "1"],
                    "correct_index": 3,
                    "explanation": "Birlik aylanada 90 gradusda ordinata maksimal 1 ga yetadi."
                },
                {
                    "question": "Qaysi chorakda ham sin(x), ham cos(x) manfiy bo'ladi?",
                    "options": ["I chorak", "II chorak", "III chorak", "IV chorak"],
                    "correct_index": 2,
                    "explanation": "III chorakda x < 0 va y < 0 bo'lgani uchun cos(x) < 0 va sin(x) < 0 bo'ladi."
                }
            ],
            "tags": ["trigonometriya", "sinus", "kosinus", "ayniyatlar", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "mat-020",
            "slug": "korsatkichli-va-logarifmik-tenglamalar",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Ko'rsatkichli va logarifmik tenglamalar",
            "grade_level": "10-sinf",
            "difficulty": "Murakkab",
            "objective": "Ko'rsatkichli tenglamalarni bir xil asosga keltirish, logarifm ta'rifi va xossalarini (yig'indi, ayirma, daraja) qo'llab logarifmik tenglamalarni yechish.",
            "theory": "a^x = b (a > 0, a != 1) ko'rinishidagi tenglama ko'rsatkichli tenglama deyiladi. Agar b > 0 bo'lsa, x = log_a(b). Logarifm ta'rifi: log_a(b) bu b sonini hosil qilish uchun a ni ko'tarish kerak bo'lgan daraja ko'rsatkichidir (a^log_a(b) = b). Logarifmning asosiy xossalari: 1) log_a(x * y) = log_a(x) + log_a(y); 2) log_a(x / y) = log_a(x) - log_a(y); 3) log_a(x^p) = p * log_a(x); 4) Asosni almashtirish: log_a(b) = log_c(b) / log_c(a). Muhim: logarifm ostidagi ifoda qat'iy musbat bo'lishi shart (x > 0).",
            "examples": [
                {
                    "title": "Ko'rsatkichli tenglamani yechish",
                    "problem": "4^(x + 1) + 2^(2x) = 320 tenglamani yeching.",
                    "step_by_step": "1) 4^(x + 1) = 4 * 4^x = 4 * (2^2)^x = 4 * (2^(2x)).\n2) 4 * 2^(2x) + 2^(2x) = 320.\n3) 5 * 2^(2x) = 320 => 2^(2x) = 64.\n4) 64 = 2^6, demak 2x = 6 => x = 3.",
                    "answer": "x = 3"
                },
                {
                    "title": "Logarifmik tenglamani yechish",
                    "problem": "log_2(x - 3) + log_2(x + 1) = 5 tenglamani yeching.",
                    "step_by_step": "1) Aniqlanish sohasi: x - 3 > 0 va x + 1 > 0 => x > 3.\n2) Logarifmlar yig'indisi xossasi: log_2((x - 3)(x + 1)) = 5.\n3) (x - 3)(x + 1) = 2^5 = 32.\n4) x^2 - 2x - 3 = 32 => x^2 - 2x - 35 = 0.\n5) (x - 7)(x + 5) = 0 => x_1 = 7, x_2 = -5.\n6) x > 3 shartiga faqat x = 7 mos keladi.",
                    "answer": "x = 7"
                }
            ],
            "exercise": "Yeching: log_3(2x - 5) = 2",
            "exercise_solution": "2x - 5 = 3^2 = 9 => 2x = 14 => x = 7 (x=7 da 2*7-5=9 > 0).",
            "check_questions": [
                {
                    "question": "log_2(32) qiymati nechaga teng?",
                    "options": ["3", "4", "5", "6"],
                    "correct_index": 2,
                    "explanation": "2^5 = 32 bo'lgani sababli log_2(32) = 5."
                },
                {
                    "question": "log_a(1) har doim nimaga teng (a > 0, a != 1)?",
                    "options": ["1", "0", "a", "Mavjud emas"],
                    "correct_index": 1,
                    "explanation": "Har qanday sonning 0-darajasi 1 bo'lgani uchun log_a(1) = 0."
                },
                {
                    "question": "3^x = 1/27 tenglamaning yechimi qaysi?",
                    "options": ["-3", "3", "-9", "1/3"],
                    "correct_index": 0,
                    "explanation": "1/27 = 3^(-3), demak x = -3."
                }
            ],
            "tags": ["ko'rsatkichli tenglama", "logarifm", "algebra", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "mat-021",
            "slug": "funksiyaning-hosilasi-va-mexanik-manosi",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Hosilaning ta'rifi, asosiy qoidalari va geometrik ma'nosi",
            "grade_level": "11-sinf",
            "difficulty": "Murakkab",
            "objective": "Funksiya hosilasi tushunchasi, darajali va ko'rsatkichli funksiyalar hosilasini topish qoidalari va urinma tenglamasini tuzish.",
            "theory": "Funksiya orttirmasining argument orttirmasiga nisbatining argument orttirmasi nolga intilgandagi limiti funksiyaning berilgan nuqtadagi hosilasi deyiladi: f'(x) = lim(delta_x -> 0) [f(x + delta_x) - f(x)] / delta_x. Hosilaning geometrik ma'nosi: f'(x_0) funksiya grafigiga x_0 nuqtada o'tkazilgan urinmaning burchak koeffitsiyentiga teng (k = tg(alpha) = f'(x_0)). Mexanik ma'nosi: harakat qonuni s(t) bo'lsa, tezlik v(t) = s'(t) va tezlanish a(t) = v'(t) = s''(t). Asosiy hosilalar: (c)' = 0, (x^n)' = n*x^(n-1), (sin x)' = cos x, (cos x)' = -sin x, (e^x)' = e^x, (ln x)' = 1/x.",
            "examples": [
                {
                    "title": "Funksiya hosilasini topish",
                    "problem": "f(x) = 3x^4 - 5x^2 + 7x - 9 funksiyaning hosilasini toping.",
                    "step_by_step": "1) (3x^4)' = 3 * 4x^3 = 12x^3.\n2) (-5x^2)' = -5 * 2x = -10x.\n3) (7x)' = 7.\n4) (-9)' = 0.\n5) Natija: f'(x) = 12x^3 - 10x + 7.",
                    "answer": "12x^3 - 10x + 7"
                },
                {
                    "title": "Urinmaning burchak koeffitsiyenti",
                    "problem": "y = x^2 - 3x + 2 parabolaga x_0 = 3 nuqtada o'tkazilgan urinmaning burchak koeffitsiyentini toping.",
                    "step_by_step": "1) y' = (x^2 - 3x + 2)' = 2x - 3.\n2) k = y'(3) = 2 * 3 - 3 = 6 - 3 = 3.",
                    "answer": "k = 3"
                }
            ],
            "exercise": "f(x) = 2x^3 + 4x funksiyaning x_0 = 1 nuqtadagi hosilasini hisoblang.",
            "exercise_solution": "f'(x) = 6x^2 + 4. f'(1) = 6*(1)^2 + 4 = 10.",
            "check_questions": [
                {
                    "question": "(x^5)' hosila nechaga teng?",
                    "options": ["5x^4", "4x^5", "5x^6", "x^4"],
                    "correct_index": 0,
                    "explanation": "(x^n)' = n*x^(n-1) qoidasiga ko'ra (x^5)' = 5x^4."
                },
                {
                    "question": "O'zgarmas sonning hosilasi nimaga teng?",
                    "options": ["1", "0", "O'ziga", "Cheksiz"],
                    "correct_index": 1,
                    "explanation": "O'zgarmas son o'zgarmaydi (orttirmasi 0), shuning uchun uning hosilasi har doim 0 ga teng."
                },
                {
                    "question": "Harakat qonuni s(t) bo'lsa, tezlanish nimaga teng?",
                    "options": ["s(t)", "s'(t)", "s''(t)", "s(t)/t"],
                    "correct_index": 2,
                    "explanation": "Tezlanish tezlikning hosilasi yoki yo'lning ikkinchi tartibli hosilasiga teng: a(t) = s''(t)."
                }
            ],
            "tags": ["hosila", "differensial", "matematik analiz", "11-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "mat-022",
            "slug": "boshlangich-funksiya-va-aniq-integral",
            "subject_id": "sub-02",
            "subject_name": "Algebra",
            "title": "Boshlang'ich funksiya, aniq integral va Nyuton-Leybnits formulasi",
            "grade_level": "11-sinf",
            "difficulty": "Murakkab",
            "objective": "Boshlang'ich funksiyalar jadvalidan foydalanish, aniq integralni Nyuton-Leybnits formulasi orqali hisoblash va egri chiziqli trapetsiya yuzini topish.",
            "theory": "Agar berilgan oraliqda F'(x) = f(x) bo'lsa, F(x) funksiya f(x) ning boshlang'ich funksiyasi deyiladi. f(x) ning barcha boshlang'ich funksiyalari to'plami F(x) + C ko'rinishida yoziladi va noaniq integral deyiladi. Nyuton-Leybnits formulasi aniq integralni hisoblashning asosiy vositasidir: int_a^b f(x)dx = F(b) - F(a). Geometrik ma'nosi: f(x) >= 0 bo'lganda int_a^b f(x)dx y = f(x) funksiya grafigi, Ox o'qi va x=a, x=b to'g'ri chiziqlari bilan chegaralangan egri chiziqli trapetsiyaning yuziga teng bo'ladi.",
            "examples": [
                {
                    "title": "Aniq integralni hisoblash",
                    "problem": "Hisoblang: int_1^3 (3x^2 + 2x) dx",
                    "step_by_step": "1) Boshlang'ich funksiyani topamiz: F(x) = x^3 + x^2.\n2) Nyuton-Leybnits formulasi: F(3) - F(1).\n3) F(3) = 3^3 + 3^2 = 27 + 9 = 36.\n4) F(1) = 1^3 + 1^2 = 1 + 1 = 2.\n5) Natija: 36 - 2 = 34.",
                    "answer": "34"
                },
                {
                    "title": "Yuza hisoblash",
                    "problem": "y = x^2 parabolaning 0 dan 2 gacha bo'lgan qismi ostidagi soha yuzini toping.",
                    "step_by_step": "S = int_0^2 x^2 dx = [x^3 / 3]_0^2 = 2^3 / 3 - 0 = 8/3 kv.birlik.",
                    "answer": "8/3 (yoki 2.67)"
                }
            ],
            "exercise": "Hisoblang: int_0^1 (4x^3 + 1) dx",
            "exercise_solution": "F(x) = x^4 + x. F(1) - F(0) = (1 + 1) - 0 = 2.",
            "check_questions": [
                {
                    "question": "f(x) = x^3 funksiyaning boshlang'ich funksiyasi qaysi?",
                    "options": ["3x^2 + C", "x^4 / 4 + C", "x^4 + C", "4x^3 + C"],
                    "correct_index": 1,
                    "explanation": "(x^4 / 4)' = 4x^3 / 4 = x^3. Demak, x^4 / 4 + C."
                },
                {
                    "question": "Nyuton-Leybnits formulasi qanday yoziladi?",
                    "options": ["F(a) - F(b)", "F(b) - F(a)", "F'(b) - F'(a)", "F(b) * F(a)"],
                    "correct_index": 1,
                    "explanation": "Aniq integral qiymati yuqori chegara va quyi chegaradagi boshlang'ich funksiya qiymatlari ayirmasiga teng: F(b) - F(a)."
                },
                {
                    "question": "int_a^a f(x)dx integrali nimaga teng?",
                    "options": ["0", "1", "f(a)", "2f(a)"],
                    "correct_index": 0,
                    "explanation": "Integrallash chegaralari ustma-ust tushganda oraliq kengligi nolga teng bo'lib, integral qiymati 0 bo'ladi."
                }
            ],
            "tags": ["integral", "boshlang'ich funksiya", "yuza", "11-sinf"],
            "duration_minutes": 35
        },

        # GEOMETRIYA (8)
        {
            "id": "mat-023",
            "slug": "burchaklar-va-uchburchaklar-tengligi-belgilari",
            "subject_id": "sub-03",
            "subject_name": "Geometriya",
            "title": "Burchaklar turlari va uchburchaklar tengligining uchta alomati",
            "grade_level": "7-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Qo'shni va vertikal burchaklar xossalarini, uchburchaklar tengligining TTB, BTB, TTT alomatlarini isbot va masalalarda qo'llash.",
            "theory": "Tekislikda bir nuqtadan chiquvchi ikki nur hosil qilgan shakl burchak deyiladi. O'tkir (<90°), to'g'ri (90°), o'tmas (>90° va <180°) va yoyiq (180°) burchaklar mavjud. Bir tomoni umumiy, qolgan ikki tomoni to'ldiruvchi nurlar bo'lgan burchaklar qo'shni burchaklar deyiladi (yig'indisi 180°). Vertikal burchaklar o'zaro tengdir. Uchburchaklar tengligining alomatlari: 1) TTB (Tomon-Burchak-Tomon): Ikki tomoni va ular orasidagi burchagi teng bo'lsa; 2) BTB (Burchak-Tomon-Burchak): Bir tomoni va unga yopishgan ikki burchagi teng bo'lsa; 3) TTT (Tomon-Tomon-Tomon): Uchta tomoni mos ravishda teng bo'lsa.",
            "examples": [
                {
                    "title": "Qo'shni burchaklarni topish",
                    "problem": "Qo'shni burchaklardan biri ikkinchisidan 40 gradusga katta. Shu burchaklarni toping.",
                    "step_by_step": "1) Kichik burchak x bo'lsin. Katta burchak: x + 40.\n2) Qo'shni burchaklar yig'indisi 180° ga teng: x + (x + 40) = 180.\n3) 2x = 140 => x = 70°.\n4) Katta burchak: 70 + 40 = 110°.",
                    "answer": "70° va 110°"
                },
                {
                    "title": "Tenglik alomatini qo'llash",
                    "problem": "ABC uchburchakda AB = AC va AD bissektrisa. ABD va ACD uchburchaklarning tengligini asoslang.",
                    "step_by_step": "1) AB = AC (shartga ko'ra);\n2) AD - umumiy tomon;\n3) <BAD = <CAD (AD bissektrisa bo'lgani uchun burchakni teng ikkiga bo'ladi).\nDemak, TTB alomatiga ko'ra delta_ABD = delta_ACD.",
                    "answer": "TTB alomati bo'yicha teng"
                }
            ],
            "exercise": "Vertikal burchaklarning yig'indisi 130 gradusga teng. Har bir burchak necha gradus?",
            "exercise_solution": "Vertikal burchaklar teng bo'lgani uchun: 130 / 2 = 65°.",
            "check_questions": [
                {
                    "question": "Qo'shni burchaklarning yig'indisi necha gradusga teng?",
                    "options": ["90°", "180°", "270°", "360°"],
                    "correct_index": 1,
                    "explanation": "Qo'shni burchaklar yig'ilib yoyiq burchak hosil qiladi, ya'ni 180°."
                },
                {
                    "question": "Uchburchaklar tengligining uchinchi alomati qanday nomlanadi?",
                    "options": ["Tomon-Tomon-Tomon (TTT)", "Burchak-Burchak-Burchak (BBB)", "Tomon-Burchak-Tomon (TTB)", "Gipotenuza-Katet"],
                    "correct_index": 0,
                    "explanation": "Agar bir uchburchakning uch tomoni ikkinchi uchburchakning mos uch tomoniga teng bo'lsa, bu uchburchaklar tengdir (TTT)."
                },
                {
                    "question": "Burchakni teng ikkiga bo'luvchi nur nima deyiladi?",
                    "options": ["Mediana", "Balandlik", "Bissektrisa", "O'rta chiziq"],
                    "correct_index": 2,
                    "explanation": "Burchak uchidan chiqib uni teng ikkita burchakka ajratuvchi nur bissektrisa deyiladi."
                }
            ],
            "tags": ["burchaklar", "uchburchaklar tengligi", "planimetriya", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-024",
            "slug": "uchburchak-ichki-burchaklari-va-tengyonli-uchburchak",
            "subject_id": "sub-03",
            "subject_name": "Geometriya",
            "title": "Uchburchak ichki burchaklari yig'indisi va tengyonli uchburchak",
            "grade_level": "7-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Uchburchak ichki burchaklari yig'indisi 180° ekanligini isbotlash, tashqi burchak xossasi va tengyonli uchburchak xossalaridan foydalanish.",
            "theory": "Teorema: Har qanday uchburchak ichki burchaklarining yig'indisi 180° ga teng: alpha + beta + gamma = 180°. Uchburchakning tashqi burchagi unga qo'shni bo'lmagan ikkita ichki burchakning yig'indisiga teng. Tengyonli uchburchak - ikkita tomoni teng bo'lgan uchburchak. Uning asosidagi burchaklari teng bo'ladi. Tengyonli uchburchak asosiga tushirilgan bissektrisa bir vaqtning o'zida ham mediana, ham balandlik bo'ladi. Barcha tomonlari teng bo'lgan uchburchak tengtomonli (muntazam) uchburchak deyiladi va uning har bir burchagi 60° dir.",
            "examples": [
                {
                    "title": "Ichki burchaklarni topish",
                    "problem": "Uchburchakning burchaklari 2:3:4 nisbatda. Shu burchaklarni toping.",
                    "step_by_step": "1) Burchaklar: 2x, 3x, 4x.\n2) Yig'indisi: 2x + 3x + 4x = 180° => 9x = 180° => x = 20°.\n3) Burchaklar: 2*20 = 40°, 3*20 = 60°, 4*20 = 80°.",
                    "answer": "40°, 60°, 80°"
                },
                {
                    "title": "Tengyonli uchburchak burchaklari",
                    "problem": "Tengyonli uchburchakning uchidagi burchagi 70°. Uning asosidagi burchaklarini toping.",
                    "step_by_step": "1) Asosidagi burchaklar teng bo'lib, har biri alpha bo'lsin.\n2) 70° + 2*alpha = 180°.\n3) 2*alpha = 110° => alpha = 55°.",
                    "answer": "55° va 55°"
                }
            ],
            "exercise": "To'g'ri burchakli tengyonli uchburchakning o'tkir burchaklari necha gradusdan?",
            "exercise_solution": "(180° - 90°) / 2 = 90° / 2 = 45°.",
            "check_questions": [
                {
                    "question": "Uchburchakning ichki burchaklari yig'indisi nechaga teng?",
                    "options": ["90°", "180°", "360°", "270°"],
                    "correct_index": 1,
                    "explanation": "Evklid geometriyasida har qanday uchburchak ichki burchaklari yig'indisi 180° bo'ladi."
                },
                {
                    "question": "Muntazam uchburchakning har bir burchagi necha gradus?",
                    "options": ["45°", "60°", "90°", "120°"],
                    "correct_index": 1,
                    "explanation": "Barcha 3 burchagi teng: 180° / 3 = 60°."
                },
                {
                    "question": "Uchburchakning tashqi burchagi nimaga teng?",
                    "options": ["Unga qo'shni burchakka", "Unga qo'shni bo'lmagan ikki ichki burchak yig'indisiga", "180° ga", "90° ga"],
                    "correct_index": 1,
                    "explanation": "Teoremaga ko'ra tashqi burchak o'ziga qo'shni bo'lmagan ikkita ichki burchak yig'indisiga teng."
                }
            ],
            "tags": ["uchburchak", "burchaklar", "tengyonli uchburchak", "7-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "mat-025",
            "slug": "pifagor-teoremasi-va-togri-burchakli-uchburchak",
            "subject_id": "sub-03",
            "subject_name": "Geometriya",
            "title": "Pifagor teoremasi va to'g'ri burchakli uchburchak metrik munosabatlari",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "To'g'ri burchakli uchburchakda katetlar va gipotenuza orasidagi munosabatlarni, balandlikning proeksiyalarga bog'liqligini va Pifagor sonlarini bilish.",
            "theory": "To'g'ri burchakli uchburchakda to'g'ri burchak qarshisidagi tomon gipotenuza (c), qolgan ikki tomon katetlar (a va b) deyiladi. Pifagor teoremasi: Gipotenuza kvadratining qiymati katetlar kvadratlarining yig'indisiga teng: c^2 = a^2 + b^2. Pifagor sonlari: a^2 + b^2 = c^2 shartni qanoatlantiruvchi butun sonlar (masalan: 3, 4, 5; 5, 12, 13; 8, 15, 17; 7, 24, 25). To'g'ri burchak uchidan tushirilgan balandlik h_c uchun: h_c^2 = a_c * b_c, a^2 = c * a_c, b^2 = c * b_c (bu yerda a_c va b_c katetlarning gipotenuzadagi proeksiyalari).",
            "examples": [
                {
                    "title": "Gipotenuzani hisoblash",
                    "problem": "Katetlari 6 sm va 8 sm bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping.",
                    "step_by_step": "1) Pifagor teoremasi: c^2 = a^2 + b^2.\n2) c^2 = 6^2 + 8^2 = 36 + 64 = 100.\n3) c = sqrt(100) = 10 sm.",
                    "answer": "10 sm"
                },
                {
                    "title": "Noma'lum katetni topish",
                    "problem": "Gipotenuzasi 13 sm, bir kateti 5 sm bo'lsa, ikkinchi katetni toping.",
                    "step_by_step": "1) b^2 = c^2 - a^2.\n2) b^2 = 13^2 - 5^2 = 169 - 25 = 144.\n3) b = sqrt(144) = 12 sm.",
                    "answer": "12 sm"
                }
            ],
            "exercise": "Katetlari 9 sm va 12 sm bo'lgan uchburchak gipotenuzasiga tushirilgan balandlikni hisoblang.",
            "exercise_solution": "c = sqrt(9^2 + 12^2) = 15 sm. S = (a * b)/2 = (c * h)/2 => h = (a * b) / c = (9 * 12) / 15 = 108 / 15 = 7.2 sm.",
            "check_questions": [
                {
                    "question": "Pifagor teoremasi qanday shakllar uchun o'rinli?",
                    "options": ["Barcha uchburchaklar", "Faqat to'g'ri burchakli uchburchaklar", "Faqat tengtomonli uchburchaklar", "Ixtiyoriy ko'pburchaklar"],
                    "correct_index": 1,
                    "explanation": "Pifagor teoremasi faqat to'g'ri burchakli uchburchaklar uchun to'g'ridan-to'g'ri o'rinlidir."
                },
                {
                    "question": "Tomonlari 3, 4, 5 bo'lgan uchburchak nima deyiladi?",
                    "options": ["Misr uchburchagi", "Arximed uchburchagi", "Evklid uchburchagi", "Nyuton uchburchagi"],
                    "correct_index": 0,
                    "explanation": "Tomonlari 3, 4, 5 bo'lgan to'g'ri burchakli uchburchak qadimdan Misr uchburchagi deb ataladi."
                },
                {
                    "question": "Gipotenuzasi 10 sm bo'lgan to'g'ri burchakli uchburchak to'g'ri burchagidan tushirilgan mediana uzunligi qancha?",
                    "options": ["10 sm", "5 sm", "2.5 sm", "7.5 sm"],
                    "correct_index": 1,
                    "explanation": "To'g'ri burchak uchidan tushirilgan mediana gipotenuzaning yarmiga teng: m = c / 2 = 10 / 2 = 5 sm."
                }
            ],
            "tags": ["pifagor teoremasi", "gipotenuza", "katet", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-026",
            "slug": "tortburchaklar-parallelogramm-romb-trapetsiya",
            "subject_id": "sub-03",
            "subject_name": "Geometriya",
            "title": "To'rtburchaklar: parallelogramm, to'g'ri to'rtburchak, romb va trapetsiya",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "To'rtburchaklarning xossalari, diogonallari, burchaklari va yuzalarini hisoblash formulalarini o'zlashtirish.",
            "theory": "Parallelogramm - qarama-qarshi tomonlari juft-jufti bilan parallel bo'lgan to'rtburchak. Xossalari: qarama-qarshi tomonlari va burchaklari teng, diagonallari kesishish nuqtasida teng ikkiga bo'linadi. Yuza: S = a * h_a. To'g'ri to'rtburchak - barcha burchaklari 90° bo'lgan parallelogramm (diagonallari teng). Romb - barcha tomonlari teng parallelogramm (diagonallari o'zaro perpendikulyar va burchak bissektrisasi bo'ladi, S = (d_1 * d_2)/2). Trapetsiya - faqat ikki tomoni parallel bo'lgan to'rtburchak. O'rta chizig'i m = (a + b)/2, yuzi S = [(a + b)/2] * h = m * h.",
            "examples": [
                {
                    "title": "Romb yuzini diagonallari orqali topish",
                    "problem": "Diagonallari 14 sm va 18 sm bo'lgan rombning yuzini toping.",
                    "step_by_step": "1) Romb yuzi formulasi: S = (d_1 * d_2) / 2.\n2) S = (14 * 18) / 2 = 7 * 18 = 126 sm^2.",
                    "answer": "126 sm^2"
                },
                {
                    "title": "Trapetsiya yuzini hisoblash",
                    "problem": "Asoslari 8 sm va 14 sm, balandligi 6 sm bo'lgan trapetsiyaning yuzini toping.",
                    "step_by_step": "1) O'rta chiziq: (8 + 14) / 2 = 22 / 2 = 11 sm.\n2) S = 11 * 6 = 66 sm^2.",
                    "answer": "66 sm^2"
                }
            ],
            "exercise": "Parallelogrammning tomoni 12 sm, unga tushirilgan balandlik 5 sm. Uning yuzini toping.",
            "exercise_solution": "S = a * h = 12 * 5 = 60 sm^2.",
            "check_questions": [
                {
                    "question": "Diagonallari o'zaro perpendikulyar bo'lgan parallelogramm qaysi?",
                    "options": ["To'g'ri to'rtburchak", "Romb", "Trapetsiya", "Ixtiyoriy to'rtburchak"],
                    "correct_index": 1,
                    "explanation": "Rombning asosiy xossalaridan biri uning diagonallari o'zaro to'g'ri burchak ostida kesishishidir."
                },
                {
                    "question": "Trapetsiyaning o'rta chizig'i qanday topiladi?",
                    "options": ["(a + b) / 2", "a * b", "sqrt(a * b)", "a + b"],
                    "correct_index": 0,
                    "explanation": "Trapetsiyaning o'rta chizig'i asoslari yig'indisining yarmiga teng."
                },
                {
                    "question": "To'g'ri to'rtburchakning diagonallari haqida qaysi fikr to'g'ri?",
                    "options": ["Doimo perpendikulyar", "O'zaro teng", "Burchak bissektrisasi bo'ladi", "Turli uzunlikda bo'ladi"],
                    "correct_index": 1,
                    "explanation": "To'g'ri to'rtburchakning diagonallari uzunligi jihatidan o'zaro tengdir."
                }
            ],
            "tags": ["parallelogramm", "romb", "trapetsiya", "to'rtburchaklar", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-027",
            "slug": "aylana-va-doira-markaziy-va-ichki-chizilgan-burchaklar",
            "subject_id": "sub-03",
            "subject_name": "Geometriya",
            "title": "Aylana, doira, markaziy va aylanaga ichki chizilgan burchaklar",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Aylana uzunligi, doira yuzi, markaziy va ichki chizilgan burchaklar orasidagi bog'liqlikni hisoblash.",
            "theory": "Tekislikda berilgan nuqtadan (markazdan) bir xil R masofada joylashgan barcha nuqtalar to'plami aylana deyiladi. Aylana bilan chegaralangan tekislik qismi doira deyiladi. Aylana uzunligi: C = 2 * pi * R. Doira yuzi: S = pi * R^2. Uchi aylananing markazida bo'lgan burchak markaziy burchak deyiladi va u tiralgan yoyining gradus o'lchoviga teng. Uchi aylanada yotib, tomonlari aylanani kesib o'tuvchi burchak ichki chizilgan burchak deyiladi. Muhim teorema: Ichki chizilgan burchak o'zi tiralgan yoyning (yoki markaziy burchakning) yarmiga teng. Diametrga tiralgan ichki chizilgan burchak har doim 90° ga teng.",
            "examples": [
                {
                    "title": "Ichki chizilgan burchakni topish",
                    "problem": "Aylananing AB yoyiga tiralgan markaziy burchak 80° ga teng. Shu yoyga tiralgan ichki chizilgan burchakni toping.",
                    "step_by_step": "1) Ichki chizilgan burchak markaziy burchakning yarmiga teng.\n2) alpha = 80° / 2 = 40°.",
                    "answer": "40°"
                },
                {
                    "title": "Doira yuzini hisoblash",
                    "problem": "Radiusi 6 sm bo'lgan doiraning yuzini toping (pi = 3.14).",
                    "step_by_step": "1) S = pi * R^2.\n2) S = 3.14 * 6^2 = 3.14 * 36 = 113.04 sm^2.",
                    "answer": "113.04 sm^2"
                }
            ],
            "exercise": "Diametrga tiralgan ichki chizilgan burchak necha gradusga teng?",
            "exercise_solution": "Diametr 180° li yarim aylanani hosil qiladi, unga tiralgan burchak: 180° / 2 = 90°.",
            "check_questions": [
                {
                    "question": "Aylana uzunligi formulasi qaysi?",
                    "options": ["pi * R^2", "2 * pi * R", "4/3 * pi * R^3", "2 * pi * R^2"],
                    "correct_index": 1,
                    "explanation": "C = 2 * pi * R aylana uzunligini hisoblash formulasidir."
                },
                {
                    "question": "Aylananing bir xil yoyiga tiralgan barcha ichki chizilgan burchaklar qanday bo'ladi?",
                    "options": ["O'zaro teng", "Har xil", "Yig'indisi 180°", "To'g'ri burchak"],
                    "correct_index": 0,
                    "explanation": "Bir xil yoyga tiralgan barcha ichki chizilgan burchaklar bitta yoyning yarmiga teng bo'lgani uchun o'zaro tengdir."
                },
                {
                    "question": "Radiusi 5 sm bo'lgan aylananing eng katta vatari (diametri) necha sm?",
                    "options": ["5 sm", "10 sm", "15 sm", "25 sm"],
                    "correct_index": 1,
                    "explanation": "Aylananing eng katta vatari diametr bo'lib, d = 2R = 2 * 5 = 10 sm."
                }
            ],
            "tags": ["aylana", "doira", "markaziy burchak", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-028",
            "slug": "tekis-shakllar-yuzalari-va-geron-formulasi",
            "subject_id": "sub-03",
            "subject_name": "Geometriya",
            "title": "Tekis shakllar yuzalari va Geron formulasi",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Uchburchak yuzini turli usullarda (Geron formulasi, ikki tomon va burchak sinusi, ichki/tashqi chizilgan aylanalar radiusi) hisoblashni o'rganish.",
            "theory": "Uchburchak yuzini hisoblashning asosiy formulalari: 1) Asos va balandlik orqali: S = (a * h_a)/2; 2) Ikki tomon va burchak orqali: S = (1/2) * a * b * sin(gamma); 3) Geron formulasi (uch tomon ma'lum bo'lganda): p = (a + b + c)/2 (yarim perimetr), S = sqrt(p * (p - a) * (p - b) * (p - c)); 4) Ichki chizilgan aylana radiusi r orqali: S = p * r; 5) Tashqi chizilgan aylana radiusi R orqali: S = (a * b * c) / (4 * R).",
            "examples": [
                {
                    "title": "Geron formulasi bo'yicha yuzani topish",
                    "problem": "Tomonlari 13 sm, 14 sm va 15 sm bo'lgan uchburchakning yuzini toping.",
                    "step_by_step": "1) Yarim perimetr: p = (13 + 14 + 15) / 2 = 42 / 2 = 21 sm.\n2) p - a = 21 - 13 = 8; p - b = 21 - 14 = 7; p - c = 21 - 15 = 6.\n3) S = sqrt(21 * 8 * 7 * 6).\n4) 21 * 7 = 147 = 3 * 49; 8 * 6 = 48 = 3 * 16.\n5) S = sqrt(49 * 16 * 9) = 7 * 4 * 3 = 84 sm^2.",
                    "answer": "84 sm^2"
                },
                {
                    "title": "Sinus orqali yuzani hisoblash",
                    "problem": "Tomonlari 8 sm va 10 sm bo'lib, ular orasidagi burchak 30° bo'lgan uchburchak yuzini toping.",
                    "step_by_step": "1) S = 0.5 * a * b * sin(30°).\n2) sin(30°) = 0.5.\n3) S = 0.5 * 8 * 10 * 0.5 = 20 sm^2.",
                    "answer": "20 sm^2"
                }
            ],
            "exercise": "Tomonlari 5 sm, 5 sm va 6 sm bo'lgan tengyonli uchburchak yuzini Geron formulasi bilan hisoblang.",
            "exercise_solution": "p = (5+5+6)/2 = 8. S = sqrt(8 * (8-5) * (8-5) * (8-6)) = sqrt(8 * 3 * 3 * 2) = sqrt(144) = 12 sm^2.",
            "check_questions": [
                {
                    "question": "Geron formulasida p harfi nimani bildiradi?",
                    "options": ["Perimetrni", "Yarim perimetrni", "Balandlikni", "Radiusni"],
                    "correct_index": 1,
                    "explanation": "p = (a + b + c) / 2 bu yarim perimetrdir."
                },
                {
                    "question": "Uchburchak yuzi va ichki chizilgan aylana radiusi bog'lanishi qaysi?",
                    "options": ["S = p * r", "S = 2 * p * r", "S = p / r", "S = r^2 * p"],
                    "correct_index": 0,
                    "explanation": "S = p * r (bu yerda p - yarim perimetr, r - ichki chizilgan aylana radiusi)."
                },
                {
                    "question": "Tomoni a bo'lgan muntazam uchburchak yuzi formulasi qaysi?",
                    "options": ["(a^2 * sqrt(3)) / 4", "(a^2 * sqrt(3)) / 2", "a^2 / 2", "a^2 * sqrt(3)"],
                    "correct_index": 0,
                    "explanation": "S = (1/2)*a*a*sin(60°) = (a^2 * sqrt(3)) / 4."
                }
            ],
            "tags": ["yuza", "geron formulasi", "uchburchak", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-029",
            "slug": "vektorlar-va-ular-ustida-amallar",
            "subject_id": "sub-03",
            "subject_name": "Geometriya",
            "title": "Vektorlar, koordinatalari va skalyar ko'paytmasi",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Vektor tushunchasi, yo'nalishi, uzunligi, vektorlarni qo'shish (uchburchak va parallelogramm qoidalari) va skalyar ko'paytmasini hisoblash.",
            "theory": "Son qiymati (moduli) va yo'nalishi bilan aniqlanadigan kattalik vektor deyiladi. Agar vektorning boshi A(x_1, y_1) va oxiri B(x_2, y_2) bo'lsa, uning koordinatalari: a = (x_2 - x_1; y_2 - y_1). Vektor uzunligi (moduli): |a| = sqrt(x^2 + y^2). Vektorlarni qo'shganda ularning mos koordinatalari qo'shiladi: a + b = (x_1 + x_2; y_1 + y_2). Ikki vektorning skalyar ko'paytmasi deb ularning modullari bilan ular orasidagi burchak kosinusining ko'paytmasiga aytiladi: a * b = |a| * |b| * cos(phi) = x_1*x_2 + y_1*y_2. Ikki vektor perpendikulyar bo'lishining zaruriy va yetarli sharti ularning skalyar ko'paytmasi nolga teng bo'lishidir (a * b = 0).",
            "examples": [
                {
                    "title": "Vektor uzunligini topish",
                    "problem": "a(3; -4) vektorining uzunligini hisoblang.",
                    "step_by_step": "1) |a| = sqrt(x^2 + y^2).\n2) |a| = sqrt(3^2 + (-4)^2) = sqrt(9 + 16) = sqrt(25) = 5.",
                    "answer": "5"
                },
                {
                    "title": "Skalyar ko'paytma va perpendikulyarlik",
                    "problem": "a(2; 5) va b(10; k) vektorlar o'zaro perpendikulyar bo'lsa, k ni toping.",
                    "step_by_step": "1) Perpendikulyarlik sharti: x_1 * x_2 + y_1 * y_2 = 0.\n2) 2 * 10 + 5 * k = 0.\n3) 20 + 5k = 0 => 5k = -20 => k = -4.",
                    "answer": "k = -4"
                }
            ],
            "exercise": "a(1; 2) va b(3; 4) vektorlarning skalyar ko'paytmasini toping.",
            "exercise_solution": "a * b = 1 * 3 + 2 * 4 = 3 + 8 = 11.",
            "check_questions": [
                {
                    "question": "Ikki vektor qachon perpendikulyar bo'ladi?",
                    "options": ["Skalyar ko'paytmasi 0 bo'lganda", "Uzunliklari teng bo'lganda", "Skalyar ko'paytmasi 1 bo'lganda", "Yo'nalishlari bir xil bo'lganda"],
                    "correct_index": 0,
                    "explanation": "cos(90°) = 0 bo'lgani sababli perpendikulyar vektorlarning skalyar ko'paytmasi 0 ga teng."
                },
                {
                    "question": "a(6; 8) vektorining uzunligi qancha?",
                    "options": ["10", "14", "48", "7"],
                    "correct_index": 0,
                    "explanation": "sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10."
                },
                {
                    "question": "Nol vektorning uzunligi nimaga teng?",
                    "options": ["0", "1", "-1", "Mavjud emas"],
                    "correct_index": 0,
                    "explanation": "Nol vektorning boshi va oxiri ustma-ust tushadi, uzunligi 0 ga teng."
                }
            ],
            "tags": ["vektorlar", "skalyar ko'paytma", "uzunlik", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "mat-030",
            "slug": "stereometriya-fazoviy-jismlar-va-hajmlar",
            "subject_id": "sub-03",
            "subject_name": "Geometriya",
            "title": "Stereometriya: prizma, piramida, silindr, konus va shar",
            "grade_level": "10-11-sinf",
            "difficulty": "Murakkab",
            "objective": "Fazoviy jismlarning sirt yuzalari va hajmlari formulalarini bilish hamda amaliy ko'p qirrali va aylanma jismlar masalalarini yechish.",
            "theory": "Stereometriya fazoviy shakllarning xossalarini o'rganadi. Ko'pqirralilar: Prizma hajmi: V = S_asos * h. To'g'ri burchakli parallelepiped: V = a * b * c, to'la sirti S_t = 2(ab + bc + ac). Piramida hajmi: V = (1/3) * S_asos * h. Aylanma jismlar: Silindr hajmi: V = pi * R^2 * h, yon sirti S_yon = 2 * pi * R * h. Konus hajmi: V = (1/3) * pi * R^2 * h, yon sirti S_yon = pi * R * l (bu yerda l - yasovchi). Shar hajmi: V = (4/3) * pi * R^3, sfera yuzi: S = 4 * pi * R^2.",
            "examples": [
                {
                    "title": "Silindr hajmini hisoblash",
                    "problem": "Asosining radiusi 4 sm, balandligi 10 sm bo'lgan silindrning hajmini toping (pi = 3).",
                    "step_by_step": "1) V = pi * R^2 * h.\n2) V = 3 * 4^2 * 10 = 3 * 16 * 10 = 480 sm^3.",
                    "answer": "480 sm^3"
                },
                {
                    "title": "Shar hajmi va sirtini topish",
                    "problem": "Radiusi 3 sm bo'lgan sharning hajmi va sfera sirtining yuzini hisoblang (pi = 3.14).",
                    "step_by_step": "1) V = (4/3) * pi * R^3 = (4/3) * 3.14 * 27 = 4 * 3.14 * 9 = 113.04 sm^3.\n2) S = 4 * pi * R^2 = 4 * 3.14 * 9 = 113.04 sm^2.",
                    "answer": "Hajmi: 113.04 sm^3, Sirti: 113.04 sm^2"
                }
            ],
            "exercise": "Asosi tomoni 6 sm bo'lgan kvadrat, balandligi 10 sm bo'lgan to'g'ri to'rtburchakli piramida hajmini toping.",
            "exercise_solution": "S_asos = 6^2 = 36 sm^2. V = (1/3) * S_asos * h = (1/3) * 36 * 10 = 120 sm^3.",
            "check_questions": [
                {
                    "question": "Piramida hajmi formulasi qaysi?",
                    "options": ["S_asos * h", "(1/2) * S_asos * h", "(1/3) * S_asos * h", "(4/3) * S_asos * h"],
                    "correct_index": 2,
                    "explanation": "Piramida hajmi uning asosi yuzi bilan balandligi ko'paytmasining uchdan biriga teng."
                },
                {
                    "question": "Sfera sirti yuzi qaysi formula bilan hisoblanadi?",
                    "options": ["4 * pi * R^2", "pi * R^2", "(4/3) * pi * R^3", "2 * pi * R^2"],
                    "correct_index": 0,
                    "explanation": "Sfera yuzi 4 * pi * R^2 formula orqali topiladi."
                },
                {
                    "question": "Konusning yasovchisi (l), balandligi (h) va radiusi (R) orasidagi munosabat qanday?",
                    "options": ["l^2 = h^2 + R^2", "l = h + R", "h^2 = l^2 + R^2", "R^2 = l^2 + h^2"],
                    "correct_index": 0,
                    "explanation": "Balandlik, radius va yasovchi to'g'ri burchakli uchburchak hosil qiladi, Pifagor teoremasiga ko'ra: l^2 = h^2 + R^2."
                }
            ],
            "tags": ["stereometriya", "fazoviy jismlar", "hajm", "11-sinf"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_math_materials()
    print(f"Generated {len(mats)} Math/Algebra/Geometry materials.")
