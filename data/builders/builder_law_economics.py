# -*- coding: utf-8 -*-
"""
Builder for Huquq, Iqtisod, Tarbiya (12 materials: law-001 to law-012)
- sub-25: Davlat va huquq asoslari (4: law-001 to law-004)
- sub-26: Tarbiya (4: law-005 to law-008)
- sub-27: Iqtisodiy bilim asoslari (4: law-009 to law-012)
"""

def get_law_economics_materials():
    materials = [
        # DAVLAT VA HUQUQ ASOSLARI (4)
        {
            "id": "law-001",
            "slug": "davlat-va-huquq-tushunchasi-davlat-hokimiyati",
            "subject_id": "sub-25",
            "subject_name": "Davlat va huquq asoslari",
            "title": "Davlat va huquq tushunchasi: belgilar, vazifalar va hokimiyatlar bo'linishi",
            "grade_level": "8-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Davlatning asosiy belgilari, boshqaruv shakllari (monarxiya, respublika), huquqiy davlat va davlat hokimiyatining uch bo'g'inga bo'linishi prinsipini o'rganish.",
            "theory": "Davlat — ma'lum hududda yashovchi aholini boshqaruvchi, o'z suverenitetiga, qonun chiqarish va soliq undirish vakolatiga ega bo'lgan siyosiy tashkilotdir. Davlatning 4 ta asosiy belgisi: 1) Yaxlit hudud va chegaralar; 2) Aholi (fuqarolar); 3) Suverenitet (ichki va tashqi mustaqillik); 4) Ommaviy hokimiyat apparati va huquq tizimi. Boshqaruv shakllari: Monarxiya (hokimiyat meros bo'lib o'tadi) va Respublika (oliy hokimiyat xalq tomonidan muayyan muddatga saylanadi). Hokimiyatlar bo'linishi prinsipi (Sharl Lui Monteskyo): yagona davlat hokimiyati mustaqil uch tarmoqqa bo'linadi: 1) Qonun chiqaruvchi hokimiyat (Parlament — Oliy Majlis); 2) Ijro etuvchi hokimiyat (Hukumat — Vazirlar Mahkamasi); 3) Sud hokimiyati (Konstitutsiyaviy sud, Oliy sud). Ular o'rtasida 'tiyib turish va muvozanat' (checks and balances) tizimi amal qiladi.",
            "examples": [
                {
                    "title": "Hokimiyatlar bo'linishi amalda",
                    "problem": "Nima sababdan bitta shaxs yoki organ bir vaqtning o'zida ham qonun chiqaruvchi, ham ijro etuvchi, ham sudya bo'la olmaydi?",
                    "step_by_step": "Agar barcha hokimiyat bitta qo'lda to'plansa, cheklanmagan zolimlik (diktatura va tiranlik) kelib chiqadi. Hokimiyatlar bo'linishi inson huquqlari poymol bo'lmasligi va qonun ustuvorligini ta'minlash uchun zarurdir.",
                    "answer": "Yakka hukmronlik (diktatura)ning oldini olish va huquqlarni himoya qilish uchun"
                },
                {
                    "title": "Boshqaruv shaklini aniqlash",
                    "problem": "O'zbekiston Respublikasi boshqaruv shakliga ko'ra qanday davlat?",
                    "step_by_step": "O'zbekiston — Respublika. Davlat boshlig'i (Prezident) va parlament xalq tomonidan umumxalq teng va to'g'ridan-to'g'ri saylovlar orqali saylanadi.",
                    "answer": "Respublika (Prezidentlik boshqaruvidagi respublika)"
                }
            ],
            "exercise": "Huquqiy davlatning eng bosh xususiyati nimada namoyon bo'ladi?",
            "exercise_solution": "Qonun ustuvorligi (barcha fuqarolar, amaldorlar va davlat organlari qonun oldida tengligi) va inson huquqlarining oliy qadriyat deb tan olinishi.",
            "check_questions": [
                {
                    "question": "Hokimiyatlar bo'linishi prinsipiga ko'ra qonun chiqaruvchi hokimiyatni qaysi organ amalga oshiradi?",
                    "options": ["Vazirlar Mahkamasi", "Oliy Majlis (Parlament)", "Oliy sud", "Bosh prokuratura"],
                    "correct_index": 1,
                    "explanation": "Qonunlarni faqat xalq saylagan parlament (O'zbekistonda Oliy Majlis) qabul qiladi."
                },
                {
                    "question": "Davlatning o'z hududida to'la mustaqil bo'lishi va tashqi munosabatlarda teng huquqliligi nima deb ataladi?",
                    "options": ["Legitimlik", "Suverenitet", "Imunitet", "Monopoliya"],
                    "correct_index": 1,
                    "explanation": "Suverenitet — davlat mustaqilligi va oliy hokimiyatining asosiy belgisidir."
                },
                {
                    "question": "Hokimiyat vakolatlari meros bo'yicha o'tadigan davlat boshqaruv shakli qaysi?",
                    "options": ["Respublika", "Monarxiya", "Federatsiya", "Konfederatsiya"],
                    "correct_index": 1,
                    "explanation": "Monarxiyada (qirollik, amirlik) toj-taxt nasldan-naslga meros qilib qoldiriladi."
                }
            ],
            "tags": ["huquq", "davlat", "suverenitet", "hokimiyatlar bo'linishi", "parlament", "8-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "law-002",
            "slug": "inson-huquqlari-va-ozbekiston-konstitutsiyasi",
            "subject_id": "sub-25",
            "subject_name": "Davlat va huquq asoslari",
            "title": "Inson huquqlari umumjahon deklaratsiyasi va O'zbekiston Respublikasi Konstitutsiyasi",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "1948-yilgi Inson huquqlari umumjahon deklaratsiyasi, shaxsiy, siyosiy, iqtisodiy-ijtimoiy va madaniy huquqlar hamda konstitutsiyaviy burchlarni bilish.",
            "theory": "1948-yil 10-dekabrda BMT Bosh Assambleyasi tomonidan 'Inson huquqlari umumjahon deklaratsiyasi' qabul qilingan. Yangi tahrirdagi O'zbekiston Respublikasi Konstitutsiyasining bosh tamoyili: 'Inson — jamiyat — davlat' (inson huquq va erkinliklari har qanday davlat manfaatidan ustun turadi). Asosiy huquqlar guruhlari: 1) Shaxsiy huquqlar — yashash huquqi, erkinlik va shaxsiy daxlsizlik, sha'n va qadr-qimmat himoyasi, aybsizlik prezumpsiyasi (aybi sudda isbotlanmaguncha har kim begunohdir); 2) Siyosiy huquqlar — saylash va saylanish huquqi, davlat xizmatiga kirish, so'z erkinligi, miting va namoyishlar erkinligi; 3) Iqtisodiy va ijtimoiy huquqlar — mehnat qilish, munosib ish haqi, xususiy mulkdorlik, bepul umumiy o'rta ta'lim, malakali tibbiy xizmat, dam olish huquqi; 4) Ekologik huquqlar — har kim qulay atrof-muhitga bo'lgan huquqqa ega. Fuqarolarning konstitutsiyaviy burchlari: qonunlarga rioya qilish, soliq to'lash, tabiatni asrash, Vatanni himoya qilish (harbiy xizmat).",
            "examples": [
                {
                    "title": "Aybsizlik prezumpsiyasi",
                    "problem": "'Aybsizlik prezumpsiyasi' (Presumption of innocence) printsipi amalda nimani anglatadi?",
                    "step_by_step": "Har qanday shaxsning jinoyat sodir etishda aybdorligi qonuniy tartibda, ochiq sud muhokamasida isbotlanmaguncha va sud hukmi qonuniy kuchga kirmaguncha u aybsiz hisoblanadi. Hech kim o'zining aybsizligini isbotlashga majbur emas.",
                    "answer": "Sudning qonuniy hukmi chiqmaguncha har qanday gumonlanuvchi aybsiz hisoblanadi"
                },
                {
                    "title": "Xabeas Korpus (Habeas Corpus) qoidasi",
                    "problem": "Shaxsni qamoqqa olishga kim ruxsat beradi?",
                    "step_by_step": "Konstitutsiyaga binoan, shaxsni qamoqqa olish, ushlab turish va ozodlikdan mahrum etishga faqat sud qaroriga asosan yo'l qo'yiladi.",
                    "answer": "Faqat sud qarori bilan qamoqqa olinadi"
                }
            ],
            "exercise": "Fuqarolarning Konstitutsiyada belgilangan 4 ta asosiy burchini sanang.",
            "exercise_solution": "1) Konstitutsiya va qonunlarga rioya etish; 2) Boshqa insonlarning huquqlarini hurmat qilish; 3) Qonun bilan belgilangan soliqlarni to'lash; 4) Tabiat va madaniy merosni asrash; 5) Vatanni himoya qilish.",
            "check_questions": [
                {
                    "question": "Inson huquqlari umumjahon deklaratsiyasi qachon qabul qilingan?",
                    "options": ["1945-yil 9-may", "1948-yil 10-dekabr", "1991-yil 1-sentyabr", "1992-yil 8-dekabr"],
                    "correct_index": 1,
                    "explanation": "BMT tomonidan Deklaratsiya 1948-yil 10-dekabrda qabul qilingan (har yili Xalqaro inson huquqlari kuni)."
                },
                {
                    "question": "Shaxsning aybi qonunda belgilangan tartibda sudda isbotlanmaguncha aybsiz deb hisoblanishi nima deyiladi?",
                    "options": ["Imunitet", "Aybsizlik prezumpsiyasi", "Amnitsiya", "Reabilitatsiya"],
                    "correct_index": 1,
                    "explanation": "Aybsizlik prezumpsiyasi demokratik odil sudlovning fundamental kafolatidir."
                },
                {
                    "question": "Yangi tahrirdagi Konstitutsiyada ta'limga oid qaysi norma qat'iy kafolatlangan?",
                    "options": ["Faqat pullik ta'lim", "Bepul umumiy o'rta ta'lim davlat kafolatidadir", "Oliy ta'lim majburiyligi", "Chet elda o'qish"],
                    "correct_index": 1,
                    "explanation": "Davlat har bir fuqaroning bepul umumiy o'rta ta'lim olishini kafolatlaydi."
                }
            ],
            "tags": ["huquq", "inson huquqlari", "konstitutsiya", "deklaratsiya", "aybsizlik prezumpsiyasi", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "law-003",
            "slug": "fuqarolik-huquqi-va-shartnomalar-tizimi",
            "subject_id": "sub-25",
            "subject_name": "Davlat va huquq asoslari",
            "title": "Fuqarolik huquqi asoslari: mulk huquqi, bitimlar va shartnomalar",
            "grade_level": "10-sinf",
            "difficulty": "O'rta",
            "objective": "Fuqarolik huquq layoqati va muomala layoqati, mulk huquqining 3 ta vakolati (egalik, foydalanish, tasarruf) va shartnoma tuzish qoidalarini o'rganish.",
            "theory": "Fuqarolik huquqi shaxslar (jismoniy va yuridik shaxslar) o'rtasidagi mulkiy va shaxsiy nomulkiy munosabatlarni tartibga soladi. Huquq layoqati — fuqarolik huquqlariga ega bo'lish layoqati bo'lib, inson tug'ilgan paytdan boshlanadi va vafot etganda tugaydi. Muomala layoqati — o'z harakatlari bilan huquqlarga ega bo'lish va burchlar orttirish layoqati (14 yoshgacha — to'liq layoqatsiz; 14-18 yosh — qisman layoqatli; 18 yoshdan (voyaga yetgach) — to'liq muomala layoqati boshlanadi). Mulk huquqi 3 ta klassik vakolatdan iborat: 1) Egalik qilish (mulkni amalda o'zida saqlab turish); 2) Foydalanish (undan foydali xossalarini olish, mahsulot yetishtirish); 3) Tasarruf etish (mulk taqdirini hal qilish: sotish, hadya qilish, vasiyat qilish). Shartnoma — ikki yoki undan ortiq shaxslarning fuqarolik huquq va burchlarini belgilash, o'zgartirish yoki bekor qilish to'g'risidagi kelishuvidir (oldi-sotdi, ijara, xizmat ko'rsatish).",
            "examples": [
                {
                    "title": "Muomala layoqatini aniqlash",
                    "problem": "16 yoshli o'quvchi o'ziga tegishli velosipedni yoki noutbukni ota-onasisiz mustaqil sotishi mumkinmi?",
                    "step_by_step": "14 yoshdan 18 yoshgacha bo'lgan voyaga yetmaganlar faqat o'z stipendiyasi yoki maoshini mustaqil tasarruf qilishi va mayda maishiy bitimlar tuzishi mumkin. Qimmatbaho mulkni sotish uchun esa ota-onasining (qonuniy vakillarining) yozma roziligi talab qilinadi.",
                    "answer": "Faqat ota-onasining yozma roziligi bilan sotishi mumkin"
                },
                {
                    "title": "Mulkni tasarruf etish vakolati",
                    "problem": "Ijarachi uyni ijaraga olib yashamoqda. U ushbu uyni boshqa shaxsga sotib yubora oladimi?",
                    "step_by_step": "Yo'q. Ijarachida faqat egalik qilish va foydalanish huquqi bor. Tasarruf etish (sotish, sovg'a qilish) huquqi faqat qonuniy mulkdorga tegishli.",
                    "answer": "Yo'q, chunki unda tasarruf etish huquqi yo'q"
                }
            ],
            "exercise": "Bitimlar qanday shakllarda (og'zaki, yozma, notarial) tuziladi va qachon notarial tasdiqlash majburiy?",
            "exercise_solution": "Ko'chmas mulk (uy, bino, yer) oldi-sotdisi va avtotransport vositalarini boshqarish ishonchnomalari qonun bo'yicha majburiy notarial tasdiqlashni talab qiladi.",
            "check_questions": [
                {
                    "question": "Fuqaroning to'liq muomala layoqati necha yoshdan boshlanadi?",
                    "options": ["14 yoshdan", "16 yoshdan", "18 yoshdan (voyaga yetgach)", "21 yoshdan"],
                    "correct_index": 2,
                    "explanation": "Qonunchilikka binoan 18 yoshga to'lgan fuqaro to'liq muomala layoqatiga ega bo'ladi."
                },
                {
                    "question": "Mulkdorning mulk taqdirini hal qilish (sotish, hadya qilish, yo'q qilish) huquqi qanday ataladi?",
                    "options": ["Egalik qilish", "Foydalanish", "Tasarruf etish", "Ipoteka"],
                    "correct_index": 2,
                    "explanation": "Tasarruf etish — mulkning yuridik taqdirini erkin belgilash huquqidir."
                },
                {
                    "question": "Fuqarolik huquq layoqati qachon boshlanadi?",
                    "options": ["Pasport olganda", "Maktabga borganda", "Inson tug'ilgan paytdan", "18 yoshda"],
                    "correct_index": 2,
                    "explanation": "Inson tug'ilgan ondan boshlab huquq subyekti sifatida huquq layoqatiga ega bo'ladi."
                }
            ],
            "tags": ["fuqarolik huquqi", "mulk huquqi", "muomala layoqati", "shartnoma", "bitim", "10-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "law-004",
            "slug": "mehnat-huquqi-va-yoshlar-mehnatini-muhofaza-qilish",
            "subject_id": "sub-25",
            "subject_name": "Davlat va huquq asoslari",
            "title": "Mehnat huquqi: Mehnat shartnomasi, ish vaqti va voyaga yetmaganlar mehnatini himoya qilish",
            "grade_level": "10-11-sinf",
            "difficulty": "O'rta",
            "objective": "Mehnat kodeksi talablari, mehnat shartnomasi tuzish, sinov muddati, voyaga yetmaganlar uchun imtiyozlar va dam olish vaqti qoidalarini o'rganish.",
            "theory": "Mehnat huquqi xodim va ish beruvchi o'rtasidagi munosabatlarni tartibga soladi. Mehnat shartnomasi — xodim bilan ish beruvchi o'rtasidagi kelishuv bo'lib, unga ko'ra xodim muayyan mutaxassislik bo'yicha ishlaydi va ichki mehnat tartibiga bo'ysunadi, ish beruvchi esa o'z vaqtida oylik ish haqi to'laydi va xavfsiz mehnat sharoitini yaratadi. Ishga qabul qilishga umumiy qoidaga ko'ra 16 yoshdan ruxsat beriladi (ota-onasining yozma roziligi bilan o'qishdan bo'sh vaqtda yengil ishlar uchun 15 yoshdan, madaniy-tomosha sohasida undan ham kichikroq yoshdan mumkin). Ish vaqti davomiyligi: kattalar uchun haftasiga 40 soatdan oshmasligi kerak; 16 yoshdan 18 yoshgacha bo'lganlar uchun haftasiga ko'pi bilan 36 soat; 15 yoshdan 16 yoshgacha bo'lganlar uchun haftasiga 24 soat. Voyaga yetmaganlar uchun taqiqlar: tungi vaqtda (22:00 dan 06:00 gacha), dam olish kunlari va yer osti, zararli, xavfli mehnat sharoitlarida ishlatish qat'iyan taqiqlanadi.",
            "examples": [
                {
                    "title": "Voyaga yetmagan xodim uchun sinov muddati",
                    "problem": "17 yoshli kollej bitiruvchisini ishga qabul qilishda ish beruvchi unga 3 oylik sinov muddati belgilashi mumkinmi?",
                    "step_by_step": "Mehnat kodeksiga ko'ra 18 yoshga to'lmagan shaxslar, homilador ayollar va o'quv yurtini tamomlab birinchi bor ishga kirayotgan bitiruvchilar uchun dastlabki sinov muddati belgilash qat'iyan taqiqlanadi.",
                    "answer": "Yo'q, voyaga yetmaganlarga sinov muddati belgilanmaydi"
                },
                {
                    "title": "Ish vaqti me'yori",
                    "problem": "Ish beruvchi 17 yoshli xodimni kuniga 8 soatdan (haftasiga 40 soat) ishlashga majbur qila oladimi?",
                    "step_by_step": "Yo'q, 16 dan 18 yoshgacha bo'lganlar uchun qisqartirilgan ish vaqti belgilanadi — haftasiga ko'pi bilan 36 soat (kuniga 7.2 soat).",
                    "answer": "Yo'q, haftasiga 36 soatdan oshmasligi shart"
                }
            ],
            "exercise": "Yillik asosiy mehnat ta'tili kamida necha kalendar kunidan iborat bo'lishi kerak?",
            "exercise_solution": "Yangi Mehnat kodeksiga ko'ra yillik asosiy eng kam mehnat ta'tili 21 kalendar kunidan kam bo'lmasligi kerak (voyaga yetmaganlar uchun esa kamida 30 kalendar kuni).",
            "check_questions": [
                {
                    "question": "Umumiy qoidaga ko'ra necha yoshdan boshlab mehnat shartnomasi tuzishga ruxsat etiladi?",
                    "options": ["14 yoshdan", "16 yoshdan", "18 yoshdan", "21 yoshdan"],
                    "correct_index": 1,
                    "explanation": "O'zbekiston Mehnat kodeksi bo'yicha ishga qabul qilishning umumiy yoshi 16 yoshdir."
                },
                {
                    "question": "Voyaga yetmagan xodimlarni tungi smenada (22:00 dan 06:00 gacha) ishlatish mumkinmi?",
                    "options": ["Ha, agar o'zi xohlasa", "Qat'iyan man etiladi", "Faqat qo'shimcha haq to'lansa", "Ota-onasi ruxsat bersa"],
                    "correct_index": 1,
                    "explanation": "Qonunchilik voyaga yetmaganlarni tungi, zararli va xavfli ishlarga jalb etishni mutlaqo taqiqlaydi."
                },
                {
                    "question": "Katta yoshli xodimlar uchun haftalik normal ish vaqti qancha soatdan oshmasligi kerak?",
                    "options": ["30 soat", "36 soat", "40 soat", "48 soat"],
                    "correct_index": 2,
                    "explanation": "Oddiy sharoitda haftalik normal ish vaqti 40 soatdan oshishi mumkin emas."
                }
            ],
            "tags": ["mehnat huquqi", "mehnat shartnomasi", "ish vaqti", "yoshlar mehnati", "ta'til", "11-sinf"],
            "duration_minutes": 35
        },

        # TARBIYA (4)
        {
            "id": "law-005",
            "slug": "odob-axloq-qoidalari-va-salomlashish-madaniyati",
            "subject_id": "sub-26",
            "subject_name": "Tarbiya",
            "title": "Odob-axloq qoidalari, salomlashish madaniyati va muomala odobi",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Insoniylik fazilatlari, xushmuomalalik, salomlashish tartibi, kattalarga hurmat va jamoat joylarida o'zini tutish odobini shakllantirish.",
            "theory": "Odob — insonning jamiyatda boshqalar bilan munosabatlarida go'zal xulq-atvor qoidalariga rioya qilishi, axloq esa inson ichki dunyosining ma'naviy qadriyatlaridir. O'zbek xalqida 'Odobning boshi — salom' deb bejiz aytilmagan. Salomlashish odobi qoidalari: 1) Kichiklar kattalarga, ulovdagi kishi piyodaga, piyoda yurgan kishi o'tirganga, ozchilik ko'pchilikka birinchi bo'lib salom beradi; 2) Salomlashganda ko'ziga samimiy qarab, tabassum bilan 'Assalomu alaykum!' (Sizga tinchlik va omonlik bo'lsin) deyiladi; 3) Ota-onaga, ustozlarga va keksalarga doimo ehtirom ko'rsatiladi. Muomala odobi: so'zlayotgan kishining gapini bo'lmaslik, birovning shaxsiy buyumlarini ruxsatsiz olmaslik, jamoat transportida keksalarga va homilador ayollarga joy berish har bir madaniyatli yoshning burchidir.",
            "examples": [
                {
                    "title": "Salomlashish tartibi",
                    "problem": "Sinf xonasiga kirib kelgan o'quvchi birinchi bo'lib nima qilishi kerak?",
                    "step_by_step": "Xonaga kirganda birinchi bo'lib xonada o'tirgan ustoz va tengdoshlariga ochiq chehra bilan salom beradi, so'ng o'z o'rniga o'tiradi.",
                    "answer": "Birinchi bo'lib o'tirganlarga salom beradi"
                },
                {
                    "title": "Kattalarga joy berish",
                    "problem": "Avtobusda ketayotganingizda qariya yoki bolali ayol chiqdi. Odob qoidasi nima qilishni talab qiladi?",
                    "step_by_step": "Darhol o'rindan turib, xushmuomalalik bilan 'Marhamat, o'tiring' deb joy bo'shatish sharqona ehtirom va insoniylik burchidir.",
                    "answer": "Darhol o'rindan turib joy beriladi"
                }
            ],
            "exercise": "'Kattaga hurmatda, kichikka izzatda bo'l' maqolining ma'nosini tushuntiring.",
            "exercise_solution": "Katta yoshlilarga tajribasi va yoshi uchun hurmat ko'rsatish, o'zidan kichiklarga esa mehrli, g'amxo'r va himoyachi bo'lish lozimligini bildiradi.",
            "check_questions": [
                {
                    "question": "'Assalomu alaykum' salomining ma'nosi nima?",
                    "options": ["Xayrli tong", "Sizga tinchlik va salomatlik tilayman", "Omad yor bo'lsin", "Kuningiz yaxshi o'tsin"],
                    "correct_index": 1,
                    "explanation": "Bu ezgu tilak bo'lib, suhbatdoshga tinchlik, omonlik va salomatlik tilash demakdir."
                },
                {
                    "question": "Salomlashish qoidasiga ko'ra kim birinchi salom berishi odobdan?",
                    "options": ["Kattalar kichiklarga", "Kichik yoshlilar kattalarga", "O'tirganlar yurib kelayotganga", "Farqi yo'q"],
                    "correct_index": 1,
                    "explanation": "Kichiklar kattalarga birinchi bo'lib salom berishi o'zbekona odob qoidasidir."
                },
                {
                    "question": "Birov so'zlayotganda suhbatdosh qanday harakat qilishi to'g'ri?",
                    "options": ["Gapini bo'lib o'z fikrini aytishi", "Diqqat bilan oxirigacha eshitib, keyin fikr bildirishi", "Telefoniga qarab o'tirishi", "Boshqa tomonga qarab ketishi"],
                    "correct_index": 1,
                    "explanation": "Birovning so'zini bo'lmasdan tinglash yuksak madaniyat belgisidir."
                }
            ],
            "tags": ["tarbiya", "odob", "axloq", "salomlashish", "hurmat", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "law-006",
            "slug": "oilaviy-qadriyatlar-va-ota-onaga-hurmat",
            "subject_id": "sub-26",
            "subject_name": "Tarbiya",
            "title": "Oila muqaddasligi, ota-onaga ehtirom va farzandlik burchi",
            "grade_level": "7-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Oila jamiyatning asosi ekanligi, ota-ona oldidagi farzandlik burchlari, mehr-oqibat va sog'lom oilaviy muhitning shaxs kamolotidagi o'rnini anglash.",
            "theory": "Oila — jamiyatning asosiy bo'g'ini, mehr-muhabbat, tarbiya va ma'naviyat qo'rg'onidir. Har bir insonning shaxs sifatida shakllanishi, dunyoqarashi va fazilatlari oiladagi muhitga bog'liq. O'zbek xalqida ota-ona ulug' zot sifatida e'zozlanadi ('Ota rozi — Xudo rozi', 'Jannat onalar oyog'i ostidadir'). Farzandlik burchi: 1) Ota-onaning so'zlariga quloq solish, ularga qattiq gapirmaslik ('Uff' ham demaslik); 2) Ota-ona keksayganda ularga mehr bilan qarash, moddiy va ma'naviy tayanch bo'lish (Konstitutsiyamizda ham: 'Voyaga yetgan, mehnatga layoqatli farzandlar o'z ota-onalari haqida g'amxo'rlik qilishga majburdirlar' deb belgilangan); 3) Aka-uka, opa-singillar o'rtasida mehr-oqibat va totuvlikni asrash.",
            "examples": [
                {
                    "title": "Farzandlik burchi amalda",
                    "problem": "Ota-onangiz sizdan uy ishlarida yordam so'raganda kompyuterda o'yin o'ynayotgan edingiz. To'g'ri axloqiy tanlov qanday bo'lishi kerak?",
                    "step_by_step": "O'yinni darhol to'xtatib, ochiq chehra bilan ota-onaning iltimosini bajarish kerak. Ota-onaning xizmatida bo'lish har qanday virtual o'yindan cheksiz ustun turadi.",
                    "answer": "Darhol o'yindan chiqib, ota-onaga yordam berish"
                },
                {
                    "title": "Konstitutsiyadagi oilaviy majburiyat",
                    "problem": "Ota-onaga g'amxo'rlik qilish faqat axloqiy qoidami yoki qonuniy burch hammi?",
                    "step_by_step": "O'zbekiston Respublikasi Konstitutsiyasida bu qoida qat'iy yuridik burch sifatida mustahkamlangan: voyaga yetgan farzandlar muhtoj ota-onalarini boqishga qonunan majburdirlar.",
                    "answer": "Ham axloqiy, ham qonuniy konstitutsiyaviy burchdir"
                }
            ],
            "exercise": "'Ona yurti — omonlik, ota uyi — omonat' kabi oila haqidagi 2 ta xalq maqolini tahlil qiling.",
            "exercise_solution": "1) 'Oila — kichik vatan': Oila mustahkam bo'lsa, butun jamiyat va davlat qudratli bo'ladi; 2) 'Otang borida do'st orttir': Ota borligida uning qadriga yetish va uning do'stona nasihatlarini olish zarurligi.",
            "check_questions": [
                {
                    "question": "'Jannat onalar oyog'i ostidadir' hadisining ma'nosi nimaga undaydi?",
                    "options": ["Dunyo bo'ylab sayohat qilishga", "Onani cheksiz e'zozlash, uning xizmatida bo'lib duosini olishga", "Faqat onadan pul so'rashga", "Uyda o'tirishga"],
                    "correct_index": 1,
                    "explanation": "Bu hikmat inson hayotidagi eng buyuk baxt ona roziligi va duosida ekanligini ta'kidlaydi."
                },
                {
                    "question": "Konstitutsiyaga ko'ra voyaga yetgan mehnatga layoqatli farzandlar kimga g'amxo'rlik qilishga majbur?",
                    "options": ["Do'stlariga", "O'z ota-onalariga", "Qo'shnilariga", "Maktabiga"],
                    "correct_index": 1,
                    "explanation": "Farzandlarning keksaygan ota-onalarini parvarishlashi qonuniy konstitutsiyaviy majburiyatdir."
                },
                {
                    "question": "Oilada aka-uka va opa-singillar o'rtasida qanday fazilat ustun bo'lishi kerak?",
                    "options": ["Raqobat va hasad", "Mehr-oqibat, o'zaro ko'mak va hamjihatlik", "Befarqlik", "Kibr"],
                    "correct_index": 1,
                    "explanation": "Qon-qardoshlar orasidagi mehr-oqibat va hamjihatlik oilaning poydevoridir."
                }
            ],
            "tags": ["tarbiya", "oila", "ota-ona", "farzandlik burchi", "mehr-oqibat", "7-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "law-007",
            "slug": "vatanparvarlik-va-milliy-ozlikni-anglash",
            "subject_id": "sub-26",
            "subject_name": "Tarbiya",
            "title": "Vatanparvarlik, milliy g'urur va millatlararo totuvlik madaniyati",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Vatanga muhabbat tushunchasi, ajdodlar merosi bilan faxrlanish, yurt tinchligini asrash va O'zbekistondagi millatlararo bag'rikenglik tamoyillarini o'rganish.",
            "theory": "Vatan — insonning kindik qoni to'kilgan, o'sib-ulg'aygan, ota-bobolari xoki yotgan muqaddas tuprog'idir. Vatanparvarlik — o'z Vatanini sevish, uning tarixi va qadriyatlarini asrash, uning gullab-yashnashiga o'z mehnati va bilimi bilan hissa qo'shish, kerak bo'lsa uni himoya qilish uchun jonini fido etishga tayyorlik fazilatidir. Buyuk allomalarimiz — Temur Malik, Najmiddin Kubro, Jaloliddin Manguberdi vatan ozodligi yo'lida mislsiz jasorat ko'rsatganlar. O'zbekiston — ko'p millatli yurt (130 dan ortiq millat va elat vakillari ahil-inoq yashaydi). Millatlararo totuvlik va diniy bag'rikenglik (tolerantlik) jamiyatimizning eng buyuk boyligidir. Turli millat vakillarining tili, madaniyati va urf-odatlari teng qadrlanadi va davlat tomonidan qo'llab-quvvatlanadi.",
            "examples": [
                {
                    "title": "Jaloliddin Manguberdi jasorati",
                    "problem": "Mo'g'ul bosqinchisi Chingizxon qaysi jasur sarkardaga qarab 'Otaning shunday o'g'li bo'lishi kerak!' deb tan bergan?",
                    "step_by_step": "Sind daryosi bo'yidagi qonli jangda so'nggi nafasigacha kurashib, oti bilan 15 metr baland qirg'oqdan o'zini daryoga tashlab narigi qirg'oqqa suzib o'tgan Najmiddin Kubro shogirdi, vatanparvar sarkarda Jaloliddin Manguberdiga tan bergan.",
                    "answer": "Jaloliddin Manguberdiga"
                },
                {
                    "title": "Haqiqiy vatanparvarlik nimada?",
                    "problem": "Zamonaviy o'quvchi yoki talabaning kundalik hayotdagi vatanparvarligi nimada namoyon bo'ladi?",
                    "step_by_step": "Faqat balandparvoz gaplarda emas, balki chuqur bilim olishda, chet tillarini va zamonaviy kasblarni mukammal egallab, jahon arenalarida bayrog'imizni yuksaklarga ko'tarishda va yurt ravnaqiga hissa qo'shishda namoyon bo'ladi.",
                    "answer": "Chuqur bilim olish, kasb egasi bo'lish va yurt ravnaqiga hissa qo'shishda"
                }
            ],
            "exercise": "O'zbekistondagi 'Milliy madaniy markazlar' qanday vazifani bajaradi?",
            "exercise_solution": "Turli millat vakillarining (rus, qozoq, tojik, koreys, tatar va boshqalar) o'z ona tili, milliy urf-odatlari, folklori va bayramlarini erkin nishonlashini ta'minlab, xalqlar do'stligini mustahkamlaydi.",
            "check_questions": [
                {
                    "question": "'Vatan sajdagoh kabi muqaddasdir' degan hikmat nimani uqtiradi?",
                    "options": ["Boshqa yurtlarga bormaslikni", "Vatanga muhabbat va uning muqaddasligini e'zozlashni", "Faqat tarixni o'rganishni", "Uyda o'tirishni"],
                    "correct_index": 1,
                    "explanation": "Bu hikmat Vatan har bir inson uchun eng muqaddas, tengi yo'q qadriyat ekanligini ifodalaydi."
                },
                {
                    "question": "O'zbekistonda nechta millat va elat vakillari tinch-totuv yashab kelmoqda?",
                    "options": ["Faqat 3 ta", "10 ta", "130 dan ortiq", "50 ta"],
                    "correct_index": 2,
                    "explanation": "O'zbekiston 130 dan ziyod millat va elatlar yagona oila kabi ahil yashaydigan bag'rikeng zamindir."
                },
                {
                    "question": "30-iyul sanasi O'zbekistonda qanday bayram sifatida nishonlanadi?",
                    "options": ["O'qituvchilar kuni", "Xalqlar do'stligi kuni", "Matbuot kuni", "Vatan himoyachilari kuni"],
                    "correct_index": 1,
                    "explanation": "30-iyul mamlakatimizda rasman 'Xalqlar do'stligi kuni' sifatida nishonlanadi."
                }
            ],
            "tags": ["tarbiya", "vatanparvarlik", "jaloliddin manguberdi", "millatlararo totuvlik", "tolerantlik", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "law-008",
            "slug": "ijtimoiy-masuliyat-va-media-savodxonlik",
            "subject_id": "sub-26",
            "subject_name": "Tarbiya",
            "title": "Ijtimoiy mas'uliyat, media savodxonlik va axborot xurujlariga qarshi immunitet",
            "grade_level": "9-11-sinf",
            "difficulty": "O'rta",
            "objective": "Ijtimoiy tarmoqlarda odob-axloq, feyk (soxta) yangiliklarni aniqlash (faktcheking), kibertazyiq (kiberbulling) va ma'naviy immunitetni rivojlantirish.",
            "theory": "Axborot asrida yashayotgan yoshlar uchun media savodxonlik hayotiy zaruratdir. Media savodxonlik — turli manbalardan (internet, ijtimoiy tarmoqlar, TV) kelayotgan axborotlarni tanqidiy tahlil qila olish, to'g'ri va yolg'onni ajratish hamda xavfsiz foydalanish qobiliyatidir. Axborot xurujlari: yoshlar ongini zaharlash, radikallashuv, vatanparvarlikdan uzoqlashtirish va axloqiy tubanlikka undashga qaratilgan g'oyaviy ta'sirlardir. Bunga qarshi eng kuchli qalqon — mustahkam ma'naviy immunitet va chuqur ilmdir. Faktcheking (Fact-checking) qoidalari: 1) Manbaga qarash (rasmiy saytmi yoki noma'lum kanal?); 2) Boshqa ishonchli manbalar bilan solishtirish; 3) Hissiyotga berilmay, xolis mantiq bilan baholash. Ijtimoiy tarmoq madaniyati: kiberbulling (kamsitish, haqorat) qilmaslik, yolg'on ma'lumotlarni tarqatmaslik.",
            "examples": [
                {
                    "title": "Feyk yangilikni fosh qilish",
                    "problem": "'Shoshilinch! Ertaga barcha maktablar butunlay yopiladi, hamma bu xabarni 10 kishiga yuborsin!' xabari kelganda nima qilish kerak?",
                    "step_by_step": "1) Vahima va hissiyotga berilmaslik;\n2) Xabarda rasmiy davlat organi (Maktabgacha va maktab ta'limi vazirligi) havolasi yo'q;\n3) Vazirlikning rasmiy sayti va kanalini tekshirish — rasmiy xabar yo'q;\n4) Bu odatiy feyk (spam). Uni boshqalarga tarqatmaslik va xabar beruvchiga ogohlantirish berish lozim.",
                    "answer": "Tekshirmasdan boshqalarga tarqatmaslik, rasmiy manbani tekshirish"
                },
                {
                    "title": "Kiberbullingga qarshi kurash",
                    "problem": "Ijtimoiy tarmoqda tengdoshingiz sha'niga yomon izohlar yozib kamsitishayotganini ko'rsangiz nima qilasiz?",
                    "step_by_step": "Bunday haqoratomuz izohlarga qo'shilmaslik, jabrlanuvchini ma'naviy qo'llab-quvvatlash, administratorga shikoyat qilish (report) va zarurat tug'ilganda kattalarga/o'qituvchiga xabar berish kerak.",
                    "answer": "Shikoyat qilish (report) va jabrlanuvchini qo'llab-quvvatlash"
                }
            ],
            "exercise": "Axborot xurujlariga qarshi 'Ma'naviy immunitet' tushunchasini izohlang.",
            "exercise_solution": "Insonning har qanday buzg'unchi, yot va zararli g'oyalarga ko'r-ko'rona ergashmasdan, o'z milliy qadriyatlari, aqli va bilimi bilan to'g'ri yo'lni tanlay olish ichki ma'naviy himoya qobiliyatidir.",
            "check_questions": [
                {
                    "question": "Internetdagi xabarning rost yoki yolg'onligini faktlar asosida tekshirish nima deyiladi?",
                    "options": ["Spam", "Faktcheking (Fact-checking)", "Fishing", "Browsing"],
                    "correct_index": 1,
                    "explanation": "Fact-checking axborotning ishonchliligini birlamchi manbalar orqali tekshirish amaliyotidir."
                },
                {
                    "question": "Ijtimoiy tarmoqlarda birovni masxara qilish, qo'rqitish va kamsitish nima deb ataladi?",
                    "options": ["Kiberbulling (Cyberbullying)", "Xakerlik", "Moderatsiya", "Kasting"],
                    "correct_index": 0,
                    "explanation": "Kiberbulling internet orqali amalga oshiriladigan ruhiy tazyiq va bezorilikdir."
                },
                {
                    "question": "Eng ishonchli axborot qaysi manbalarda e'lon qilinadi?",
                    "options": ["Noma'lum Telegram guruhlarida", "Rasmiy davlat axborot agentliklari va tasdiqlangan manbalarda", "Anonim izohlarda", "Tasodifiy bloglarda"],
                    "correct_index": 1,
                    "explanation": "Rasmiy va tekshirilgan ommaviy axborot vositalari haqqoniy ma'lumot kafolatidir."
                }
            ],
            "tags": ["tarbiya", "media savodxonlik", "faktcheking", "feyk xabar", "kiberbulling", "ma'naviy immunitet", "10-sinf"],
            "duration_minutes": 35
        },

        # IQTISODIY BILIM ASOSLARI (4)
        {
            "id": "law-009",
            "slug": "iqtisodiyotga-kirish-ehtiyojlar-va-cheklanganlik",
            "subject_id": "sub-27",
            "subject_name": "Iqtisodiy bilim asoslari",
            "title": "Iqtisodiyotga kirish: Cheksiz ehtiyojlar, cheklangan resurslar va Iqtisodiyotning 3 ta asosiy savoli",
            "grade_level": "8-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Iqtisodiyot predmeti, moddiy va nomoddiy ne'matlar, ishlab chiqarish omillari (yer, mehnat, kapital, tadbirkorlik) hamda cheklanganlik muammosini tushunish.",
            "theory": "Iqtisodiyot — insonlarning cheksiz ehtiyojlarini cheklangan resurslar sharoitida maksimal qondirish qonuniyatlarini o'rganadigan fandir (Oikos — xo'jalik, nomos — qonun). Bosh muammo: Ehtiyojlar cheksiz, ammo ularni qondiruvchi resurslar (tabiiy boyliklar, xomashyo, vaqt, pul) cheklangandir. Ishlab chiqarishning 4 ta asosiy omili: 1) Yer (tabiiy resurslar — daromadi: renta); 2) Mehnat (inson kuchi va aqli — daromadi: ish haqi); 3) Kapital (binolar, stanoklar, mashinalar, asboblar — daromadi: foiz); 4) Tadbirkorlik qobiliyati (barcha omillarni birlashtirib xavf-xatarga borish — daromadi: foyda). Har qanday iqtisodiy tizim 3 ta asosiy savolga javob berishi shart: 1) Nima ishlab chiqarish kerak? 2) Qanday ishlab chiqarish kerak? 3) Kim uchun ishlab chiqarish kerak? Muqobil qiymat (imkoniyat qiymati) — biror tanlov qilinganda voz kechilgan ikkinchi eng yaxshi muqobil imkoniyat qiymatidir.",
            "examples": [
                {
                    "title": "Muqobil qiymatni hisoblash",
                    "problem": "Sizda 50 000 so'm pul bor. Siz yo yangi kitob sotib olishingiz, yo kinoga chipta xarid qilishingiz mumkin. Agar kitob sotib olsangiz, uning muqobil qiymati nima bo'ladi?",
                    "step_by_step": "Muqobil qiymat — bu tanlov sababli voz kechilgan eng afzal imkoniyat. Kitob sotib olingach, kinoga borishdan va kinodan olinadigan zavqdan voz kechildi. Demak, kitobning muqobil qiymati — kinoga tushish imkoniyatidir.",
                    "answer": "Kinoga borish imkoniyati"
                },
                {
                    "title": "Ishlab chiqarish omillari",
                    "problem": "Novvoyxona faoliyatidagi 4 ta ishlab chiqarish omilini ko'rsating.",
                    "step_by_step": "Yer — un, suv, bino turgan yer; Mehnat — nonvoy mehnati; Kapital — pechka, xamir qoruvchi uskuna, patnislar; Tadbirkorlik — novvoyxona egasining yangi xil nonlar chiqarish va boshqaruv tashabbusi.",
                    "answer": "Yer (un/suv), Mehnat (nonvoy), Kapital (pech), Tadbirkorlik (biznes egasi)"
                }
            ],
            "exercise": "Iqtisodiyotning 3 ta asosiy savolini sanang.",
            "exercise_solution": "1. Nima ishlab chiqarish kerak? 2. Qanday ishlab chiqarish kerak? 3. Kim uchun ishlab chiqarish kerak?",
            "check_questions": [
                {
                    "question": "Iqtisodiyot fanining bosh fundamental muammosi nima?",
                    "options": ["Pul yetishmasligi", "Cheksiz ehtiyojlar va cheklangan resurslar qarama-qarshiligi", "Ishsizlik", "Savdo cheklovlari"],
                    "correct_index": 1,
                    "explanation": "Inson ehtiyojlari doim o'sib boradi, lekin tabiat va jamiyat resurslari cheklangandir."
                },
                {
                    "question": "Bino, mashinalar, stanok va uskunalar qaysi ishlab chiqarish omiliga kiradi?",
                    "options": ["Mehnat", "Yer", "Kapital (jismoniy kapital)", "Tadbirkorlik"],
                    "correct_index": 2,
                    "explanation": "Mahsulot ishlab chiqarishda ishlatiladigan vositalar jismoniy kapital deyiladi."
                },
                {
                    "question": "Biror qaror qabul qilinganda voz kechilgan ikkinchi eng yaxshi muqobil imkoniyat nima deyiladi?",
                    "options": ["Foyda", "Muqobil qiymat (imkoniyat boy berilishi)", "Zarar", "Soliq"],
                    "correct_index": 1,
                    "explanation": "Opportunity cost (muqobil qiymat) — eng yaxshi rad etilgan variant qiymatidir."
                }
            ],
            "tags": ["iqtisodiyot", "ehtiyojlar", "resurslar", "muqobil qiymat", "kapital", "8-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "law-010",
            "slug": "bozor-iqtisodiyoti-talab-va-taklif-qonuni",
            "subject_id": "sub-27",
            "subject_name": "Iqtisodiy bilim asoslari",
            "title": "Bozor mexanizmi: Talab va taklif qonuni hamda muvozanatli narx",
            "grade_level": "8-9-sinf",
            "difficulty": "O'rta",
            "objective": "Talab qonuni (Demand), taklif qonuni (Supply), narxning talab va taklifga ta'siri hamda muvozanatli narx (Equilibrium Price)ning shakllanishini o'rganish.",
            "theory": "Bozor — xaridorlar (iste'molchilar) va sotuvchilar (ishlab chiqaruvchilar) o'rtasidagi oldi-sotdi munosabatlari tizimidir. Asosiy bozor qonuniyatlari: 1) Talab (Demand, D) — iste'molchilarning ma'lum narxda sotib olishga qodir bo'lgan tovarlar miqdoridir. Talab qonuni: Boshqa shartlar o'zgarmaganda, tovar narxi oshsa unga bo'lgan talab kamayadi, narx pasaysa talab ortadi (teskari bog'liqlik: P oshsa, Q_d kamayadi); 2) Taklif (Supply, S) — ishlab chiqaruvchilarning ma'lum narxda bozorga chiqarishga tayyor tovarlar miqdoridir. Taklif qonuni: Tovar narxi oshsa taklif miqdori ortadi, narx pasaysa taklif kamayadi (to'g'ri bog'liqlik: P oshsa, Q_s ortadi); 3) Bozor muvozanati (Equilibrium): Talab va taklif miqdorlari tenglashgan nuqta (Q_d = Q_s) muvozanat nuqtasi deyiladi, unga mos kelgan narx muvozanatli narx (P_e) bo'ladi. Agar narx muvozanatdan yuqori bo'lsa tovar ortiqchaligi (defitsit emas, profisit), past bo'lsa tovar taqchilligi (defitsit) yuzaga keladi.",
            "examples": [
                {
                    "title": "Bozor muvozanatini hisoblash",
                    "problem": "Talab funksiyasi Q_d = 100 - 2P, taklif funksiyasi Q_s = 20 + 2P bo'lsa, muvozanatli narx (P) va muvozanatli miqdorni (Q) toping.",
                    "step_by_step": "1) Muvozanat sharti: Q_d = Q_s.\n2) 100 - 2P = 20 + 2P.\n3) 4P = 80 => P = 20 so'm (muvozanatli narx).\n4) Miqdor: Q = 100 - 2*20 = 60 dona.",
                    "answer": "Narx P = 20, Miqdor Q = 60"
                },
                {
                    "title": "Talabga ta'sir etuvchi nonarx omillar",
                    "problem": "Aholi daromadlari sezilarli darajada oshsa, sifatli mebellar bozoridagi talab egri chizig'i qayerga siljiydi?",
                    "step_by_step": "Aholining xarid qobiliyati ortishi bilan narx o'zgarmasa ham ko'proq xarid qilinadi, ya'ni talab ortadi va talab chizig'i o'ngga-yuqoriga siljiydi.",
                    "answer": "O'ngga-yuqoriga (talab ortishi tomonga) siljiydi"
                }
            ],
            "exercise": "Bozorda narx sun'iy ravishda muvozanat narxidan past qilib belgilansa, qanday hodisa ro'y beradi?",
            "exercise_solution": "Talab keskin oshib ketadi, ammo ishlab chiqaruvchilar arzon narxda kam mahsulot chiqaradi — natijada tovar taqchilligi (defitsit) va navbatlar yuzaga keladi.",
            "check_questions": [
                {
                    "question": "Talab qonuniga ko'ra tovar narxi pasaysa, unga bo'lgan talab hajmi qanday o'zgaradi?",
                    "options": ["Kamayadi", "Oshadi", "O'zgarmaydi", "Nolga tushadi"],
                    "correct_index": 1,
                    "explanation": "Narx arzonlashganda odamlar ushbu tovarni ko'proq xarid qila oladi (talab hajmi oshadi)."
                },
                {
                    "question": "Bozor muvozanati (Equilibrium) qachon qaror topadi?",
                    "options": ["Sotuvchilar ko'payganda", "Talab miqdori taklif miqdoriga tenglashganda (Q_d = Q_s)", "Davlat narxni belgilaganda", "Faqat eksport bo'lganda"],
                    "correct_index": 1,
                    "explanation": "Xaridorlar olmoqchi bo'lgan miqdor sotuvchilar sotmoqchi bo'lgan miqdorga tenglashganida muvozanat hosil bo'ladi."
                },
                {
                    "question": "Agar taklif talabdan sezilarli darajada ko'p bo'lsa (Q_s > Q_d), tovar narxi bilan nima sodir bo'ladi?",
                    "options": ["Narx keskin oshadi", "Bozorda raqobat sababli narx pasayadi", "O'zgarmaydi", "Tovar yo'qoladi"],
                    "correct_index": 1,
                    "explanation": "Tovarning ko'pligi (ortiqchaligi) sotuvchilarni narxni tushirishga majbur qiladi."
                }
            ],
            "tags": ["iqtisodiyot", "talab", "taklif", "bozor mexanizmi", "muvozanatli narx", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "law-011",
            "slug": "pul-inflyatsiya-va-bank-tizimi",
            "subject_id": "sub-27",
            "subject_name": "Iqtisodiy bilim asoslari",
            "title": "Pulning kelib chiqishi, funksiyalari, inflyatsiya va zamonaviy bank tizimi",
            "grade_level": "9-10-sinf",
            "difficulty": "O'rta",
            "objective": "Pulning 5 ta funksiyasi, inflyatsiya sabablari va oqibatlari, Markaziy bank va tijorat banklari faoliyati hamda kredit foizlarini hisoblash.",
            "theory": "Pul — boshqa barcha tovarlar va xizmatlar uchun umumiy ekvivalent bo'lgan maxsus tovardir. Pul evolyutsiyasi: tovar pullar (mol, tuz, chig'anoqlar) -> metall pullar (oltin, kumush tangalar) -> qog'oz pullar (banknotlar) -> elektron pullar va raqamli valyutalar. Pulning funksiyalari: 1) Qiymat o'lchovi (narxni belgilaydi); 2) Muomala vositasi (oldi-sotdida vositachi); 3) To'lov vositasi (qarz, soliq, maosh to'lash); 4) Jamg'arish vositasi (boylik to'plash). Inflyatsiya — mamlakatda narx-navoning umumiy darajasi o'sishi va pulning xarid qobiliyati pasayishi (qadrsizlanishi). Sabablari: muomalada haddan tashqari ko'p pul bo'lishi (talab inflyatsiyasi), xomashyo va yoqilg'i narxi oshishi (xarajatlar inflyatsiyasi). Bank tizimi: 1) Markaziy bank — pul emissiyasi (chop etish), milliy valyutani barqaror saqlash va banklarni nazorat qilish; 2) Tijorat banklari — aholi va korxonalardan omonat (depozit) qabul qilish va kreditlar berish.",
            "examples": [
                {
                    "title": "Inflyatsiyaning xarid qobiliyatiga ta'siri",
                    "problem": "Yillik inflyatsiya darajasi 10% bo'lsa, o'tgan yili 100 000 so'mga olingan tovarlar savatchasini xarid qilish uchun bu yil necha pul kerak bo'ladi?",
                    "step_by_step": "Narxlar 10% ga oshadi: 100 000 * 0.10 = 10 000 so'm qimmatlashadi. Yangi narx: 100 000 + 10 000 = 110 000 so'm.",
                    "answer": "110 000 so'm"
                },
                {
                    "title": "Bank kredit foizini hisoblash",
                    "problem": "Tadbirkor yillik 20% stavka bilan 1 yilga 10 000 000 so'm oddiy kredit oldi. Yil oxirida u qancha foiz va jami qancha pul qaytaradi?",
                    "step_by_step": "1) Foiz to'lovi = 10 000 000 * 0.20 = 2 000 000 so'm;\n2) Jami qaytariladigan summa = 10 000 000 + 2 000 000 = 12 000 000 so'm.",
                    "answer": "Foiz: 2 000 000 so'm, Jami: 12 000 000 so'm"
                }
            ],
            "exercise": "Markaziy bank asosiy stavkani (qayta moliyalash stavkasi) oshirsa, tijorat banklarining kreditlari qimmatlashadimi yoki arzonlashadimi?",
            "exercise_solution": "Qimmatlashadi: Markaziy bank stavkasi oshganda pul qimmatlashadi, tijorat banklari ham kredit foizlarini oshiradi, bu esa iqtisodiyotda inflyatsiyani jilovlash uchun qo'llaniladi.",
            "check_questions": [
                {
                    "question": "Mamlakatda tovarlar narxining umumiy ko'tarilishi va pulning qadrsizlanishi nima deyiladi?",
                    "options": ["Deflyatsiya", "Inflyatsiya", "Devalvatsiya", "Stagnatsiya"],
                    "correct_index": 1,
                    "explanation": "Inflyatsiya tovarlar narxining barqaror o'sishi va pulning xarid qobiliyati tushishidir."
                },
                {
                    "question": "Mamlakatda qog'oz va tanga pullarni muomalaga chiqarish (emissiya) huquqiga faqat qaysi tashkilot ega?",
                    "options": ["Tijorat banklari", "Markaziy bank", "Moliya vazirligi", "Soliq qo'mitasi"],
                    "correct_index": 1,
                    "explanation": "Faqat davlatning Markaziy banki qonuniy milliy valyutani chiqarish monopoliyasiga ega."
                },
                {
                    "question": "Bankka foiz evaziga vaqtincha saqlashga qo'yilgan pul nima deyiladi?",
                    "options": ["Kredit", "Omonat (depozit)", "Soliq", "Lizing"],
                    "correct_index": 1,
                    "explanation": "Depozit — fuqarolarning bankka daromad olish maqsadida joylashtirgan omonatidir."
                }
            ],
            "tags": ["iqtisodiyot", "pul", "inflyatsiya", "markaziy bank", "kredit", "depozit", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "law-012",
            "slug": "shaxsiy-moliya-va-investitsiya-savodxonligi",
            "subject_id": "sub-27",
            "subject_name": "Iqtisodiy bilim asoslari",
            "title": "Moliyaviy savodxonlik: Shaxsiy byudjet, jamg'arma, aksiyalar va murakkab foiz qoidasi",
            "grade_level": "11-sinf",
            "difficulty": "O'rta",
            "objective": "Daromad va xarajatlar balansi (50/30/20 qoidasi), moliyaviy xavfsizlik yostiqchasi, aksiyalar va obligatsiyalar hamda Eynshteynning 'murakkab foiz' mo'jizasini o'rganish.",
            "theory": "Moliyaviy savodxonlik — shaxsiy pullarni oqilona boshqarish, daromad va xarajatlarni rejalashtirish hamda investitsiya orqali kapitalni ko'paytirish ko'nikmasidir. Shaxsiy byudjetni taqsimlashning mashhur '50/30/20 qoidasi': 50% — zaruriy xarajatlar (oziq-ovqat, kommunal, transport); 30% — xohish-istaklar (dam olish, ko'ngilochar, kiyim); 20% — jamg'arma va qarz to'lash. Moliyaviy xavfsizlik yostiqchasi: kutilmagan vaziyatlar uchun shaxsning kamida 3-6 oylik xarajatlariga teng zaxira puli. Investitsiya instrumentlari: 1) Bank depozitlari (past xavf, barqaror daromad); 2) Obligatsiyalar (qarz qog'ozi, davlat yoki kompaniyaga qarz berish, foiz olish); 3) Aksiyalar (kompaniya ulushiga egalik qilish, dividend olish va narx o'sishidan foyda qilish). Murakkab foiz (Compound interest) — olingan foiz daromadining asosiy summaga qo'shilib, keyingi davrda foiz ustiga ham foiz hisoblanishi: A = P * (1 + r/n)^(n*t).",
            "examples": [
                {
                    "title": "50/30/20 qoidasini qo'llash",
                    "problem": "Oylik daromadi 6 000 000 so'm bo'lgan mutaxassis 50/30/20 qoidasi bo'yicha pulini qanday taqsimlashi kerak?",
                    "step_by_step": "1) Zaruriy xarajatlar (50%): 6 000 000 * 0.50 = 3 000 000 so'm;\n2) Xohish-istaklar (30%): 6 000 000 * 0.30 = 1 800 000 so'm;\n3) Kelajak jamg'armasi va investitsiya (20%): 6 000 000 * 0.20 = 1 200 000 so'm.",
                    "answer": "3 mln (zaruriy), 1.8 mln (xohishlar), 1.2 mln (jamg'arma)"
                },
                {
                    "title": "Murakkab foiz qudrati",
                    "problem": "10 000 000 so'mni yillik 20% murakkab foiz bilan 2 yilga qo'yilsa, muddat oxirida qancha pul bo'ladi?",
                    "step_by_step": "1-yil oxirida: 10 000 000 + 20% = 12 000 000 so'm;\n2-yil oxirida: 12 000 000 ga 20% hisoblanadi: 12 000 000 * 1.20 = 14 400 000 so'm (oddiy foizdan 400 000 so'm ko'p!).",
                    "answer": "14 400 000 so'm"
                }
            ],
            "exercise": "Aksiya va obligatsiya o'rtasidagi asosiy farq nimada?",
            "exercise_solution": "Aksiya egasi kompaniyaning hammuallifiga (ulushdoriga) aylanadi va biznes xavfini bo'lishadi; Obligatsiya egasi esa shunchaki kompaniyaga foiz evaziga qarz bergan kreditor hisoblanadi (xavfi pastroq).",
            "check_questions": [
                {
                    "question": "Moliyaviy xavfsizlik yostiqchasi (favqulodda zaxira) qancha mablag'ni tashkil qilishi tavsiya etiladi?",
                    "options": ["1 kunlik xarajat", "Kamida 3-6 oylik doimiy xarajatlar miqdorida", "10 yillik maosh", "Zaxira kerak emas"],
                    "correct_index": 1,
                    "explanation": "Ish yo'qotilganda yoki kutilmagan vaziyatda 3-6 oylik xarajatlar zaxirasi moliyaviy barqarorlikni ta'minlaydi."
                },
                {
                    "question": "Kompaniyaga egalik ulushini beruvchi qimmatli qog'oz nima deb ataladi?",
                    "options": ["Obligatsiya", "Aksiya", "Veksel", "Chek"],
                    "correct_index": 1,
                    "explanation": "Aksiya egasi kompaniya foydasidan dividend olish va korxona qiymati o'sishidan daromad qilish huquqiga ega bo'ladi."
                },
                {
                    "question": "Albert Eynshteyn 'Dunyoning sakkizinchi mo'jizasi' deb qaysi moliyaviy hodisani atagan?",
                    "options": ["Inflyatsiya", "Murakkab foiz (Compound interest)", "Qog'oz pul", "Kredit karta"],
                    "correct_index": 1,
                    "explanation": "Murakkab foiz uzoq muddatda kichik jamg'armani ham ulkan boylikka aylantirish quvvatiga ega bo'lgani uchun shunday atalgan."
                }
            ],
            "tags": ["moliyaviy savodxonlik", "shaxsiy byudjet", "investitsiya", "aksiya", "murakkab foiz", "11-sinf"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_law_economics_materials()
    print(f"Generated {len(mats)} Law/Economics materials.")
