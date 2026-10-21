# -*- coding: utf-8 -*-
"""
Builder for Ona tili va O'zbek adabiyoti (18 materials: lit-001 to lit-018)
- sub-15: Ona tili (10: lit-001 to lit-010)
- sub-16: O'zbek adabiyoti (8: lit-011 to lit-018)
"""

def get_language_literature_materials():
    materials = [
        # ONA TILI (10)
        {
            "id": "lit-001",
            "slug": "fonetika-unli-va-undosh-tovushlar-tasnifi",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Fonetika: nutq tovushlari, unlilar va undoshlarning tasnifi",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Nutq tovushlari va harflar farqi, 6 ta asosiy unli va 24 ta undosh tovushning hosil bo'lish o'rni va usuliga ko'ra tasnifini bilish.",
            "theory": "Fonetika — tilning tovush qurilishini o'rganadigan tilshunoslik bo'limidir. Tovush — talaffuz qilinadi va eshitiladi, harf — yoziladi va ko'riladi. O'zbek adabiy tilida 6 ta unli tovush (a, o, i, u, o', e) va 24 ta undosh tovush bor. Unli tovushlar og'iz bo'shlig'ida to'siqqa uchramay, faqat ovozdan hosil bo'ladi va bo'g'in hosil qiladi. Undosh tovushlar to'siqqa uchrab hosil bo'ladi va ovoz hamda shovqin ishtirokiga ko'ra jarangli (b, d, z, v, g, j...), jarangsimon/sonor (m, n, l, r, ng) va jarangsiz (p, t, s, f, k, sh, ch, x, q, h) undoshlarga bo'linadi. Singarmonizm va tovush o'zgarishlari: tovush tushishi (shahri -> shahar+i emas, shahar -> shahri), tovush ortishi va almashishi (yurak+i -> yuragi).",
            "examples": [
                {
                    "title": "Tovush almashinishi qoidasi",
                    "problem": "'Kitob' va 'quloq' so'zlariga egalik qo'shimchasi qo'shilganda qanday fonetik hodisa yuz beradi?",
                    "step_by_step": "1) Kitob + i = kitobi (b saqlanadi), lekin oxiri k/q bilan tugagan so'zlarda: bilak + i -> bilagi (k -> g almashadi);\n2) Quloq + i -> qulog'i (q -> g' almashadi). Bu jarangsiz undoshning jarangli juftiga almashinishidir.",
                    "answer": "k -> g va q -> g' tovush almashinishi"
                },
                {
                    "title": "Jarangli va jarangsiz juftliklar",
                    "problem": "b, d, z, g jarangli undoshlarining jarangsiz juftlarini toping.",
                    "step_by_step": "b -> p; d -> t; z -> s; g -> k.",
                    "answer": "p, t, s, k"
                }
            ],
            "exercise": "'Ko'ngil' va 'burun' so'zlariga III shaxs egalik qo'shimchasi (-i) qo'shilganda so'z qanday yoziladi va qaysi hodisa ro'y beradi?",
            "exercise_solution": "Ko'ngli, burni. Ikkinchi bo'g'indagi tor unli (i, u) tushib qoladi (tovush tushishi hodisasi).",
            "check_questions": [
                {
                    "question": "O'zbek adabiy tilida nechta unli tovush mavjud?",
                    "options": ["5 ta", "6 ta", "8 ta", "10 ta"],
                    "correct_index": 1,
                    "explanation": "O'zbek tilida 6 ta asosiy unli tovush bor: a, o, i, u, o', e."
                },
                {
                    "question": "Faqat ovozdan iborat bo'lgan, bo'g'in hosil qiluvchi tovushlar nima deyiladi?",
                    "options": ["Undoshlar", "Unlilar", "Sonorlar", "Bo'g'iz tovushlari"],
                    "correct_index": 1,
                    "explanation": "Unli tovushlar to'siqsiz chiqadi va har bir bo'g'inning asosini tashkil qiladi."
                },
                {
                    "question": "'Barg' so'zi oxiridagi jarangli 'g' tovushi talaffuzda qaysi tovushga aylanadi?",
                    "options": ["k", "q", "x", "h"],
                    "correct_index": 0,
                    "explanation": "So'z oxiridagi jarangli undoshlar talaffuzda ko'pincha o'zining jarangsiz juftiga aylanadi (bark deb aytiladi)."
                }
            ],
            "tags": ["ona tili", "fonetika", "unlilar", "undoshlar", "tovush almashinuvi", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "lit-002",
            "slug": "leksikologiya-soz-manosi-sinonim-antonim-omonim",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Leksikologiya: so'zning to'g'ri va ko'chma ma'nolari, omonimlar, sinonimlar, antonimlar",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "So'zning leksik boyligi, ko'chma ma'nolar (metafora, metonimiya), ma'nodosh, shakldosh va zid ma'noli so'zlardan nutqda to'g'ri foydalanish.",
            "theory": "Tilning lug'at tarkibini (so'z boyligini) o'rganadigan tilshunoslik bo'limi leksikologiya deyiladi. So'zning boshlang'ich asosiy ma'nosi to'g'ri ma'no, o'xshashlik yoki aloqadorlik asosida ko'chgan ma'nosi ko'chma ma'no deyiladi (oltin soat — to'g'ri, oltin fasl — ko'chma). Omonimlar (shakldosh so'zlar) — aytilishi va yozilishi bir xil, ammo ma'nosi butunlay boshqa bo'lgan so'zlar (ot — hayvon, ot — harakat, ot — ism). Sinonimlar (ma'nodosh so'zlar) — yozilishi har xil, ma'nosi bir-biriga yaqin so'zlar (yuz, bet, chehra, oraz, aft; ulug', katta, azim). Ular nutqni boyitadi va takrorning oldini oladi. Antonimlar (zid ma'noli so'zlar) — bir-biriga qarama-qarshi ma'noni bildiruvchi so'zlar (oq — qora, yaxshi — yomon, baland — past). Paronimlar — talaffuzi o'xshash, ma'nosi farqli so'zlar (asl — asr, ta'lim — ta'zim).",
            "examples": [
                {
                    "title": "Ko'chma ma'no (metafora)",
                    "problem": "'Quyosh kulib boqdi' va 'temir intizom' birikmalaridagi ko'chma ma'nolarni tushuntiring.",
                    "step_by_step": "Insonning kulish xususiyati quyoshga o'xshatish orqali ko'chirilgan (jonlantirish/metafora); temirning mustahkamligi intizomga ko'chirilgan.",
                    "answer": "Metafora (belgi va harakatning o'xshashlik asosida ko'chishi)"
                },
                {
                    "title": "Omonimlarni aniqlash",
                    "problem": "'Yoz' so'zining kamida 2 ta mustaqil ma'nosini ko'rsating.",
                    "step_by_step": "1) Yoz — yil fasli (issiq fasl, ot);\n2) Yoz — qog'ozga tushirmoq (buyruq fe'li);\n3) Yoz — tugunni yozmoq (ochmoq fe'li).",
                    "answer": "Fasl nomi (ot) va harakat (fe'l)"
                }
            ],
            "exercise": "'Katta' so'zining 3 ta sinonimini yozing va gaplarda qo'llang.",
            "exercise_solution": "Ulug', yirik, azim. Masalan: 'Azim chinor soyasida dam oldik'.",
            "check_questions": [
                {
                    "question": "Shakli bir xil, ammo ma'nosi butunlay boshqa bo'lgan so'zlar nima deyiladi?",
                    "options": ["Sinonimlar", "Antonimlar", "Omonimlar", "Paronimlar"],
                    "correct_index": 2,
                    "explanation": "Yozilishi bir xil, ma'nosi mustaqil bo'lgan so'zlar omonimlar (shakldosh so'zlar) deyiladi."
                },
                {
                    "question": "Nutqda so'z takrorlanishining oldini olish uchun qaysi vositadan foydalaniladi?",
                    "options": ["Antonimlar", "Sinonimlar", "Omonimlar", "Qisqartmalar"],
                    "correct_index": 1,
                    "explanation": "Sinonimlar bir xil ma'noni turli so'zlar bilan ifodalab, nutqni rang-barang qiladi."
                },
                {
                    "question": "'Ko'p — oz' so'zlari o'zaro qanday munosabatda?",
                    "options": ["Omonim", "Sinonim", "Antonim", "Paronim"],
                    "correct_index": 2,
                    "explanation": "Bir-biriga qarama-qarshi ma'noni anglatuvchi so'zlar antonimlar deyiladi."
                }
            ],
            "tags": ["ona tili", "leksikologiya", "sinonim", "antonim", "omonim", "metafora", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "lit-003",
            "slug": "morfemika-va-soz-yasalishi",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Morfemika: so'zning tarkibi, o'zak va qo'shimchalar, so'z yasalish usullari",
            "grade_level": "6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "O'zak, asos, so'z yasovchi va shakl yasovchi (lug'aviy hamda sintaktik) qo'shimchalarni ajrata olish hamda so'z yasalish qoidalarini bilish.",
            "theory": "Morfemika — so'z tarkibini (morfemalarni) o'rganadi. So'zning ma'noli eng kichik bo'lagi morfema deyiladi. Morfemalar ikki xil: o'zak va qo'shimcha. O'zak — so'zning asosiy lug'aviy ma'nosini anglatuvchi qismi. Qo'shimchalar 2 ta katta guruhga bo'linadi: 1) So'z yasovchi qo'shimchalar — yangi ma'noli so'z hosil qiladi (ish -> ishchi, bog' -> bog'bon, do'st -> do'stlik, o'qi -> o'qituvchi); 2) Shakl yasovchi qo'shimchalar — yangi so'z yasamaydi, so'zning shaklini o'zgartiradi (lug'aviy shakl: kichraytirish -cha, ko'plik -lar; sintaktik shakl: kelishik -ning, -ni, -ga, egalik -im, -ing). So'z yasalish usullari: affiksatsiya (qo'shimcha qo'shish) va kompozitsiya (qo'shma so'zlar: oyna+vola, bilag+uzuk; juft so'zlar: ota-ona; takroriy: baland-baland).",
            "examples": [
                {
                    "title": "So'zni tarkibiga ko'ra tahlil qilish",
                    "problem": "'Vatandoshlarimizga' so'zini morfemalarga ajrating.",
                    "step_by_step": "1) Vatan — o'zak morfema;\n2) -dosh — so'z yasovchi qo'shimcha (yangi so'z: vatandosh);\n3) -lar — ko'plik qo'shimchasi (lug'aviy shakl yasovchi);\n4) -imiz — I shaxs ko'plik egalik qo'shimchasi (sintaktik shakl);\n5) -ga — jo'nalish kelishigi qo'shimchasi (sintaktik shakl).",
                    "answer": "Vatan (o'zak) + dosh (yasovchi) + lar + imiz + ga (shakl yasovchilar)"
                },
                {
                    "title": "Qo'shma so'z hosil qilish",
                    "problem": "Har xil so'z turkumlaridan qo'shma so'z yasalishiga misol keltiring.",
                    "step_by_step": "Echki+emar (ot+fe'l = ot); Temir+yo'l (ot+ot = ot); Oq+ko'ngil (sifat+ot = sifat).",
                    "answer": "Echkiemar, temiryo'l, oqko'ngil"
                }
            ],
            "exercise": "Berilgan qo'shimchalardan so'z yasovchi va shakl yasovchilarni ajrating: -kor, -lar, -chan, -ning, -chi.",
            "exercise_solution": "So'z yasovchilar: -kor (paxtakor), -chan (uyatchan), -chi (temirchi). Shakl yasovchilar: -lar (kitoblar), -ning (maktabning).",
            "check_questions": [
                {
                    "question": "Yangi so'z yasaydigan qo'shimchalar qanday nomlanadi?",
                    "options": ["Lug'aviy shakl yasovchi", "Sintaktik shakl yasovchi", "So'z yasovchi qo'shimchalar", "Kelishik qo'shimchalari"],
                    "correct_index": 2,
                    "explanation": "So'z yasovchi qo'shimchalar asosga qo'shilib yangi lug'aviy ma'nodagi yangi so'z hosil qiladi."
                },
                {
                    "question": "Kelishik va egalik qo'shimchalari qaysi guruhga kiradi?",
                    "options": ["So'z yasovchi", "Sintaktik shakl yasovchi", "O'zak morfema", "Uslubiy qo'shimchalar"],
                    "correct_index": 1,
                    "explanation": "Ular so'zlarni gapda bir-biriga bog'lash uchun xizmat qiluvchi sintaktik shakllardir."
                },
                {
                    "question": "Quyidagi so'zlardan qaysi biri qo'shma so'z?",
                    "options": ["Paxtakor", "Ota-ona", "Oshqovoq", "Bog'bon"],
                    "correct_index": 2,
                    "explanation": "Osh va qovoq mustaqil o'zaklarining birikuvidan 'oshqovoq' qo'shma so'zi hosil bo'lgan."
                }
            ],
            "tags": ["ona tili", "morfemika", "o'zak", "qo'shimcha", "so'z yasalishi", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "lit-004",
            "slug": "ot-soz-turkumi-va-kelishiklar",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Ot so'z turkumi: egalik, ko'plik va kelishik tizimi",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Otning grammatik belgilari, atoqli va turdosh otlar, egalik kategoriyasi hamda 6 ta kelishikning qo'llanishi va imlosini to'liq o'zlashtirish.",
            "theory": "Kim? Nima? Qayer? so'rog'iga javob bo'lib, narsa-buyum, shaxs, joy, tushunchalarni bildiruvchi mustaqil so'z turkumi ot deyiladi. Turlari: Atoqli otlar (yakka narsalarga berilgan maxsus nomlar: Alisher Navoiy, Toshkent, 'O'tkan kunlar' — bosh harf bilan yoziladi); Turdosh otlar (bir jinsdagi narsalarning umumiy nomi: shahar, daryo, kitob). Otning grammatik kategoriyalari: 1) Ko'plik: -lar qo'shimchasi; 2) Egalik kategoriyasi: narsaning kimga tegishli ekanligini bildiradi (I shaxs: -im/-m, -imiz; II shaxs: -ing/-ng, -ingiz; III shaxs: -i/-si); 3) Kelishik kategoriyasi (6 ta): Bosh kelishik (belgisiz, kim? nima?), Qaratqich kelishigi (-ning, kimning? nimaning?), Tushum kelishigi (-ni, kimni? nimani?), Jo'nalish kelishigi (-ga/-ka/-qa, kimgacha? nimaga? qayerga?), O'rin-payt kelishigi (-da, kimda? nimada? qayerda?), Chiqish kelishigi (-dan, kimdan? nimadan? qayerdan?).",
            "examples": [
                {
                    "title": "Kelishik qo'shimchalari imlosi",
                    "problem": "'Tog'', 'bog'', 'yurak', 'chelak' so'zlariga jo'nalish kelishigi qo'shilganda qanday yoziladi?",
                    "step_by_step": "1) Oxiri k bilan tugasa -ka qo'shiladi: yurakka, chelakka.\n2) Oxiri q bilan tugasa -qa qo'shiladi: qishloqqa.\n3) Oxiri g' bilan tugasa -ga qo'shiladi: tog'ga, bog'ga.",
                    "answer": "Yurakka, chelakka, tog'ga, bog'ga"
                },
                {
                    "title": "Qaratqich va tushum kelishigining belgisiz qo'llanishi",
                    "problem": "'Maktab bog'i' va 'kitob o'qidi' birikmalaridagi belgisiz kelishiklarni aniqlang.",
                    "step_by_step": "1) Maktab(ning) bog'i — qaratqich kelishigi belgisiz qo'llangan.\n2) Kitob(ni) o'qidi — tushum kelishigi belgisiz qo'llangan.",
                    "answer": "Qaratqich va tushum kelishigi"
                }
            ],
            "exercise": "'Daftar' so'zini barcha 6 ta kelishikda turlang.",
            "exercise_solution": "Bosh: daftar; Qaratqich: daftarning; Tushum: daftarni; Jo'nalish: daftarga; O'rin-payt: daftarda; Chiqish: daftardan.",
            "check_questions": [
                {
                    "question": "O'zbek tilida nechta kelishik mavjud?",
                    "options": ["4 ta", "5 ta", "6 ta", "7 ta"],
                    "correct_index": 2,
                    "explanation": "O'zbek tilida 6 ta kelishik bor: Bosh, Qaratqich, Tushum, Jo'nalish, O'rin-payt, Chiqish."
                },
                {
                    "question": "'Kitobim' so'zidagi -im qo'shimchasi qanday qo'shimcha?",
                    "options": ["Ko'plik", "I shaxs egalik", "Jo'nalish kelishigi", "So'z yasovchi"],
                    "correct_index": 1,
                    "explanation": "-im qo'shimchasi narsa I shaxsga (menga) tegishli ekanligini ko'rsatuvchi egalik qo'shimchasidir."
                },
                {
                    "question": "Chiqish kelishigi qaysi qo'shimcha yordamida yasaladi?",
                    "options": ["-ga", "-da", "-dan", "-ning"],
                    "correct_index": 2,
                    "explanation": "Chiqish kelishigi qo'shimchasi -dan bo'lib, harakatning boshlanish o'rnini bildiradi."
                }
            ],
            "tags": ["ona tili", "ot", "kelishiklar", "egalik", "bosh kelishik", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lit-005",
            "slug": "sifat-va-son-soz-turkumlari",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Sifat va son: darajalar, ma'no turlari va yozilish qoidalari",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Sifat darajalari (oddiy, qiyosiy, orttirma, ozaytirma) va son ma'no turlari (sanoq, dona, tartib, jamlovchi, chamalash, taqsim) qoidalarini amalda qo'llash.",
            "theory": "Sifat — narsa-buyumning belgisini (rangi, shakli, xususiyati, mazasini) bildiruvchi so'z turkumi (Qanday? Qanaqa?). Sifat darajalari: 1) Oddiy daraja — belgi me'yorda (oq, shirin, baland); 2) Qiyosiy daraja — belgi me'yordan ozroq yoki ko'proq (-roq: oqroq, shirinroq); 3) Orttirma daraja — eng yuqori darajada (eng, juda, g'oyat, ko'p so'zlari yoki ko'p-ko'k, qip-qizil); 4) Ozaytirma daraja — belgining kamligi (-ish, -imtir: oqish, ko'kimtir). Son — narsa-buyumning miqdorini va tartibini bildiruvchi so'z turkumi (Qancha? Nechta? Nechanchi?). Ma'no turlari: 1) Sanoq son (besh, o'n); 2) Dona son (-ta: beshta); 3) Tartib son (-inchi: beshinchi); 4) Jamlovchi son (-ov, -ala: beshov, ikkala); 5) Chamalash son (-tacha, -lab, -tacha: o'ntacha, yuzlab); 6) Taqsim son (-tadan: beshtadan).",
            "examples": [
                {
                    "title": "Orttirma daraja imlosi",
                    "problem": "'Qip-qizil', 'yam-yashil', 'tumuq' so'zlari qanday yoziladi?",
                    "step_by_step": "Rang-tus sifatlarining birinchi bo'g'iniga p/m tovushini qo'shish orqali yasalgan orttirma daraja defis bilan yoziladi: qip-qizil, yam-yashil, bus-butun, ko'p-ko'k. 'Eng katta', 'juda chiroyli' esa ajratib yoziladi.",
                    "answer": "Qip-qizil, yam-yashil (defis bilan)"
                },
                {
                    "title": "Tartib sonlar imlosi",
                    "problem": "Arab va rim raqamlari bilan tartib sonlar qanday yoziladi?",
                    "step_by_step": "Arab raqamlaridan keyin chiziqcha (defis) bilan -inchi yoziladi yoki faqat defis qo'yiladi: 5-sinf, 1-o'rin. Rim raqamlaridan keyin esa defis qo'yilmaydi: XXI asr, V bob.",
                    "answer": "5-sinf (defis bilan), XXI asr (defissiz)"
                }
            ],
            "exercise": "'Yettovlon' va 'o'ntacha' sonlari qaysi ma'no guruhiga kiradi?",
            "exercise_solution": "'Yettovlon' — jamlovchi son; 'o'ntacha' — chamalash son.",
            "check_questions": [
                {
                    "question": "'Ko'kimtir' sifati qaysi darajaga kiradi?",
                    "options": ["Oddiy daraja", "Qiyosiy daraja", "Orttirma daraja", "Ozaytirma daraja"],
                    "correct_index": 3,
                    "explanation": "-imtir qo'shimchasi belgining me'yordan ozligini (ko'kroq emas, xira ko'k) ifodalaydi."
                },
                {
                    "question": "Rim raqamlari bilan yozilganda tartib sonlaridan keyin defis qo'yiladimi?",
                    "options": ["Ha, doimo qo'yiladi", "Yo'q, qo'yilmaydi", "Ixtiyoriy", "Faqat asrlarda qo'yiladi"],
                    "correct_index": 1,
                    "explanation": "Qoidaga ko'ra Rim raqamlaridan keyin hech qachon defis qo'yilmaydi (masalan: XXI asr)."
                },
                {
                    "question": "Jamlovchi son qo'shimchasi qaysi qatorda berilgan?",
                    "options": ["-ta", "-inchi", "-ov, -ala", "-tadan"],
                    "correct_index": 2,
                    "explanation": "-ov, -ala, -ovlon (uchov, ikkala) sonlarni birgalikda jamlab ifodalaydi."
                }
            ],
            "tags": ["ona tili", "sifat", "son", "darajalar", "tartib son", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lit-006",
            "slug": "fel-soz-turkumi-zamonlar-va-nisbatlar",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Fe'l: zamonlar, mayllar, nisbatlar va vazifa shakllari",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Fe'l zamonlari (o'tgan, hozirgi, kelasi), 5 ta fe'l nisbati, mayllar va fe'lning noaniq shakllari (sifatdosh, ravishdosh, harakat nomi)ni farqlash.",
            "theory": "Harakat va holatni bildirib, Nima qildi? Nima qilyapti? Nima qiladi? so'roqlariga javob bo'ladigan mustaqil so'z turkumi fe'l deyiladi. Fe'l zamonlari: 1) O'tgan zamon (-di, -gan, -ibdi); 2) Hozirgi zamon (-yap, -moqda, -yotir: o'qiyapti, yozmoqda); 3) Kelasi zamon (-moqchi, -ajak, -ar: bormoqchi, kelar). Fe'l nisbatlari (5 ta): Bosh nisbat (o'qiydi); O'zlik nisbati (-in, -il: kiyindi, yuvindi); Majhul nisbat (-il, -in: xat yozildi, bino qurildi — bajaruvchi noma'lum); Birgalik nisbati (-ish: gaplashdi, kulishdi); Orttirma nisbat (-dir, -tir, -t, -ir: o'qitdi, yozdirdi). Fe'lning vazifa shakllari: Sifatdosh (-gan, -yotgan: o'qigan bola); Ravishdosh (-b, -ib, -gach, -guncha: kulib gapirdi); Harakat nomi (-sh, -ish, -moq, -v: o'qish, yozmoq).",
            "examples": [
                {
                    "title": "Majhul nisbatni aniqlash",
                    "problem": "'Yangi maktab qurildi' gapidagi fe'lning nisbatini aniqlang va tushuntiring.",
                    "step_by_step": "Qurildi fe'lida -il qo'shimchasi bor. Bino kim tomonidan qurilgani noma'lum, harakat obyekt (maktab) ustida bajarilgan. Bu majhul nisbatdir.",
                    "answer": "Majhul nisbat"
                },
                {
                    "title": "Ravishdosh va sifatdosh farqi",
                    "problem": "'Kelgan mehmon' va 'Yugurib keldi' birikmalaridagi fe'l shakllarini toping.",
                    "step_by_step": "1) Kelgan mehmon — qanday mehmon? -gan qo'shimchasi otga bog'lanib belgi bildirmoqda (sifatdosh);\n2) Yugurib keldi — qanday keldi? -ib qo'shimchasi fe'lga bog'lanib harakat tarzini bildirmoqda (ravishdosh).",
                    "answer": "Kelgan — sifatdosh, Yugurib — ravishdosh"
                }
            ],
            "exercise": "Fe'llarni nisbatlar bo'yicha guruhlang: kiyindi, yozishdi, quritdi, ko'rildi, aytdi.",
            "exercise_solution": "Aytdi — bosh nisbat; Kiyindi — o'zlik nisbati; Ko'rildi — majhul nisbat; Yozishdi — birgalik nisbati; Quritdi — orttirma nisbat.",
            "check_questions": [
                {
                    "question": "Bajaruvchisi grammatik jihatdan noma'lum bo'lgan fe'l nisbati qaysi?",
                    "options": ["O'zlik nisbati", "Majhul nisbat", "Birgalik nisbati", "Orttirma nisbat"],
                    "correct_index": 1,
                    "explanation": "Majhul nisbatda harakat kim tomonidan bajarilgani noma'lum bo'ladi (-il, -in qo'shimchalari)."
                },
                {
                    "question": "Hozirgi zamon davom fe'li qo'shimchasi qaysi?",
                    "options": ["-di", "-gan", "-yap, -moqda", "-ajak"],
                    "correct_index": 2,
                    "explanation": "-yap, -moqda, -yotir nutq so'zlanayotgan paytda davom etayotgan harakatni bildiradi."
                },
                {
                    "question": "'O'qish — baxt keltirar' gapidagi 'o'qish' so'zi fe'lning qaysi shakli?",
                    "options": ["Sifatdosh", "Ravishdosh", "Harakat nomi", "Sof fe'l"],
                    "correct_index": 2,
                    "explanation": "-sh, -ish qo'shimchalari harakatning nomini ifodalovchi shakl yasaydi."
                }
            ],
            "tags": ["ona tili", "fe'l", "zamonlar", "nisbatlar", "ravishdosh", "sifatdosh", "7-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lit-007",
            "slug": "sintaksis-soz-birikmasi-va-bosh-bolaklar",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Sintaksis: so'z birikmasi, gap va gapning bosh bo'laklari (ega va kesim)",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "So'z birikmasidagi tobe va hokim so'z, teng va tobe bog'lanish, gapning ifoda maqsadiga ko'ra turlari hamda ega va kesim moslashuvini o'rganish.",
            "theory": "Sintaksis — so'z birikmalari va gaplarning tuzilishi hamda qonuniyatlarini o'rganuvchi bo'limdir. Kamida ikkita mustaqil so'zning grammatik va ma'no jihatdan bog'lanishi so'z birikmasi deyiladi. Biri ikkinchisiga tobe bo'ladi (qiziqarli kitob: qiziqarli — tobe, kitob — hokim so'z). Tobe bog'lanish usullari: boshqaruv (kelishik bilan: kitobni o'qidi), moslashuv (shaxs-sonda: bizning maktabimiz), bitishuv (ohang va o'rin bilan: tez yurmoq). Gap — tugallangan fikrni ifodalovchi nutq birligi. Gapning bosh bo'laklari: 1) Ega — gapda kim yoki nima haqida fikr yuritilayotganini bildiradi (Kim? Nima? Qayer?); 2) Kesim — eganing harakati, holati yoki belgisini bildirib gapni grammatik jihatdan shakllantiradi (Nima qildi? Qanday? Kimdir?). Ega va kesim shaxs va sonda o'zaro moslashadi.",
            "examples": [
                {
                    "title": "Tobe va hokim so'zni aniqlash",
                    "problem": "'Vatanga muhabbat' birikmasida qaysi so'z hokim, qaysi so'z tobe?",
                    "step_by_step": "'Muhabbat' — hokim so'z (savol beriladi: nimaga muhabbat?);\n'Vatanga' — tobe so'z (jo'nalish kelishigi orqali hokim so'zga tobelangan, boshqaruv usuli).",
                    "answer": "Muhabbat — hokim, Vatanga — tobe"
                },
                {
                    "title": "Ega va kesimni topish",
                    "problem": "'Ilm — insonning eng katta boyligidir' gapida ega va kesimni aniqlang.",
                    "step_by_step": "1) Ega: Nima? — Ilm.\n2) Kesim: Ilm nimadir? — insonning eng katta boyligidir (ot-kesim). Ega va ot-kesim orasida tire qo'yiladi.",
                    "answer": "Ega: Ilm; Kesim: boyligidir"
                }
            ],
            "exercise": "Qaysi hollarda ega va ot-kesim o'rtasida tire qo'yiladi?",
            "exercise_solution": "Ega ham, kesim ham bosh kelishikdagi ot, olmosh yoki harakat nomi bilan ifodalanganda, shuningdek son bilan ifodalanganda ega va kesim orasiga tire qo'yiladi (masalan: O'qish — katta mehnat).",
            "check_questions": [
                {
                    "question": "So'z birikmasida o'ziga savol oladigan bo'lak nima deyiladi?",
                    "options": ["Hokim so'z", "Tobe so'z", "Kirish so'z", "Uyushiq bo'lak"],
                    "correct_index": 1,
                    "explanation": "Hokim so'zdan tobe so'zga savol beriladi, ya'ni tobe so'z savolga javob bo'ladi."
                },
                {
                    "question": "Tugallangan fikrni anglatuvchi eng kichik nutq birligi nima?",
                    "options": ["Fonema", "Morfema", "So'z birikmasi", "Gap"],
                    "correct_index": 3,
                    "explanation": "Gap tugallangan ohang va grammatik markazga ega fikr birligidir."
                },
                {
                    "question": "Ega va kesim o'zaro qanday bog'lanadi?",
                    "options": ["Faqat bitishuv", "Shaxs va sonda moslashuv", "Boshqaruv", "Bog'lanmaydi"],
                    "correct_index": 1,
                    "explanation": "Ega va kesim o'zaro shaxs-son qo'shimchalari vositasida moslashadi (masalan: Men keldim, Ular keldilar)."
                }
            ],
            "tags": ["ona tili", "sintaksis", "so'z birikmasi", "ega", "kesim", "moslashuv", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lit-008",
            "slug": "gapning-ikkinchi-darajali-bolaklari",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Gapning ikkinchi darajali bo'laklari: to'ldiruvchi, aniqlovchi va hollar",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Aniqlovchi (sifatlovchi va qaratqichli), to'ldiruvchi (vositasiz va vositali) hamda hol turlarini (o'rin, payt, sabab, maqsad, tarz, miqdor) gapda tahlil qilish.",
            "theory": "Gapning bosh bo'laklarini yoki bir-birini aniqlab, to'ldirib, kengaytirib keluvchi bo'laklar ikkinchi darajali bo'laklar deyiladi: 1) Aniqlovchi — ot yoki otlashgan so'zga bog'lanib uning belgisini bildiradi (Qanday? Qaysi? Kimning? Nimaning?). Sifatlovchi aniqlovchi (yashil bog') va Qaratqichli aniqlovchi (maktabning hovlisi); 2) To'ldiruvchi — fe'lga bog'lanib harakatning obyektini bildiradi (Kimni? Nimani? Kimga? Kimdan?). Vositasiz to'ldiruvchi (tushum kelishigidagi so'z: kitobni o'qidi); Vositali to'ldiruvchi (boshqa kelishiklar va ko'makchilar bilan: do'stimga aytdim, qalam bilan yozdi); 3) Hol — fe'lga bog'lanib harakatning bajarilish o'rni, payti, sababi, maqsadi, tarzi va darajasini bildiradi (Qayerda? Qachon? Nega? Nima maqsadda? Qanday qilib? Qancha?).",
            "examples": [
                {
                    "title": "Gap bo'laklari bo'yicha to'liq tahlil",
                    "problem": "'Kuzda qushlar janubga qarab tez uchadilar' gapini bo'laklarga ajrating.",
                    "step_by_step": "1) Ega: Qushlar (kimlar?);\n2) Kesim: Uchadilar (nima qiladilar?);\n3) Payt holi: Kuzda (qachon?);\n4) O'rin holi: Janubga qarab (qayerga?);\n5) Tarz holi: Tez (qanday qilib?).",
                    "answer": "Ega: qushlar; Kesim: uchadilar; Hollar: kuzda, janubga qarab, tez"
                },
                {
                    "title": "Vositasiz va vositali to'ldiruvchi",
                    "problem": "'Akam ukasiga qiziq ertakni aytib berdi' gapidagi to'ldiruvchilarni toping.",
                    "step_by_step": "1) Ertakni — nimani? (tushum kelishigida, vositasiz to'ldiruvchi);\n2) Ukasiga — kimga? (jo'nalish kelishigida, vositali to'ldiruvchi).",
                    "answer": "Vositasiz: ertakni; Vositali: ukasiga"
                }
            ],
            "exercise": "'Kechagi suhbat juda maroqli o'tdi' gapidagi aniqlovchi va hollarni aniqlang.",
            "exercise_solution": "Kechagi — qanday suhbat? (sifatlovchi aniqlovchi); Juda — qanchalik? (daraja-miqdor holi); Maroqli — qanday? (tarz holi).",
            "check_questions": [
                {
                    "question": "Tushum kelishigidagi so'z bilan ifodalangan to'ldiruvchi qanday ataladi?",
                    "options": ["Vositali to'ldiruvchi", "Vositasiz to'ldiruvchi", "Qaratqichli to'ldiruvchi", "Hol"],
                    "correct_index": 1,
                    "explanation": "Bevosita tushum kelishigidagi so'z vositasiz to'ldiruvchi deyiladi (masalan: nonni yedi)."
                },
                {
                    "question": "Harakatning bajarilish sababini bildiruvchi hol qaysi so'roqqa javob bo'ladi?",
                    "options": ["Qayerda?", "Qachon?", "Nega? Nima sababdan?", "Qanday qilib?"],
                    "correct_index": 2,
                    "explanation": "Sabab holi 'nega? nima sababli?' so'roqlariga javob bo'ladi (masalan: quvonganidan yig'ladi)."
                },
                {
                    "question": "Qaratqich kelishigidagi (-ning) so'z gapda qanday bo'lak vazifasida keladi?",
                    "options": ["Ega", "Qaratqichli aniqlovchi", "To'ldiruvchi", "Hol"],
                    "correct_index": 1,
                    "explanation": "-ning qo'shimchali so'z o'zidan keyingi egalik qo'shimchali so'zga bog'lanib qaratqichli aniqlovchi bo'ladi."
                }
            ],
            "tags": ["ona tili", "aniqlovchi", "to'ldiruvchi", "hol", "gap bo'laklari", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lit-009",
            "slug": "qoshma-gaplar-va-ularning-turlari",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Qo'shma gap sintaksisi: bog'langan, ergashgan va bog'lovchisiz qo'shma gaplar",
            "grade_level": "9-sinf",
            "difficulty": "Murakkab",
            "objective": "Qo'shma gap turlari (teng va tobe munosabat), bog'lovchilar, ergash gap turlari hamda vergul va tinish belgilarini to'g'ri qo'llash.",
            "theory": "Ikki yoki undan ortiq sodda gapning mazmun va grammatik jihatdan birikuvidan tashkil topgan gap qo'shma gap deyiladi. 3 ta asosiy turi bor: 1) Bog'langan qo'shma gap — tarkibidagi sodda gaplar teng huquqli bo'lib, teng bog'lovchilar yordamida bog'lanadi (biriktiruv: va, hamda; zidlov: ammo, lekin, biroq; ayiruv: yo, yoki; inkor: na... na...); 2) Ergashgan qo'shma gap — biri ikkinchisiga tobe bo'lgan gaplar (Bosh gap va Ergash gap). Ergash gap bosh gapdagi biror bo'lakni yoki butun fikrni izohlaydi (chunki, go'yo, agar, -sa, deb, uchun...); 3) Bog'lovchisiz qo'shma gap — tarkibidagi sodda gaplar hech qanday bog'lovchisiz, faqat ohang va ma'no orqali bog'lanadi (Quyosh botdi, qorong'ulik tushdi). Tinish belgilari: mazmun qarama-qarshi bo'lsa yoki sabab-natija bo'lsa tire, izoh bo'lsa ikki nuqta qo'yiladi.",
            "examples": [
                {
                    "title": "Bog'lovchisiz qo'shma gapda ikki nuqta",
                    "problem": "'Bir narsani unutma: ilm — eng katta boylik' gapida nima uchun ikki nuqta qo'yilgan?",
                    "step_by_step": "Ikkinchi sodda gap birinchi gapdagi fikrni to'ldirib, izohlab kelmoqda (qanday narsani unutma?). Shuning uchun ular orasida ikki nuqta qo'yiladi.",
                    "answer": "Ikkinchi gap birinchisini izohlagani uchun ikki nuqta qo'yiladi"
                },
                {
                    "title": "Ergashgan qo'shma gapni aniqlash",
                    "problem": "'Kimki mehnat qilsa, u albatta baxt topadi' gapining turini aniqlang.",
                    "step_by_step": "1) Bosh gap: 'u albatta baxt topadi'.\n2) Ergash gap: 'Kimki mehnat qilsa' (ega ergash gap).\n3) -sa shart mayli va 'kimki' nisbiy so'zi orqali bog'langan ergashgan qo'shma gap.",
                    "answer": "Ega ergash gapli qo'shma gap"
                }
            ],
            "exercise": "'Yomg'ir yog'di va havo tozalandi' gapini bog'lovchisiz qo'shma gapga aylantiring.",
            "exercise_solution": "'Yomg'ir yog'di, havo tozalandi' (bog'lovchi tushirilib, o'rniga vergul qo'yiladi).",
            "check_questions": [
                {
                    "question": "'Ammo, lekin, biroq' bog'lovchilari qanday bog'lovchilar guruhiga kiradi?",
                    "options": ["Biriktiruv", "Zidlov bog'lovchilari", "Ayiruv", "Ergashtiruvchi"],
                    "correct_index": 1,
                    "explanation": "Ammo, lekin, biroq zid ma'noli sodda gaplarni bog'lovchi zidlov bog'lovchilaridir."
                },
                {
                    "question": "Bog'lovchisiz qo'shma gaplar qanday vosita orqali bog'lanadi?",
                    "options": ["Faqat teng bog'lovchilar", "Faqat ergashtiruvchi bog'lovchilar", "Ohang va ma'no uyg'unligi", "Yuklamalar"],
                    "correct_index": 2,
                    "explanation": "Bog'lovchisiz qo'shma gapda bog'lovchi qatnashmaydi, gaplar ohang va mazmun orqali tutashadi."
                },
                {
                    "question": "Ergashgan qo'shma gap qismlari qanday ataladi?",
                    "options": ["Ega va kesim", "Bosh gap va ergash gap", "Birinchi va ikkinchi bog'lovchi", "Uyushiq gaplar"],
                    "correct_index": 1,
                    "explanation": "Ergashgan qo'shma gap hokim qism bo'lgan Bosh gap va unga tobelangan Ergash gapdan iborat bo'ladi."
                }
            ],
            "tags": ["ona tili", "qo'shma gap", "bog'langan gap", "ergashgan gap", "sintaksis", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lit-010",
            "slug": "uslubiyat-asoslari-va-nutq-madaniyati",
            "subject_id": "sub-15",
            "subject_name": "Ona tili",
            "title": "Nutq uslublari va nutq madaniyati asoslari",
            "grade_level": "10-11-sinf",
            "difficulty": "Murakkab",
            "objective": "5 ta funksional nutq uslubi (so'zlashuv, badiiy, rasmiy-idoraviy, ilmiy, publitsistik) xususiyatlari va nutqning tozaligi, aniqligi hamda boyligini ta'minlash.",
            "theory": "Jamiyatda tilning muayyan sohada qo'llanishiga moslashgan ko'rinishlari nutq uslublari deyiladi. O'zbek adabiy tilida 5 ta asosiy funksional uslub bor: 1) So'zlashuv uslubi — erkin muloqotda, norasmiy vaziyatda qo'llaniladi (ohangdorlik, qisqarishlar, his-tuyg'u ustun); 2) Badiiy uslub — badiiy adabiyotda qo'llaniladi, obrazlilik, tasviriy vositalar (tashbeh, istiora, sifatlash, jonlantirish) va hissiy bo'yoqqa boy; 3) Ilmiy uslub — ilmiy asarlar, darsliklar va tadqiqotlarda qo'llaniladi (qat'iy mantiqiylik, aniqlik, atamalar (terminlar), dalillilik); 4) Rasmiy-idoraviy uslub — qonunlar, farmonlar, arizalar, rasmiy hujjatlarda ishlatiladi (standart qoliplar, shablonlar, emotsiyasizlik: 'Ma'lum qilamanki', 'Qaror qiladi'); 5) Publitsistik uslub — OAV, gazeta, jurnal, radio-televideniye, miting va ommaviy chiqishlar uslubi (ta'sirchanlik, ommaboplik, chaqiriq ruhi).",
            "examples": [
                {
                    "title": "Uslubni aniqlash",
                    "problem": "'Ushbu qonun rasmiy e'lon qilingan kundan e'tiboran kuchga kiradi' jumlasi qaysi uslubga xos?",
                    "step_by_step": "Jumlada qat'iy huquqiy me'yor, standart kantselyariya birikmasi qo'llangan. Bu rasmiy-idoraviy uslubdir.",
                    "answer": "Rasmiy-idoraviy uslub"
                },
                {
                    "title": "Badiiy tasvir vositasi",
                    "problem": "'Kuzgi xazonlar oltin gilamdek to'shaldi' jumlasidagi badiiy san'at turini ayting.",
                    "step_by_step": "Xazonlar to'shalishi oltin gilamga o'xshatilgan (-dek qo'shimchasi orqali). Bu o'xshatish (tashbeh) san'atidir.",
                    "answer": "O'xshatish (tashbeh)"
                }
            ],
            "exercise": "Ilmiy uslubning 3 ta asosiy xususiyatini ko'rsating.",
            "exercise_solution": "1) Terminlar (ilmiy atamalar)ning keng qo'llanilishi; 2) Mantiqiy qat'iylik va his-tuyg'uning yo'qligi; 3) Fikrning mavhum-umumlashtiruvchi xarakteri.",
            "check_questions": [
                {
                    "question": "Qonunlar, arizalar va shartnomalar qaysi nutq uslubida yoziladi?",
                    "options": ["So'zlashuv uslubi", "Badiiy uslub", "Rasmiy-idoraviy uslub", "Publitsistik uslub"],
                    "correct_index": 2,
                    "explanation": "Rasmiy davlat va idora hujjatlari qat'iy rasmiy-idoraviy uslubda yuritiladi."
                },
                {
                    "question": "Gazeta, jurnal va ommaviy axborot vositalarida qaysi uslub yetakchi?",
                    "options": ["Ilmiy uslub", "Publitsistik uslub", "So'zlashuv uslubi", "Rasmiy uslub"],
                    "correct_index": 1,
                    "explanation": "Ijtimoiy-siyosiy va ommabop mavzulardagi OAV tili publitsistik uslub deyiladi."
                },
                {
                    "question": "Metafora, epitet va mubolag'a kabi vositalar qaysi uslubga eng xos?",
                    "options": ["Badiiy uslub", "Ilmiy uslub", "Rasmiy uslub", "Kantselyariya"],
                    "correct_index": 0,
                    "explanation": "Badiiy uslub obrazli tafakkur va tasviriy vositalarga asoslanadi."
                }
            ],
            "tags": ["ona tili", "uslubiyat", "nutq madaniyati", "badiiy uslub", "ilmiy uslub", "11-sinf"],
            "duration_minutes": 35
        },

        # O‘ZBEK ADABIYOTI (8)
        {
            "id": "lit-011",
            "slug": "ozbek-xalq-ogzaki-ijodi-va-alpomish-dostoni",
            "subject_id": "sub-16",
            "subject_name": "O‘zbek adabiyoti",
            "title": "O'zbek xalq og'zaki ijodi (folklorshunoslik) va 'Alpomish' qahramonlik dostoni",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Folkslor janrlari (ertak, maqol, topishmoq, doston), baxshichilik san'ati va 'Alpomish' dostonining g'oyaviy-badiiy tahlili.",
            "theory": "Xalq og'zaki ijodi (folklor) xalq ommasi tomonidan yaratilgan, og'zaki tarzda avloddan-avlodga o'tib kelgan madaniy merosdir. Doston — folklorning eng yirik epik janri bo'lib, baxshilar tomonidan do'mbira jo'rligida kuylangan (Fozil Yo'ldosh o'g'li, Po'lkan shoir, Ergash Jumanbulbul o'g'li). 'Alpomish' — o'zbek xalqining eng mashhur qahramonlik dostoni (ming yillik tarixga ega). Bosh qahramon — Hakimbek (Alpomish), sevgilisi — Barchinoy, sodiq do'sti — Qorajon, oti — Boychibor. Dostonda el-yurt birligi, mardlik, sadoqat, oilaviy mehr va qonxo'r dushmanlarga (Surxayl, Alpampish) qarshi mardonavor kurash kuylanadi. Barchinning 4 ta sharti: poyga (Boychibor g'alabasi), yoy tortish, tanga otish va kurash.",
            "examples": [
                {
                    "title": "Barchinning to'rtta sharti",
                    "problem": "'Alpomish' dostonida Barchinoy Qalmoq elida sovchilarga qanday 4 ta shart qo'yadi?",
                    "step_by_step": "1) Ot poygasi (ming chaqirimlik); 2) Muxammon yoydan otish (14 botmonli yoy); 3) Tanga urish; 4) Kurash tushish (Alpomish Qorajon bilan barchasini yengib chiqadi).",
                    "answer": "Poyga, yoy tortish, tanga otish, kurash"
                },
                {
                    "title": "Fozil Yo'ldosh o'g'li varianti",
                    "problem": "Nima sababdan Fozil Yo'ldosh o'g'lidan yozib olingan 'Alpomish' varianti eng mukammal hisoblanadi?",
                    "step_by_step": "Fozil shoir o'zbek tilining boy xalqona tilidan, yuksak poetik san'atdan mahorat bilan foydalangan va voqealar tizimi to'liq va badiiy barkamol saqlangan.",
                    "answer": "Badiiy yuksakligi va to'liqligi tufayli"
                }
            ],
            "exercise": "Alpomishning oti Boychibor qanday xususiyatlarga ega sadoqatli do'st sifatida tasvirlangan?",
            "exercise_solution": "Boychibor egasining tilini tushunadigan, unga xavf-xatardan ogohlik beruvchi, poygada qanot bog'lab uchadigan afsonaviy xalq tulpori sifatida gavdalantirilgan.",
            "check_questions": [
                {
                    "question": "'Alpomish' dostonining eng mukammal varianti qaysi baxshidan yozib olingan?",
                    "options": ["Ergash Jumanbulbul o'g'li", "Fozil Yo'ldosh o'g'li", "Po'lkan shoir", "Islom shoir"],
                    "correct_index": 1,
                    "explanation": "Fozil Yo'ldosh o'g'li kuylagan nusxa dostondagi eng badiiy pishiq variant hisoblanadi."
                },
                {
                    "question": "Alpomishning bolalikdagi asl ismi nima bo'lgan?",
                    "options": ["Boysari", "Hakimbek", "Qorajon", "Yodgor"],
                    "correct_index": 1,
                    "explanation": "Alpomishning yoshlikdagi ismi Hakimbek bo'lib, keyinchalik jasorati uchun Alpomish laqabini oladi."
                },
                {
                    "question": "Dostonlar xalq ijrochiligida qaysi cholg'u jo'rligida kuylangan?",
                    "options": ["Dutor", "Nay", "Do'mbira", "G'ijjak"],
                    "correct_index": 2,
                    "explanation": "Baxshilar qahramonlik dostonlarini qadimdan do'mbira jo'rligida bo'g'iz tovushi bilan ijro etganlar."
                }
            ],
            "tags": ["adabiyot", "folklor", "alpomish", "doston", "baxshi", "5-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lit-012",
            "slug": "qutadgu-bilig-va-turkiy-yozma-yodgorliklar",
            "subject_id": "sub-16",
            "subject_name": "O‘zbek adabiyoti",
            "title": "Ilk o'rta asr turkiy adabiyoti: Yusuf Xos Hojibning 'Qutadg'u bilig' asari",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "'Qutadg'u bilig' ('Baxtga eltuvchi bilim') dostoni, uning 4 ta ramziy qahramoni va davlatni boshqarish odobi falsafasini tushunish.",
            "theory": "XI asrda Qoraxoniylar davrida yaratilgan 'Qutadg'u bilig' (1069-1070) turkiy tildagi ilk didaktik (pand-nasihat) va falsafiy dostondir. Muallifi — Yusuf Xos Hojib Bolasog'uniy. Asar Qashqarda yozilgan va Tavg'och Bug'roxonga taqdim etilgan. Asar 4 ta ramziy timsol va ularning bahs-munozarasi asosiga qurilgan: 1) Kuntug'di (hukmdor) — Adolat timsoli; 2) Oyto'ldi (vazir) — Baxt va davlat timsoli; 3) O'gdulmish (vazirning o'g'li) — Aql va zakovat timsoli; 4) O'zg'urmish (vazirning qarindoshi, zohid) — Qanoat va oqibat timsoli. Asarning asosiy g'oyasi: insoniyat baxt-saodatga faqat ilm, odillik, aql va qanoat orqali erishishi mumkin.",
            "examples": [
                {
                    "title": "To'rtta ramziy qahramon mohiyati",
                    "problem": "'Qutadg'u bilig'dagi O'gdulmish qanday fazilatni ifodalaydi?",
                    "step_by_step": "O'gdulmish vazir Oyto'ldining o'g'li bo'lib, mukammal aql-idrok, zakovat va teran tafakkur ramzi hisoblanadi. U davlat boshqaruvida ilmning o'rnini ko'rsatadi.",
                    "answer": "Aql va zakovat timsoli"
                },
                {
                    "title": "Asarning tili va vazni",
                    "problem": "Doston qaysi vaznda yozilgan va uning nomi qanday ma'noni bildiradi?",
                    "step_by_step": "'Qutadg'u bilig' — 'Baxt va saodatga eltuvchi bilim' deganidir. Asar aruz vaznining mutaqorib bahrida (masnaviy shaklida) yozilgan.",
                    "answer": "'Baxtga eltuvchi bilim'; aruz vaznida"
                }
            ],
            "exercise": "Yusuf Xos Hojib til odobi va so'zlash madaniyati haqida qanday mashhur baytni aytgan?",
            "exercise_solution": "'Kishilik bezagi so'zdir, buni bil, So'zingga ehtiyot bo'l, tilingni tiyib yur' ma'nosidagi pandiy baytlar orqali til kishiga bosh ham, balo ham keltirishi mumkinligini ta'kidlaydi.",
            "check_questions": [
                {
                    "question": "'Qutadg'u bilig' asari qachon va kim tomonidan yozilgan?",
                    "options": ["X asrda Ahmad Yassaviy", "XI asrda Yusuf Xos Hojib", "XII asrda Alisher Navoiy", "XIV asrda Lutfiy"],
                    "correct_index": 1,
                    "explanation": "Asar 1069-1070 yillarda Yusuf Xos Hojib tomonidan yaratilgan."
                },
                {
                    "question": "Dostonda Adolat timsoli sifatida qaysi obraz tasvirlangan?",
                    "options": ["Kuntug'di", "Oyto'ldi", "O'gdulmish", "O'zg'urmish"],
                    "correct_index": 0,
                    "explanation": "Kuntug'di — adolatli podsho bo'lib, qonun va adolat ramzidir."
                },
                {
                    "question": "'Qutadg'u bilig' so'zining o'zbekcha tarjimasi nima?",
                    "options": ["Xalqlar kitobi", "Baxtga eltuvchi bilim", "Tillar devoni", "Hikmatlar majmuasi"],
                    "correct_index": 1,
                    "explanation": "Qut — baxt, bilig — bilim, qutadg'u bilig — baxtli qiluvchi, saodatga eltuvchi bilim demakdir."
                }
            ],
            "tags": ["adabiyot", "qutadg'u bilig", "yusuf xos hojib", "turkiy adabiyot", "adolat", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lit-013",
            "slug": "alisher-navoiy-hayoti-va-xamsa-asari",
            "subject_id": "sub-16",
            "subject_name": "O‘zbek adabiyoti",
            "title": "Alisher Navoiy — turkiy adabiyot quyoshi: 'Xamsa' dostoni va lirik merosi",
            "grade_level": "7-8-sinf",
            "difficulty": "Murakkab",
            "objective": "Alisher Navoiy hayoti, 'Xazoyinul maoniy' devonlari, 'Muhokamatul-lug'atayn' va turkiy tilda birinchi bo'lib yaratilgan ulkan 'Xamsa' (beshlik) tahlili.",
            "theory": "Nizomiddin Mir Alisher Navoiy (1441-1501) — buyuk o'zbek shoiri, mutafakkir va davlat arbobi. Turkiy tilning boyligi va go'zalligini butun dunyoga isbotlagan ('Muhokamatul-lug'atayn' — 'Ikki til muhokamasi' asarida turkiy tilni forsiy tildan kam emasligini ilmiy asoslagan). 1483-1485 yillarda qisqa muddatda birinchi bo'lib turkiy tilda 5 ta dostondan iborat 'Xamsa' yaratdi: 1) 'Hayratul-abror' ('Yaxshilar hayrati' — falsafiy-ta'limiy doston); 2) 'Farhod va Shirin' (Farhod — mehnat va qahramonlik timsoli); 3) 'Layli va Majnun' (ilohiy va samimiy muhabbat madhi); 4) 'Sab'ai sayyor' ('Yetti sayyora' — Bahrom Go'r sarguzashtlari); 5) 'Saddi Iskandariy' ('Iskandar devori' — adolatli podshohlik haqidagi doston). Shoir lirik merosini to'rtta devondan iborat 'Xazoyinul maoniy' ('Ma'nolar xazinasi') to'plamiga jamlagan.",
            "examples": [
                {
                    "title": "Navoiy g'azalidan namuna tahlili",
                    "problem": "'Orazin yopqoch ko'zumdin sochilur har lahza yosh, Bo'ylakim, paydo bo'lur yulduz, nihon bo'lg'och quyosh' baytini sharhlang.",
                    "step_by_step": "Yor o'z yuzini (quyoshni) bekitgach, oshiq ko'zidan yoshlar (yulduzlar) to'kiladi. Quyosh botganda osmonda yulduzlar paydo bo'lishiga o'xshatish orqali ajoyib tazod (zidlik) va tashbeh san'ati qo'llanilgan.",
                    "answer": "Quyoshning botishi va yulduzlar chiqishi orqali oshiq kechinmasi ifodalangan"
                },
                {
                    "title": "'Xamsa'ning birinchi dostoni",
                    "problem": "Navoiy 'Xamsa'sining birinchi dostoni qaysi va u necha maqolatdan iborat?",
                    "step_by_step": "Birinchi doston — 'Hayratul-abror' bo'lib, pand-nasihat va ijtimoiy-falsafiy yo'nalishda yozilgan hamda 20 ta maqolat va hikoyatlardan tashkil topgan.",
                    "answer": "'Hayratul-abror' (20 maqolat)"
                }
            ],
            "exercise": "Farhod obrazining qaysi fazilatlari uni Sharq adabiyotidagi an'anaviy qahramonlardan ajratib turadi?",
            "exercise_solution": "Navoiy Farhodni oddiy sevgi asiri emas, balki tosh yo'nuvchi, mehnatni sevadigan, xalq uchun tog'ni teshib suv olib keluvchi mard, donishmand va xalqparvar qahramon qilib tasvirlaydi.",
            "check_questions": [
                {
                    "question": "Alisher Navoiy qaysi asarida turkiy tilning forsiy tildan kam emasligini ilmiy isbotlab bergan?",
                    "options": ["Mahbubul-qulub", "Muhokamatul-lug'atayn", "Mizanul-avzon", "Majolisun-nafois"],
                    "correct_index": 1,
                    "explanation": "'Muhokamatul-lug'atayn' (Ikki til muhokamasi) asarida shoir turkiy tilning cheksiz lug'at boyligini isbotlagan."
                },
                {
                    "question": "Navoiyning 'Xamsa'si nechta dostondan iborat?",
                    "options": ["3 ta", "4 ta", "5 ta", "7 ta"],
                    "correct_index": 2,
                    "explanation": "'Xamsa' arabcha 'beshlik' degan ma'noni bildirib, 5 ta mustaqil dostondan tashkil topgan."
                },
                {
                    "question": "'Xazoyinul maoniy' to'plami nechta devonni o'z ichiga oladi?",
                    "options": ["2 ta", "3 ta", "4 ta ('Chor devon')", "5 ta"],
                    "correct_index": 2,
                    "explanation": "Shoir inson umrining to'rt fasliga moslab 4 ta devon tuzgan (Chor devon)."
                }
            ],
            "tags": ["adabiyot", "alisher navoiy", "xamsa", "farhod va shirin", "g'azal", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lit-014",
            "slug": "zahiriddin-muhammad-bobur-va-boburnoma",
            "subject_id": "sub-16",
            "subject_name": "O‘zbek adabiyoti",
            "title": "Zahiriddin Muhammad Bobur: hayoti, nozik lirika va 'Boburnoma' qomusi",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Boburning sarguzashtli hayoti, vatan sog'inchi aks etgan ruboiylari va tarixiy-memuar durdona — 'Boburnoma' asari mohiyatini o'rganish.",
            "theory": "Zahiriddin Muhammad Bobur (1483-1530) — Temuriylar sulolasining yorqin vakili, buyuk shoir, sarkarda va Boburiylar imperiyasi asoschisi. Andijonda tug'ilgan, 12 yoshida Farg'ona taxtiga o'tirgan. Murakkab siyosiy kurashlar oqibatida vatanini tark etishga majbur bo'lgan va Kobul hamda Hindistonda ulkan saltanat barpo etgan. Lirik merosi: vatan sog'inchi, dard va sadoqat mavzusidagi betakror ruboiylar va g'azallar ustasi ('Tole' yo'qi jonimg'a baloliq bo'ldi, Har yonki chekdim oyoq, ranj-u balo bo'ldi...'). 'Boburnoma' (Vaqoye') — Boburning shoh asari bo'lib, memuar (xotira) janrida yozilgan. Unda Farg'ona, Movarounnahr, Afg'oniston va Hindistonning tabiati, shaharlari, hayvonot va o'simlik olami, xalqlari, urf-odatlari va tarixiy voqealari xolis va yuksak mahorat bilan tasvirlangan.",
            "examples": [
                {
                    "title": "Bobur ruboiysidan namuna",
                    "problem": "'Yod etmas emish kishini g'urbatda kishi, Shod etmas emish ko'ngulni mehnatda kishi. Ko'nglum bu g'ariblikda shod o'lmadi, oh, G'urbatda sevinmas emish, albatta, kishi' ruboiysi g'oyasi nima?",
                    "step_by_step": "Ushbu ruboiyda o'z yurtidan olisda sarson kechgan shoirning chuqur vatan sog'inchi, musofirlikdagi cheksiz ruhiy iztirobi va g'urbatda hech qanday boylik ko'ngilni shod eta olmasligi haqiqati ifodalangan.",
                    "answer": "Vatan sog'inchi va musofirlik iztiroblari"
                },
                {
                    "title": "'Boburnoma'ning ensiklopedik tabiati",
                    "problem": "Nima sababdan 'Boburnoma' butun dunyo olimlari tomonidan qadrlanadi?",
                    "step_by_step": "Chunki u faqat tarixiy voqealar yilnomasi emas, balki geografiya, botanika, zoologiya, etnografiya va tilshunoslik bo'yicha nodir qomusiy manba hisoblanadi.",
                    "answer": "Tarixiy, geografik va ilmiy qomusiy manba bo'lgani uchun"
                }
            ],
            "exercise": "Bobur aruz vazniga oid qaysi ilmiy risolasini yozgan?",
            "exercise_solution": "'Muxtasar' (Aruz risolasi) nomli ilmiy asarida aruz vazni qonuniyatlarini chuqur tadqiq etgan.",
            "check_questions": [
                {
                    "question": "Boburning dunyoga mashhur tarixiy-memuar asari qaysi?",
                    "options": ["Shajarayi turk", "Boburnoma", "Temurnoma", "Tarixi Rashidiy"],
                    "correct_index": 1,
                    "explanation": "'Boburnoma' Boburning o'z ko'rgan-kechirganlari asosida yozilgan nodir memuar asaridir."
                },
                {
                    "question": "Bobur qaysi lirik janrning yetuk ustasi hisoblanadi?",
                    "options": ["Doston", "Ruboiy", "Qasida", "Masnaviy"],
                    "correct_index": 1,
                    "explanation": "Bobur o'zbek adabiyotida ruboiy janrini eng yuksak cho'qqiga olib chiqqan shoirdir."
                },
                {
                    "question": "Bobur qayerda tavallud topgan?",
                    "options": ["Samarqandda", "Andijonda", "Hirotda", "Kobulda"],
                    "correct_index": 1,
                    "explanation": "Bobur 1483-yil 14-fevralda Andijon shahrida tug'ilgan."
                }
            ],
            "tags": ["adabiyot", "bobur", "boburnoma", "ruboiy", "andijon", "temuriylar", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lit-015",
            "slug": "jadid-adabiyoti-behbudiy-va-avloniy",
            "subject_id": "sub-16",
            "subject_name": "O‘zbek adabiyoti",
            "title": "Jadid ma'rifatparvarlik adabiyoti: Mahmudxo'ja Behbudiy va Abdulla Avloniy",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Jadidchilik harakati g'oyalari, yangi usul maktablari, teatr san'ati va Behbudiyning 'Padarkush' dramasi hamda Avloniy merosini o'rganish.",
            "theory": "XIX asr oxiri va XX asr boshlarida Turkistonda xalqni jaholat va mustamlakachilik zulmidan ozod etish, ma'rifatga yetaklash maqsadida jadidchilik (yangilik tarafdorlari) harakati vujudga keldi. Mahmudxo'ja Behbudiy (1875-1919) — jadidlar yetakchisi, publitsist va dramaturg. 1911-yilda yozilgan 'Padarkush' dramasi o'zbek professional dramaturgiyasining ilk namunasi hisoblanadi. Unda o'qimagan, ilmsiz Toshmurod boyning o'g'li maishatga berilib, otasini o'ldirgani (padarkush bo'lgani) fojiasi orqali jaholatning dahshatli oqibati ochib beriladi. Abdulla Avloniy (1878-1934) — 'Birinchi muallim', 'Turkiy guliston yoxud axloq' asarlari muallifi. Uning mashhur shiori: 'Tarbiya biz uchun yo hayot — yo mamot, yo najot — yo halokat, yo saodat — yo falokat masalasidir'.",
            "examples": [
                {
                    "title": "'Padarkush' dramasining bosh g'oyasi",
                    "problem": "'Padarkush' dramasida muallif xalqqa qanday asosiy saboq bermoqchi bo'lgan?",
                    "step_by_step": "Ilmsizlik, ma'rifatsizlik va bolani to'g'ri tarbiyalamaslik oilani ham, jamiyatni ham fojia va halokatga yetaklashini ko'rsatish.",
                    "answer": "Ilmsizlik va jaholat fojiasini ko'rsatish"
                },
                {
                    "title": "Avloniyning tarbiya haqidagi qarashi",
                    "problem": "Abdulla Avloniy tarbiyaga nega millat taqdirini hal qiluvchi kuch deb qaragan?",
                    "step_by_step": "Chunki tarbiyali, bilimli avlod millatni erkinlik va taraqqiyotga olib chiqadi; tarbiyasiz avlod esa millatni qaramlik va inqirozga mahkum etadi.",
                    "answer": "Tarbiyali avlod millatning ozodligi va kelajagi asosi bo'lgani uchun"
                }
            ],
            "exercise": "Mahmudxo'ja Behbudiyning Samarqandda nashr ettirgan mashhur jurnali va gazetasi qaysi?",
            "exercise_solution": "'Oyna' jurnali va 'Samarqand' gazetasi.",
            "check_questions": [
                {
                    "question": "O'zbek professional dramaturgiyasining ilk asari qaysi?",
                    "options": ["Boy ila xizmatchi", "Padarkush", "O'tkan kunlar", "Zaharli hayot"],
                    "correct_index": 1,
                    "explanation": "Mahmudxo'ja Behbudiyning 1911-yilda yozilgan 'Padarkush' dramasi ilk milliy dramamizdir."
                },
                {
                    "question": "'Tarbiya biz uchun yo hayot — yo mamot...' degan fikr qaysi mutafakkirga tegishli?",
                    "options": ["Abdulla Avloniy", "Fitrat", "Cho'lpon", "Hamza"],
                    "correct_index": 0,
                    "explanation": "Ushbu mashhur hikmat Abdulla Avloniyning 'Turkiy guliston yoxud axloq' asaridan olingan."
                },
                {
                    "question": "'Jadid' so'zi qanday ma'noni anglatadi?",
                    "options": ["Qadimgi", "Yangi (yangilik tarafdori)", "Muallim", "Ozodlik"],
                    "correct_index": 1,
                    "explanation": "'Jadid' arabcha so'z bo'lib, yangi degan ma'noni bildiradi (usuli jadid — yangi usul)."
                }
            ],
            "tags": ["jadidlar", "behbudiy", "padarkush", "avloniy", "tarbiya", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lit-016",
            "slug": "abdulla-qodiriy-va-otkan-kunlar-romani",
            "subject_id": "sub-16",
            "subject_name": "O‘zbek adabiyoti",
            "title": "Abdulla Qodiriy: birinchi o'zbek romani — 'O'tkan kunlar' badiiy olami",
            "grade_level": "9-sinf",
            "difficulty": "Murakkab",
            "objective": "Abdulla Qodiriy hayoti, romanchilik maktabining yaratilishi, Otabek, Kumush, Zaynab obrazlari va Qo'qon xonligi davridagi xalq fojiasini tahlil qilish.",
            "theory": "Abdulla Qodiriy (Julqunboy, 1894-1938) — o'zbek romanchiligining asoschisi, buyuk so'z san'atkori. 'O'tkan kunlar' (1922-1926) — o'zbek adabiyotidagi birinchi tarixiy roman. Voqealar XIX asr o'rtalarida, Qo'qon xonligidagi o'zaro toj-taxt talashuvlar va qonli nizo davrida Toshkent va Marg'ilonda kechadi. Muallifning maqsadi: 'Moziyga qaytib ish ko'rmoq xayrlidir...'. Asosiy qahramonlar: Otabek — yangicha fikrlovchi, vatanparvar, ma'rifatli yosh savdogar; Kumushbibi — go'zallik, vafo va iffat timsoli; Mirzakarim qutidor va Oftoboyim; Yusufbek hoji — dono, yurt g'amida yonuvchi davlat arbobi; Zaynab — rashk va xurofot qurboni bo'lib Kumushni zaharlagan ikkinchi xotin; Homid — hasadgo'y va xiyonatkor qiyofa. Fojia faqat sevgi fojiasi emas, balki tarqoqlik, xurofot va o'zaro qirg'inlar girdobidagi butun millat fojiasidir.",
            "examples": [
                {
                    "title": "Yusufbek hojining xalqqa murojaati",
                    "problem": "'O'tkan kunlar'da Yusufbek hoji qo'zg'olonga chiqqan xalqqa qarata nima deydi?",
                    "step_by_step": "Yusufbek hoji o'zaro qon to'kishni to'xtatishga chaqiradi: 'Biz o'zaro urushib kuchsizlansak, ertaga yov kelib yurtimizni xor qiladi, bir-biringizning qoningizni to'kmang!' deb ogohlantiradi.",
                    "answer": "O'zaro nizo va qon to'kishdan qaytaradi"
                },
                {
                    "title": "Otabek va Kumush uchrashuvi",
                    "problem": "Otabekning Marg'ilonda Kumushni birinchi marta ko'rgan paytidagi badiiy tasvirning kuchi nimada?",
                    "step_by_step": "Qodiriy sharqona iffat va go'zallikni nihoyatda nozik, jozibador til bilan chizadi: 'Qora qosh, qiyiq ko'z, oydek to'lin yuz...' Otabekning qalbida bir ko'rishda o'chmas muhabbat paydo bo'ladi.",
                    "answer": "Sharqona go'zallik va nozik psixologik tasvir"
                }
            ],
            "exercise": "Romanda Homidning qilgan asosiy razilligi nimadan iborat edi?",
            "exercise_solution": "Homid Kumushga uylanish ilinjida soxta xat to'qib, Otabekni xoin qilib ko'rsatishga va oilani buzishga uringan, fitnalar uyushtirgan.",
            "check_questions": [
                {
                    "question": "O'zbek adabiyotidagi birinchi roman qaysi?",
                    "options": ["Kecha va kunduz", "O'tkan kunlar", "Mehrobdan chayon", "Sarob"],
                    "correct_index": 1,
                    "explanation": "Abdulla Qodiriyning 'O'tkan kunlar' romani 1920-yillarda yaratilgan ilk milliy romandir."
                },
                {
                    "question": "'O'tkan kunlar' romanidagi bosh qahramon Otabekning otasi kim?",
                    "options": ["Mirzakarim qutidor", "Yusufbek hoji", "Hasanali", "Ziyo shohichi"],
                    "correct_index": 1,
                    "explanation": "Otabekning otasi Toshkentning obro'li oqsoqoli Yusufbek hojidir."
                },
                {
                    "question": "Roman so'ngida Kumushbibining vafotiga nima sabab bo'ladi?",
                    "options": ["Og'ir kasallik", "Zaynab tomonidan zaharlanish", "Jangdagi jarohat", "Baxtsiz hodisa"],
                    "correct_index": 1,
                    "explanation": "Kumushbibi rashk o'tida yongan Zaynab bergan zaharlangan anor suvidan vafot etadi."
                }
            ],
            "tags": ["adabiyot", "abdulla qodiriy", "o'tkan kunlar", "otabek", "kumushbibi", "roman", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lit-017",
            "slug": "cholpon-va-usmon-nosir-sheriyati",
            "subject_id": "sub-16",
            "subject_name": "O‘zbek adabiyoti",
            "title": "Cho'lpon va Usmon Nosir: milliy uyg'onish, erk va olovli she'riyat",
            "grade_level": "10-sinf",
            "difficulty": "Murakkab",
            "objective": "Abdulhamid Cho'lponning 'Kecha va kunduz' romani, hurriyatparvar she'rlari hamda 'O'zbekistonning Lermontovi' — Usmon Nosir lirikasini o'rganish.",
            "theory": "Abdulhamid Sulaymon o'g'li Cho'lpon (1897-1938) — yangi o'zbek she'riyatining yetakchisi, erkinlik va istiqlol kuychisi ('Go'zal', 'Ko'ngil', 'Buzilgan o'lkaga'). Uning 'Kecha va kunduz' romani milliy fojia, qoloqlik va mustamlaka zulmidagi xalq hayotini Zebi va Miryoqub obrazlari orqali yuksak badiiylik bilan gavdalantiradi. Cho'lpon: 'Ko'ngil, sen munchalar nega zanjirlar bilan bog'landing?.. Tiriksan, o'lmagansan, sen-da odamsan, kishisan...' Usmon Nosir (1912-1944) — o'zbek adabiyotining otashin yosh shoiri. U she'riyatga vulqondek otilib kirdi ('Yurak', 'Naxshon', 'Monolog'). Uning mashhur satrlari: 'Yurak, sensan mening sozim, Tilimni nayga jo'r etding. Mayli, xor o'lsin parvozim, Seni yondirsa bu o'tlar... She'rim, yana o'zing yaxshisan, Boqiy qolar yurak naqshisan...' Ikkala shoir ham qatag'on davrida fojiali halok bo'lgan.",
            "examples": [
                {
                    "title": "Cho'lponning 'Ko'ngil' she'ri tahlili",
                    "problem": "Cho'lponning 'Ko'ngil' she'ridagi 'Kishan kiyma, bo'yning egma, ki sen ham hur tug'ilg'onsen!' chaqirig'i nimaga qaratilgan?",
                    "step_by_step": "Shoir inson va millat erkinligini ulug'laydi, har qanday ruhiy va siyosiy qullikka qarshi chiqib, xalqni o'z qadr-qimmatini anglashga va erk uchun kurashishga undaydi.",
                    "answer": "Milliy erkinlik va qullikka qarshi isyon"
                },
                {
                    "title": "Usmon Nosirning 'Yurak' she'ri",
                    "problem": "Usmon Nosir nima sababdan o'z she'rida yuragiga 'Yurak, to'xtama, ur!' deb murojaat qiladi?",
                    "step_by_step": "Shoir hayotni jo'shqin ijodda, yonib yashashda ko'radi. Uning uchun befarq yashash o'lim bilan teng, u so'nggi nafasigacha eliga xizmat qilishni xohlaydi.",
                    "answer": "Otashin ijodiy hayot va faol kurashchanlik ifodasi"
                }
            ],
            "exercise": "Cho'lponning 'Kecha va kunduz' romanidagi Zebi obrazining fojeali qismatini tushuntiring.",
            "exercise_solution": "Beg'ubor, sho'x va orzularga to'la Zebi qariya Akbarali mingboshiga to'rtinchi xotin qilib zo'rlab uzatiladi, mingboshining zaharlanib o'lishida nohaq ayblanib, Sibirga surgun qilinadi.",
            "check_questions": [
                {
                    "question": "'Kecha va kunduz' romanining muallifi kim?",
                    "options": ["Abdulla Qodiriy", "Cho'lpon", "Oybek", "G'afur G'ulom"],
                    "correct_index": 1,
                    "explanation": "'Kecha va kunduz' romani Abdulhamid Cho'lpon tomonidan yozilgan."
                },
                {
                    "question": "'Yurak, sensan mening sozim...' satrlari bilan boshlanuvchi she'r muallifi kim?",
                    "options": ["Hamid Olimjon", "Usmon Nosir", "Cho'lpon", "Mirtemir"],
                    "correct_index": 1,
                    "explanation": "Bu olovli satrlar yosh shoir Usmon Nosirning mashhur 'Yurak' she'ridan olingan."
                },
                {
                    "question": "Cho'lpon qaysi jahon klassikasining asarini o'zbek tiliga yuksak mahorat bilan tarjima qilgan?",
                    "options": ["Dante 'Ilohiy komediya'", "Shekspir 'Hamlet'", "Gomer 'Iliada'", "Servantes 'Don Kixot'"],
                    "correct_index": 1,
                    "explanation": "Cho'lpon Shekspirning 'Hamlet' va 'Otello' tragediyalarini o'zbek tiliga benuqson tarjima qilgan."
                }
            ],
            "tags": ["adabiyot", "cho'lpon", "usmon nosir", "yurak", "kecha va kunduz", "sheriyat", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lit-018",
            "slug": "erkin-vohidov-va-abdulla-oripov-ijodi",
            "subject_id": "sub-16",
            "subject_name": "O‘zbek adabiyoti",
            "title": "Zamonaviy o'zbek adabiyoti: Erkin Vohidov va Abdulla Oripov — millat iftixorlari",
            "grade_level": "11-sinf",
            "difficulty": "O'rta",
            "objective": "O'zbekiston Qahramonlari Erkin Vohidov ('O'zbegim' qasidasi, 'Ruhlar isyoni') va Abdulla Oripov ('O'zbekiston' qasidasi, O'zbekiston Respublikasi Davlat madhiyasi) ijodini o'rganish.",
            "theory": "XX asr ikkinchi yarmi o'zbek adabiyotining ikki buyuk ustuni — O'zbekiston Qahramonlari, xalq shoirlari Erkin Vohidov (1936-2016) va Abdulla Oripov (1941-2016). Erkin Vohidov — chuqur falsafiy mushohada, Sharq mumtoz an'analari va nozik qochirimlar ustasi. Uning 'O'zbegim' qasidasi (1968) mustabid tuzum davrida milliy g'urur va o'zlikni anglashning qudratli madhiyasiga aylangan. 'Ruhlar isyoni' dostonida inson erki va hurriyati ulug'langan. Abdulla Oripov — yuksak samimiyat, dard va vatanparvarlik kuychisi. U O'zbekiston Respublikasi Davlat madhiyasi matni muallifidir. 'O'zbekiston' qasidasi, 'Munojotni tinglab', 'Jannatga yo'l' dostoni hamda Dante 'Ilohiy komediya'sining o'zbekcha yuksak tarjimasi uning qalamiga mansub. Ikkala shoir ham istiqlol va milliy ruh tiklanishining yorqin timsolidir.",
            "examples": [
                {
                    "title": "'O'zbegim' qasidasining tarixiy ahamiyati",
                    "problem": "Erkin Vohidovning 1968-yilda yozilgan 'O'zbegim' qasidasi nima sababdan katta shov-shuvga sabab bo'lgan?",
                    "step_by_step": "Sho'rolar mafkurasi hukmron bo'lgan davrda o'zbek xalqining ming yillik buyuk o'tmishini, Al-Xorazmiy, Beruniy, Ibn Sino, Navoiy, Boburlarni ochiq e'tirof etib, milliy g'ururni uyg'otgan jasoratli asar bo'lgan.",
                    "answer": "Sovet davrida milliy o'zlik va g'ururni dadil kuylagani uchun"
                },
                {
                    "title": "O'zbekiston Davlat madhiyasi",
                    "problem": "O'zbekiston Respublikasi Davlat madhiyasining she'ri kimga, musiqasi kimga tegishli?",
                    "step_by_step": "Matn muallifi — Abdulla Oripov; Musiqa muallifi — Mutal Burhonov.",
                    "answer": "So'zi: Abdulla Oripov, Musiqasi: Mutal Burhonov"
                }
            ],
            "exercise": "Abdulla Oripovning 'Genetika' she'rida qanday falsafiy g'oya ilgari suriladi?",
            "exercise_solution": "Inson o'z ajdodlarining qon-qardoshlik rishtalari, milliy ildizlari va tabiat qonunlariga sodiq qolishi kerakligi, tomirdagi pokiza nasl davomiyligi ulug'lanadi.",
            "check_questions": [
                {
                    "question": "O'zbekiston Respublikasi Davlat madhiyasi matnining muallifi kim?",
                    "options": ["Erkin Vohidov", "Abdulla Oripov", "Muhammad Yusuf", "Oybek"],
                    "correct_index": 1,
                    "explanation": "Mustaqil O'zbekiston madhiyasi matni O'zbekiston Qahramoni Abdulla Oripov tomonidan yozilgan."
                },
                {
                    "question": "'O'zbegim' qasidasi va 'Ruhlar isyoni' dostonining muallifi kim?",
                    "options": ["Erkin Vohidov", "Abdulla Oripov", "G'afur G'ulom", "Hamid Olimjon"],
                    "correct_index": 0,
                    "explanation": "Bu ikki mashhur asar O'zbekiston xalq shoiri Erkin Vohidov qalamiga mansub."
                },
                {
                    "question": "Abdulla Oripov jahon adabiyotining qaysi shoh asarini o'zbek tiliga mahorat bilan tarjima qilgan?",
                    "options": ["Faust", "Ilohiy komediya (Dante)", "Shohnoma", "Iliada"],
                    "correct_index": 1,
                    "explanation": "Abdulla Oripov Dante Aligyerining buyuk 'Ilohiy komediya' asarini bevosita o'zbek tiliga o'girgan."
                }
            ],
            "tags": ["adabiyot", "erkin vohidov", "abdulla oripov", "o'zbegim", "madhiya", "zamonaviy adabiyot", "11-sinf"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_language_literature_materials()
    print(f"Generated {len(mats)} Language/Literature materials.")
