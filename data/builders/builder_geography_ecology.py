# -*- coding: utf-8 -*-
"""
Builder for Geografiya va Ekologiya (12 materials: geo-001 to geo-012)
- sub-12: Geografiya (7: geo-001 to geo-007)
- sub-13: Ekologiya (5: geo-008 to geo-012)
"""

def get_geography_ecology_materials():
    materials = [
        # GEOGRAFIYA (7)
        {
            "id": "geo-001",
            "slug": "globus-geografik-xaritalar-va-masshtab",
            "subject_id": "sub-12",
            "subject_name": "Geografiya",
            "title": "Globus, geografik xaritalar va masshtab tushunchasi",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Globus va xarita farqi, geografik koordinatalar (kenglik va uzoqlik) hamda masshtab bo'yicha masofalarni hisoblash.",
            "theory": "Globus — Yer sharining eng aniq, xatosiz kichraytirilgan uch o'lchamli modelidir. Geografik xarita — Yer yuzasining yoki uning bir qismining tekis qog'ozda shartli belgilar va masshtab yordamida kichraytirib tasvirlanishidir. Masshtab joydagi haqiqiy masofa xaritada necha marta kichraytirilganini ko'rsatuvchi kasr sondir. Masshtab turlari: sonli (masalan, 1 : 100 000), nomli (1 sm da 1 km) va chiziqli. Geografik to'r parallel (ekvatorga parallel chiziqlar — kenglik) va meridian (qutblarni tutashtiruvchi chiziqlar — uzoqlik) chiziqlaridan iborat. Boshlang'ich meridian — Grinvich meridiani (0°).",
            "examples": [
                {
                    "title": "Masshtab bo'yicha masofani topish",
                    "problem": "Masshtabi 1 : 2 000 000 bo'lgan xaritada Toshkent va Samarqand orasidagi masofa 15 sm ga teng. Haqiqiy masofani toping.",
                    "step_by_step": "1) 1 : 2 000 000 sonli masshtabni nomli masshtabga o'tkazamiz: 1 sm da 20 km.\n2) Haqiqiy masofa = 15 sm * 20 km = 300 km.",
                    "answer": "300 km"
                },
                {
                    "title": "Geografik koordinatalarni aniqlash",
                    "problem": "Toshkent shahrining geografik koordinatalari qanday?",
                    "step_by_step": "Toshkent shahri taxminan 41° shimoliy kenglik va 69° sharqiy uzoqlikda joylashgan (41° shim.k., 69° sharq.u.).",
                    "answer": "41° sh.k., 69° sh.u."
                }
            ],
            "exercise": "Joydagi 45 km masofa xaritada 9 sm qilib chizilgan. Xaritaning sonli masshtabini toping.",
            "exercise_solution": "1 sm ga 45 / 9 = 5 km to'g'ri keladi. 5 km = 500 000 sm. Masshtab: 1 : 500 000.",
            "check_questions": [
                {
                    "question": "Yerning eng aniq modeli qaysi?",
                    "options": ["Xarita", "Globus", "Topografik reja", "Aerofotosurat"],
                    "correct_index": 1,
                    "explanation": "Globus sharsimon shaklga ega bo'lib, shakl va masofalarni buzmasdan ko'rsatadi."
                },
                {
                    "question": "0 gradusli kenglik chizig'i nima deb ataladi?",
                    "options": ["Grinvich meridiani", "Ekvator", "Shimoliy qutb", "Tropik"],
                    "correct_index": 1,
                    "explanation": "Ekvator Yer sharini Shimoliy va Janubiy yarimsharlarga bo'luvchi 0° kenglik chizig'idir."
                },
                {
                    "question": "1 : 50 000 masshtabda 1 sm qog'ozda yer yuzidagi qancha masofaga to'g'ri keladi?",
                    "options": ["50 m", "500 m", "5 km", "50 km"],
                    "correct_index": 1,
                    "explanation": "50 000 sm = 500 metr."
                }
            ],
            "tags": ["geografiya", "globus", "xarita", "masshtab", "koordinata", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "geo-002",
            "slug": "litosfera-va-yer-relefi",
            "subject_id": "sub-12",
            "subject_name": "Geografiya",
            "title": "Litosfera: Yerning ichki tuzilishi, plitalar tektonikasi va relef",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Yer qobig'i, mantiya, yadro, litosfera plitalarining harakati, zilzilalar, vulqonlar va tog' hosil bo'lish jarayonlarini o'rganish.",
            "theory": "Yer sharining qattiq tosh qobig'i litosfera deyiladi. Yerning ichki tuzilishi: 1) Yer qobig'i (materikda 30-70 km, okeanda 5-10 km); 2) Mantiya (yuqori mantiya va astenosfera, 2900 km gacha); 3) Yadro (tashqi suyuq yadro va ichki qattiq temir-nikel yadro). Plitalar tektonikasi nazariyasiga (A. Vegener) ko'ra litosfera yirik tektonik plitalardan iborat bo'lib, astenosfera ustida siljiydi. Plitalar to'qnashgan joylarda tog'lar (burmali tog'lar: Himoloy, Alp, Tyan-Shan), zilzilalar va vulqonlar vujudga keladi; ajralgan joylarda (rift vodiylari) esa o'rta okean tizmalari hosil bo'ladi. Relef shakllari: tekisliklar (pasttekislik, qirlar, yassitog'liklar) va tog'lar (past, o'rta, baland tog'lar).",
            "examples": [
                {
                    "title": "Yer qobig'i turlari",
                    "problem": "Materik va okean yer qobig'ining asosiy farqi nimada?",
                    "step_by_step": "Materik qobig'i 3 qavatdan iborat (cho'kindi, granit, bazalt) va qalinligi 30-70 km; Okean qobig'ida granit qavati yo'q (faqat cho'kindi va bazalt) va qalinligi ancha yupqa (5-10 km).",
                    "answer": "Okean qobig'ida granit qavati bo'lmaydi"
                },
                {
                    "title": "Eng baland cho'qqi",
                    "problem": "Yer yuzidagi eng baland tog' cho'qqisi qaysi va uning balandligi qancha?",
                    "step_by_step": "Himoloy tog'laridagi Jomolungma (Everest) cho'qqisi, balandligi 8848 metr.",
                    "answer": "Jomolungma (Everest) — 8848 m"
                }
            ],
            "exercise": "Zilzila kuchi va tebranishini qayd etuvchi asbob nima deb ataladi va zilzila kuchi qaysi shkalada o'lchanadi?",
            "exercise_solution": "Asbob seysmograf deyiladi; kuchi Rixter shkalasi (magnituda bo'yicha) va 12 balli MSK-64 shkalasida o'lchanadi.",
            "check_questions": [
                {
                    "question": "Yerning markazida qaysi qatlam joylashgan?",
                    "options": ["Yer qobig'i", "Mantiya", "Yadro", "Litosfera"],
                    "correct_index": 2,
                    "explanation": "Yerning markazida o'ta yuqori harorat va bosim ostidagi temir-nikelli yadro joylashgan."
                },
                {
                    "question": "Tinch okeani atrofidagi eng faol zilzila va vulqonlar zonasi nima deb ataladi?",
                    "options": ["Alp-Himoloy kamari", "Tinch okeani 'Olovli halqasi'", "O'rta Atlantika tizmasi", "Rift zonasi"],
                    "correct_index": 1,
                    "explanation": "Dunyo vulqonlarining aksariyati Tinch okeani 'Olovli halqasi' bo'ylab joylashgan."
                },
                {
                    "question": "Balandligi dengiz sathidan 200 metrgacha bo'lgan tekisliklar nima deyiladi?",
                    "options": ["Qirlar", "Yassitog'liklar", "Pasttekisliklar", "Botiqlar"],
                    "correct_index": 2,
                    "explanation": "0 dan 200 metrgacha balandlikka ega tekisliklar pasttekislik deb yuritiladi."
                }
            ],
            "tags": ["litosfera", "yer tuzilishi", "plitalar tektonikasi", "relef", "zilzila", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "geo-003",
            "slug": "gidrosfera-dunyo-okeani-va-quruqlik-suvlari",
            "subject_id": "sub-12",
            "subject_name": "Geografiya",
            "title": "Gidrosfera: Dunyo okeani qismlari, oqimlar va quruqlik suvlari",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Gidrosfera tarkibi, Dunyo okeanining 4 ta okeani, okean oqimlari (Golfstrim), daryolar, ko'llar va yerosti suvlari gidrologiyasini o'rganish.",
            "theory": "Yerning suv qobig'i gidrosfera deyiladi (Yer yuzasining 71% qismini egallaydi). 96.5% suv Dunyo okeanida to'plangan. 4 ta asosiy okean: Tinch okeani (eng katta va eng chuqur — Mariana botig'i, 11 022 m), Atlantika okeani, Hind okeani va Shimoliy Muz okeani. Dunyo okeani suvi sho'r bo'lib, o'rtacha sho'rligi 35 promille (har 1 litr suvda 35 g tuz). Eng sho'r dengiz — Qizil dengiz (41 promille). Okean oqimlari — iliq (Golfstrim) va sovuq (Peru, Labrador) oqimlar bo'lib, iqlimga kuchli ta'sir qiladi. Quruqlik suvlari: daryolar (boshlanishi — boshlanma, quyilishi — quyilish joyi), ko'llar (oqadigan va oqmas), muzliklar (chuchuk suvning eng katta zaxirasi) va yerosti suvlari.",
            "examples": [
                {
                    "title": "Dunyoning eng katta daryosi va ko'li",
                    "problem": "Dunyodagi eng sersuv daryo va eng katta ko'lni ko'rsating.",
                    "step_by_step": "Eng sersuv daryo — Janubiy Amerikadagi Amazonka daryosi; Eng katta maydonga ega ko'l — Kaspiy dengizi (ko'li); Eng chuqur chuchuk suvli ko'l — Baykal (1642 m).",
                    "answer": "Amazonka (daryo), Kaspiy (ko'l)"
                },
                {
                    "title": "Okean suvi sho'rligi",
                    "problem": "100 litr okean suvida o'rtacha necha kg tuz erigan bo'ladi?",
                    "step_by_step": "Sho'rlik 35 promille (1 litrda 35 g). 100 litrda: 100 * 35 g = 3500 g = 3.5 kg tuz.",
                    "answer": "3.5 kg tuz"
                }
            ],
            "exercise": "Golfstrim iliq oqimi Yevropa iqlimiga qanday ta'sir ko'rsatadi?",
            "exercise_solution": "Golfstrim oqimi Shimoli-G'arbiy Yevropaga iliq va sernam havo massalarini olib kelib, qish faslini ancha yumshatadi va dengiz portlarining muzlamasligini ta'minlaydi.",
            "check_questions": [
                {
                    "question": "Dunyo okeanining eng chuqur nuqtasi qaysi?",
                    "options": ["Yava botig'i", "Mariana botig'i (11 022 m)", "Puerto-Riko", "Grenlandiya dengizi"],
                    "correct_index": 1,
                    "explanation": "Tinch okeanidagi Mariana botig'i yer yuzidagi eng chuqur joydir (11 022 m)."
                },
                {
                    "question": "Yer yuzidagi chuchuk suvning eng katta qismi qayerda saqlanadi?",
                    "options": ["Daryolarda", "Ko'llarda", "Antarktida va Grenlandiya muzliklarida", "Atmosferada"],
                    "correct_index": 2,
                    "explanation": "Chuchuk suv zaxirasining qariyb 70% i qutb muzliklarida to'plangan."
                },
                {
                    "question": "Dunyodagi eng chuqur chuchuk suvli ko'l qaysi?",
                    "options": ["Kaspiy", "Viktoriya", "Baykal", "Orol"],
                    "correct_index": 2,
                    "explanation": "Rossiyadagi Baykal ko'li 1642 metr chuqurlik bilan dunyodagi eng chuqur ko'ldir."
                }
            ],
            "tags": ["gidrosfera", "dunyo okeani", "mariana", "amazonka", "daryolar", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "geo-004",
            "slug": "atmosfera-va-iqlim-hosil-qiluvchi-omillar",
            "subject_id": "sub-12",
            "subject_name": "Geografiya",
            "title": "Atmosfera qatlamlari, havo massalari, siklon va antisiklonlar",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Troposfera, stratosfera, atmosfera bosimi, doimiy shamollar (passatlar, mussonlar) va iqlim mintaqalarini tushunish.",
            "theory": "Yerning gazsimon havo qobig'i atmosfera deyiladi. Tarkibi: 78% azot, 21% kislorod, 0.9% argon, 0.04% karbonat angidrid. Qatlamlari: Troposfera (10-18 km gacha — barcha ob-havo hodisalari, bulutlar, yog'inlar ro'y beradi, har 100 metr balandlikda harorat 0.6 °C ga pasayadi); Stratosfera (ozon qatlami 20-25 km da joylashgan bo'lib ultrabinafsha nurlarni yutadi); Mezosfera, Termosfera (qutb yog'dusi) va Ekzosfera. Atmosfera bosimi balandlikka ko'tarilgan sari kamayadi (har 10.5 m da 1 mm sim.ust. ga). Shamol — havoning yuqori bosimli sohadan past bosimli sohaga gorizontal harakati. Doimiy shamollar: Passatlar (tropiklardan ekvatorga) va G'arbiy shamollar. Siklon — markazida past bosim bo'lgan havo uyurmasi (sernam, bulutli ob-havo); Antisiklon — markazida yuqori bosim bo'lgan havo uyurmasi (ochiq, quruq, kamshamol ob-havo).",
            "examples": [
                {
                    "title": "Balandlik bo'yicha haroratni hisoblash",
                    "problem": "Tog' etagida (dengiz sathida) havo harorati +24 °C bo'lsa, 3000 metr balandlikdagi cho'qqida harorat necha gradus bo'ladi?",
                    "step_by_step": "1) Har 1000 metrda harorat 6 °C ga pasayadi.\n2) 3000 m da harorat pasayishi: 3 * 6 °C = 18 °C.\n3) Cho'qqidagi harorat: +24 °C - 18 °C = +6 °C.",
                    "answer": "+6 °C"
                },
                {
                    "title": "Atmosfera bosimini hisoblash",
                    "problem": "Etagida bosim 760 mm sim.ust. bo'lgan tog'ning 1050 m balandligidagi bosimini toping.",
                    "step_by_step": "Har 10.5 metrda bosim 1 mm ga kamayadi. 1050 / 10.5 = 100 mm ga kamayadi. Bosim: 760 - 100 = 660 mm sim.ust.",
                    "answer": "660 mm simob ustuni"
                }
            ],
            "exercise": "Musson shamollarining yozgi va qishki yo'nalishlarini tushuntiring.",
            "exercise_solution": "Yozda quruqlik qizib past bosim hosil bo'ladi, musson okeandan quruqlikka esib kuchli yomg'irlar olib keladi; qishda esa sovuq quruqlikdan iliqroq okeanga qarab esadi.",
            "check_questions": [
                {
                    "question": "Atmosferaning barcha ob-havo hodisalari (bulut, yomg'ir, momaqaldiroq) sodir bo'ladigan pastki qatlami qaysi?",
                    "options": ["Stratosfera", "Troposfera", "Mezosfera", "Ionosfera"],
                    "correct_index": 1,
                    "explanation": "Troposferada atmosfera massasining 80% dan ortig'i va deyarli barcha suv bug'i to'plangan."
                },
                {
                    "question": "Ozon qatlami qaysi atmosferik qavatda joylashgan va uning vazifasi nima?",
                    "options": ["Troposferada, nafas olish uchun", "Stratosferada, zararli ultrabinafsha nurlardan himoyalash", "Termosferada, haroratni saqlash", "Ekzosferada"],
                    "correct_index": 1,
                    "explanation": "Ozon ekrani stratosferada (20-25 km) joylashgan va tiriklikni halokatli nurlardan asraydi."
                },
                {
                    "question": "Siklon markazida qanday atmosfera bosimi bo'ladi?",
                    "options": ["Yuqori bosim", "Past bosim", "Normal o'zgarmas bosim", "Bosim bo'lmaydi"],
                    "correct_index": 1,
                    "explanation": "Siklon markazida past bosim bo'lib, shamol chekkadan markazga qarab aylanib esadi."
                }
            ],
            "tags": ["atmosfera", "iqlim", "troposfera", "bosim", "shamol", "siklon", "7-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "geo-005",
            "slug": "yevrosiyo-materigi-tabiiy-geografiyasi",
            "subject_id": "sub-12",
            "subject_name": "Geografiya",
            "title": "Yevrosiyo materigi: tabiiy zonalari, relefi va ichki suvlari",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Yer sharidagi eng yirik materik — Yevrosiyoning geografik o'rni, ekstremal nuqtalari, relef tuzilishi va tabiiy zonalari xilma-xilligini o'rganish.",
            "theory": "Yevrosiyo — Yer sharidagi eng katta materik (maydoni 54 mln km^2, quruqlikning 1/3 qismi). Ikki dunyo qismidan (Yevropa va Osiyo) iborat bo'lib, Ural tog'lari, Emba daryosi, Kaspiy dengizi va Kuma-Manich botig'i orqali ajraladi. Ekstremal nuqtalar: Shimolda Chelyuskin burni, Janubda Piay burni, G'arbda Roka burni, Sharqda Dejnyov burni. Relefi: Eng baland cho'qqi — Everest (8848 m), eng chuqur quruqlik botiqligi — O'lik dengiz (-405 m). Yevrosiyoda barcha iqlim mintaqalari va tabiiy zonalar (arktik cho'llar, tundra, tayga, aralash o'rmonlar, dasht, cho'llar, savannalar va doimiy yashil ekvatorial o'rmonlar) mavjud. Eng yirik daryolari: Yanszi (Osiyodagi eng uzun), Volga (Yevropadagi eng uzun), Ob, Yenisey, Lena, Amur, Gang va Hind.",
            "examples": [
                {
                    "title": "Materikning ichki suvlari rekordi",
                    "problem": "Yevrosiyoda joylashgan va dunyoda eng katta maydonga ega ko'lni ko'rsating.",
                    "step_by_step": "Kaspiy dengizi — maydoni 371 000 km^2 bo'lib, okean bilan to'g'ridan-to'g'ri tutashmagan dunyodagi eng katta ko'ldir.",
                    "answer": "Kaspiy ko'li (dengizi)"
                },
                {
                    "title": "Dunyo qismlari chegarasi",
                    "problem": "Yevropa va Osiyo qit'alarini ajratib turuvchi asosiy tog' tizmasi qaysi?",
                    "step_by_step": "Shimoldan janubga cho'zilgan qadimgi Ural tog'lari Yevropa va Osiyo orasidagi tabiiy chegara hisoblanadi.",
                    "answer": "Ural tog'lari"
                }
            ],
            "exercise": "Yevrosiyo tayga zonasida asosan qanday o'simliklar ustunlik qiladi?",
            "exercise_solution": "Tayga zonasi ignabargli daraxtlar (qarag'ay, qoraqarag'ay, tilog'och, oqqarag'ay) o'rmonlaridan iborat.",
            "check_questions": [
                {
                    "question": "Yevrosiyo materigi maydoni qancha?",
                    "options": ["30.3 mln km^2", "54 mln km^2", "17.8 mln km^2", "14 mln km^2"],
                    "correct_index": 1,
                    "explanation": "Yevrosiyo 54 million kvadrat kilometr maydoni bilan eng ulkan materikdir."
                },
                {
                    "question": "Yevropadagi eng uzun daryo qaysi?",
                    "options": ["Dunay", "Volga", "Reyn", "Dneprl"],
                    "correct_index": 1,
                    "explanation": "Volga daryosi (3530 km) Yevropaning eng uzun daryosi hisoblanadi."
                },
                {
                    "question": "Yer yuzidagi eng sovuq quruqlik nuqtalaridan biri — Oymyakon qaysi hududda joylashgan?",
                    "options": ["Skandinaviyada", "Sharqiy Sibirda (Yoqutiston)", "Tibet platosida", "Uralda"],
                    "correct_index": 1,
                    "explanation": "Shimoliy yarimsharning sovuqlik qutbi Oymyakon bo'lib, harorat -71 °C gacha tushgan."
                }
            ],
            "tags": ["yevrosiyo", "materiklar", "geografiya", "everest", "tayga", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "geo-006",
            "slug": "ozbekistonning-tabiiy-geografik-orni-va-boyliklari",
            "subject_id": "sub-12",
            "subject_name": "Geografiya",
            "title": "O'zbekistonning tabiiy geografiyasi, relefi, iqlimi va foydali qazilmalari",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "O'zbekiston hududi (448.9 ming km^2), chegaralari, relef xususiyatlari (tekislik va tog'lar), keskin kontinental iqlimi va mineral xomashyo boyliklarini o'rganish.",
            "theory": "O'zbekiston Markaziy Osiyoning markazida joylashgan bo'lib, maydoni 448.9 ming km^2 ni tashkil etadi. Dengizga chiqish uchun kamida 2 ta davlat hududidan o'tish talab qilinadigan (double-landlocked) dunyodagi 2 ta davlatdan biri (Lixtenshteyn bilan birga). Relefi: Hududning 78-80% qismi tekisliklardan (Qizilqum cho'li, Ustyurt platosi, Qarshi cho'li), 20-22% qismi tog'lar va tog'oldi botiqlaridan (Tyan-Shan va Hisor-Olay tog' tizmalari) iborat. Eng baland nuqtasi — Hazrati Sulton cho'qqisi (4643 m, Hisor tizmasida); eng past nuqtasi — Mingbuloq botig'i (-12.8 m, Qizilqumda). Iqlimi: keskin kontinental, quruq, quyoshli (yiliga 2800-3000 soat quyoshli kunlar). Asosiy daryolari: Amudaryo va Sirdaryo. Foydali qazilmalari: oltin (Muruntov koni — dunyodagi eng yirik ochiq oltin koni), tabiiy gaz (Gazli, Sho'rtan, Muborak), rangli metallar (Olmaliq — mis, molibden), uran (Navoiy).",
            "examples": [
                {
                    "title": "O'zbekistonning ekstremal nuqtalari",
                    "problem": "O'zbekistonning eng baland va eng past tabiiy geografik nuqtalarini ayting.",
                    "step_by_step": "Eng baland nuqta — Hisor tizmasidagi Hazrati Sulton cho'qqisi (4643 m);\nEng past nuqta — Qizilqumdagi Mingbuloq botig'i (dengiz sathidan -12.8 m pastda).",
                    "answer": "Hazrati Sulton (4643 m) va Mingbuloq (-12.8 m)"
                },
                {
                    "title": "Muruntov oltin koni",
                    "problem": "Nima sababdan Navoiy viloyatidagi Muruntov koni jahon miqyosida mashhur?",
                    "step_by_step": "Muruntov — dunyodagi eng yirik ochiq usulda qazib olinadigan oltin koni bo'lib, yiliga o'nlab tonna eng yuqori sifatli (999.9 proba) oltin yetkazib beradi.",
                    "answer": "Dunyodagi eng yirik ochiq oltin koni bo'lgani uchun"
                }
            ],
            "exercise": "O'zbekiston chegaradosh bo'lgan 5 ta davlatni sanang.",
            "exercise_solution": "Qozog'iston (shimol va shimoli-g'arbda), Qirg'iziston (shimoli-sharqda), Tojikiston (sharq va janubi-sharqda), Afg'oniston (janubda), Turkmaniston (janubi-g'arbda).",
            "check_questions": [
                {
                    "question": "O'zbekiston Respublikasi hududi qancha maydonni egallaydi?",
                    "options": ["448.9 ming km^2", "300 ming km^2", "550 ming km^2", "1.2 mln km^2"],
                    "correct_index": 0,
                    "explanation": "O'zbekiston maydoni 448 978 km^2 (taxminan 448.9 ming km^2) ga teng."
                },
                {
                    "question": "O'zbekistonning eng baland cho'qqisi qaysi va uning balandligi qancha?",
                    "options": ["Katta Chimyon (3309 m)", "Hazrati Sulton (4643 m)", "Adelung (4301 m)", "Gissar (3800 m)"],
                    "correct_index": 1,
                    "explanation": "Hisor tizmasidagi Hazrati Sulton cho'qqisi 4643 metr balandlik bilan eng yuqori nuqtadir."
                },
                {
                    "question": "O'zbekiston iqlimi qanday xarakterga ega?",
                    "options": ["Dengiz iqlimi", "Keskin kontinental va quruq", "Ekvatorial", "Mo''tadil sernam"],
                    "correct_index": 1,
                    "explanation": "Okeanlardan uzoqda joylashganligi sababli yozi issiq va quruq, qishi sovuq keskin kontinental iqlim hukmron."
                }
            ],
            "tags": ["o'zbekiston geografiyasi", "relef", "qizilqum", "muruntov", "hazrati sulton", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "geo-007",
            "slug": "ozbekiston-aholisi-va-iqtisodiy-tarmoqlari",
            "subject_id": "sub-12",
            "subject_name": "Geografiya",
            "title": "O'zbekiston aholisi, demografiyasi va iqtisodiy geografiyasi",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Aholi soni, zichligi, demografik o'sish, urbanizatsiya, sanoat tarmoqlari (energetika, avtomobilsozlik, to'qimachilik) va iqtisodiy rayonlarni tahlil qilish.",
            "theory": "O'zbekiston — Markaziy Osiyodagi aholisi eng ko'p davlat (37 milliondan ortiq kishi). Demografik jihatdan yuqori tabiiy o'sishga va yoshlar salmog'ining kattaligiga ega (o'rtacha yosh ~29 yosh). Aholi zichligi viloyatlar bo'yicha notekis: eng yuqori zichlik Farg'ona vodiysida (Andijon viloyatida 750+ kishi/km^2), eng kam zichlik Navoiy viloyati va Qoraqalpog'istonda (10-15 kishi/km^2). Iqtisodiyot tarmoqlari: 1) Energetika — issiqlik elektr stansiyalari (Sirdaryo IES, Yangi Toshkent IES, Tolimarjon IES) va gidroelektr stansiyalar (Chorvoq GES) hamda rivojlanayotgan quyosh va shamol stansiyalari; 2) Mashinasozlik — Asaka va Pitnakdagi avtomobil zavodlari, Samarqanddagi SamAuto avtobus va yuk mashinalari; 3) Kimyo sanoati — mineral o'g'itlar (Navoiyazot, Farg'onaazot, Maksam-Chirchiq); 4) To'qimachilik va yengil sanoat — ip-kalava, paxta-to'qima klasterlari.",
            "examples": [
                {
                    "title": "Aholi zichligini hisoblash",
                    "problem": "Hudud maydoni 4200 km^2 va aholisi 3 360 000 kishi bo'lgan Andijon viloyatining o'rtacha aholi zichligini toping.",
                    "step_by_step": "1) Zichlik = Aholi soni / Maydon.\n2) Zichlik = 3 360 000 / 4200 = 800 kishi/km^2.",
                    "answer": "800 kishi/km^2"
                },
                {
                    "title": "Muqobil energetika loyihalari",
                    "problem": "O'zbekistonda nima sababdan quyosh va shamol elektr stansiyalarini qurish tezlashmoqda?",
                    "step_by_step": "Yiliga 300 kundan ortiq quyoshli kunlar borligi, tabiiy gaz sarfini kamaytirish va ekologiyaga zararli chiqindilarni kamaytirish (yashil energiya o'tishi).",
                    "answer": "Quyosh resurslari boyligi va gazni tejash maqsadida"
                }
            ],
            "exercise": "O'zbekistonning eng yirik avtomobil ishlab chiqarish korxonasi qaysi shaharda joylashgan?",
            "exercise_solution": "Andijon viloyatining Asaka shahrida (UzAuto Motors zavodi) joylashgan.",
            "check_questions": [
                {
                    "question": "O'zbekiston aholisi soni qancha kishidan oshdi?",
                    "options": ["25 million", "31 million", "37 million", "45 million"],
                    "correct_index": 2,
                    "explanation": "O'zbekiston aholisi 37 million kishidan oshib, Markaziy Osiyoda 1-o'rinda turadi."
                },
                {
                    "question": "O'zbekistonda aholi zichligi eng yuqori bo'lgan viloyat qaysi?",
                    "options": ["Navoiy viloyati", "Qashqadaryo viloyati", "Andijon viloyati", "Buxoro viloyati"],
                    "correct_index": 2,
                    "explanation": "Andijon viloyatida 1 km^2 ga 750-800 nafardan ortiq aholi to'g'ri kelib, respublikada eng zich joylashgan."
                },
                {
                    "question": "O'zbekistondagi eng yirik issiqlik elektr stansiyasi (IES) qaysi?",
                    "options": ["Chorvoq GES", "Sirdaryo IES (Shirin shahri)", "Toshkent IES", "Tuyamo'yin"],
                    "correct_index": 1,
                    "explanation": "Sirdaryo IES 3000 MVt dan ortiq quvvati bilan mintaqadagi eng yirik elektr stansiyalaridan biridir."
                }
            ],
            "tags": ["aholi", "demografiya", "o'zbekiston iqtisodiyoti", "sanoat", "asaka", "9-sinf"],
            "duration_minutes": 35
        },

        # EKOLOGIYA (5)
        {
            "id": "geo-008",
            "slug": "ekologiya-faniga-kirish-va-ekologik-omillar",
            "subject_id": "sub-13",
            "subject_name": "Ekologiya",
            "title": "Ekologiya tushunchasi va ekologik omillar: abiotik, biotik va antropogen",
            "grade_level": "9-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Ekologiya predmeti (Ernst Gekkel), ekologik omillar tasnifi, optimum qonuni va cheklovchi (limitlovchi) omillar qoidasini bilish.",
            "theory": "Ekologiya (yunoncha 'oikos' — uy, vatan va 'logos' — ta'limot) — organizmlarning o'zaro hamda atrof-muhit bilan munosabatlarini o'rganuvchi fandir. Bu atamani 1866-yilda nemis biologi Ernst Gekkel fanga kiritgan. Ekologik omillar 3 guruhga bo'linadi: 1) Abiotik omillar — jonsiz tabiat ta'siri (harorat, yorug'lik, namlik, bosim, shamol, tuproq tarkibi); 2) Biotik omillar — tirik mavjudotlarning bir-biriga o'zaro ta'siri (simbioz, yirtqichlik, raqobat, parazitizm, kommensalizm); 3) Antropogen omillar — inson faoliyatining tabiatga to'g'ridan-to'g'ri yoki bilvosita ta'siri. Optimum qonuni: Har bir omilning organizm hayoti uchun eng qulay bo'lgan optimal darajasi bo'ladi. Libixning minimum qoidasi: Organizmning yashashi va mahsuldorligini eng kam miqdorda bo'lgan (cheklovchi/limitlovchi) omil belgilaydi.",
            "examples": [
                {
                    "title": "Biotik munosabatlarni aniqlash",
                    "problem": "Dukakli o'simliklar ildizidagi tuganak bakteriyalari bilan o'zaro munosabati qanday biotik omil hisoblanadi?",
                    "step_by_step": "Bakteriyalar havodagi azotni o'zlashtirib o'simlikka beradi, o'simlik esa bakteriyani organik moddalar bilan ta'minlaydi. Bu o'zaro foydali simbioz (mutualizm) munosabatidir.",
                    "answer": "Simbioz (mutualizm)"
                },
                {
                    "title": "Libix minimum qoidasi",
                    "problem": "Ekin maydonida barcha oziq moddalar, suv va yorug'lik yetarli, ammo fosfor elementi yetishmaydi. Hosildorlik nimaga bog'liq bo'ladi?",
                    "step_by_step": "Libix qoidasiga ko'ra hosildorlik aynan yetishmayotgan minimal omil — fosfor miqdori bilan cheklanadi.",
                    "answer": "Yetishmayotgan minimal omil (fosfor) bilan cheklanadi"
                }
            ],
            "exercise": "Antropogen omillarning ijobiy va salbiy ta'sirlariga 2 tadan misol keltiring.",
            "exercise_solution": "Ijobiy: qo'riqxonalar tashkil etish, ko'kalamzorlashtirish (daraxt ekish); Salbiy: o'rmonlarni kesish, sanoat chiqindilari bilan havoni ifloslantirish.",
            "check_questions": [
                {
                    "question": "'Ekologiya' atamasini fanga birinchi bo'lib kiritgan olim kim?",
                    "options": ["Charlz Darvin", "Ernst Gekkel", "Karl Linney", "Vladimir Vernadskiy"],
                    "correct_index": 1,
                    "explanation": "Ernst Gekkel 1866-yilda 'Organizmning umumiy morfologiyasi' asarida ekologiya atamasini qo'llagan."
                },
                {
                    "question": "Quyidagilardan qaysi biri abiotik omil hisoblanadi?",
                    "options": ["O'simliklar raqobati", "Quyosh radiatsiyasi va harorat", "Ovchilik", "Zamburug' parazitligi"],
                    "correct_index": 1,
                    "explanation": "Quyosh nuri, harorat, suv va bosim jonsiz tabiat (abiotik) omillaridir."
                },
                {
                    "question": "Organizm hayoti uchun eng qulay sharoit darajasi nima deyiladi?",
                    "options": ["Pessimum", "Optimum", "Minimum", "Maksimum"],
                    "correct_index": 1,
                    "explanation": "Omilning hayot faoliyati eng yaxshi kechadigan darajasi optimum deyiladi."
                }
            ],
            "tags": ["ekologiya", "ekologik omillar", "abiotik", "biotik", "antropogen", "libix", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "geo-009",
            "slug": "ekotizim-va-oziq-zanjirlari",
            "subject_id": "sub-13",
            "subject_name": "Ekologiya",
            "title": "Ekotizimlar: biotsenoz, produtsentlar, konsumentlar, redutsentlar va oziq to'rlari",
            "grade_level": "10-sinf",
            "difficulty": "O'rta",
            "objective": "Ekotizim tarkibiy qismlari, trofik darajalar, oziq zanjirlari va Lindeman qoidasi (10% ekologik piramida qoidasi) bo'yicha hisoblashlarni bajarish.",
            "theory": "Muayyan hududda birgalikda yashovchi barcha tirik organizmlar va ularning yashash muhiti birgalikda ekotizim (biogeotsenoz) deyiladi (A. Tensli, 1935). Ekotizimning 3 ta asosiy funksional guruhlari: 1) Produtsentlar (hosil qiluvchilar) — fotosintez qiluvchi avtotrof o'simliklar va sianobakteriyalar; 2) Konsumentlar (iste'mol qiluvchilar) — tayyor organik moddalar bilan oziqlanuvchi geterotrof hayvonlar (I tartib — o'txo'rlar, II va III tartib — yirtqichlar); 3) Redutsentlar (parchalovchilar) — o'lik organik qoldiqlarni noorganik moddalargacha parchalovchi zamburug'lar va chirish bakteriyalari. Oziq zanjiri: yaylov zanjiri (o'simlik -> o'txo'r -> yirtqich) va detrit zanjiri (o'lik qoldiq -> chuvalchang -> qush). Lindeman qoidasi (10% qoidasi): Bir trofik darajadan keyingi yuqori darajaga energiyaning faqat taxminan 10% i o'tadi, qolgan 90% i issiqlik sifatida sarflanadi.",
            "examples": [
                {
                    "title": "Lindeman qoidasi bo'yicha biomassa hisobi",
                    "problem": "Massasi 50 kg bo'lgan bo'ri o'sishi uchun qancha o'simlik biomassasi talab qilinadi (zanjir: o'simlik -> kiyik -> bo'ri)?",
                    "step_by_step": "1) 10% qoidasiga ko'ra: 50 kg bo'ri hosil bo'lishi uchun 10 marta ko'p o'txo'r kerak: 50 * 10 = 500 kg kiyik.\n2) 500 kg kiyik uchun 10 marta ko'p o'simlik kerak: 500 * 10 = 5000 kg o'simlik.\nNatija: 5000 kg (5 tonna) o'simlik.",
                    "answer": "5000 kg (5 tonna)"
                },
                {
                    "title": "Yaylov oziq zanjirini tuzish",
                    "problem": "Beda, burgut, ilon, sichqon organizmlaridan to'g'ri oziq zanjiri tuzing.",
                    "step_by_step": "1) Produtsent: Beda ->\n2) I tartib konsument: Sichqon ->\n3) II tartib konsument: Ilon ->\n4) III tartib konsument: Burgut.",
                    "answer": "Beda -> Sichqon -> Ilon -> Burgut"
                }
            ],
            "exercise": "Detrit oziq zanjiri qanday bo'g'indan boshlanadi?",
            "exercise_solution": "Detrit oziq zanjiri yashil o'simlikdan emas, balki o'lik organik qoldiqlar (chirindi, tushgan barglar, jasadlar)dan boshlanadi.",
            "check_questions": [
                {
                    "question": "Ekotizimda o'lik organik moddalarni noorganik moddalargacha parchalovchi organizmlar nima deyiladi?",
                    "options": ["Produtsentlar", "Konsumentlar", "Redutsentlar", "Parazitlar"],
                    "correct_index": 2,
                    "explanation": "Zamburug'lar va tuproq bakteriyalari redutsentlar bo'lib, moddalar aylanishini yakunlaydi."
                },
                {
                    "question": "Lindeman qoidasiga ko'ra bitta trofik pog'onadan keyingisiga energiyaning qancha qismi o'tadi?",
                    "options": ["100%", "50%", "Taxminan 10%", "1%"],
                    "correct_index": 2,
                    "explanation": "Har bir bosqichda energiyaning taxminan 90% i yo'qotiladi va faqat 10% i keyingi bo'g'inga o'tadi."
                },
                {
                    "question": "Biotsenoz tushunchasi nimani anglatadi?",
                    "options": ["Faqat o'simliklar jamoasini", "Muayyan hududdagi barcha tirik organizmlar majmuini", "Faqat tuproq qatlamini", "Iqlim sharoitini"],
                    "correct_index": 1,
                    "explanation": "Biotsenoz — birgalikda yashovchi o'simliklar, hayvonlar va mikroorganizmlar to'plamidir."
                }
            ],
            "tags": ["ekotizim", "biotsenoz", "produtsent", "konsument", "lindeman qoidasi", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "geo-010",
            "slug": "biosfera-va-vernadskiy-talimoti",
            "subject_id": "sub-13",
            "subject_name": "Ekologiya",
            "title": "Biosfera chegaralari, tirik modda funksiyalari va V.I. Vernadskiy ta'limoti",
            "grade_level": "10-sinf",
            "difficulty": "Murakkab",
            "objective": "Biosfera tuzilishi va chegaralari, V.I. Vernadskiyning tirik modda haqidagi ta'limoti hamda noosfera (aql sohasi) konsepsiyasini o'rganish.",
            "theory": "Biosfera — Yerning tirik organizmlar tarqalgan va ularning hayot faoliyati ta'sirida o'zgargan global qobig'idir. Akademik V.I. Vernadskiy biosfera haqidagi yaxlit ta'limotni yaratgan. Biosfera chegaralari: Atmosferada — ozon qatlamigacha (20-25 km); Gidrosferada — butun Dunyo okeani tubigacha (11 km chuqurlik); Litosferada — yer qobig'ining 3-4 km chuqurligigacha (bakteriyalar hayoti mavjud bo'lgan chegara). Vernadskiy bo'yicha biosferadagi moddalar: tirik modda (barcha tirik mavjudotlar biomassasi), biogen modda (tirik organizmlar yaratgan moddalar: ko'mir, neft, torf, ohaktosh), biojonsiz modda (tuproq, havo) va jonsiz (kosmik/otqindi) moddalar. Tirik moddaning asosiy biogeokimyoviy funksiyalari: gaz funksiyasi (O2, CO2 balansi), konsentratsion funksiya (Ca, P, Si to'plash), oksidlanish-qaytarilish va energetik funksiyalar. Noosfera — inson aqli va ongli faoliyati biosferaning asosiy rivojlanish omiliga aylangan oliy bosqichidir.",
            "examples": [
                {
                    "title": "Biogen moddalar kelib chiqishi",
                    "problem": "Toshko'mir va ohaktosh qatlamlarining hosil bo'lishida tirik organizmlarning o'rni qanday?",
                    "step_by_step": "Toshko'mir qadimgi daraxtsimon qirqquloqlarning chirimay ko'milib qolishidan; ohaktosh esa dengiz mollyuskalari va foraminiferalarining kalsiy karbonatli chig'anoqlari to'planishidan hosil bo'lgan biogen moddalardir.",
                    "answer": "Qadimgi o'simliklar va hayvon qoldiqlari to'planishidan hosil bo'lgan"
                },
                {
                    "title": "Noosfera tushunchasi",
                    "problem": "V.I. Vernadskiy fikricha, insoniyat biosferadan noosferaga o'tish uchun nimalarga erishishi kerak?",
                    "step_by_step": "Insoniyat urushlardan voz kechishi, fan va ekologik qonunlar asosida tabiat bilan uyg'un yashashi, sayyora resurslarini ongli ravishda tiklab boshqarishi lozim.",
                    "answer": "Aql va ilm asosida tabiat bilan uyg'un boshqaruv"
                }
            ],
            "exercise": "Tirik moddaning konsentratsion funksiyasiga 2 ta misol keltiring.",
            "exercise_solution": "1) Mollyuskalar va marjonlarning suvdagi kalsiyni to'plab chig'anoq va skelet hosil qilishi; 2) Qirqbo'g'imlar va diatom suv o'tlarining kremniy (Si) elementini to'plashi.",
            "check_questions": [
                {
                    "question": "Biosfera haqidagi fundamental ta'limot asoschisi kim?",
                    "options": ["Charlz Darvin", "V.I. Vernadskiy", "Eduard Zyuss", "Lui Paster"],
                    "correct_index": 1,
                    "explanation": "Vladimir Ivanovich Vernadskiy 1926-yilda 'Biosfera' asarida bu ta'limotni ilmiy asoslab berdi."
                },
                {
                    "question": "Atmosferada hayotning yuqori chegarasini qaysi omil cheklaydi?",
                    "options": ["Ozon qatlamining yo'qligi va qotil ultrabinafsha nurlanish", "Kislorod ko'pligi", "Havo zichligi", "Bulutlar"],
                    "correct_index": 0,
                    "explanation": "Ozon ekranidan yuqorida qattiq kosmik va ultrabinafsha nurlanish barcha tiriklikni nobud qiladi."
                },
                {
                    "question": "Inson aqli va mehnati hal qiluvchi kuchga aylangan biosfera bosqichi nima deyiladi?",
                    "options": ["Texnosfera", "Noosfera", "Stratosfera", "Antroposfera"],
                    "correct_index": 1,
                    "explanation": "Vernadskiy aql doirasini noosfera (yunoncha 'noos' — aql) deb atagan."
                }
            ],
            "tags": ["biosfera", "vernadskiy", "tirik modda", "noosfera", "biogeokimyo", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "geo-011",
            "slug": "orol-dengizi-muammosi-va-mintaqaviy-ekologiya",
            "subject_id": "sub-13",
            "subject_name": "Ekologiya",
            "title": "Orol fojiasi: sabablari, oqibatlari va Orolbo'yi ekologik tiklanish choralari",
            "grade_level": "11-sinf",
            "difficulty": "O'rta",
            "objective": "Orol dengizining qurishi sabablari, Orolqum cho'lining paydo bo'lishi, chang-tuz bo'ronlari va mintaqada saksovulzorlar barpo etish choralarini o'rganish.",
            "theory": "1960-yillargacha Orol dengizi maydoni jihatidan dunyoda 4-o'rinda turadigan yirik berk ko'l edi (maydoni 68 ming km^2). 1960-yillardan boshlab Amudaryo va Sirdaryo suvlarining paxta va sholi maydonlarini sug'orish uchun me'yordan ortiq olinishi (Qoraqum kanali va boshqalar) oqibatida dengizga suv kelishi keskin kamaydi. Natijada Orol sathi 30 metrga pasaydi, maydoni 10 barobarga qisqardi va sho'rligi 10-15 barobar ortdi, mahalliy baliq turlari butunlay qirilib ketdi. Dengiz tubining 5.5 million gektaridan ortiq maydonida yangi 'Orolqum' qum-tuz cho'li hosil bo'ldi. Har yili bu yerdan havoga 100 million tonnadan ortiq tuzli chang ko'tarilib, minglab kilometrlarga (Tyanshan muzliklarigacha) tarqalmoqda. Tiklanish choralari: Orolqum tubida millionlab gektar maydonda saksovul va sho'rga chidamli butalar ekish, Orolbo'yi mintaqasi aholisini toza ichimlik suvi bilan ta'minlash, tomchilatib sug'orishni joriy etish va BMT maxsus Trast fondi faoliyati.",
            "examples": [
                {
                    "title": "Orol tubida saksovul ekish",
                    "problem": "Nima sababdan qurigan dengiz tubiga aynan saksovul (Haloxylon) ekilmoqda?",
                    "step_by_step": "Saksovul kuchli ildiz tizimiga ega bo'lib, qum va tuzlarni ushlab qoladi, shamol eroziyasini to'xtatadi va sho'rxok cho'l sharoitida o'sa oladigan eng bardoshli o'simlikdir. Bitta saksovul tupi 10 tonnagacha qumni ushlab tura oladi.",
                    "answer": "Qum-tuz ko'chishini to'xtatish va ekotizimni mustahkamlash uchun"
                },
                {
                    "title": "Iqlimga ta'siri",
                    "problem": "Orol dengizining qurishi mintaqa iqlimiga qanday salbiy ta'sir ko'rsatdi?",
                    "step_by_step": "Ilgari ulkan suv havzasi sifatida iqlimni yumshatib turgan (termos vazifasi). U qurigach, mintaqa iqlimi yanada kontinentallashdi: yoz fasli quruq va jazirama, qish fasli esa qahraton va ayozli bo'lib qoldi.",
                    "answer": "Kontinentallik oshdi: yoz issiqroq, qish ancha sovuqroq bo'ldi"
                }
            ],
            "exercise": "Orol dengiziga quyiluvchi ikkita asosiy daryoni va ularning boshlanish manbalarini yozing.",
            "exercise_solution": "Amudaryo (Pomir tog'laridan) va Sirdaryo (Tyanshan tog'laridan) boshlanadi.",
            "check_questions": [
                {
                    "question": "Orol dengizining qurishi natijasida hosil bo'lgan yangi qumli cho'l qanday ataladi?",
                    "options": ["Qizilqum", "Qoraqum", "Orolqum", "Ustyurt"],
                    "correct_index": 2,
                    "explanation": "Qurigan dengiz tubida paydo bo'lgan cho'l xalqaro miqyosda Orolqum deb ataladi."
                },
                {
                    "question": "Orol fojiasining eng asosiy antropogen sababi nima bo'lgan?",
                    "options": ["Global isish", "Amudaryo va Sirdaryo suvlarining sug'orishga me'yordan ortiq olinishi", "Dengiz tubidagi yoriqlar", "Sanoat chiqindilari"],
                    "correct_index": 1,
                    "explanation": "Daryo oqimining dehqonchilik maydonlariga haddan tashqari ko'p burilishi dengizga suv yetib bormasligiga olib kelgan."
                },
                {
                    "question": "Orolqum tubida qum ko'chishini to'xtatuvchi asosiy o'simlik qaysi?",
                    "options": ["Yantoq", "Saksovul", "Qamish", "Shirinmiya"],
                    "correct_index": 1,
                    "explanation": "Saksovul o'zining chuqur ildizlari bilan qum va zaharli tuzlarni mahkam tutib turadi."
                }
            ],
            "tags": ["orol dengizi", "orolqum", "ekologik fojia", "saksovul", "amudaryo", "11-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "geo-012",
            "slug": "global-iqlim-ozgarishi-va-yashil-iqtisodiyot",
            "subject_id": "sub-13",
            "subject_name": "Ekologiya",
            "title": "Global iqlim o'zgarishi, issiqxona effekti va Yashil energetikaga o'tish",
            "grade_level": "11-sinf",
            "difficulty": "Murakkab",
            "objective": "Issiqxona gazlari (CO2, CH4), Parij iqlim bitimi, qayta tiklanuvchi energiya manbalari (quyosh, shamol) va yashil iqtisodiyot tamoyillarini o'rganish.",
            "theory": "Global iqlim isishi — inson faoliyati (qazilma yoqilg'ilar: ko'mir, neft, gaz yoqilishi) natijasida atmosferada issiqxona gazlari (CO2, metan CH4, azot oksidlari) konsentratsiyasining ortishi oqibatida sayyora o'rtacha haroratining ko'tarilishidir. Issiqxona effekti mexanizmi: Quyosh nurlari yer sirtini isitadi, yerdan qaytgan infraqizil (issiqlik) nurlarini esa atmosferadagi issiqxona gazlari koinotga chiqib ketishiga yo'l qo'ymay tutib qoladi. Oqibatlari: Qutb va tog' muzliklarining erishi, Dunyo okeani sathining ko'tarilishi, qurg'oqchilik, o'rmon yong'inlari va ekstremal ob-havo hodisalari. Xalqaro yechim: Parij iqlim bitimi (global harorat o'sishini sanoatgacha bo'lgan davrga nisbatan 1.5-2 °C dan oshirmaslik). Yashil iqtisodiyot: Qayta tiklanuvchi energiya manbalari (quyosh fotoelektr stansiyalari, shamol generatorlari, vodorod energetikasi), energiya tejamkor texnologiyalar, elektromobillar va uglerod neytralligi (Net Zero).",
            "examples": [
                {
                    "title": "Asosiy issiqxona gazi",
                    "problem": "Inson faoliyati natijasida atmosferaga eng ko'p chiqariladigan issiqxona gazi qaysi?",
                    "step_by_step": "Uglerod (IV) oksid yoki karbonat angidrid (CO2) yoqilg'i yoqish, sanoat va transport orqali eng katta hajmda atmosferaga chiqariladi.",
                    "answer": "Karbonat angidrid (CO2)"
                },
                {
                    "title": "Uglerod neytralligi nima?",
                    "problem": "'Uglerod neytralligi' (Net Zero) iborasi nimani anglatadi?",
                    "step_by_step": "Atmosferaga chiqarilayotgan barcha issiqxona gazlari miqdorining yangi o'rmonlar barpo etish va ushlash texnologiyalari orqali to'liq yutilishi va kompensatsiya qilinishi (sof qoldiq nolga teng).",
                    "answer": "Chiqarilayotgan CO2 miqdori va yutilayotgan miqdorning tenglashishi"
                }
            ],
            "exercise": "O'zbekistonda amalga oshirilayotgan 'Yashil makon' umummilliy loyihasining maqsadi nima?",
            "exercise_solution": "Har yili 200 million tup ko'chat ekib, shaharlar va qishloqlarda yashillik darajasini 30% dan oshirish, havoni chang va zaharli gazlardan tozalash hamda iqlim o'zgarishiga qarshi kurashish.",
            "check_questions": [
                {
                    "question": "Parij iqlim bitimining asosiy maqsadi nima?",
                    "options": ["Orol dengizini suv bilan to'ldirish", "Global o'rtacha harorat ko'tarilishini 1.5 - 2 °C darajasida ushlab qolish", "Plastikdan butunlay voz kechish", "Neft qazib olishni taqiqlash"],
                    "correct_index": 1,
                    "explanation": "Parij bitimi global isishni 2 °C dan sezilarli darajada past, 1.5 °C chegarasida ushlab qolishni maqsad qilgan."
                },
                {
                    "question": "Qayta tiklanuvchi yashil energiya manbai qaysi?",
                    "options": ["Toshko'mir", "Quyosh va shamol energiyasi", "Tabiiy gaz", "Mazut"],
                    "correct_index": 1,
                    "explanation": "Quyosh, shamol, gidro va geotermal energiya tabiiy ravishda qayta tiklanadi va CO2 chiqarmaydi."
                },
                {
                    "question": "Issiqxona gazlaridan qaysi biri metan hisoblanadi?",
                    "options": ["CO2", "CH4", "N2O", "O3"],
                    "correct_index": 1,
                    "explanation": "CH4 — metan gazi bo'lib, CO2 ga qaraganda issiqlikni tutib qolish qobiliyati 25-28 barobar yuqori."
                }
            ],
            "tags": ["iqlim o'zgarishi", "issiqxona effekti", "yashil iqtisodiyot", "parij bitimi", "quyosh energiyasi", "11-sinf"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_geography_ecology_materials()
    print(f"Generated {len(mats)} Geography/Ecology materials.")
