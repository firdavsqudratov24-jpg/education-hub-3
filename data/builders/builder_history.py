# -*- coding: utf-8 -*-
"""
Builder for O‘zbekiston va Jahon tarixi (16 materials: his-001 to his-016)
- sub-23: O‘zbekiston tarixi (10: his-001 to his-010)
- sub-24: Jahon tarixi (6: his-011 to his-016)
"""

def get_history_materials():
    materials = [
        # O‘ZBEKISTON TARIXI (10)
        {
            "id": "his-001",
            "slug": "ozbekiston-hududida-ibtidoiy-jamoa-tuzumi",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "O'zbekiston hududida ibtidoiy jamoa tuzumi: Selung'ur, Teshiktosh va Zamonbobo",
            "grade_level": "5-6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Tosh davri bosqichlari (paleolit, mezolit, neolit, eneolit), O'zbekistondagi qadimgi odamlar makonlari va Teshiktosh neandertal bolasi topilmasini bilish.",
            "theory": "O'zbekiston hududi insoniyatning eng qadimgi beshiklaridan biridir. Ibtidoiy davr quyidagi bosqichlarga bo'linadi: 1) Quyi paleolit — Farg'ona vodiysidagi Selung'ur g'ori (1-1.5 million yil avval, 'Farg'ona odami' tishi va ilk tosh qurollar topilgan); 2) O'rta paleolit (Mustye davri) — Surxondaryodagi Boysun tog'larida joylashgan Teshiktosh g'ori (1938-yilda A.P. Okladnikov tomonidan 8-9 yoshli neandertal bolasi suyagi va tog' echkisi shoxlari bilan o'ralgan dafn marosimi topilgan); 3) Yuqori paleolit — Samarqand makoni, Ko'lbuloq; 4) Mezolit (o'rta tosh davri) — o'q-yoyning kashf etilishi, hayvonlarni xonakilashtirishning boshlanishi, Machay g'ori, Zarautsoy qoyatosh rasmlari; 5) Neolit (yangi tosh davri) — 'Neolit inqilobi' (o'zlashtiruvchi xo'jalikdan — terimchilik va ovchilikdan ishlab chiqaruvchi xo'jalikka — dehqonchilik va chorvachilikka o'tilishi), Kaltaminor madaniyati; 6) Eneolit va bronza davri — Zamonbobo va Sopollitepa, Jarqo'ton ilk shahar madaniyati.",
            "examples": [
                {
                    "title": "Teshiktosh g'ori kashfiyoti",
                    "problem": "Teshiktosh g'oridan topilgan neandertal bola qabri insoniyat tarixida qanday muhim tushunchani isbotladi?",
                    "step_by_step": "Murdaning qabrga kalla suyagi tog' echkisi shoxlari bilan qatorlab o'ralgan holda ko'milishi o'rta tosh davridagi odamlarda ilk diniy tasavvurlar va narigi dunyoga ishonch paydo bo'lganini isbotlaydi.",
                    "answer": "Dastlabki diniy tasavvurlar va dafn marosimi mavjudligini isbotladi"
                },
                {
                    "title": "Neolit inqilobining mohiyati",
                    "problem": "'Neolit inqilobi' insoniyat hayotida qanday tub burilish yasadi?",
                    "step_by_step": "Inson tabiat tayyor bergan narsalarni terish va ovlashdan o'zi oziq-ovqat yetishtirishga — dehqonchilik va chorvachilikka o'tdi, o'troq hayot boshlandi.",
                    "answer": "O'zlashtiruvchi xo'jalikdan ishlab chiqaruvchi xo'jalikka o'tildi"
                }
            ],
            "exercise": "Zarautsoy qoyatosh rasmlarida asosan nimalar tasvirlangan?",
            "exercise_solution": "Zarautsoyda itlar yordamida yovvoyi buqalar va tog' echkilarini niqoblangan ovchilar tomonidan o'q-yoy bilan ov qilish sahnalari tasvirlangan.",
            "check_questions": [
                {
                    "question": "O'zbekistonda neandertal odami qabri qaysi g'ordan topilgan?",
                    "options": ["Selung'ur", "Teshiktosh", "Machay", "Obirahmat"],
                    "correct_index": 1,
                    "explanation": "Boysun tog'laridagi Teshiktosh g'oridan neandertal bolasi qoldiqlari topilgan."
                },
                {
                    "question": "O'q-yoy insoniyat tomonidan qaysi davrda kashf etilgan?",
                    "options": ["Paleolit", "Mezolit", "Neolit", "Bronza davri"],
                    "correct_index": 1,
                    "explanation": "O'q-yoy mezolit (o'rta tosh davri) da ixtiro qilinib, ov samaradorligini keskin oshirgan."
                },
                {
                    "question": "Eng qadimgi dehqonchilik madaniyatiga asos solingan 'Neolit inqilobi' nima?",
                    "options": ["Tosh qurollardan voz kechish", "Ishlab chiqaruvchi xo'jalikka (dehqonchilik va chorvachilik) o'tish", "Yozuvning ixtiro qilinishi", "Temir eritish"],
                    "correct_index": 1,
                    "explanation": "Tayyor mahsulotni iste'mol qilishdan o'zi ekin ekib oziq-ovqat yetishtirishga o'tish neolit inqilobi deyiladi."
                }
            ],
            "tags": ["o'zbekiston tarixi", "ibtidoiy jamoa", "teshiktosh", "paleolit", "neolit", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "his-002",
            "slug": "qadimgi-davlatlar-baqtriya-sogdiyona-va-xorazm",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "O'zbekiston hududidagi ilk davlatchilik: Qadimgi Baqtriya, So'g'diyona va Xorazm",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Miloddan avvalgi I ming yillikdagi ilk davlat birlashmalari, Avesto kitobi va Zardushtiylik dini, sun'iy sug'orish kanallari va shaharsozlik madaniyatini o'rganish.",
            "theory": "Miloddan avvalgi IX-VIII asrlarda O'zbekiston hududida yirik sun'iy sug'orish tarmoqlarining barpo etilishi ilk davlat birlashmalarining shakllanishiga olib keldi. Asosiy tarixiy-madaniy viloyatlar: 1) Qadimgi Baqtriya (Surxondaryo, Janubiy Tojikiston, Shimoliy Afg'oniston) — markazi Baqtra (Balx) shahri, 'Ming shahar yurti' deb atalgan; 2) Qadimgi Xorazm (Amudaryo quyi oqimi) — ulkan kanallar (Qirqqiz qal'a, Jonbosqal'a, Qo'yqirilgan qal'a), 'Avesto' vatani deb hisoblanadi; 3) So'g'diyona (Zarafshon va Qashqadaryo vohalari) — markazi Maroqanda (Samarqand). Dini: Zardushtiylik (muqaddas kitobi — 'Avesto', asoschisi Zaratushtra). Zardushtiylik ezgulik xudosi Axuramazda va yovuzlik timsoli Axriman kurashiga asoslangan. Olov, suv, tuproq va havo muqaddas hisoblangan, murdalar suyaklari ossuariylarda (ostodon) saqlangan.",
            "examples": [
                {
                    "title": "Avestoning bosh g'oyasi",
                    "problem": "Zardushtiylikning muqaddas kitobi 'Avesto'ning uchlik axloqiy formulasi qanday?",
                    "step_by_step": "'Ezgulik fikr (Humata), Ezgu so'z (Huxta), Ezgu amal (Hvarshta)'. Zardushtiylik insonni faqat yaxshi o'ylar, haq so'zlar va ezgu mehnat bilan yashashga undagan.",
                    "answer": "Ezgu fikr, ezgu so'z, ezgu amal"
                },
                {
                    "title": "Qo'yqirilgan qal'a astronomiyasi",
                    "problem": "Xorazmdagi Qo'yqirilgan qal'a (mil.avv. IV-III asrlar) qanday noyob arxitekturaviy vazifani bajargan?",
                    "step_by_step": "Qal'a aylana shaklida qurilgan bo'lib, u bir vaqtning o'zida ham ibodatxona, ham osmon jismlarini (yulduzlar va quyoshni) kuzatuvchi qadimgi rasadxona vazifasini o'tagan.",
                    "answer": "Ibodatxona va qadimgi rasadxona"
                }
            ],
            "exercise": "Zardushtiylikda nima sababdan jasadlar to'g'ridan-to'g'ri tuproqqa ko'milmagan?",
            "exercise_solution": "Zardushtiylikda tuproq, olov va suv muqaddas sanalgan. Murdani yerga ko'mish tuproqni harom qiladi deb hisoblanib, maxsus suyakdonlar (ossuariylar)da saqlangan.",
            "check_questions": [
                {
                    "question": "Zardushtiylik dinining muqaddas kitobi nima deb ataladi?",
                    "options": ["Veda", "Avesto", "Injil", "Qur'on"],
                    "correct_index": 1,
                    "explanation": "Zardushtiylarning muqaddas yozma yodgorligi 'Avesto'dir."
                },
                {
                    "question": "Qadimgi Samarqand shahri antik manbalarda qanday nom bilan atalgan?",
                    "options": ["Baqtra", "Maroqanda", "Kesh", "Termiz"],
                    "correct_index": 1,
                    "explanation": "Yunon-rim tarixchilari (Arrian, Kursiy Ruf) Samarqandni Maroqanda deb atashgan."
                },
                {
                    "question": "'Avesto' dagi ezgulik va yorug'lik xudosi kim?",
                    "options": ["Axriman", "Axuramazda", "Mitra", "Anaxita"],
                    "correct_index": 1,
                    "explanation": "Axuramazda (Hormuzd) — zardushtiylikda yorug'lik, donolik va ezgulik tangrisidir."
                }
            ],
            "tags": ["o'zbekiston tarixi", "baqtriya", "so'g'diyona", "xorazm", "avesto", "zardushtiylik", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "his-003",
            "slug": "ahmoniylar-va-aleksandr-makedonskiy-bosqini",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "Xalq ozodlik kurashlari: To'maris, Shiroq va Aleksandr Makedonskiyga qarshi Spitamen qo'zg'oloni",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Fors podshosi Kir II ning massagetlar tomonidan tor-mor etilishi, Doro I ga qarshi Shiroq jasorati va Aleksandr Makedonskiyga qarshi Spitamen boshchiligidagi ozodlik kurashini o'rganish.",
            "theory": "Miloddan avvalgi VI asrda Eron ahmoniylari O'rta Osiyoni bosib olishga urindi. Mil. avv. 530-yilda Kir II massagetlar yurtiga bostirib kirdi, ammo To'maris boshchiligidagi jangchilar forslarni butunlay yakson qildi va Kir II o'ldirildi. Mil. avv. 519-yilda saklar podshosi Skunxa va cho'pon Shiroq o'z jonini fido qilib Doro I qo'shinini dashtda suvsizlik va halokatga boshladi. Mil. avv. 329-yilda Aleksandr Makedonskiy (Iskandar Zulqarnayn) Movarounnahrga bostirib kirdi. Maroqanda (Samarqand) vayron qilindi. Bunga javoban So'g'diyona va Baqtriyada Spitamen boshchiligida xalq qo'zg'oloni ko'tarildi (mil. avv. 329-327 yillar). Spitamen yunon-makedon qo'shiniga bir necha bor qaqshatqich zarba berdi (Politimet / Zarafshon jangi). Iskandar mahalliy zodagonlar bilan kelishish uchun Oksiartning qizi Ruxshona (Roksana)ga uylanishga majbur bo'ldi.",
            "examples": [
                {
                    "title": "To'maris jasorati",
                    "problem": "Gerodot o'z 'Tarix' asarida To'maris va Kir II jangi haqida nima deb yozgan?",
                    "step_by_step": "Gerodot bu jangni 'varvarlar o'rtasida bo'lgan barcha janglarning eng qonlisi va dahshatlisi' deb atagan. To'maris Kirning kallasini qon to'ldirilgan meshga solib: 'Qonxo'r eding, mana endi qonga to'y!' degan afsonaviy so'zlarni aytgan.",
                    "answer": "Forslar tor-mor qilingan va Kir II o'ldirilgan"
                },
                {
                    "title": "Spitamen partizanlik taktikasi",
                    "problem": "Spitamen Aleksandr Makedonskiyning kuchli muntazam armiyasiga qarshi qanday jang usulini qo'lladi?",
                    "step_by_step": "U dasht ko'chmanchilari (massagetlar) bilan ittifoq tuzib, to'satdan tezkor zarba berish va dashtga chekinish (partizanlik) taktikasidan foydalandi.",
                    "answer": "Tezkor zarba va chekinish (partizanlik) usuli"
                }
            ],
            "exercise": "Cho'pon Shiroqning jasorati nimadan iborat bo'lgan?",
            "exercise_solution": "Shiroq o'z burni va quloqlarini kesib, xoin qiyofasida Doro I armiyasini aldaydi va ularni 7 kun suvsiz Qizilqum cho'li qa'riga boshlab, dushmanning katta qismini qirib yuboradi va o'zi mardonavor halok bo'ladi.",
            "check_questions": [
                {
                    "question": "Miloddan avvalgi 530-yilda forslar bosqiniga qarshi kurashgan massagetlar malikasi kim?",
                    "options": ["Zarina", "To'maris", "Ruxshona", "Barchin"],
                    "correct_index": 1,
                    "explanation": "Malika To'maris fors shohi Kir II ni tor-mor keltirib, mustaqillikni himoya qilgan."
                },
                {
                    "question": "Aleksandr Makedonskiyga qarshi 3 yil davomida (mil. avv. 329-327) mardonavor kurashgan so'g'd sarkardasi kim?",
                    "options": ["Oksiart", "Spitamen", "Skunxa", "Bess"],
                    "correct_index": 1,
                    "explanation": "Spitamen Iskandar armiyasiga eng kuchli qarshilik ko'rsatgan buyuk vatanparvar sarkardadir."
                },
                {
                    "question": "Aleksandr Makedonskiy qaysi so'g'd aslzodasining qizi Ruxshonaga uylangan?",
                    "options": ["Spitamen", "Oksiart", "Doro", "Por"],
                    "correct_index": 1,
                    "explanation": "Iskandar mahalliy zodagonlar bilan yarashish maqsadida Oksiartning qizi Ruxshonaga uylangan."
                }
            ],
            "tags": ["o'zbekiston tarixi", "to'maris", "shiroq", "spitamen", "makedonskiy", "6-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "his-004",
            "slug": "buyuk-ipak-yoli-va-kushon-saltanati",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "Buyuk Ipak yo'li va Kushon saltanati: madaniyatlar chorrahasi",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Buyuk Ipak yo'lining vujudga kelishi (mil. avv. II asr), yo'nalishlari hamda Kushon imperiyasi davridagi buddaviylik madaniyati (Dalvarzintepa, Fayoztepa)ni o'rganish.",
            "theory": "Buyuk Ipak yo'li miloddan avvalgi II asrda xitoylik sayyoh Chjan Syan elchiligi natijasida muntazam savdo yo'liga aylandi. U Xitoyning qadimgi poytaxti Chanyandan boshlanib, O'rta Osiyo orqali O'rta Yer dengizi va Rim imperiyasigacha 7000 km dan ortiq masofaga cho'zilgan. Ipak, chinnibuyumlar, qog'oz, otlar, dorivor giyohlar bilan birga madaniyatlar, dinlar va ilmiy yutuqlar almashilgan. Kushon imperiyasi (milodiy I-III asrlar) — Kanishka davrida ulkan imperiyaga aylangan (Hindiston, Pokiston, Afg'oniston va O'zbekiston janubi). Dinlararo bag'rikenglik hukm surgan: zardushtiylik, buddaviylik, ellin xudolari barobar e'zozlangan. Dalvarzintepadan (Surxondaryo) 36 kg sof tilla taqinchoqlar va dunyodagi eng qadimgi fil suyagi shaxmat donalari topilgan; Fayoztepa va Qoratepada ulkan budda monastirlari qad rostlagan.",
            "examples": [
                {
                    "title": "Dalvarzintepa xazinasi",
                    "problem": "Dalvarzintepada qilingan qaysi arxeologik topilma Kushon davri san'atini butun dunyoga tanitdi?",
                    "step_by_step": "1972-yilda arxeologlar Dalvarzintepadan 36 kg dan ortiq og'irlikdagi sof tilla quyma va zargarlik buyumlari xazinasini hamda qadimgi budda haykallarini topdilar.",
                    "answer": "36 kg lik tilla xazina va budda haykallari"
                },
                {
                    "title": "Buyuk Ipak yo'li xalqaro ahamiyati",
                    "problem": "Nima uchun Buyuk Ipak yo'li faqat savdo yo'li emas, balki sivilizatsiyalar ko'prigi deb ataladi?",
                    "step_by_step": "Chunki u orqali qog'oz, shoyi, kompas, dinlar (buddaviylik, islom), me'morchilik san'ati va ilmiy bilimlar Sharq va G'arb o'rtasida keng tarqalgan.",
                    "answer": "Ilmiy bilimlar, madaniyat va texnologiyalar almashinuvi vositasi bo'lgani uchun"
                }
            ],
            "exercise": "Kushon saltanatining eng qudratli hukmdori kim bo'lgan va uning davrida qaysi din keng tarqalgan?",
            "exercise_solution": "Kanishka I (milodiy II asr); uning davrida buddaviylik davlat homiyligidagi keng tarqalgan dinga aylangan.",
            "check_questions": [
                {
                    "question": "Buyuk Ipak yo'lining asosiy qatnovi qaysi asrda shakllangan?",
                    "options": ["Mil.avv. X asrda", "Mil.avv. II asrda", "Milodiy V asrda", "Milodiy IX asrda"],
                    "correct_index": 1,
                    "explanation": "Miloddan avvalgi II asrda Chjan Syan sayohatidan so'ng muntazam savdo aloqalari yo'lga qo'yilgan."
                },
                {
                    "question": "Kushon imperiyasining eng gullagan davri qaysi shoh hukmronligiga to'g'ri keladi?",
                    "options": ["Kudzul Kadfiz", "Kanishka", "Vima Kadfiz", "Vasudeva"],
                    "correct_index": 1,
                    "explanation": "Kanishka I davrida saltanat o'z qudratining cho'qqisiga erishgan."
                },
                {
                    "question": "O'zbekistondagi mashhur Fayoztepa va Qoratepa budda yodgorliklari qaysi viloyatda joylashgan?",
                    "options": ["Samarqand", "Buxoro", "Surxondaryo (Termiz)", "Xorazm"],
                    "correct_index": 2,
                    "explanation": "Fayoztepa va Qoratepa qadimgi Termiz yaqinida, Surxondaryoda joylashgan."
                }
            ],
            "tags": ["o'zbekiston tarixi", "buyuk ipak yo'li", "kushonlar", "kanishka", "dalvarzintepa", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "his-005",
            "slug": "somoniylar-davlati-va-sharq-uygonish-davri",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "Ilk O'rta asrlar: Somoniylar davlati va Birinchi Sharq Renessansi (IX-XII asrlar)",
            "grade_level": "7-8-sinf",
            "difficulty": "Murakkab",
            "objective": "Ismoil Somoniy davlati, Buxoroning poytaxtga aylanishi, devonlar tizimi hamda Al-Xorazmiy, Al-Farg'oniy, Beruniy, Ibn Sino ilmiy merosini o'rganish.",
            "theory": "IX asr oxirida Movarounnahr va Xuroson arab xalifaligidan ajralib chiqib, mustaqil Somoniylar davlati (875-999) barpo etildi. Asoschisi — Ismoil Somoniy. Buxoro poytaxtga aylanib, 'Qubbatul Islom' va jahon ilm-fan markaziga aylandi. Boshqaruv devonlar tizimi (10 ta devon: vazir, moliya, xiroj, mushrif, barid/pochta...) orqali yuritildi. Buxoroda mashhur 'Sivonul-hikmat' kutubxonasi faoliyat yuritgan. IX-XII asrlarda mintaqada 'Birinchi Sharq Uyg'onish davri' (Sharq Renessansi) yuz berdi: 1) Muhammad al-Xorazmiy — algebra fanining asoschisi ('al-jabr'), algoritm atamasi muallifi; 2) Ahmad al-Farg'oniy — astronomiya, Nil daryosida 'Nilometr' quruvchisi; 3) Abu Rayhon Beruniy — Yer radiusini hisoblagan, 'Qadimgi xalqlardan qolgan yodgorliklar', 'Hindiston', 'Geodeziya'; 4) Abu Ali ibn Sino — 'Tib qonunlari' muallifi, jahon tabobati otasi; 5) Imom al-Buxoriy — hadis ilmining sultoni ('Al-jome' as-sahih').",
            "examples": [
                {
                    "title": "Al-Xorazmiy kashfiyoti",
                    "problem": "'Algoritm' va 'Algebra' atamalari Al-Xorazmiy nomi bilan qanday bog'liq?",
                    "step_by_step": "1) 'Al-jabr' asari nomidan zamonaviy 'Algebra' fani nomi kelib chiqqan;\n2) Uning lotinlashtirilgan 'Algoritmi' ismi esa amallarning ketma-ket aniq bajarilish qoidasi — 'Algoritm' tushunchasiga asos bo'lgan.",
                    "answer": "'Al-jabr' kitobidan Algebra, 'Algoritmi' ismidan Algoritm atamalari olingan"
                },
                {
                    "title": "Ibn Sinoning 'Tib qonunlari'",
                    "problem": "Ibn Sinoning 'Al-Qonun fit-tibb' asari Yevropa tibbiyotida qanday mavqega ega bo'lgan?",
                    "step_by_step": "Bu asar lotin tiliga tarjima qilinib, 500 yildan ortiq vaqt davomida Yevropaning barcha yetakchi universitetlarida (Sorbonna, Bolonya) asosiy tibbiyot darsligi sifatida o'qitilgan.",
                    "answer": "Yevropa universitetlarida 5 asr davomida asosiy darslik bo'lgan"
                }
            ],
            "exercise": "Abu Rayhon Beruniy Yer sharining radiusini qanday aniqlik bilan hisoblagan?",
            "exercise_solution": "Beruniy trigonometrik usul bilan Yer radiusini 6339.6 km deb hisoblagan (zamonaviy o'lchovdan bor-yo'g'i ~16 km ga farq qiladi, 99.8% aniqlik).",
            "check_questions": [
                {
                    "question": "Somoniylar davlatining poytaxti qaysi shahar bo'lgan?",
                    "options": ["Samarqand", "Buxoro", "Urganch", "Hirot"],
                    "correct_index": 1,
                    "explanation": "Buxoro shahri Somoniylar davrida saltanat poytaxti va buyuk madaniyat markazi bo'lgan."
                },
                {
                    "question": "Algebra faniga asos solgan buyuk alloma kim?",
                    "options": ["Abu Rayhon Beruniy", "Muhammad al-Xorazmiy", "Mirzo Ulug'bek", "Ibn Sino"],
                    "correct_index": 1,
                    "explanation": "Al-Xorazmiy tenglamalarni yechish qoidalarini ishlab chiqib, algebraga asos solgan."
                },
                {
                    "question": "Hadis ilmining buyuk namoyandasi, 'Al-jome' as-sahih' muallifi kim?",
                    "options": ["Imom at-Termiziy", "Imom al-Buxoriy", "Mahmud az-Zamaxshariy", "Burhoniddin Marg'inoniy"],
                    "correct_index": 1,
                    "explanation": "Imom al-Buxoriy islom olamida Qur'ondan keyingi eng ishonchli hadislar to'plamini tuzgan."
                }
            ],
            "tags": ["o'zbekiston tarixi", "somoniylar", "sharq renessansi", "xorazmiy", "beruniy", "ibn sino", "buxoriy", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "his-006",
            "slug": "amir-temur-va-temuriylar-saltanati",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "Sohibqiron Amir Temur: markazlashgan qudratli davlat va Temuriylar renessansi",
            "grade_level": "8-sinf",
            "difficulty": "Murakkab",
            "objective": "Amir Temur harbiy san'ati, davlat boshqaruvi ('Temur tuzuklari'), bunyodkorlik ishlari hamda Mirzo Ulug'bek va Husayn Boyqaro davridagi madaniy yuksalish.",
            "theory": "Amir Temur (1336-1405) — buyuk sarkarda, davlat arbobi va Temuriylar saltanatining asoschisi. Kesh (Shahrisabz) yaqinidagi Xo'ja Ilg'or qishlog'ida tug'ilgan. Mo'g'ullar zulmiga qarshi 10 yillik kurashdan so'ng 1370-yilda Balx qurultoyida Movarounnahrning oliy hukmdori deb e'lon qilindi va Samarqandni poytaxt etdi. Uning bosh shiori: 'Kuch — adolatdadir'. 'Temur tuzuklari' — davlat boshqaruvi va harbiy qonun-qoidalar majmuasidir. U 27 ta davlatni o'z ichiga olgan qudratli saltanat tuzdi, Oltin O'rda xoni To'xtamishni (1395) va Usmonli turk sultoni Boyazid Yildirimni (Anqara jangi, 1402) yengib Yevropani istilodan qutqardi. Bunyodkorlik: Samarqandda Bibixonim jome masjidi, Go'ri Amir maqbarasi, Shahrisabzda Oqsaroy, Turkistonda Ahmad Yassaviy maqbarasini qurdirdi. Mirzo Ulug'bek (1394-1449) — davlat arbobi va buyuk astronom, Samarqandda rasadxona qurib, 1018 ta yulduz jadvalini ('Ziji jadidi Ko'ragoniy') tuzgan.",
            "examples": [
                {
                    "title": "'Kuch — adolatdadir' shiori",
                    "problem": "Amir Temur davlat boshqaruvida nima sababdan adolatni eng oliy tamoyil qilib belgilagan?",
                    "step_by_step": "Sohibqiron adolatsiz davlat uzoq yashay olmasligini, xalq rozi bo'lsa saltanat mustahkam bo'lishini chuqur tushungan. Barcha qonunlar, soliqlarning me'yori va amaldorlar nazorati adolat qoidasiga bo'ysundirilgan.",
                    "answer": "Davlatning barqarorligi va qudrati xalq roziligi va adolatda ekani uchun"
                },
                {
                    "title": "Ulug'bek rasadxonasining aniqligi",
                    "problem": "Mirzo Ulug'bek bir yillik vaqt davomiyligini qanday aniqlikda hisoblagan?",
                    "step_by_step": "Ulug'bek yil hisobini 365 kun, 6 soat, 10 daqiqa, 8 soniya deb belgilagan. Bu zamonaviy atom soatlaridan bor-yo'g'i 58 soniyaga farq qiladi.",
                    "answer": "Zamonaviy ko'rsatkichdan atigi 58 soniya farq bilan hisoblagan"
                }
            ],
            "exercise": "Amir Temur tomonidan Fransiyaga qirol Karl VI ga yuborilgan maktubning maqsadi nima edi?",
            "exercise_solution": "Ipak yo'li bo'ylab savdo-sotiqni erkin rivojlantirish, savdogarlar xavfsizligini kafolatlash va davlatlararo diplomatik munosabatlarni o'rnatish.",
            "check_questions": [
                {
                    "question": "Amir Temur qachon va qayerdagi qurultoyda Movarounnahrning oliy hukmdori deb e'lon qilingan?",
                    "options": ["1365-yilda Samarqandda", "1370-yilda Balxda", "1380-yilda Keshda", "1395-yilda Buxoroda"],
                    "correct_index": 1,
                    "explanation": "1370-yil aprelda Balx qurultoyida Amir Temur rasman buyuk amir deb e'tirof etilgan."
                },
                {
                    "question": "Amir Temurning davlat va harbiy boshqaruv qonun-qoidalari aks etgan kitobi nima deb ataladi?",
                    "options": ["Zafarnoma", "Temur tuzuklari", "Tarixi Jahonkushoy", "Qobusnoma"],
                    "correct_index": 1,
                    "explanation": "'Temur tuzuklari' Sohibqironning o'z tajribalari va davlat boshqaruvi dasturidir."
                },
                {
                    "question": "Mirzo Ulug'bek rasadxonasida tuzilgan 1018 yulduzning koordinatalari jadvali nima deb ataladi?",
                    "options": ["Ziji jadidi Ko'ragoniy", "Al-Qonun", "Suratul-arz", "Xamsa"],
                    "correct_index": 0,
                    "explanation": "'Ziji jadidi Ko'ragoniy' (Ulug'bek yulduzlar jadvali) asrlar davomida dunyo astronomlarining qo'llanmasi bo'lgan."
                }
            ],
            "tags": ["o'zbekiston tarixi", "amir temur", "temuriylar", "ulug'bek", "samarqand", "oqsaroy", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "his-007",
            "slug": "uch-xonlik-davri-buxoro-xiv-va-qoqon",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "O'zbek xonliklari davri: Buxoro amirligi, Xiva xonligi va Qo'qon xonligi",
            "grade_level": "8-9-sinf",
            "difficulty": "O'rta",
            "objective": "XVI-XIX asrlarda O'zbekiston hududidagi uchta davlatning vujudga kelishi, siyosiy tuzilishi, iqtisodiyoti, o'zaro nizolar va parokandalik oqibatlarini o'rganish.",
            "theory": "XVI asrda shayboniylar istilosidan so'ng Movarounnahr va Xorazm hududida uchta mustaqil davlat vujudga keldi: 1) Buxoro xonligi (amirligi) — shayboniylar, ashtarxoniylar va mang'itlar sulolasi boshqargan. Poytaxti — Buxoro. Amir Shohmurod va Amir Nasrullo davrida markaziy hokimiyat mustahkamlangan; 2) Xiva xonligi (Xorazm) — shayboniylarning arabshohiylar va qo'ng'irotlar sulolasi tomonidan boshqarilgan. Poytaxti dastlab Vazir, so'ng Xiva bo'lgan (Ichan qal'a me'moriy ansambli, Muhammad Rahimxon I va Feruz davri madaniy yuksalishi); 3) Qo'qon xonligi — XVIII asr boshida Farg'ona vodiysida tashkil topgan (minglar sulolasi, asoschisi Shohruxbiy). Poytaxti — Qo'qon. Olimxon, Umarxon va Nodirabegim davrida hududi kengaygan (Toshkent va Janubiy Qozog'istonni qo'shib olgan), Xudoyorxon o'rdasi qurilgan. Uch xonlikning o'zaro urushlari, iqtisodiy tarqoqlik va taraqqiyotdan orqada qolish XIX asr o'rtalarida Rossiya imperiyasi tomonidan osonlik bilan bosib olinishiga sabab bo'ldi.",
            "examples": [
                {
                    "title": "Xiva shahrining o'rni",
                    "problem": "Xivadagi 'Ichan qal'a' yodgorligining o'ziga xosligi nimada?",
                    "step_by_step": "Ichan qal'a — butunlay yaxlit saqlanib qolgan ochiq osmon ostidagi tarixiy muzey-shahar bo'lib, Markaziy Osiyodagi birinchi YUNESKO Butunjahon madaniy merosi ro'yxatiga kiritilgan yodgorlikdir.",
                    "answer": "Yaxlit saqlangan muzey-shahar (YUNESKO merosi)"
                },
                {
                    "title": "Xonliklar parokandaligi fojiasi",
                    "problem": "Uch xonlik o'rtasidagi to'xtovsiz urushlar qanday oqibatga olib keldi?",
                    "step_by_step": "Doimiy qonli urushlar xalq xo'jaligini vayron qildi, ilmiy-texnik taraqqiyotdan uzilib qolishga va chor Rossiyasi qo'shinlari oldida himoyasiz qolib, mustamlaka bo'lishga olib keldi.",
                    "answer": "Iqtisodiy inqiroz va chorizm mustamlakasiga aylanish"
                }
            ],
            "exercise": "Qo'qon xonligida ma'rifat va adabiyot homiysi bo'lgan mashhur shoira va malika kim edi?",
            "exercise_solution": "Nodirabegim (Mohlaroyim) — Umarxonning rafiqasi, shoira va davlat arbobi.",
            "check_questions": [
                {
                    "question": "Buxoroda 1756-yildan 1920-yilgacha qaysi sulola hukmronlik qilgan?",
                    "options": ["Shayboniylar", "Ashtarxoniylar", "Mang'itlar", "Qo'ng'irotlar"],
                    "correct_index": 2,
                    "explanation": "Buxoro amirligida 1756-yildan to qulaguncha mang'it amirlari hukmronlik qilgan."
                },
                {
                    "question": "Farg'ona vodiysida tashkil topgan Qo'qon xonligiga qaysi sulola asos solgan?",
                    "options": ["Minglar", "Qo'ng'irotlar", "Mang'itlar", "Kenagaslar"],
                    "correct_index": 0,
                    "explanation": "Qo'qon xonligi o'zbeklarning ming urug'i vakili Shohruxbiy tomonidan tashkil etilgan."
                },
                {
                    "question": "Shoir Feruz taxallusi bilan ijod qilgan Xiva xoni kim?",
                    "options": ["Muhammad Rahimxon II", "Eltuzarxon", "Ollaqulixon", "Asfandiyorxon"],
                    "correct_index": 0,
                    "explanation": "Muhammad Rahimxon II Feruz taxallusi bilan g'azallar yozgan, kitob bosishni yo'lga qo'ygan."
                }
            ],
            "tags": ["o'zbekiston tarixi", "buxoro amirligi", "xiva xonligi", "qo'qon xonligi", "ichan qal'a", "nodirabegim", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "his-008",
            "slug": "chor-rossiyasi-istilosi-va-mustamlaka-tuzumi",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "Chor Rossiyasi istilosi, Turkiston general-gubernatorligi va milliy ozodlik harakatlari",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Chorizm bosqini bosqichlari (Toshkentning olinishi, 1865), Turkiston general-gubernatorligi tuzumi hamda Dukchi eshon (1898) va 1916-yilgi xalq qo'zg'olonlarini o'rganish.",
            "theory": "Rossiya imperiyasi to'qimachilik sanoatini arzon paxta xomashyosi va yangi bozorlar bilan ta'minlash maqsadida 1860-yillardan O'rta Osiyoga harbiy yurish boshladi. 1865-yil iyun oyida general M. Chernyayev boshchiligidagi qo'shin Toshkentni 3 kunlik qamaldan so'ng egalladi. 1867-yilda Turkiston general-gubernatorligi tashkil etildi (birinchi gubernator — K. Kaufman). 1868-yilda Buxoro amirligi, 1873-yilda Xiva xonligi vassalga aylantirildi (protektorat), 1876-yilda esa Qo'qon xonligi butunlay tugatildi va Farg'ona viloyatiga aylantirildi. Mustamlaka zulmi: xalq yerlarining tortib olinishi, paxta yakkahokimligi (monokultura), og'ir soliqlar. Bunga javoban milliy ozodlik qo'zg'olonlari ko'tarildi: 1) 1898-yilgi Andijon qo'zg'oloni (rahbari — Muhammadali eshon / Dukchi eshon); 2) 1916-yilgi umumxalq qo'zg'oloni (podshoning mardikorlikka olish to'g'risidagi farmoniga qarshi: Jizzax, Toshkent, Andijon qo'zg'olonlari).",
            "examples": [
                {
                    "title": "Toshkent mudofaasi (1865)",
                    "problem": "1865-yilda general Chernyayev qo'shinlariga qarshi Toshkent mudofaasini kim boshqargan?",
                    "step_by_step": "Toshkent mudofaasiga Qo'qon qo'shini lashkarboshisi Alimqul boshchilik qilgan. U qattiq yaralanib halok bo'lgach, shahar mudofaasi zaiflashib, oqsoqollar taslim bo'lishga majbur bo'lgan.",
                    "answer": "Lashkarboshi Alimqul"
                },
                {
                    "title": "1916-yilgi qo'zg'olon sababi",
                    "problem": "1916-yilgi butun Turkiston bo'ylab ko'tarilgan xalq qo'zg'oloniga qaysi voqea sabab bo'ldi?",
                    "step_by_step": "Rossiya podshosi Nikolay II ning 1916-yil 25-iyundagi Turkistonning 19 yoshdan 43 yoshgacha bo'lgan tub aholisini Birinchi jahon urushi front orti qora ishlariga (mardikorlikka) majburiy safarbar qilish haqidagi farmoni xalq g'azabini portlatdi.",
                    "answer": "Front orti mardikorligiga majburiy olish to'g'risidagi farmon"
                }
            ],
            "exercise": "Dukchi eshon boshchiligidagi Andijon qo'zg'oloni qachon bo'lib o'tdi va uning maqsadi nima edi?",
            "exercise_solution": "1898-yil may oyida; maqsadi chorizm mustamlakachilarini quvib chiqarish va xonlik boshqaruvini tiklash edi.",
            "check_questions": [
                {
                    "question": "Turkiston general-gubernatorligi qaysi yili tashkil etildi va uning markazi qaysi shahar bo'ldi?",
                    "options": ["1865-yil Samarqand", "1867-yil Toshkent", "1876-yil Qo'qon", "1880-yil Ashxobod"],
                    "correct_index": 1,
                    "explanation": "1867-yilda Turkiston general-gubernatorligi tuzildi va Toshkent uning ma'muriy markazi bo'ldi."
                },
                {
                    "question": "Qo'qon xonligi qaysi yili rasman tugatildi?",
                    "options": ["1865-yilda", "1868-yilda", "1873-yilda", "1876-yilda"],
                    "correct_index": 3,
                    "explanation": "Po'latxon qo'zg'oloni bostirilgach, 1876-yil fevralda Qo'qon xonligi rasman tugatilib, Farg'ona viloyatiga aylantirildi."
                },
                {
                    "question": "1916-yilgi xalq harakatida eng qonli to'qnashuv va qirg'in qaysi shaharda yuz berdi?",
                    "options": ["Jizzaxda", "Xivada", "Buxoroda", "Qarshida"],
                    "correct_index": 0,
                    "explanation": "Jizzaxda general Ivanov qo'shinlari qo'zg'olonni bostirishda shaharni to'plardan o'qqa tutib, yondirib yuborgan."
                }
            ],
            "tags": ["o'zbekiston tarixi", "chorizm", "toshkent", "turkiston", "1916 qo'zg'oloni", "dukchi eshon", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "his-009",
            "slug": "turkiston-muxtoriyati-va-sovet-qatagoni",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "Turkiston Muxtoriyati (1917-1918), bosmachilik harakati va 1937-1938 yillardagi sovet qatag'oni",
            "grade_level": "9-sinf",
            "difficulty": "Murakkab",
            "objective": "Turkiston Muxtoriyati (Qo'qon muxtoriyati), qizil armiya qirg'ini, qurolli istiqlolchilik harakati va 'Katta terror' davri milliy ziyolilar qatag'onini o'rganish.",
            "theory": "1917-yil noyabrda Qo'qonda IV umumturkiston o'lka musulmonlar qurultoyida Turkiston Muxtoriyati (demokratik mustaqil respublika) e'lon qilindi. Hukumat rahbarlari: Muhammadjon Tinishboyev, so'ng Mustafo Cho'qay. 1918-yil fevralda bolsheviklar qizil armiyasi va dashnoqlar Qo'qonga bostirib kirib, 3 kun ichida shaharni yondirdi va 10 mingdan ortiq begunoh aholini qirib tashladi. Muxtoriyat fojiasi butun Farg'ona vodiysi, Buxoro va Xorazmda Sovet bosqiniga qarshi qurolli milliy ozodlik ('Istiqlolchilik' / sovetcha 'bosmachilik') harakatini keltirib chiqardi (Madaminbek, Shermuhammadbek, Ibrohimbek). 1924-yilda O'rta Osiyoda milliy-hududiy chegaralanish o'tkazilib, O'zbekiston SSR tuzildi. 1937-1938 yillardagi stalincha qatag'on ('Katta qatag'on'): millatning butun aqliy qaymog'i — Fitrat, Cho'lpon, Abdulla Qodiriy, Fayzulla Xo'jayev, Akmal Ikromov va minglab ma'rifatparvarlar 'xalq dushmani' sifatida otib tashlandi.",
            "examples": [
                {
                    "title": "Turkiston Muxtoriyatining ahamiyati",
                    "problem": "Bor-yo'g'i 72 kun yashagan Turkiston Muxtoriyatining tarixiy ahamiyati nimada?",
                    "step_by_step": "U o'zbek va butun Turkiston xalqlarining zamonaviy parlamentarizm, demokratik taraqqiyot va milliy mustaqillikka intilishining ilk yorqin amaliy ifodasi bo'ldi.",
                    "answer": "Demokratik milliy davlatchilikka intilishning ilk ramzi"
                },
                {
                    "title": "1937-1938 yillardagi qatag'on ko'lami",
                    "problem": "O'zbekistonda stalincha qatag'on qurbonlari xotirasi qanday abadiylashtirilgan?",
                    "step_by_step": "Toshkentda 'Shahidlar xotirasi' yodgorlik majmuasi va Qatag'on qurbonlari xotirasi davlat muzeyi barpo etilgan, har yili 31-avgust Qatag'on qurbonlarini yod etish kuni sifatida nishonlanadi.",
                    "answer": "'Shahidlar xotirasi' majmuasi va 31-avgust yod etish kuni"
                }
            ],
            "exercise": "Mustafo Cho'qay xorijga muhojirlikka ketgach, milliy istiqlol uchun qanday kurash olib bordi?",
            "exercise_solution": "Parij va Berlinda 'Yosh Turkiston' jurnalini nashr etib, sovet mustamlakachiligining asl qiyofasini va Turkiston mustaqilligi g'oyasini Yevropa xalqlariga yetkazdi.",
            "check_questions": [
                {
                    "question": "Turkiston Muxtoriyati qaysi shaharda e'lon qilingan va necha kun yashagan?",
                    "options": ["Toshkentda, 1 yil", "Qo'qonda, 72 kun", "Samarqandda, 100 kun", "Buxoroda, 6 oy"],
                    "correct_index": 1,
                    "explanation": "1917-yil 27-noyabrda Qo'qonda e'lon qilingan va bolsheviklar tomonidan 72 kundan keyin qonga botirilgan."
                },
                {
                    "question": "1938-yil 4-oktyabrda Toshkentda otib tashlangan buyuk o'zbek adiblari kimlar edi?",
                    "options": ["Alisher Navoiy va Bobur", "Abdulla Qodiriy, Cho'lpon, Fitrat", "G'afur G'ulom va Oybek", "Hamza va Avloniy"],
                    "correct_index": 1,
                    "explanation": "Qodiriy, Cho'lpon va Fitrat 1938-yil 4-oktyabr kuni qatag'on qilinib otib tashlangan."
                },
                {
                    "question": "O'zbekiston SSR qaysi yili tashkil topgan?",
                    "options": ["1917-yil", "1920-yil", "1924-yil", "1936-yil"],
                    "correct_index": 2,
                    "explanation": "1924-yil oktyabr oyida milliy-hududiy chegaralanish natijasida O'zbekiston SSR tuzildi."
                }
            ],
            "tags": ["o'zbekiston tarixi", "turkiston muxtoriyati", "qo'qon", "mustafo cho'qay", "qatag'on", "qodiriy", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "his-010",
            "slug": "ozbekiston-respublikasi-mustaqilligi-va-taraqqiyoti",
            "subject_id": "sub-23",
            "subject_name": "O‘zbekiston tarixi",
            "title": "O'zbekiston Respublikasining davlat mustaqilligi: e'lon qilinishi, Konstitutsiya va zamonaviy taraqqiyot",
            "grade_level": "11-sinf",
            "difficulty": "O'rta",
            "objective": "Mustaqillik Deklaratsiyasi, 1991-yil 31-avgust davlat mustaqilligining e'lon qilinishi, Davlat ramzlari, Bosh qomusimiz (Konstitutsiya) va Yangi O'zbekiston islohotlarini o'rganish.",
            "theory": "1990-yil 20-iyunda O'zbekiston SSR Oliy Kengashi tomonidan 'Mustaqillik Deklaratsiyasi' qabul qilindi. 1991-yil 31-avgustda O'zbekiston Respublikasining davlat mustaqilligi tantanali ravishda e'lon qilindi va 1-sentyabr Mustaqillik kuni deb belgilandi. Davlat ramzlari: Davlat bayrog'i (1991-yil 18-noyabr), Davlat gerbi (1992-yil 2-iyul), Davlat madhiyasi (1992-yil 10-dekabr). 1992-yil 8-dekabrda Mustaqil O'zbekistonning birinchi Konstitutsiyasi qabul qilindi (2023-yil 30-apreldagi umumxalq referendumi bilan yangi tahrirdagi Konstitutsiya qabul qilindi: O'zbekiston — suveren, demokratik, huquqiy, ijtimoiy va dunyoviy davlat). 1992-yil 2-martda O'zbekiston Birlashgan Millatlar Tashkilotiga (BMT) to'la huquqli a'zo bo'ldi. 1994-yilda milliy valyuta — so'm muomalaga kiritildi. Yangi O'zbekiston taraqqiyot strategiyasi inson qadrini ulug'lash, iqtisodiyotni liberallashtirish, ta'limni rivojlantirish va ochiq tashqi siyosatga tayanadi.",
            "examples": [
                {
                    "title": "BMTga a'zolik",
                    "problem": "O'zbekiston Respublikasi qachon Birlashgan Millatlar Tashkilotiga a'zo bo'ldi va Nyu-Yorkda bayrog'imiz qachon ko'tarildi?",
                    "step_by_step": "1992-yil 2-martda BMT Bosh Assambleyasining yalpi majlisida O'zbekiston bir ovozdan BMT a'zoligiga qabul qilindi va tashkilot bosh qarorgohi oldida davlatimiz bayrog'i hilpiradi.",
                    "answer": "1992-yil 2-mart kuni"
                },
                {
                    "title": "Yangi tahrirdagi Konstitutsiya",
                    "problem": "2023-yilgi referendumda qabul qilingan Konstitutsiyada O'zbekiston qanday davlat deb e'lon qilingan?",
                    "step_by_step": "Yangi tahrirdagi 1-moddaga ko'ra: 'O'zbekiston — boshqaruvning respublika shakliga ega bo'lgan suveren, demokratik, huquqiy, ijtimoiy va dunyoviy davlat'.",
                    "answer": "Suveren, demokratik, huquqiy, ijtimoiy va dunyoviy davlat"
                }
            ],
            "exercise": "O'zbekiston milliy valyutasi — so'm qachon muomalaga kiritilgan?",
            "exercise_solution": "1994-yil 1-iyulda O'zbekiston Respublikasining milliy valyutasi 'so'm' rasman muomalaga chiqarildi.",
            "check_questions": [
                {
                    "question": "O'zbekiston Respublikasi davlat mustaqilligi qachon e'lon qilingan?",
                    "options": ["1990-yil 20-iyun", "1991-yil 31-avgust", "1991-yil 18-noyabr", "1992-yil 8-dekabr"],
                    "correct_index": 1,
                    "explanation": "1991-yil 31-avgustda Oliy Kengashning navbatdan tashqari sessiyasida mustaqillik e'lon qilingan."
                },
                {
                    "question": "O'zbekiston Respublikasi Davlat bayrog'i qachon qabul qilingan?",
                    "options": ["1991-yil 31-avgust", "1991-yil 18-noyabr", "1992-yil 2-iyul", "1992-yil 8-dekabr"],
                    "correct_index": 1,
                    "explanation": "Davlat bayrog'i to'g'risidagi qonun 1991-yil 18-noyabrda qabul qilingan."
                },
                {
                    "question": "O'zbekiston Respublikasi Konstitutsiyasi kuni qaysi sana?",
                    "options": ["1-sentyabr", "18-noyabr", "8-dekabr", "2-mart"],
                    "correct_index": 2,
                    "explanation": "8-dekabr — O'zbekiston Respublikasi Konstitutsiyasi qabul qilingan kun sifatida umumxalq bayrami hisoblanadi."
                }
            ],
            "tags": ["o'zbekiston tarixi", "mustaqillik", "konstitutsiya", "bmt", "davlat ramzlari", "so'm", "11-sinf"],
            "duration_minutes": 35
        },

        # JAHON TARIXI (6)
        {
            "id": "his-011",
            "slug": "qadimgi-misr-va-mexr-sivilizatsiyasi",
            "subject_id": "sub-24",
            "subject_name": "Jahon tarixi",
            "title": "Qadimgi Misr sivilizatsiyasi: fir'avnlar, piramidalar va Nil in'omi",
            "grade_level": "6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Qadimgi Misr davlatchiligi, Nil daryosining roli, fir'avnlar hokimiyati, Xeops ehromi va iyeroglif yozuvlarini bilish.",
            "theory": "Qadimgi Misr — insoniyatning ilk daryo sivilizatsiyalaridan biridir. Tarixchi Gerodot uni 'Nil in'omi' deb atagan (chunki Nil toshqini qora unumdor loyqa qoldirib, dehqonchilikka asos bo'lgan). Miloddan avvalgi 3000-yillarda podsho Menes (Mina) Yuqori va Quyi Misrni birlashtirdi. Fir'avn — Misrning cheklanmagan hokimiyatga ega hukmdori, tirik xudo (Quyosh xudosi Ra o'g'li) hisoblangan. Qadimgi podsholik davrida ulkan piramidalar (ehromlar) qurildi: Gizada joylashgan Xeops ehromi (balandligi 147 metr, dunyoning yetti mo'jizasidan biri). Misrliklar jasadlarni mumiyolagan va ichki a'zolarini kanopalarga solgan. Yozuvi — iyerogliflar (toshga o'yilgan muqaddas belgilar, papirusga yozilgan). Jan-Fransua Shampolyon 1822-yilda Rozetta toshi orqali iyerogliflarni o'qishga muvaffaq bo'lgan.",
            "examples": [
                {
                    "title": "Xeops piramidasi ko'lami",
                    "problem": "Xeops ehromini qurishda qancha tosh blok ishlatilgan va uning vazni qancha?",
                    "step_by_step": "Ehrom 2 million 300 mingdan ortiq har biri o'rtacha 2.5 tonnalik ohaktosh bloklardan tashkil topgan. U minglab yillar davomida dunyodagi eng baland inshoot bo'lib qolgan.",
                    "answer": "2.3 millionta tosh blokdan iborat"
                },
                {
                    "title": "Rozetta toshi kashfiyoti",
                    "problem": "Qadimgi Misr iyerogliflarini o'qishda Rozetta toshi qanday yordam berdi?",
                    "step_by_step": "Rozetta toshida bitta matn uch tilda (iyeroglif, demotik va qadimgi yunoncha) yozilgan edi. Shampolyon ma'lum bo'lgan yunoncha matn bilan qiyoslab iyerogliflar alifbosini yechdi.",
                    "answer": "Yunoncha va iyeroglif matnlarni qiyoslash orqali"
                }
            ],
            "exercise": "Tutanxamun maqbarasi nima sababdan arxeologiya olamida buyuk sensatsiya bo'lgan?",
            "exercise_solution": "1922-yilda Hovard Karter tomonidan topilgan Tutanxamun maqbarasi qadimgi talonchilardan omon qolgan yagona daxlsiz fir'avn qabri bo'lib, sof tilladan yasalgan tobut va minglab bebaho san'at asarlarini saqlagan edi.",
            "check_questions": [
                {
                    "question": "Qadimgi Misr podsholari qanday nomlangan?",
                    "options": ["Xon", "Imperator", "Fir'avn (Faraon)", "Shoh"],
                    "correct_index": 2,
                    "explanation": "Misr hukmdorlari fir'avn deb atalgan."
                },
                {
                    "question": "Dunyoning yetti mo'jizasidan biri bo'lgan eng katta Misr ehromi kimga atab qurilgan?",
                    "options": ["Ramzes II", "Tutanxamun", "Xeops (Xufu)", "Exnaton"],
                    "correct_index": 2,
                    "explanation": "Gizada joylashgan eng yirik ehrom fir'avn Xeopsga atab barpo etilgan."
                },
                {
                    "question": "Misrliklar yozuv uchun qaysi o'simlikdan foydalanganlar?",
                    "options": ["Qamish", "Papirus", "Bambuk", "Barg"],
                    "correct_index": 1,
                    "explanation": "Nil bo'ylarida o'suvchi papirus qamishidan qog'ozsimon yozuv materiali tayyorlangan."
                }
            ],
            "tags": ["jahon tarixi", "qadimgi misr", "nil", "fir'avn", "xeops", "iyeroglif", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "his-012",
            "slug": "antik-dunyo-qadimgi-yunoniston-va-rim",
            "subject_id": "sub-24",
            "subject_name": "Jahon tarixi",
            "title": "Antik dunyo: Qadimgi Yunoniston demokratiyasi va Rim imperiyasi qudrati",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Afina demokratiyasi, Sparta harbiy tuzumi, Olimpiada o'yinlari, Rim respublikasi va imperiyasi, Yuliy Sezar va Rim qonunchiligini o'rganish.",
            "theory": "Antik sivilizatsiya Yevropa madaniyatining poydevoridir. Qadimgi Yunoniston (Ellada) polislar (shahar-davlatlar)dan iborat bo'lgan. Asosiy polislari: 1) Afina — demokratiya (xalq hokimiyati) vatani (Solon va Perikl islohotlari, Xalq majlisi, teatr, falsafa — Suqrot, Aflotun, Arastu); 2) Sparta — qat'iy harbiy tartib va lakonik nutqqa asoslangan aristokratik davlat (Leonid va 300 spartalik jasorati). Mil. avv. 776-yildan Olimpiya o'yinlari o'tkazilgan. Qadimgi Rim (mil. avv. 753-yilda Romul tomonidan asos solingan). Rim tarixi 3 davrga bo'linadi: Podsholik, Respublika (Senat, konsullar, gladiatorlar va Spartak qo'zg'oloni) va Imperiya (Yuliy Sezar diktaturasi, Oktavian Avgust). Rim huquqi zamonaviy huquq tizimining asosini tashkil qiladi. 476-yilda G'arbiy Rim imperiyasining varvarlar tomonidan qulashi bilan Qadimgi dunyo tarixi tugab, O'rta asrlar davri boshlangan.",
            "examples": [
                {
                    "title": "Afina demokratiyasi mohiyati",
                    "problem": "Afina polasida fuqarolarning davlat ishlaridagi ishtiroki qanday ta'minlangan?",
                    "step_by_step": "Barcha 20 yoshga to'lgan erkin erkak fuqarolar Xalq majlisida (Ekklesiya) ovoz bergan, qonunlar qabul qilgan va sudlovda qatnashgan. Mansabdor shaxslar ko'pincha qur'a tashlash orqali saylangan.",
                    "answer": "Xalq majlisi va to'g'ridan-to'g'ri ovoz berish orqali"
                },
                {
                    "title": "Spartak qo'zg'oloni",
                    "problem": "Miloddan avvalgi 74-71 yillarda Rimda ko'tarilgan qullar qo'zg'oloni rahbari kim bo'lgan?",
                    "step_by_step": "Kapuya shahridagi gladiatorlar maktabidan qochgan frakiyalik jasur gladiator Spartak ulkan qo'shin to'plab Rim armiyasiga qarshi mardonavor jang qilgan.",
                    "answer": "Gladiator Spartak"
                }
            ],
            "exercise": "'Lakonik nutq' iborasi qayerdan kelib chiqqan va u nimani anglatadi?",
            "exercise_solution": "Qadimgi Spartada (Lakoniya viloyatida) yashovchilar ortiqcha so'zlamasdan, qisqa, aniq va lo'nda gapirishga o'rgatilgan, shu sababli qisqa nutq lakonik nutq deyiladi.",
            "check_questions": [
                {
                    "question": "Ilk Olimpiya o'yinlari qachon o'tkazilgan?",
                    "options": ["Mil.avv. 1000-yilda", "Mil.avv. 776-yilda", "Milodiy 1-yilda", "Mil.avv. 500-yilda"],
                    "correct_index": 1,
                    "explanation": "Tarixda dastlabki Olimpiada miloddan avvalgi 776-yilda Zevs sharafiga o'tkazilgan."
                },
                {
                    "question": "Qadimgi dunyo tarixining yakuni deb qaysi voqea qabul qilingan?",
                    "options": ["Iskandar Zulqarnayn vafoti", "Rim shahrining qurilishi", "G'arbiy Rim imperiyasining qulashi (476-yil)", "Yuliy Sezarning o'ldirilishi"],
                    "correct_index": 2,
                    "explanation": "476-yilda Rimning qulashi bilan quldorlik qadimgi dunyo tugab, o'rta asrlar boshlanadi."
                },
                {
                    "question": "Afinada 'Oltin asr' deb atalgan demokratiyaning eng gullagan davri qaysi arbob nomi bilan bog'liq?",
                    "options": ["Solon", "Perikl", "Drakont", "Aleksandr"],
                    "correct_index": 1,
                    "explanation": "Miloddan avvalgi V asrda Perikl rahbarligida Afina o'zining eng yuksak madaniy va siyosiy cho'qqisiga chiqqan."
                }
            ],
            "tags": ["jahon tarixi", "qadimgi yunoniston", "afina", "sparta", "rim imperiyasi", "olimpiada", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "his-013",
            "slug": "orta-asrlar-feodalizm-va-salib-yurishlari",
            "subject_id": "sub-24",
            "subject_name": "Jahon tarixi",
            "title": "O'rta asrlar Yevropasi: feodalizm tuzumi, ritsarlik va Salib yurishlari",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Feodal narvon (vassallik tizimi), katolik cherkovi qudrati, inkvizitsiya, shaharlar taraqqiyoti va Salib yurishlari sabab va oqibatlarini o'rganish.",
            "theory": "V-XV asrlar insoniyat tarixida O'rta asrlar (feodalizm) davri deyiladi. Feodalizmning asosi — yer egaligi (feod) bo'lib, jamiyat 'Feodal narvoni' tizimida qurilgan: Qirol -> Gersog va Graflar -> Baronlar -> Ritsarlar (ritsar kodeksi: mardlik, sadoqat, xonimga xizmat). Dehqonlar esa feodalga qaram bo'lib, barshina (ishlab berish) va obrok (mahsulot solig'i) to'lagan. O'rta asrlarda Yevropada Rim katolik cherkovi ulkan siyosiy va iqtisodiy kuchga aylangan (Papa hokimiyati, indulgensiya — gunohlarni pulga kechirish yorlig'i, bid'atchilarga qarshi diniy sud — inkvizitsiya). Salib yurishlari (1096-1270) — Rim papasi Urban II chaqirig'i bilan 'Quddusni va Iso qabrini musulmonlardan ozod qilish' shiori ostida Sharqqa qilingan 8 ta yirik bosqinchilik yurishidir. Salibchilar Sharqning boy madaniyati, shakar, paxta, qog'oz va gigiyena odatlari bilan tanishib Yevropaga olib qaytdilar.",
            "examples": [
                {
                    "title": "'Vassalimning vassali mening vassalim emas' qoidasi",
                    "problem": "O'rta asrlar feodal narvonidagi ushbu mashhur qoida nimani anglatgan?",
                    "step_by_step": "Ritsarlar faqat o'zlariga yer bergan bevosita senyorga (baronga) bo'ysungan, oliy hukmdor bo'lgan qirolga esa to'g'ridan-to'g'ri bo'ysunmagan. Bu feodal tarqoqlikning yorqin ifodasi bo'lgan.",
                    "answer": "Faqat o'zining bevosita senyoriga bo'ysunish qoidasi"
                },
                {
                    "title": "Salib yurishlarining oqibati",
                    "problem": "Salibchilar Sharqda o'z maqsadiga to'liq erisha oldimi?",
                    "step_by_step": "Yo'q, musulmon sarkardasi Salohiddin Ayyubiy 1187-yilda Quddusni ozod qildi va oxir-oqibat salibchilar Sharqdan butunlay quvib chiqarildi.",
                    "answer": "Salibchilar mag'lub bo'lib Sharqdan quvilgan"
                }
            ],
            "exercise": "O'rta asrlar Yevropa shaharlarida hunarmandlarning kasbiy birlashmasi nima deb atalgan?",
            "exercise_solution": "Sexlar (tsex) deb atalgan bo'lib, ular mahsulot sifati, narxi va xomashyo taqsimotini qat'iy nazorat qilgan.",
            "check_questions": [
                {
                    "question": "Feodalizm davrida harbiy xizmati evaziga yer olgan zodagon jangchi nima deyilgan?",
                    "options": ["Vandal", "Ritsar", "Gladiator", "Samuray"],
                    "correct_index": 1,
                    "explanation": "Ritsarlar o'rta asrlarda otliq og'ir qurollangan zodagon jangchilar qatlami bo'lgan."
                },
                {
                    "question": "Katolik cherkovi tomonidan sotilgan gunohlarni kechirish yorlig'i nima deb ataladi?",
                    "options": ["Inkvizitsiya", "Indulgensiya", "Anatema", "Bullar"],
                    "correct_index": 1,
                    "explanation": "Indulgensiya sotish cherkov boyishining asosiy vositalaridan biriga aylangan."
                },
                {
                    "question": "1187-yilda Quddusni salibchilardan ozod qilgan mashhur Sharq sarkardasi kim?",
                    "options": ["Baybars", "Salohiddin Ayyubiy", "Alp Arslon", "Nuriddin Mahmud"],
                    "correct_index": 1,
                    "explanation": "Sulton Salohiddin (Saladin) Hattin jangida salibchilarni yengib Quddusni qaytarib olgan."
                }
            ],
            "tags": ["jahon tarixi", "o'rta asrlar", "feodalizm", "ritsarlar", "salib yurishlari", "salohiddin", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "his-014",
            "slug": "buyuk-geografik-kashfiyotlar-va-uygonish-davri",
            "subject_id": "sub-24",
            "subject_name": "Jahon tarixi",
            "title": "Uyg'onish davri (Renessans) va Buyuk geografik kashfiyotlar",
            "grade_level": "7-8-sinf",
            "difficulty": "O'rta",
            "objective": "Gumanizm g'oyalari, Leonardo da Vinchi, Mikelanjelo, Xristofor Kolumb, Vasko da Gama va Magellan sayohatlarining dunyo xaritasini o'zgartirishi.",
            "theory": "XIV-XVI asrlarda Yevropada (Italiyadan boshlab) Uyg'onish davri (Renessans) yuz berdi. Asosiy g'oyasi — Gumanizm (insonparvarlik — insonni olamning markazi deb bilish). Buyuk vakillari: Leonardo da Vinchi ('Mona Liza', 'So'nggi kechlik', buyuk ixtirolar), Mikelanjelo ('Dovud' haykali, Sikstin kapellasi freskalari), Rafael Santi ('Sikstin madonnasi'), Vilyam Shekspir. Buyuk geografik kashfiyotlar (XV asr oxiri - XVI asr): Yevropaliklar Hindistonga yangi dengiz yo'lini qidirishga tushdilar (Usmonlilar quruqlikdagi Ipak yo'lini to'sib qo'ygandi): 1) 1492-yil — Xristofor Kolumb Atlantika okeani orqali g'arbga suzib, yangi qit'a — Amerikani kashf etdi (o'zi buni Hindiston deb o'ylagan, Amerigo Vespuchchi yangi qit'a ekanini isbotlagan); 2) 1498-yil — Vasko da Gama Afrikani aylanib o'tib, Hindistonga dengiz yo'lini ochdi; 3) 1519-1522 yillar — Fernand Magellan ekspeditsiyasi ilk bor dunyo bo'ylab sayohat qilib, Yerning sharsimonligini amalda isbotladi.",
            "examples": [
                {
                    "title": "Magellan sayohatining ahamiyati",
                    "problem": "Fernand Magellan boshchiligidagi ekspeditsiya qanday ikkita fundamental geografik kashfiyot qildi?",
                    "step_by_step": "1) Dunyo okeani yagona va o'zaro tutash ekanligini isbotladi;\n2) Yer sharini aylanib chiqib, uning sharsimon shaklda ekanligini amalda to'liq isbotladi.",
                    "answer": "Yerning sharsimonligi va Dunyo okeanining yaxlitligi isbotlandi"
                },
                {
                    "title": "Leonardo da Vinchi universal dahosi",
                    "problem": "Nima sababdan Leonardo da Vinchi 'Homo Universalis' (Universal inson) deb ataladi?",
                    "step_by_step": "Chunki u bir vaqtning o'zida buyuk rassom, haykaltarosh, me'mor, anatom, muhandis, matematik va aviatsiya (vertolyot, parashyut) asoschisi bo'lgan.",
                    "answer": "Ilm-fan va san'atning barcha sohalarida daho bo'lgani uchun"
                }
            ],
            "exercise": "Yevropaga Amerikadan keltirilgan 4 ta muhim qishloq xo'jaligi o'simligini sanang.",
            "exercise_solution": "Kartoshka, pomidor, makkajo'xori (makkajo'xori), tamaki, kungaboqar va kakao.",
            "check_questions": [
                {
                    "question": "1492-yilda Amerika qit'asini kashf etgan dengizchi kim?",
                    "options": ["Vasko da Gama", "Xristofor Kolumb", "Fernand Magellan", "Jeyms Kuk"],
                    "correct_index": 1,
                    "explanation": "Ispaniya bayrog'i ostida suzgan Xristofor Kolumb 1492-yilda Amerikani kashf etgan."
                },
                {
                    "question": "Yer sharini ilk bor aylanib chiqqan dengiz sayohatiga kim rahbarlik qilgan?",
                    "options": ["Kolumb", "Amerigo Vespuchchi", "Fernand Magellan", "Frensis Dreyk"],
                    "correct_index": 2,
                    "explanation": "Magellan 1519-1522 yillarda tarixda birinchi bor yer sharini aylanib chiqqan."
                },
                {
                    "question": "Mashhur 'Mona Liza' (Jokonda) asarini qaysi buyuk musavvir chizgan?",
                    "options": ["Rafael Santi", "Mikelanjelo", "Leonardo da Vinchi", "Rembrandt"],
                    "correct_index": 2,
                    "explanation": "'Mona Liza' Uyg'onish davrining buyuk dahosi Leonardo da Vinchi qalamiga mansub."
                }
            ],
            "tags": ["jahon tarixi", "renessans", "kolumb", "magellan", "leonardo da vinchi", "geografik kashfiyotlar", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "his-015",
            "slug": "sanoat-tontarilishi-va-fransuz-inqilobi",
            "subject_id": "sub-24",
            "subject_name": "Jahon tarixi",
            "title": "Yangi davr: Angliyadagi sanoat to'ntarilishi va Buyuk Fransuz inqilobi",
            "grade_level": "8-sinf",
            "difficulty": "Murakkab",
            "objective": "Bug' dvigateli (Jeyms Vatt), fabrika ishlab chiqarishiga o'tish, 1789-yilgi Fransuz inqilobi, Bastiliyaning olinishi va Inson huquqlari deklaratsiyasini tahlil qilish.",
            "theory": "XVIII asrning ikkinchi yarmida Angliyada sanoat to'ntarilishi boshlandi — qo'l mehnatiga asoslangan manufakturadan mashinalar yordamida ishlaydigan yirik fabrika-zavod tizimiga o'tildi. Asosiy ixtirolar: Jeyms Xargrivsning 'Jenni' mexanik yigiruv mashinasi, Jeyms Vattning universal bug' dvigateli (1784), Jorj Stefensonning parovozi (temiryo'llar davri) va Robert Fultonning paroxodi. Buyuk Fransuz burjua inqilobi (1789-1799): sabablari — qirol absolyutizmi, feodal qoloqlik va uchinchi tabaqa (xalq va burjuaziya)ning huquqsizligi. 1789-yil 14-iyulda qo'zg'olonchilar qirol qamoqxonasi — Bastiliya qal'asini shturm bilan oldi (Fransiya milliy bayrami). 1789-yil 26-avgustda 'Inson va fuqaro huquqlari deklaratsiyasi' qabul qilindi ('Barcha insonlar erkin va teng huquqli bo'lib tug'iladilar'). Shiori: 'Erkinlik, Tenglik, Birodarlik' (Liberté, Égalité, Fraternité).",
            "examples": [
                {
                    "title": "Bug' dvigatelining inqilobiy ta'siri",
                    "problem": "Nima sababdan Jeyms Vattning bug' mashinasi sanoat to'ntarilishining yuragi hisoblanadi?",
                    "step_by_step": "Ilgari fabrikalar faqat suv tegirmoni bor daryo bo'ylarida qurilgan. Bug' mashinasi esa zavodlarni istalgan joyda, qazib olinadigan ko'mir hisobiga kecha-yu kunduz uzluksiz quvvat bilan ishlashini ta'minladi.",
                    "answer": "Korxonalarni daryolarga bog'liqlikdan xalos etib, qudratli universal kuch bergani uchun"
                },
                {
                    "title": "Bastiliyaning qulashi ramzi",
                    "problem": "Bastiliya qal'asining olinishi nima uchun inqilobning g'alabasi deb baholandi?",
                    "step_by_step": "Bastiliya qirollik mustabid tuzumi va istibdodining eng qudratli ramzi edi. Uning qulashi mutlaq monarxiya ustidan xalq irodasining g'alabasini anglatdi.",
                    "answer": "Qirol mutlaq zulmining qulash ramzi bo'lgani uchun"
                }
            ],
            "exercise": "'Inson va fuqaro huquqlari deklaratsiyasi'ning 1-moddasida qanday buyuk tamoyil e'lon qilingan?",
            "exercise_solution": "'Insonlar erkin va teng huquqli bo'lib tug'iladilar va yashaydilar. Ijtimoiy farqlar faqat umumiy manfaatga asoslanishi mumkin'.",
            "check_questions": [
                {
                    "question": "Sanoat to'ntarilishi ilk bor qaysi davlatda boshlangan?",
                    "options": ["Fransiyada", "Angliyada (Buyuk Britaniya)", "Germaniyada", "AQShda"],
                    "correct_index": 1,
                    "explanation": "XVIII asr o'rtalarida sanoat to'ntarilishi birinchi bo'lib Angliyada sodir bo'ldi."
                },
                {
                    "question": "Universal bug' dvigatelini yaratgan ingliz ixtirochisi kim?",
                    "options": ["Tomas Edison", "Jeyms Vatt", "Isaak Nyuton", "Maykl Faradey"],
                    "correct_index": 1,
                    "explanation": "Jeyms Vatt 1784-yilda patentlangan bug' dvigatelini yaratdi."
                },
                {
                    "question": "Buyuk Fransuz inqilobining boshlanish kuni qaysi voqea bilan belgilanadi?",
                    "options": ["1789-yil 14-iyulda Bastiliya qal'asining olinishi", "Napoleonning hokimiyatga kelishi", "Qirol Lyudovik XVI ning qatl etilishi", "Vaterloo jangi"],
                    "correct_index": 0,
                    "explanation": "1789-yil 14-iyul kuni xalq Bastiliyani ishg'ol qildi va bu Fransiyada inqilob ramziga aylandi."
                }
            ],
            "tags": ["jahon tarixi", "sanoat to'ntarilishi", "jeyms vatt", "fransuz inqilobi", "bastiliya", "deklaratsiya", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "his-016",
            "slug": "birinchi-va-ikkinchi-jahon-urushlari-bmt",
            "subject_id": "sub-24",
            "subject_name": "Jahon tarixi",
            "title": "XX asr fojialari: Birinchi va Ikkinchi jahon urushlari, fashizmning tor-mor etilishi va BMT",
            "grade_level": "9-11-sinf",
            "difficulty": "Murakkab",
            "objective": "Jahon urushlari sabablari, fashizm va natsizm mafkurasi, antifashistik koalitsiya g'alabasi, atom fojiasi (Xirosima) va Birlashgan Millatlar Tashkilotining tashkil topishi.",
            "theory": "XX asr insoniyat tarixidagi eng qonli urushlar davri bo'ldi: 1) Birinchi jahon urushi (1914-1918) — Antanta (Angliya, Fransiya, Rossiya) va Uchlar ittifoqi (Germaniya, Avstriya-Vengriya, Usmonli imperiyasi) o'rtasida dunyoni qayta taqsimlash uchun kechdi (20 million qurbon); 2) Ikkinchi jahon urushi (1939-1945) — insoniyat tarixidagi eng dahshatli qirg'in (70 milliondan ortiq qurbon). Fashistik Germaniya (Gitler), fashistik Italiya va militaristik Yaponiya dunyoni egallash va irqiy genotsid (Xolokost — 6 million yahudiyning qirilishi) rejasini tuzdi. 1941-yilda Gitler SSSRga bostirib kirdi. Antifashistik koalitsiya (SSSR, AQSh, Buyuk Britaniya) shakllandi. Burilish janglari: Moskva (1941), Stalingrad (1942-1943), Kursk (1943). 1944-yil 6-iyunda Normandiyada ikkinchi front ochildi. 1945-yil may oyida Berlin egallandi va fashistlar Germaniyasi so'zsiz taslim bo'ldi. 1945-yil 6 va 9-avgustda AQSh Yaponiyaning Xirosima va Nagasaki shaharlariga atom bombasi tashladi. 1945-yil 24-oktyabrda jahonda tinchlik va xavfsizlikni saqlash maqsadida Birlashgan Millatlar Tashkiloti (BMT) tuzildi.",
            "examples": [
                {
                    "title": "O'zbekiston xalqining g'alabaga qo'shgan hissasi",
                    "problem": "Ikkinchi jahon urushida O'zbekiston xalqi qanday fidoyilik ko'rsatdi?",
                    "step_by_step": "O'zbekistondan 1.5 milliondan ortiq inson frontga ketdi, 500 mingdan ortig'i halok bo'ldi. Yuzlab harbiy korxonalar ko'chirib keltirilib, qurol-yarog' ishlab chiqarildi. Toshkentga evakuatsiya qilingan 1.5 million kishi, jumladan 200 ming yetim bola qabul qilinib, oilalarga joylashtirildi (Shomahmudovlar oilasi jasorati).",
                    "answer": "Frontda 500 ming qurbon, 1.5 million evakuatsiya qilinganlarga boshpana va qurol-yarog' ta'minoti"
                },
                {
                    "title": "BMT tashkil topishi",
                    "problem": "BMT Nizomi qachon va qayerda qabul qilindi va tashkilotning bosh maqsadi nima?",
                    "step_by_step": "1945-yil 26-iyunda San-Fransisko konferensiyasida 50 ta davlat tomonidan imzolandi va 1945-yil 24-oktyabrda kuchga kirdi. Maqsadi: kelgusi avlodlarni urush balosidan qutqarish va xalqaro hamkorlikni ta'minlash.",
                    "answer": "1945-yil 24-oktyabr; dunyoda tinchlikni saqlash va urushlarning oldini olish"
                }
            ],
            "exercise": "Nurnberg xalqaro harbiy tribunali (1945-1946) qanday tarixiy saboq berdi?",
            "exercise_solution": "Tarixda ilk bor urush boshlagan tajovuzkorlar, insoniyatga qarshi jinoyat qilgan fashist rahbarlari xalqaro sud qilinib, qilmishlariga yarasha adolatli jazolandi.",
            "check_questions": [
                {
                    "question": "Ikkinchi jahon urushi qachon boshlangan va qachon yakunlangan?",
                    "options": ["1914-1918", "1939-yil 1-sentyabr — 1945-yil 2-sentyabr", "1941-1945", "1938-1946"],
                    "correct_index": 1,
                    "explanation": "Urush 1939-yil 1-sentyabrda Germaniyaning Polshaga hujumi bilan boshlanib, 1945-yil 2-sentyabrda Yaponiyaning taslim bo'lishi bilan tugadi."
                },
                {
                    "question": "Birlashgan Millatlar Tashkiloti (BMT) qaysi yili tashkil topgan?",
                    "options": ["1919-yil", "1945-yil", "1950-yil", "1991-yil"],
                    "correct_index": 1,
                    "explanation": "BMT 1945-yil 24-oktyabrda urushdan so'ng tinchlikni saqlash maqsadida tuzildi."
                },
                {
                    "question": "1945-yil avgustida dunyoda birinchi bo'lib atom bombasi tashlangan shahar qaysi?",
                    "options": ["Tokio", "Xirosima", "Nagasaki", "Berlin"],
                    "correct_index": 1,
                    "explanation": "6-avgustda Xirosimaga, 9-avgustda Nagasakiga atom quroli qo'llanilgan."
                }
            ],
            "tags": ["jahon tarixi", "ikkinchi jahon urushi", "bmt", "xirosima", "fashizm", "nurnberg", "11-sinf"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_history_materials()
    print(f"Generated {len(mats)} History materials.")
