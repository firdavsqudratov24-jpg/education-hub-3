# -*- coding: utf-8 -*-
"""
Builder for San’at, Texnologiya va boshqa amaliy fanlar (12 materials: art-001 to art-012)
- sub-31: Texnologiya (2: art-001 to art-002)
- sub-32: Tasviriy san’at (2: art-003 to art-004)
- sub-33: Musiqa madaniyati (2: art-005 to art-006)
- sub-34: Jismoniy tarbiya (2: art-007 to art-008)
- sub-35: Chizmachilik (2: art-009 to art-010)
- sub-36: Hayot xavfsizligi (2: art-011 to art-012)
"""

def get_practical_arts_materials():
    materials = [
        # TEXNOLOGIYA (2)
        {
            "id": "art-001",
            "slug": "yogochga-ishlov-berish-va-duradgorlik-asboblari",
            "subject_id": "sub-31",
            "subject_name": "Texnologiya",
            "title": "Texnologiya: Yog'ochga ishlov berish, duradgorlik asboblari va xavfsizlik texnikasi",
            "grade_level": "5-6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Yog'och turlari, uning xossalari, asosiy duradgorlik asboblari (arra, randa, iskana, parma) bilan ishlash va texnika xavfsizligi qoidalarini o'rganish.",
            "theory": "Texnologiya fani materiallarga qo'l va mexanik asboblar yordamida ishlov berish orqali xalq iste'moli buyumlarini tayyorlash san'atini o'rgatadi. Yog'och — qadimiy, ekologik toza va qayta ishlanuvchi tabiiy xomashyo. Yog'och turlari: qattiq (chinor, yong'oq, eman) va yumshoq (terak, tol, qarag'ay). Duradgorlik asboblari: 1) O'lchash va belgilash — metall chizg'ich, burchaklik, reysmus; 2) Qirqish — arra (qo'l arra, loba); 3) Randallash — randa (sherxebel — dag'al yo'nish uchun, fuganok — tekis silliqlash uchun); 4) O'yish va teshish — iskana (stameska), parma (drel). Xavfsizlik qoidalari: asboblarni soz holda ushlash, tig'li asboblar bilan ishlaganda qo'l harakatini tig' yo'nalishidan uzoq tutish, ko'zni himoyalovchi ko'zoynak taqish va ish joyini tartibli saqlash shart.",
            "examples": [
                {
                    "title": "Yog'och bo'lagini to'g'ri arralash",
                    "problem": "Yog'och taxtani belgilangan chiziq bo'yicha to'g'ri va xavfsiz arralash tartibi qanday?",
                    "step_by_step": "1) Taxta dastgohga (vertak) qisqich bilan mahkam o'rnatiladi;\n2) Arra boshlang'ich chiziqqa 45° burchak ostida qo'yiladi va chap qo'l bosh barmog'i bilan yo'nalish olinadi;\n3) Dastlabki iz hosil bo'lgach, qo'l chetga olinadi va bir maromda, ortiqcha bosimsiz arralanadi.",
                    "answer": "Mahkam qisish -> 45 gradus burchakda iz ochish -> bir maromda arralash"
                },
                {
                    "title": "Randalash yo'nalishi",
                    "problem": "Yog'och qaysi yo'nalishda randalanadi: tolalari bo'ylabmi yoki tolalarga qarshimi?",
                    "step_by_step": "Yog'och har doim tolalari yo'nalishi bo'ylab randalanadi. Agar tolalarga qarshi randalansa, sirt qiriladi, tolalar yulinadi va silliq bo'lmaydi.",
                    "answer": "Tolalari yo'nalishi bo'ylab randalanadi"
                }
            ],
            "exercise": "Yog'och buyum tayyorlangach, uni chirishdan saqlash va chiroyli qilish uchun qanday pardozlash ishlari bajariladi?",
            "exercise_solution": "Sirt jilvir qog'oz (qumqog'oz) bilan silliqlanadi, dog' tushiriladi (morilka) va ustidan himoya loki (lak) yoki tabiiy zig'ir moyi surtiladi.",
            "check_questions": [
                {
                    "question": "Yog'och sirtini dastlabki dag'al yo'nish uchun qaysi asbob ishlatiladi?",
                    "options": ["Fuganok", "Sherxebel", "Iskana", "Loba"],
                    "correct_index": 1,
                    "explanation": "Sherxebel yarim doira shaklidagi pichog'i bilan qalin qatlamni tezda yo'nib olishga xizmat qiladi."
                },
                {
                    "question": "Duradgorlik dastgohi nima deb ataladi?",
                    "options": ["Kovobur", "Vertak (stanok)", "Molybert", "Molbert"],
                    "correct_index": 1,
                    "explanation": "Vertak — yog'ochga ishlov berish uchun maxsus qisqichlari bo'lgan duradgorlik stolidir."
                },
                {
                    "question": "Quyidagi daraxtlardan qaysi birining yog'ochi qattiq va mustahkam hisoblanadi?",
                    "options": ["Terak", "Yong'oq (Grek yong'og'i)", "Tol", "Jo'ka"],
                    "correct_index": 1,
                    "explanation": "Yong'oq daraxti qattiq, mustahkam va qimmatbaho mebelbop yog'och beradi."
                }
            ],
            "tags": ["texnologiya", "duradgorlik", "yog'och", "arra", "randa", "xavfsizlik", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "art-002",
            "slug": "robototexnika-va-avtomatika-elementlari",
            "subject_id": "sub-31",
            "subject_name": "Texnologiya",
            "title": "Zamonaviy texnologiya: Robototexnika, datchiklar va Arduino platformasi",
            "grade_level": "7-9-sinf",
            "difficulty": "O'rta",
            "objective": "Robot tushunchasi, mikrokontrollerlar (Arduino), datchiklar (sensorlar: ultratovush, harorat, yorug'lik) va ijrochi mexanizmlarni (servomotor) boshqarish.",
            "theory": "Robototexnika — robotlarni loyihalash, yasash va dasturlash bilan shug'ullanuvchi amaliy fan va texnologiya sohasidir. Har qanday robot 3 ta asosiy qismdan iborat: 1) Sensorlar (datchiklar / sezish a'zolari) — tashqi muhitdan ma'lumot oladi (ultratovushli datchik — masofani o'lchaydi; fotorezistor — yorug'likni sezadi; PIR datchik — harakatni aniqlaydi); 2) Boshqaruvchi miya (mikrokontroller — Arduino, ESP32, Raspberry Pi) — datchiklardan kelgan signalni qayta ishlaydi va dastur bo'yicha qaror qabul qiladi; 3) Ijrochi mexanizmlar (Aktuatorlar) — harakatni bajaradi (o'zgarmas tok motorlari, servomotorlar, g'ildiraklar, manipulyator qo'llar). Arduino — elektron qurilmalar va robotlarni tez yig'ish uchun ochiq mikrokontroller platformasi bo'lib, C++ ga asoslangan sodda tilda dasturlanadi (setup() va loop() funksiyalari).",
            "examples": [
                {
                    "title": "To'siqlarni aylanib o'tuvchi robot mantiqi",
                    "problem": "Robot oldidagi to'siqni ko'rib to'xtashi uchun qanday datchik va qanday dasturiy shart qo'yiladi?",
                    "step_by_step": "1) Ultratovushli masofa datchigi (HC-SR04) o'rnatiladi;\n2) Shart: if (distance < 15) { stop(); turnRight(); } else { moveForward(); };\n3) Masofa 15 sm dan kam bo'lsa robot to'xtab o'ngga buriladi, aks holda to'g'riga harakatlanadi.",
                    "answer": "Ultratovush datchigi va if (distance < 15) sharti"
                },
                {
                    "title": "Arduino dastur tuzilishi",
                    "problem": "Arduino dasturidagi void setup() va void loop() funksiyalarining farqi nimada?",
                    "step_by_step": "void setup() — mikrokontroller yoqilganda faqat 1 marta bajariladi (pinlarni sozlash); void loop() — mikrokontroller o'chirilguncha cheksiz takrorlanib ishlayveradi.",
                    "answer": "setup() 1 marta, loop() esa cheksiz takrorlanadi"
                }
            ],
            "exercise": "Aqlli uy tizimida qorong'i tushganda chiroqni avtomatik yoqish uchun qaysi datchik ishlatiladi?",
            "exercise_solution": "Fotorezistor (LDR — Light Dependent Resistor) yorug'lik tushganda qarshiligini o'zgartiradi va qorong'ilikni aniqlaydi.",
            "check_questions": [
                {
                    "question": "Robototexnikada masofani o'lchash uchun ko'rshapalaklar tamoyilida ishlovchi qaysi datchik ishlatiladi?",
                    "options": ["Harorat datchigi", "Ultratovushli datchik (Ultrasonic)", "Barometr", "Potensiometr"],
                    "correct_index": 1,
                    "explanation": "Ultratovush to'lqini to'siqdan qaytish vaqtiga qarab masofani aniq o'lchaydi."
                },
                {
                    "question": "Robotning g'ildiraklari yoki qo'lini aniq burchakka (masalan 90 gradusga) burish uchun qanday motor ishlatiladi?",
                    "options": ["Oddiy motor", "Servomotor (Servo)", "Dizel motor", "Turbina"],
                    "correct_index": 1,
                    "explanation": "Servomotorlar o'qni belgilangan aniq burchakka (0-180°) burish va ushlab turish imkonini beradi."
                },
                {
                    "question": "Arduino platasining bosh boshqaruvchi mikrosxemasi nima deb ataladi?",
                    "options": ["Tranzistor", "Mikrokontroller", "Kondensator", "Rele"],
                    "correct_index": 1,
                    "explanation": "Arduino da ATmega mikrokontrolleri barcha dasturlarni xotirasida saqlab boshqaradi."
                }
            ],
            "tags": ["texnologiya", "robototexnika", "arduino", "datchik", "servomotor", "8-sinf"],
            "duration_minutes": 30
        },

        # TASVIRIY SAN’AT (2)
        {
            "id": "art-003",
            "slug": "tasviriy-sanat-rangshunoslik-va-rangtasvir-asoslari",
            "subject_id": "sub-32",
            "subject_name": "Tasviriy san’at",
            "title": "Tasviriy san’at: Rangshunoslik, ranglar doirasi va rangtasvir (Jivopis) asoslari",
            "grade_level": "5-6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Asosiy va qo'shimcha ranglar, issiq va sovuq ranglar gammasi, rangtasvir janrlari (natyurmort, manzara, portret) va yorug'-soya qonuniyatlarini bilish.",
            "theory": "Tasviriy san'at voqelikni badiiy obrazlar, ranglar, chiziqlar va shakllar orqali ko'rgazmali aks ettiruvchi san'at turidir. Turlari: Rangtasvir (bo'yoqlar bilan — akvarel, guash, moybo'yoq), Grafika (qalam, tush, gravyura), Haykaltaroshlik va Amaliy-dekorativ san'at. Rangshunoslik asoslari: 1) Asosiy ranglar (boshqa ranglarni aralashtirib hosil qilib bo'lmaydi) — Qizil, Sariq, Ko'k; 2) Qo'shimcha (hosila) ranglar — asosiy ranglar aralashmasidan hosil bo'ladi (Qizil + Sariq = Zarg'aldoq; Sariq + Ko'k = Yashil; Qizil + Ko'k = Binafsha); 3) Rang harorati: Issiq ranglar (quyosh va olov ranglari — qizil, sariq, olovrang); Sovuq ranglar (suv, muz va osmon ranglari — ko'k, moviy, binafsha, yashil). Yorug'-soya bosqichlari: yorug'lik, yarimsoya, xususiy soya, tushuvchi soya, yaltiroq (blik) va refleks.",
            "examples": [
                {
                    "title": "Hajmli sharni tasvirlashda yorug'-soya",
                    "problem": "Tekis qog'ozda chizilgan doiraga qanday qilib hajmli shar ko'rinishi beriladi?",
                    "step_by_step": "Yorug'lik tushayotgan tomonga blik (eng yorqin nuqta) qo'yiladi, undan keyin yorug'lik, yarimsoya, eng qorong'i xususiy soya, stol sirtidan qaytgan yorug'lik (refleks) va shardan yerga tushgan tushuvchi soya bir tekis shtrixlanadi.",
                    "answer": "Yorug'-soya (blik, yorug', soya, refleks) orqali hajm hosil qilinadi"
                },
                {
                    "title": "Rangtasvir janrlari",
                    "problem": "Natyurmort, Manzara va Portret janrlarining farqini ayting.",
                    "step_by_step": "Natyurmort — jonsiz narsalar (mevalar, idishlar, gullar) tasviri; Manzara (peyzaj) — tabiat va shahar ko'rinishlari; Portret — inson yoki odamlar guruhi qiyofasi tasviri.",
                    "answer": "Natyurmort (buyumlar), Manzara (tabiat), Portret (inson)"
                }
            ],
            "exercise": "Akvarel (suvbo'yoq) bo'yog'ining asosiy texnik xususiyati nima?",
            "exercise_solution": "Akvarel bo'yog'i suvda oson eriydigan, shaffof (yengil) bo'yoq bo'lib, qog'oz oqi hisobiga yorug'lik beriladi va qalin qatlam hosil qilmaydi.",
            "check_questions": [
                {
                    "question": "Tasviriy san'atda 3 ta asosiy rang qaysi?",
                    "options": ["Oq, qora, qizil", "Qizil, sariq, ko'k", "Yashil, zarg'aldoq, binafsha", "Moviy, pushti, jigarrang"],
                    "correct_index": 1,
                    "explanation": "Qizil, sariq va ko'k — boshqa ranglarni qo'shib hosil qilib bo'lmaydigan birlamchi ranglardir."
                },
                {
                    "question": "Quyidagilardan qaysi biri sovuq ranglar guruhiga kiradi?",
                    "options": ["Olovrang", "Ko'k va moviy", "Sariq", "Qizil"],
                    "correct_index": 1,
                    "explanation": "Ko'k, moviy va binafsha sovuq ranglar hisoblanadi."
                },
                {
                    "question": "Buyumlar, mevalar va gullar kompozitsiyasi tasvirlangan janr nima deyiladi?",
                    "options": ["Portret", "Natyurmort", "Manzara", "Marina"],
                    "correct_index": 1,
                    "explanation": "Natyurmort (fransuzcha 'o'lik tabiat') jonsiz narsalar tasvirlangan janrdir."
                }
            ],
            "tags": ["tasviriy san'at", "rangshunoslik", "natyurmort", "akvarel", "yorug'-soya", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "art-004",
            "slug": "kompozitsiya-va-sharq-miniatyura-sanati",
            "subject_id": "sub-32",
            "subject_name": "Tasviriy san’at",
            "title": "Kompozitsiya qonuniyatlari, chiziqli perspektiva va Kamoliddin Behzod miniatyurasi",
            "grade_level": "7-8-sinf",
            "difficulty": "O'rta",
            "objective": "Kompozitsiya markazi, chiziqli va havo perspektivasi, qisqarish nuqtasi hamda Kamoliddin Behzod boshchiligidagi Hirot miniatyura maktabini o'rganish.",
            "theory": "Kompozitsiya — asar g'oyasini ifodalash uchun barcha tasviriy elementlarni (shakl, rang, hajm, masofa) yagona bir butunlikka uyg'unlashtirish san'atidir. Kompozitsiya markazi tomoshabin nigohini eng birinchi o'ziga tortadigan bosh qismdir. Chiziqli perspektiva: ufq chizig'iga (gorizont) yaqinlashgan sari narsalar kichrayib boradi va parallel to'g'ri chiziqlar bitta 'Yo'qolish nuqtasi'da (ufqda) kesishadi. Havo perspektivasi: uzoqdagi narsalar xiralashadi, kontrastini yo'qotadi va moviy-ko'kimtir tus oladi. Sharq miniatyura san'ati: O'rta asrlar sharq kitob illyustratsiyasi san'ati bo'lib, nur-soyasiz, yorqin lok-bo'yoqlar va nozik chiziqlar bilan yassi-dekorativ uslubda chizilgan. 'Sharq Rafaeli' deb tan olingan Kamoliddin Behzod (1455-1535) Hirot miniatyura maktabining dahosi bo'lib, Navoiy, Dehlaviy, Nizomiy asarlariga betakror miniatyuralar chizgan.",
            "examples": [
                {
                    "title": "Perspektiva qonuni amalda",
                    "problem": "Uzoqlashib borayotgan temiryo'l relslari yoki daraxtlar qatorda qanday chiziladi?",
                    "step_by_step": "Oldingi plandagi daraxtlar va relslar katta, aniq va yorqin rangda chiziladi. Ufq chizig'iga yaqinlashgan sari daraxtlar kichrayadi, relslar esa bitta nuqtaga birlashadi (chiziqli perspektiva).",
                    "answer": "Ufq chizig'iga qarab kichrayadi va bir nuqtada birlashadi"
                },
                {
                    "title": "Kamoliddin Behzod mahorati",
                    "problem": "Behzod miniatyuralarining o'z davri rassomlaridan asosiy ustunligi nimada edi?",
                    "step_by_step": "Behzod qahramonlarning yuz ifodasi, ichki ruhiy kechinmalari, harakatlari dinamikasi va tabiat manzarasini nihoyatda jonli, tabiiy va mayda detallarigacha nozik aks ettira olgan.",
                    "answer": "Inson ruhiyati va harakatlarini jonli, nozik tasvirlay olganligi"
                }
            ],
            "exercise": "Ufq chizig'i (gorizont) deganda tasviriy san'atda nima tushuniladi?",
            "exercise_solution": "Rassom ko'zi balandligi sathida joylashgan, osmon bilan yerni shartli ravishda ajratib turuvchi ko'rinmas gorizontal chiziq.",
            "check_questions": [
                {
                    "question": "'Sharq Rafaeli' deya ulug'langan buyuk o'zbek miniatyurachi musavviri kim?",
                    "options": ["Mahmud Muzahhib", "Kamoliddin Behzod", "Murod Samarqandiy", "Rizo Abbosiy"],
                    "correct_index": 1,
                    "explanation": "Kamoliddin Behzod o'zining tengsiz miniatyuralari bilan butun dunyoga tanilgan."
                },
                {
                    "question": "Uzoqdagi tog'larning ko'kimtir, xira bo'lib ko'rinishi qaysi perspektiva qonuniyatidir?",
                    "options": ["Chiziqli perspektiva", "Havo perspektivasi", "Teskari perspektiva", "Sferik perspektiva"],
                    "correct_index": 1,
                    "explanation": "Havo qatlami va chang zarralari yorug'likni sochib, uzoqdagi jismlarga moviy tus berishi havo perspektivasidir."
                },
                {
                    "question": "Miniatyura asarlarining xarakterli xususiyati qaysi?",
                    "options": ["Katta devoriy surat bo'lishi", "Kitob sahifasidagi o'ta nozik, yorqin detallarga boy jajji tasvir bo'lishi", "Faqat qora-oq chizilishi", "Moybo'yoqda chizilishi"],
                    "correct_index": 1,
                    "explanation": "Miniatyura kitob qo'lyozmalarini bezatuvchi nozik va nafis jajji san'at asaridir."
                }
            ],
            "tags": ["tasviriy san'at", "kompozitsiya", "perspektiva", "behzod", "miniatyura", "hirot", "7-sinf"],
            "duration_minutes": 30
        },

        # MUSIQA MADANIYATI (2)
        {
            "id": "art-005",
            "slug": "musiqiy-savod-nota-yozuvi-va-musiqa-elementlari",
            "subject_id": "sub-33",
            "subject_name": "Musiqa madaniyati",
            "title": "Musiqiy savodxonlik: Nota yozuvi, kalitlar, o'lchovlar va musiqa ifoda vositalari",
            "grade_level": "5-6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Nota yo'li (noto'no'st), Skripka kaliti, 7 ta asosiy nota, cho'zimlar (butun, yarim, chorak, sakkiztalik), o'lchov (takt) va templarni bilish.",
            "theory": "Musiqa — inson his-tuyg'ulari, orzu-umidlari va fikrlarini tovushlar orqali ifodalovchi san'at turidir. Musiqa ifoda vositalari: Melodiya (kuy), Ritm (zarb/o'lchov), Temp (tezlik), Dinamika (kuchlilik: forte — baland, piano — sekin), Tembr (ovoz bo'yog'i). Musiqiy savod: Notalar 5 ta parallel chiziqdan iborat 'Nota yo'li' (notonosets) ustida, chiziqlar orasida va yordamchi chiziqlarda yoziladi. Skripka kaliti (Sol kaliti) 2-chiziqdan boshlanib, sol notasining o'rnini belgilaydi. 7 ta asosiy nota: Do, Re, Mi, Fa, Sol, Lya, Si. Notalar cho'zimi (davomiyligi): Butun nota (4 hissa sanaladi: 1-va, 2-va, 3-va, 4-va); Yarimta nota (2 hissa); Choraktalik nota (1 hissa); Sakkiztalik nota (yarim hissa). Musiqiy o'lchovlar: 2/4, 3/4 (vals o'lchovi), 4/4.",
            "examples": [
                {
                    "title": "Notalar cho'zimini hisoblash",
                    "problem": "Bitta butun notaning ichida nechta choraktalik nota bor?",
                    "step_by_step": "1 ta butun nota = 2 ta yarimta nota = 4 ta choraktalik nota (har biri 1 hissadan, jami 4 hissa).",
                    "answer": "4 ta choraktalik nota"
                },
                {
                    "title": "Musiqiy dinamika belgilari",
                    "problem": "Notada 'f' va 'p' harflari nimani anglatadi?",
                    "step_by_step": "'f' — forte (baland, jarangdor ovoz bilan ijro etish); 'p' — piano (sekin, mayin ovoz bilan ijro etish).",
                    "answer": "f — forte (baland), p — piano (sekin)"
                }
            ],
            "exercise": "3/4 musiqiy o'lchovida har bir taktda nechta choraktalik nota bo'ladi va bu o'lchov qaysi mashhur raqsga xos?",
            "exercise_solution": "Har bir taktda 3 ta choraktalik nota bo'ladi va bu o'lchov mashhur Vals raqsiga xosdir.",
            "check_questions": [
                {
                    "question": "Skripka kaliti ikkinchi chiziqda qaysi notaning o'rnini belgilaydi?",
                    "options": ["Do", "Mi", "Sol", "Lya"],
                    "correct_index": 2,
                    "explanation": "Skripka kaliti Sol kaliti deb ham ataladi, chunki u 2-chiziqdagi Sol notasidan boshlanadi."
                },
                {
                    "question": "4 hissa (1-va, 2-va, 3-va, 4-va) davom etadigan eng uzun asosiy nota qaysi?",
                    "options": ["Chorak nota", "Yarim nota", "Butun nota", "O'n oltitalik nota"],
                    "correct_index": 2,
                    "explanation": "Butun nota ichi bo'sh doira bo'lib, 4 taktli to'liq hissani egallaydi."
                },
                {
                    "question": "Kuyning ijro tezligi musiqada nima deb ataladi?",
                    "options": ["Dinamika", "Temp", "Ritm", "Lad"],
                    "correct_index": 1,
                    "explanation": "Temp (allegro — tez, andante — xotirjam, adajio — sekin) musiqaning ijro tezligidir."
                }
            ],
            "tags": ["musiqa", "nota yozuvi", "sol kaliti", "ritm", "temp", "forte piano", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "art-006",
            "slug": "ozbek-milliy-musiqasi-maqom-va-cholgular",
            "subject_id": "sub-33",
            "subject_name": "Musiqa madaniyati",
            "title": "O'zbek milliy musiqa merosi: Shashmaqom va milliy cholg'u asboblari",
            "grade_level": "7-8-sinf",
            "difficulty": "O'rta",
            "objective": "O'zbek xalq musiqa san'ati, Shashmaqom durdonasi, milliy cholg'u asboblari (torli, puflama, zarbli) guruhlari va YUNESKO nomoddiy madaniy merosini o'rganish.",
            "theory": "O'zbek milliy musiqa merosi ming yillik an'analarga ega. Shashmaqom (forscha 'Olti maqom') — o'zbek va tojik xalqlarining yuksak mumtoz musiqa durdonasi bo'lib, YUNESKO ning 'Insoniyat nomoddiy madaniy merosi' ro'yxatiga kiritilgan. Shashmaqom 6 ta maqomdan iborat: Rost, Navo, Dugoh, Segoh, Iroq va Buzruk. Har bir maqom cholg'u (mushkilot) va aytim (nasr) bo'limlaridan tashkil topgan. Mumtoz she'riyat (Navoiy, Bobur, Fuzuliy, Bedil) g'azallari bilan kuylanadi. O'zbek milliy cholg'ulari: 1) Torli-chertma: Dutor (ipak torli, ikki torli milliy ramz), Tanbur (uch torli, noxun bilan chalinadi), Rubob (qashqar va afg'on rubobi); 2) Torli-kamonli: G'ijjak, Sato; 3) Puflama: Nay (qamish yoki jez nay), Karnay, Surnay, Qo'shnay; 4) Zarbli: Doira (childirma), Nog'ora, Changko'biz.",
            "examples": [
                {
                    "title": "Shashmaqomning olti maqomi",
                    "problem": "Shashmaqom tarkibiga kiruvchi 6 ta maqom nomini ayting.",
                    "step_by_step": "1. Buzruk, 2. Rost, 3. Navo, 4. Dugoh, 5. Segoh, 6. Iroq.",
                    "answer": "Buzruk, Rost, Navo, Dugoh, Segoh, Iroq"
                },
                {
                    "title": "Tanbur va noxun",
                    "problem": "Tanbur cholg'usi qanday usulda chalinadi va u maqom ijrosida nega yetakchi?",
                    "step_by_step": "Tanbur ko'rsatkich barmog'iga kiyiladigan metall noxun yordamida chalinadi. Uning nozik va dardli ovozi maqom pardalarini eng aniq (mikrotonlargacha) ifodalovchi bosh cholg'u hisoblanadi.",
                    "answer": "Barmog'iga noxun kiyib chalinadi, maqomning asosiy cholg'usi"
                }
            ],
            "exercise": "Karnay va surnay cholg'ulari o'zbek xalq turmushida qanday marosimlarda chalinadi?",
            "exercise_solution": "Karnay va surnay tantanavor, jarangdor cholg'ular bo'lib, to'ylar, xalq sayillari (Navro'z) va tantanali milliy bayramlarda xushxabar va shodiyona ramzi sifatida chalinadi.",
            "check_questions": [
                {
                    "question": "'Shashmaqom' so'zi qanday ma'noni anglatadi?",
                    "options": ["Olti pardali kuy", "Olti maqom", "O'n ikki ohang", "Xalq qo'shig'i"],
                    "correct_index": 1,
                    "explanation": "Fors-tojik tilida 'shash' — olti, demak olti maqom demakdir."
                },
                {
                    "question": "O'zbek xalqining eng keng tarqalgan, ikki ipak torli milliy chertma cholg'usi qaysi?",
                    "options": ["Doira", "Dutor", "G'ijjak", "Chang"],
                    "correct_index": 1,
                    "explanation": "Dutor (du — ikki, tor — tor) o'zbek xonadonlarining milliy ramzi hisoblanadi."
                },
                {
                    "question": "Shashmaqom jahonning qaysi nufuzli tashkiloti merosi ro'yxatiga kiritilgan?",
                    "options": ["BMT", "YUNESKO (Insoniyat nomoddiy madaniy merosi)", "UNICEF", "Xalqaro musiqa kengashi"],
                    "correct_index": 1,
                    "explanation": "Shashmaqom 2003-yilda YUNESKO tomonidan insoniyatning jahon durdonasi deb e'tirof etilgan."
                }
            ],
            "tags": ["musiqa", "shashmaqom", "dutor", "tanbur", "nay", "milliy cholg'ular", "7-sinf"],
            "duration_minutes": 30
        },

        # JISMONIY TARBIYA (2)
        {
            "id": "art-007",
            "slug": "soglom-turmush-tarzi-va-yengil-atletika",
            "subject_id": "sub-34",
            "subject_name": "Jismoniy tarbiya",
            "title": "Jismoniy tarbiya: Sog'lom turmush tarzi, ertalabki badantarbiya va yengil atletika",
            "grade_level": "5-7-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Kun tartibi, chiniqish usullari, ertalabki gimnastika hamda yengil atletikaning asosiy turlari (qisqa va uzoq masofaga yugurish, sakrash) qoidalarini o'rganish.",
            "theory": "Sog'lom turmush tarzi (STT) — inson salomatligini mustahkamlash, faol uzoq umr ko'rish va mehnat qobiliyatini oshirishga qaratilgan hayot tarzidir. Asosiy omillari: 1) Muntazam jismoniy faollik; 2) To'g'ri va me'yoriy ovqatlanish; 3) Kun tartibi va sifatli uyqu (kamida 7-8 soat); 4) Zararli odatlardan (chekish, spirtli ichimliklar) xoli bo'lish; 5) Suv, quyosh va havo bilan chiniqish. Ertalabki badantarbiya (gimnastika) uyqudan keyin organizm a'zolari faoliyatini tezroq faollashtiradi va qon aylanishini yaxshilaydi. Yengil atletika — 'Sport malikasi' deb ataladi. U yugurish (qisqa — sprint 60 m, 100 m; o'rta — 800 m, 1500 m; uzoq — stayer va marafon 42 km 195 m), sakrash (uzunlikka, balandlikka) va uloqtirish (nayza, disk, yadro) turlaridan iborat.",
            "examples": [
                {
                    "title": "Qisqa va uzoq masofaga yugurish farqi",
                    "problem": "Sprint (100 m) va marafon (42 km) yugurishida nafas olish va kuchni taqsimlash qanday farq qiladi?",
                    "step_by_step": "Sprintda sportchi maksimal portlovchi tezlik bilan yuguradi (anaerob yuklama, 10-12 sekund); Marafonda esa bir tekis sur'atda kuchni uzoq soatlarga taqsimlash, ritmik nafas olish va yurak-qon tomir chidamliligi (aerob) hal qiluvchi ahamiyatga ega.",
                    "answer": "Sprintda portlovchi maksimal tezlik, marafonda esa uzoq chidamlilik va kuchni tejash"
                },
                {
                    "title": "Marafon masofasi",
                    "problem": "Klassik marafon yugurish masofasi qanchaga teng?",
                    "step_by_step": "Afsonaviy Marafon jangidan Afinagacha yugurib kelgan jangchi xotirasiga bag'ishlangan marafon masofasi 42 kilometr 195 metr (42.195 km) dir.",
                    "answer": "42 km 195 metr"
                }
            ],
            "exercise": "Sport bilan shug'ullanishdan oldin nima sababdan 10-15 daqiqa qizdiruvchi mashqlar (razminka) bajarilishi shart?",
            "exercise_solution": "Mushaklarni isitish, paylar va bo'g'imlar elastikligini oshirish, yurak urishini bosqichma-bosqich tezlashtirish va og'ir jarohatlar (mushak cho'zilishi, uzilishi) oldini olish uchun.",
            "check_questions": [
                {
                    "question": "Qaysi sport turi xalqaro miqyosda 'Sport malikasi' deb ataladi?",
                    "options": ["Suzish", "Futbol", "Yengil atletika", "Gimnastika"],
                    "correct_index": 2,
                    "explanation": "Yengil atletika (yugurish, sakrash, uloqtirish) insonning tabiiy harakatlariga asoslangan sport malikasidir."
                },
                {
                    "question": "Qisqa masofalarga yugurish (60m, 100m, 200m) nima deb ataladi?",
                    "options": ["Marafon", "Sprint", "Stayer", "Kross"],
                    "correct_index": 1,
                    "explanation": "Maksimal tezlikda qisqa masofaga yugurish sprint deyiladi."
                },
                {
                    "question": "Sog'lom inson me'yorda sutkasiga necha soat uxlashi tavsiya etiladi?",
                    "options": ["4-5 soat", "7-8 soat", "10-12 soat", "Farqi yo'q"],
                    "correct_index": 1,
                    "explanation": "Miyaning to'liq tiklanishi va sog'lom bo'lishi uchun 7-8 soatlik sifatli uyqu zarur."
                }
            ],
            "tags": ["jismoniy tarbiya", "sog'lom turmush tarzi", "yengil atletika", "marafon", "sprint", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "art-008",
            "slug": "sport-oyinlari-va-olimpiya-harakati",
            "subject_id": "sub-34",
            "subject_name": "Jismoniy tarbiya",
            "title": "Jamoaviy sport o'yinlari (futbol, basketbol, voleybol) va Olimpiya harakati",
            "grade_level": "8-11-sinf",
            "difficulty": "O'rta",
            "objective": "Futbol, basketbol, voleybol qoidalari, hakamlik, jamoaviy hamjihatlik hamda Zamonaviy Olimpiya o'yinlari va O'zbekiston sportchilari zafarlarini o'rganish.",
            "theory": "Jamoaviy sport o'yinlari jismoniy chidamlilik, tezkorlik, mantiqiy fikrlash va jamoada ishlash ko'nikmasini shakllantiradi. 1) Futbol — har bir jamoada 11 nafar o'yinchi, 45 minutdan 2 taym, to'pni qo'l bilan o'ynash taqiqlanadi (darvozabondan tashqari o'z jarima maydonida); 2) Basketbol (Jeyms Neysmit, 1891) — 5 kishidan iborat 2 jamoa, 3.05 m balandlikdagi savatga to'p tushirish (2 ochko, 3 ochkolik chiziqdan — 3 ochko, jarima to'pi — 1 ochko), to'pni olib yugurish taqiqlanadi (dribling bilan yuriladi); 3) Voleybol (Uilyam Morgan, 1895) — to'r orqali qo'l bilan urib tushirish, jamoada 6 kishi, to'pga eng ko'pi bilan 3 marta teginish mumkin. Olimpiya harakati: Pyer de Kuberten tashabbusi bilan 1896-yilda Afinada zamonaviy Olimpiada tiklandi. Shiori: 'Citius, Altius, Fortius — Communiter' ('Tezroq, Balandroq, Kuchliroq — Birgalikda'). Beshta halqa — besh qit'a birligi ramzi. O'zbekiston mustaqil davlat sifatida dzyudo, boks, erkin kurash, og'ir atletika va taekvondo bo'yicha dunyoning yetakchi sport mamlakatlaridan biridir.",
            "examples": [
                {
                    "title": "Voleybolda 'uch teginish' qoidasi",
                    "problem": "Voleybolda to'p o'z maydoniga tushganda jamoa uni raqib maydoniga o'tkazish uchun qanday kombinatsiya qo'llaydi?",
                    "step_by_step": "1-teginish — qabul qilish (himoyachi/libero to'pni bog'lovchiga uzatadi);\n2-teginish — to'pni hujumga qulay qilib chiqarib berish (pasmeyker);\n3-teginish — hujumkor zarba (raqib maydoniga qattiq urish). To'rtinchi teginish qoidabuzarlik hisoblanadi.",
                    "answer": "Qabul qilish -> Chiqarib berish -> Hujumkor zarba"
                },
                {
                    "title": "O'zbekiston Olimpiya boks maktabi",
                    "problem": "O'zbekistonlik bokschilarning Olimpiya o'yinlaridagi (Rio-2016, Parij-2024) yuksak natijalari sababi nimada?",
                    "step_by_step": "Mamlakatda kuchli boks maktabining yaratilganligi, tizimli murabbiylik uslubi, temirdek intizom va davlat tomonidan sportchilarga yaratilgan ulkan sharoitlar natijasidir.",
                    "answer": "Yetuk milliy maktab, kuchli intizom va doimiy tayyorgarlik"
                }
            ],
            "exercise": "Futbolda 'Offside' (o'yindan tashqari holat) qoidasi nimani anglatadi?",
            "exercise_solution": "Hujumchi to'p o'z jamoadoshi tomonidan unga uzatilgan lahzada raqib himoyachisidan (va to'pdan) ko'ra raqib darvoza chizig'iga yaqinroq turgan bo'lsa, offside qayd etiladi.",
            "check_questions": [
                {
                    "question": "Basketbol savatining balandligi poldan necha metr balandda joylashgan?",
                    "options": ["2.50 m", "2.75 m", "3.05 m", "3.50 m"],
                    "correct_index": 2,
                    "explanation": "Xalqaro standart basketbol halqasi balandligi 3.05 metr (10 fut) dir."
                },
                {
                    "question": "Olimpiada bayrog'idagi 5 ta tutashgan rangli halqa nimani anglatadi?",
                    "options": ["5 ta asosiy sport turini", "5 ta qit'a va ularning do'stligini", "Olimpiada o'tgan 5 ta shaharni", "5 ta faslni"],
                    "correct_index": 1,
                    "explanation": "Moviy, sariq, qora, yashil va qizil halqalar 5 ta qit'a birligini ifodalaydi."
                },
                {
                    "question": "Voleybol o'yinida bitta jamoa safida maydonda necha nafar o'yinchi bo'ladi?",
                    "options": ["5 kishi", "6 kishi", "7 kishi", "11 kishi"],
                    "correct_index": 1,
                    "explanation": "Voleybol maydonida har bir jamoadan 6 nafardan o'yinchi ishtirok etadi."
                }
            ],
            "tags": ["jismoniy tarbiya", "futbol", "basketbol", "voleybol", "olimpiada", "boks", "9-sinf"],
            "duration_minutes": 30
        },

        # CHIZMACHILIK (2)
        {
            "id": "art-009",
            "slug": "chizmachilik-standartlari-va-chiziqlar-turlari",
            "subject_id": "sub-35",
            "subject_name": "Chizmachilik",
            "title": "Chizmachilik asoslari: Davlat standartlari (GOST), chizmalar masshtabi va chiziqlar turlari",
            "grade_level": "8-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Chizmachilik formati (A4, A3), chizmachilik shriftlari, o'lcham qo'yish qoidalari va chizmalardagi asosiy chiziq turlari (tutash asosiy, ingichka, shtrix, shtrix-punktir)ni o'rganish.",
            "theory": "Chizmachilik — texnika tili bo'lib, buyumlar, detallar va inshootlarning grafik tasvirini chizma qoidalari asosida chizishni o'rgatadi. Yagona konstruktorlik hujjatlari tizimi (GOST / Standart) qoidalariga rioya qilinadi. Qog'oz formatlari: A4 (210 x 297 mm), A3 (297 x 420 mm), A2, A1. Chizma ramkasi: chapdan 20 mm (tikish uchun), qolgan uch tomondan 5 mm masofada chiziladi. Asosiy yozuv (shtamp) o'ng pastki burchakda joylashadi. Chiziq turlari: 1) Tutash asosiy qalin chiziq (s) — ko'rinadigan kontur chiziqlari (qalinligi 0.5 - 1.4 mm); 2) Tutash ingichka chiziq (s/3 - s/2) — o'lcham chiziqlari, chiqarish chiziqlari, shtrixlash; 3) Shtrix chiziq (- - -) — ko'rinmaydigan kontur chiziqlari; 4) Shtrix-punktir chiziq (- . - .) — o'q va markaz chiziqlari, simmetriya o'qi; 5) To'lqinsimon chiziq — uzilish chiziqlari. O'lcham qo'yish: o'lcham sonlari doimo millimetrda (mm belgisisiz) yoziladi.",
            "examples": [
                {
                    "title": "Chiziqlarni to'g'ri tanlash",
                    "problem": "Silindrsimon teshigi bor detalning simmetriya o'qi va ko'rinmaydigan ichki devori qaysi chiziqlar bilan chiziladi?",
                    "step_by_step": "1) Simmetriya o'qi — shtrix-punktir ingichka chiziq bilan chiziladi;\n2) Ko'rinmaydigan ichki teshik konturi — shtrix chiziq (uziq-uziq chiziq) bilan tasvirlanadi.",
                    "answer": "O'q chizig'i — shtrix-punktir; Ko'rinmas kontur — shtrix chiziq"
                },
                {
                    "title": "O'lcham qo'yish qoidasi",
                    "problem": "Chizmada detal uzunligi ustiga '75' deb yozilgan. Detalning haqiqiy uzunligi necha santimetr?",
                    "step_by_step": "Chizmachilik standartiga binoan chizmadagi barcha sonlar millimetrda ifodalanadi. 75 mm = 7.5 sm.",
                    "answer": "7.5 sm (75 mm)"
                }
            ],
            "exercise": "A4 formatining aniq o'lchamlari (bo'yi va eni millimetrda) qancha?",
            "exercise_solution": "210 mm x 297 mm.",
            "check_questions": [
                {
                    "question": "Chizmalarda ko'rinadigan tashqi qirralar qaysi chiziq turi bilan chiziladi?",
                    "options": ["Shtrix chiziq", "Tutash asosiy qalin chiziq", "Shtrix-punktir", "To'lqinsimon"],
                    "correct_index": 1,
                    "explanation": "Ko'rinadigan barcha konturlar tutash asosiy qalin chiziq (s) bilan chiziladi."
                },
                {
                    "question": "Aylana markazi va simmetriya o'qlarini ko'rsatish uchun qaysi chiziq ishlatiladi?",
                    "options": ["Tutash ingichka", "Shtrix-punktir ingichka chiziq", "Shtrix chiziq", "Qo'shaloq chiziq"],
                    "correct_index": 1,
                    "explanation": "Markaz va simmetriya o'qlari har doim shtrix-punktir chiziq bilan ifodalanadi."
                },
                {
                    "question": "Chizmalarda o'lchamlar qaysi o'lchov birligida qo'yiladi?",
                    "options": ["Santimetrda (sm)", "Millimetrda (mm, belgisiz)", "Metrda (m)", "Dyuyimda"],
                    "correct_index": 1,
                    "explanation": "Mashinasozlik va chizmachilikda barcha o'lchamlar birliksiz millimetrda yoziladi."
                }
            ],
            "tags": ["chizmachilik", "GOST", "chiziqlar", "A4 format", "o'lcham qo'yish", "8-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "art-010",
            "slug": "proeksion-chizmachilik-va-aksonometriya",
            "subject_id": "sub-35",
            "subject_name": "Chizmachilik",
            "title": "Proeksion chizmachilik: To'g'ri burchakli proeksiyalar (3 ta ko'rinish) va Aksonometriya",
            "grade_level": "8-9-sinf",
            "difficulty": "O'rta",
            "objective": "Gaspard Monj usuli, 3 ta proeksiya tekisligi (frontal, gorizontal, profil), bosh ko'rinishni tanlash va izometrik aksonometriya qurish.",
            "theory": "Fazoiy buyumlarni tekis qog'ozda aniq tasvirlash uchun to'g'ri burchakli (ortogonal) proeksiyalash usuli qo'llaniladi (Gaspard Monj tomonidan asoslangan). 3 ta o'zaro perpendikulyar proeksiyalar tekisligi: 1) V (Frontal tekislik) — oldindan ko'rinish (bosh ko'rinish — detal haqida eng ko'p ma'lumot berishi shart); 2) H (Gorizontal tekislik) — ustidan ko'rinish (bosh ko'rinish ostiga chiziladi); 3) W (Profil tekislik) — chapdan ko'rinish (bosh ko'rinishning o'ng tomoniga chiziladi). Uchala ko'rinish proeksion bog'lanish chiziqlari bilan o'zaro qat'iy bog'langan bo'ladi. Aksonometriya (fazoviy ko'rgazmali tasvir): buyumni birdaniga 3 ta o'qi (x, y, z) bo'yicha ko'rsatish usuli. To'g'ri burchakli Izometriya: x, y, z o'qlari orasidagi burchaklar teng 120° bo'ladi, barcha o'qlar bo'yicha qisqarish koeffitsiyenti 1 ga teng (haqiqiy o'lchamlarda chiziladi). Kesim va qirqimlar detalning ichki ko'rinishini ochish uchun qo'llaniladi.",
            "examples": [
                {
                    "title": "Uchta ko'rinishning o'zaro joylashuvi",
                    "problem": "Chizmada ustidan ko'rinish va chapdan ko'rinish bosh ko'rinishga nisbatan qayerda joylashadi?",
                    "step_by_step": "Chizmachilik qoidasiga binoan: Ustidan ko'rinish har doim bosh ko'rinishning ostiga joylashtiriladi; Chapdan ko'rinish esa bosh ko'rinishning o'ng yon tomoniga joylashtiriladi.",
                    "answer": "Ustidan ko'rinish — pastda, Chapdan ko'rinish — o'ngda joylashadi"
                },
                {
                    "title": "Izometriyada o'qlar burchagi",
                    "problem": "To'g'ri burchakli izometrik proeksiyada gorizontal chiziqqa nisbatan x va y o'qlari necha gradus burchak ostida o'tkaziladi?",
                    "step_by_step": "O'qlar o'rtasidagi burchak 120° bo'lgani uchun, gorizontal chiziqqa nisbatan x va y o'qlari 30° burchak ostida yuqoriga yo'naltiriladi (z o'qi vertikal).",
                    "answer": "30 gradus burchak ostida (o'zaro 120 gradus)"
                }
            ],
            "exercise": "Detalning ichki bo'shlig'i ko'rinishi uchun chizmada bajariladigan 'Qirqim' (razrez) amalini tushuntiring.",
            "exercise_solution": "Detal tasavvurda tekislik bilan kesiladi, oldingi qismi xayolan olib tashlanadi va kesilgan joy materialini ko'rsatish uchun 45° burchak ostida ingichka chiziqlar bilan shtrixlanadi.",
            "check_questions": [
                {
                    "question": "Detal haqida eng to'liq ma'lumot beruvchi oldindan ko'rinish nima deyiladi?",
                    "options": ["Bosh ko'rinish (frontal)", "Profil ko'rinish", "Ustidan ko'rinish", "Aksonometriya"],
                    "correct_index": 0,
                    "explanation": "Oldindan qaralganda detal shaklini eng yaqqol ochib beradigan ko'rinish Bosh ko'rinish qilib tanlanadi."
                },
                {
                    "question": "To'g'ri burchakli izometriyada x, y, z o'qlari orasidagi burchak necha gradusga teng?",
                    "options": ["90°", "120°", "45°", "60°"],
                    "correct_index": 1,
                    "explanation": "Izometriyada uchala fazoviy o'q o'zaro 120 graduslik burchaklar hosil qiladi."
                },
                {
                    "question": "Chizmalarda detalning kesilgan metall yuzasi qanday shtrixlanadi?",
                    "options": ["Gorizontal qalin chiziqlar bilan", "45 gradus burchak ostidagi tutash ingichka chiziqlar bilan", "Nuqtalar bilan", "Qoraytirib bo'yaladi"],
                    "correct_index": 1,
                    "explanation": "Standart bo'yicha metall qirqimlari 45° burchakdagi ingichka parallel chiziqlar bilan shtrixlanadi."
                }
            ],
            "tags": ["chizmachilik", "proeksiya", "aksonometriya", "izometriya", "bosh ko'rinish", "qirqim", "9-sinf"],
            "duration_minutes": 35
        },

        # HAYOT XAVFSIZLIGI (2)
        {
            "id": "art-011",
            "slug": "favqulodda-vaziyatlar-zilzila-va-yongin-xavfsizligi",
            "subject_id": "sub-36",
            "subject_name": "Hayot xavfsizligi",
            "title": "Hayot faoliyati xavfsizligi: Tabiiy va texnogen favqulodda vaziyatlar, Zilzila va Yong'in xavfsizligi",
            "grade_level": "5-7-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Favqulodda vaziyatlar turlari (tabiiy: zilzila, sel, toshqin; texnogen: yong'in, avariya), zilzila paytida o'zini tutish qoidalari va yong'inni o'chirish choralari.",
            "theory": "Hayot faoliyati xavfsizligi (HFX) — insonni atrof-muhitdagi xavf-xatarlardan himoya qilish, xavfsiz turmush sharoitini yaratish va favqulodda vaziyatlarda to'g'ri harakat qilishni o'rgatadi. Favqulodda vaziyatlar (FV) 2 turga bo'linadi: 1) Tabiiy tusdagi FV — zilzila, sel, ko'chki, toshqin, kuchli dovul; 2) Texnogen tusdagi FV — yong'inlar, portlashlar, kimyoviy va radiatsiyaviy avariyalar, gaz sizib chiqishi. Zilzila paytida harakatlanish: vahimaga tushmaslik, liftlardan foydalanmaslik, deraza va oynaviy buyumlardan uzoqlashish, bino ichida mustahkam eshik kesakisi, asosiy tayanch devor burchagi yoki mustahkam stol tagiga yashirinish ('Cho'k — himoyalan — ushla' qoidasi); ko'chada binolar, elektr simlari va daraxtlardan ochiq maydonga chiqish. Yong'in xavfsizligi: Yong'in sodir bo'lganda darhol 101 ga qo'ng'iroq qilish, tutunli xonadan polga yaqin egilib, og'iz-burnini nam mato bilan yopib chiqish, o't o'chirgichlardan (ognetushitel) foydalanish.",
            "examples": [
                {
                    "title": "Zilzila paytida xonadondagi xatti-harakat",
                    "problem": "Ko'p qavatli uyning 5-qavatida bo'lganingizda kuchli zilzila boshlandi. Zinadan yugurib tushish kerakmi yoki ichkarida qolishmi?",
                    "step_by_step": "Zilzila vaqtida zinapoyalar va liftlar eng birinchi qulaydi va eng xavfli joy hisoblanadi. Tebranish to'xtaguncha xonada qolib, mustahkam stol tagiga kirib ushlab turish yoki yuk ko'taruvchi asosiy devor burchagiga turish kerak. Tebranish to'xtagachgina zinadan ehtiyotkorlik bilan pastga tushiladi.",
                    "answer": "Tebranish to'xtaguncha stol tagida yoki burchakda qolish; zinaga yugurmaslik"
                },
                {
                    "title": "Gaz hidi sezilganda xavfsizlik",
                    "problem": "Xonadonda kuchli tabiiy gaz hidi sezilsa nima qilish qat'iyan man etiladi?",
                    "step_by_step": "Chiroqni yoqish yoki o'chirish, gugurt chaqish va elektr jihozlarini rozetkadan sug'urish mutlaqo man etiladi (hosil bo'lgan kichik uchqun portlashga olib keladi). Darhol derazalarni ochib xonani shamollatish, gaz jumragini yopish va tashqariga chiqib 104 ga qo'ng'iroq qilish kerak.",
                    "answer": "Gugurt chaqish va elektr kalitlarini yoqish/o'chirish mutlaqo man etiladi"
                }
            ],
            "exercise": "O'zbekistonda Favqulodda vaziyatlar vazirligi (qutqaruv xizmati) va Yong'in xavfsizligi qisqa telefon raqamlari qaysi?",
            "exercise_solution": "Yong'in xavfsizligi — 101; FVV qutqaruv xizmati — 1050 (va yagona 112).",
            "check_questions": [
                {
                    "question": "Ko'p qavatli binoda zilzila vaqtida liftdan foydalanish mumkinmi?",
                    "options": ["Ha, tezroq tushish uchun", "Qat'iyan man etiladi (elektr uzilishi va qamalib qolish xavfi bor)", "Faqat birinchi qavatdagilar", "Ixtiyoriy"],
                    "correct_index": 1,
                    "explanation": "Zilzila vaqtida elektr ta'minoti uzilib liftlar qulashi yoki ichida qamalib qolish xavfi juda yuqori."
                },
                {
                    "question": "Tutun bosgan xonadan chiqishda nega polga engashib emaklab harakatlanish kerak?",
                    "options": ["Tezroq yurish uchun", "Zaharli tutun va issiq havo yuqoriga ko'tariladi, toza kislorod polga yaqin joyda bo'ladi", "Charchamaslik uchun", "Bosh urilmasligi uchun"],
                    "correct_index": 1,
                    "explanation": "Zaharli is gazi yuqoriga intiladi, pastki qatlamda esa nafas olish mumkin bo'lgan kislorod ko'proq saqlanadi."
                },
                {
                    "question": "Zilzila vaqtida xona ichidagi eng xavfsiz joy qayer?",
                    "options": ["Deraza tagi", "Katta oyna yonida", "Yuk ko'taruvchi qalin devor burchagi va mustahkam stol tagi", "Balkonda"],
                    "correct_index": 2,
                    "explanation": "Burchaklar va mustahkam mebel osti shift bo'laklari qulaganda tirik qolish uchburchagini hosil qiladi."
                }
            ],
            "tags": ["hayot xavfsizligi", "zilzila", "yong'in xavfsizligi", "FVV", "favqulodda vaziyatlar", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "art-012",
            "slug": "ekologik-xavfsizlik-va-radiatsiyadan-himoyalanish",
            "subject_id": "sub-36",
            "subject_name": "Hayot xavfsizligi",
            "title": "Ekologik va radiatsiyaviy xavfsizlik: Toksik moddalar, gaz niqoblari va fuqaro muhofazasi",
            "grade_level": "8-11-sinf",
            "difficulty": "O'rta",
            "objective": "Kuchli ta'sir etuvchi zaharli moddalar (xlor, ammiak), radiatsiyadan himoyalanish, shaxsiy himoya vositalari (protivogaz / gaz niqobi) va fuqaro muhofazasi signallarini o'rganish.",
            "theory": "Fuqaro muhofazasi — tinchlik va urush davrida aholini, hududlarni zamonaviy qirg'in qurollari va xavfli avariyalardan himoya qilishga qaratilgan umumdavlat tadbirlari tizimidir. Kuchli ta'sir etuvchi zaharli moddalar (KTZM): 1) Xlor (Cl2) — havoga qaraganda 2.5 barobar og'ir sariq-yashil zaharli gaz. U yer yuzasi, yerto'la va chuqurliklarda to'planadi. Himoyalanish: binolarning yuqori qavatlariga yoki adirliklarga chiqish; niqobni 2% li ichimlik sodasi eritmasida namlash; 2) Ammiak (NH3) — havoga qaraganda yengil, o'tkir hidli rangsiz gaz, yuqoriga ko'tariladi. Himoyalanish: pastki qavatlar va yerto'lalarga tushish, niqobni 5% li limon yoki sirka kislotasi eritmasida namlash. Shaxsiy himoya vositalari: Nafas a'zolarini himoyalash — protivogaz (filtrlovchi gaz niqoblari: GP-5, GP-7), respiratorlar; Teri himoyasi — umumqo'shin himoya komplekti (OZK). Fuqaro muhofazasining asosiy ogohlantiruvchi signali: 'Barchaning diqqatiga!' (uzluksiz sirenalar va ovozli e'lonlar).",
            "examples": [
                {
                    "title": "Xlor va Ammiak avariyasida harakatlanish farqi",
                    "problem": "Kimyo zavodida xlor sizib chiqqanda va ammiak sizib chiqqanda qochish yo'nalishi qanday farqlanadi?",
                    "step_by_step": "Xlor havodan og'ir bo'lib yerga cho'kadi — shuning uchun balandliklarga va yuqori qavatlarga chiqish kerak. Ammiak esa havodan yengil bo'lib yuqoriga ko'tariladi — shuning uchun pastki qavatlarga va chuqurliklarga tushish kerak.",
                    "answer": "Xlorda yuqoriga/balandlikka chiqiladi; Ammiakda pastki qavatga tushiladi"
                },
                {
                    "title": "'Barchaning diqqatiga!' signali",
                    "problem": "Shaharda sirena va gudoklar uzluksiz chalinganda fuqarolar nima qilishi shart?",
                    "step_by_step": "Darhol televizor yoki radiolarni yoqish, Favqulodda vaziyatlar boshqarmasining rasmiy xabari va favqulodda harakatlar bo'yicha ko'rsatmalarini diqqat bilan eshitish lozim.",
                    "answer": "Darhol televizor va radioni yoqib, rasmiy xabarni eshitish"
                }
            ],
            "exercise": "Filtrlovchi protivogaz (gaz niqobi) kislorod miqdori 17% dan kam bo'lgan yopiq joylarda ishlatilishi mumkinmi?",
            "exercise_solution": "Yo'q, mutlaqo mumkin emas. Filtrlovchi protivogaz kislorod ishlab chiqarmaydi, faqat havoni tozalaydi. Kislorod yetishmaganda faqat izolyatsiyalovchi (kislorod ballonli) protivogazlar ishlatiladi.",
            "check_questions": [
                {
                    "question": "Xlor gazi havodan og'irmi yoki yengil?",
                    "options": ["Havodan yengil, yuqoriga ko'tariladi", "Havodan 2.5 barobar og'ir, pastga va yerto'lalarga cho'kadi", "Havo bilan teng", "Gaz emas"],
                    "correct_index": 1,
                    "explanation": "Xlor havodan sezilarli darajada og'ir bo'lgani sababli chuqurliklar va yerto'lalarda to'planadi."
                },
                {
                    "question": "Sirenalar chalinganda beriladigan fuqaro muhofazasining asosiy signali qanday nomlanadi?",
                    "options": ["Havo xavfi", "Barchaning diqqatiga!", "Evakuatsiya", "Radiatsiya xavfi"],
                    "correct_index": 1,
                    "explanation": "Uzluksiz sirena va korxona gudoklari 'Barchaning diqqatiga!' ogohlantirish signalidir."
                },
                {
                    "question": "Xlor bilan zaharlanish xavfi tug'ilganda paxta-doka bog'lamni qaysi eritmada namlash tavsiya etiladi?",
                    "options": ["Toza suvda", "2% li ichimlik sodasi eritmasida", "Sirka kislotasida", "Spirtda"],
                    "correct_index": 1,
                    "explanation": "Sodali ishqoriy eritma kislotali xlor gazini neytrallashga yordam beradi."
                }
            ],
            "tags": ["hayot xavfsizligi", "fuqaro muhofazasi", "xlor", "ammiak", "protivogaz", "ekologik xavfsizlik", "9-sinf"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_practical_arts_materials()
    print(f"Generated {len(mats)} Practical/Arts materials.")
