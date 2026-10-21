# -*- coding: utf-8 -*-
"""
Builder for Biologiya va tabiiy fanlar (18 materials)
- sub-08: Biologiya (5: bio-001 to bio-005)
- sub-09: Botanika (4: bio-006 to bio-009)
- sub-10: Zoologiya (4: bio-010 to bio-013)
- sub-11: Anatomiya (3: bio-014 to bio-016)
- sub-14: Tabiiy fanlar (2: bio-017 to bio-018)
"""

def get_biology_nature_materials():
    materials = [
        # BIOLOGIYA (5)
        {
            "id": "bio-001",
            "slug": "hujayra-nazariyasi-va-organoidlar",
            "subject_id": "sub-08",
            "subject_name": "Biologiya",
            "title": "Hujayra nazariyasi, eukariot va prokariot hujayra organoidlari",
            "grade_level": "9-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Hujayra tuzilishi, membrana, yadro, mitoxondriya, ribosoma, plastidalar funksiyalari va hujayra nazariyasi qoidalarini o'rganish.",
            "theory": "Hujayra — tiriklikning elementar tuzilish, faoliyat va rivojlanish birligidir. Shleyden va Shvann tomonidan asoslangan hujayra nazariyasining asosiy qoidalari: barcha tirik organizmlar hujayralardan tashkil topgan; hujayralar bo'linish orqali ko'payadi (R. Virxov: 'hujayradan hujayra'); hujayralar kimyoviy tarkibi va tuzilishi jihatidan o'xshashdir. Prokariotlar (bakteriyalar) shakllangan yadroga ega emas, eukariotlar (o'simlik, hayvon, zamburug'lar) esa yadro va membranali organoidlarga ega. Asosiy organoidlar: Mitoxondriya — ATF sintezlovchi 'energiya stansiyasi'; Ribosoma — oqsil sintezlovchi organoid; Endoplazmatik to'r (EPT) — moddalar sintezi va transporti; Goldji majmuasi — moddalarni to'plash va qadoqlash; Lizosoma — hujayra ichki hazm qilish organoidi.",
            "examples": [
                {
                    "title": "O'simlik va hayvon hujayralari farqi",
                    "problem": "O'simlik hujayrasida bo'lib, hayvon hujayrasida uchramaydigan 3 ta asosiy strukturani sanang.",
                    "step_by_step": "1) Sellulozadan iborat qattiq hujayra qobig'i (devori);\n2) Plastidalar (xloroplast, xromoplast, leykoplast);\n3) Hujayra shirasiga ega yirik markaziy vakuola.",
                    "answer": "Hujayra devori, plastidalar va markaziy vakuola"
                },
                {
                    "title": "Mitoxondriya funksiyasi",
                    "problem": "Nima uchun jigar va mushak hujayralarida mitoxondriyalar soni juda ko'p bo'ladi?",
                    "step_by_step": "Mushaklar harakatlanishi va jigar biokimyoviy jarayonlarni bajarishi uchun juda ko'p energiya (ATF) talab qiladi, bu energiyani aynan mitoxondriyalar sintezlaydi.",
                    "answer": "Yuqori energiya (ATF) talab qilingani sababli"
                }
            ],
            "exercise": "Ribosomalar qayerda hosil bo'ladi va ularning tarkibi nimalardan iborat?",
            "exercise_solution": "Ribosomalar yadrocha ichida hosil bo'ladi va ribosomal RNK (rRNK) hamda oqsillardan tashkil topgan.",
            "check_questions": [
                {
                    "question": "Hujayraning 'energiya stansiyasi' deb qaysi organoid ataladi?",
                    "options": ["Ribosoma", "Mitoxondriya", "Lizosoma", "Yadro"],
                    "correct_index": 1,
                    "explanation": "Mitoxondriyalarda hujayraviy nafas olish va ATF ko'rinishida energiya sintezi amalga oshadi."
                },
                {
                    "question": "Prokariot organizmlar qaysi qatorda to'g'ri ko'rsatilgan?",
                    "options": ["Bakteriyalar va sianobakteriyalar", "Zamburug'lar va lishayniklar", "O'simliklar va hayvonlar", "Viruslar va bakteriofaglar"],
                    "correct_index": 0,
                    "explanation": "Shakllangan yadroga ega bo'lmagan hujayralar prokariotlar (bakteriyalar) deyiladi."
                },
                {
                    "question": "Hujayra ichki hazm qilish vazifasini qaysi organoid bajaradi?",
                    "options": ["Goldji majmuasi", "Lizosoma", "Peroksisoma", "Vakuola"],
                    "correct_index": 1,
                    "explanation": "Lizosomalarda parchalovchi gidrolitik fermentlar saqlanadi."
                }
            ],
            "tags": ["biologiya", "hujayra", "mitoxondriya", "organoidlar", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "bio-002",
            "slug": "hujayraning-bolinishi-mitoz-va-meyoz",
            "subject_id": "sub-08",
            "subject_name": "Biologiya",
            "title": "Hujayra sikli: mitoz va meyoz bo'linish jarayonlari",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Mitoz va meyoz fazalarini (profaza, metafaza, anafaza, telofaza), ularning biologik ahamiyatini va xromosoma to'plami o'zgarishini solishtirish.",
            "theory": "Mitoz — somatik (tana) hujayralarning bo'linish usuli bo'lib, natijada genetik tarkibi aynan bir xil bo'lgan ikkita diploid (2n) qiz hujayra hosil bo'ladi. Mitoz fazalari: 1) Profaza — xromosomalar spiralizatsiyalashadi, yadro qobig'i eriydi, bo'linish duki hosil bo'ladi; 2) Metafaza — xromosomalar ekvator tekisligida saf tortadi (metafaza plastinkasi); 3) Anafaza — xromatidalar qarama-qarshi qutblarga tortiladi; 4) Telofaza — yangi yadrolar shakllanadi va sitokinez amalga oshadi. Meyoz — jinsiy hujayralarning (gametalarning) hosil bo'lish usuli bo'lib, ketma-ket ikkita bo'linishdan iborat (Meyoz I va Meyoz II). Meyoz I profazasida gomologik xromosomalar yaqinlashib (konyugatsiya) gen almashinadi (krossingover). Natijada xromosoma to'plami ikki baravar kamaygan 4 ta gaploid (1n) hujayra hosil bo'ladi.",
            "examples": [
                {
                    "title": "Mitoz va meyoz natijasini taqqoslash",
                    "problem": "Odamning tana hujayrasida 46 ta xromosoma bo'lsa, mitoz va meyoz natijasida hosil bo'lgan hujayralarda nechta xromosoma bo'ladi?",
                    "step_by_step": "1) Mitozda xromosomalar to'plami saqlanadi: 2n = 46 ta (2 ta hujayra).\n2) Meyozda xromosomalar to'plami reduksiyalanadi: 1n = 23 ta (4 ta jinsiy hujayra).",
                    "answer": "Mitozda: 46 ta; Meyozda: 23 ta"
                },
                {
                    "title": "Krossingover hodisasi",
                    "problem": "Krossingover qaysi bosqichda yuz beradi va uning biologik ahamiyati nimada?",
                    "step_by_step": "Krossingover Meyoz I ning profaza I bosqichida gomologik xromosomalar orasida ro'y beradi va organizmlarda yangi gen kombinatsiyalarini (kombinativ o'zgaruvchanlikni) ta'minlaydi.",
                    "answer": "Profaza I da; genetik xilma-xillikni ta'minlaydi"
                }
            ],
            "exercise": "Mitozning anafaza bosqichida xromosoma va DNK to'plami formulasini yozing.",
            "exercise_solution": "Anafazada xromatidalar mustaqil xromosomaga aylanadi: 4n4c (xromosomalar soni vaqtinchalik 2 baravar ortadi).",
            "check_questions": [
                {
                    "question": "Mitoz bo'linish natijasida nechta va qanday xromosomali hujayra hosil bo'ladi?",
                    "options": ["4 ta gaploid (n)", "2 ta diploid (2n)", "2 ta gaploid (n)", "4 ta diploid (2n)"],
                    "correct_index": 1,
                    "explanation": "Mitozda ona hujayradan 2 ta aynan o'xshash diploid (2n) hujayra hosil bo'ladi."
                },
                {
                    "question": "Xromosomalar ekvator tekisligida qaysi fazada joylashadi?",
                    "options": ["Profaza", "Metafaza", "Anafaza", "Telofaza"],
                    "correct_index": 1,
                    "explanation": "Metafazada xromosomalar ekvatorda joylashib 'metafaza plastinkasi'ni hosil qiladi."
                },
                {
                    "question": "Gomologik xromosomalar o'rtasida gen almashinishi hodisasi nima deyiladi?",
                    "options": ["Konyugatsiya", "Krossingover", "Replikatsiya", "Transkripsiya"],
                    "correct_index": 1,
                    "explanation": "Xromosoma yelkalari almashinuvi krossingover (kesishuv) deyiladi."
                }
            ],
            "tags": ["mitoz", "meyoz", "hujayra sikli", "krossingover", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "bio-003",
            "slug": "genetika-asoslari-mendel-qonunlari",
            "subject_id": "sub-08",
            "subject_name": "Biologiya",
            "title": "Genetika asoslari, Mendelning irsiyat qonunlari va Pennet katagi",
            "grade_level": "10-sinf",
            "difficulty": "O'rta",
            "objective": "Genotip, fenotip, dominantlik, retsessivlik tushunchalari va Mendelning 1-, 2-, 3-qonunlariga oid genetik masalalarni yechish.",
            "theory": "Irsiyat va o'zgaruvchanlik qonuniyatlarini o'rganadigan fan genetika deyiladi. Asoschisi — Gregor Mendel. Mendel qonunlari: 1) Birinchi avlod duragaylarining bir xillik qonuni (dominantlik qonuni): Gomozigota dominant (AA) va gomozigota retsessiv (aa) organizmlar chatishtirilganda F1 avlodda barcha duragaylar bir xil dominant fenotipga (Aa) ega bo'ladi; 2) Belgilarning ajralish qonuni: F1 geterozigotalar (Aa x Aa) o'zaro chatishtirilganda F2 avlodda fenotip bo'yicha 3:1, genotip bo'yicha 1:2:1 (1 AA : 2 Aa : 1 aa) nisbatda ajralish kuzatiladi; 3) Belgilarning mustaqil irsiylanish qonuni (digibrid chatishtirish): noallel genlar avlodlarga bir-biriga bog'liq bo'lmagan holda mustaqil o'tadi, F2 da fenotip bo'yicha 9:3:3:1 nisbat hosil bo'ladi.",
            "examples": [
                {
                    "title": "Monogibrid chatishtirish masalasi",
                    "problem": "No'xatda sariq rang (A) yashil rang (a) ustidan dominant. Geterozigota sariq no'xat (Aa) yashil no'xat (aa) bilan chatishtirilsa, avlodda qanday nisbat kutiladi?",
                    "step_by_step": "1) P: Aa x aa.\n2) Gametalar: A, a va a.\n3) F1 genotiplari: 1/2 Aa (sariq), 1/2 aa (yashil).\n4) Nisbat: 1 sariq : 1 yashil (50% ga 50%). Bu tahliliy chatishtirishdir.",
                    "answer": "1 sariq : 1 yashil (50% : 50%)"
                },
                {
                    "title": "Qon guruhlari irsiylanishi",
                    "problem": "I qon guruhli (I^0 I^0) ona va IV qon guruhli (I^A I^B) otadan qaysi qon guruhli bolalar tug'ilishi mumkin?",
                    "step_by_step": "1) Ona gametasi: I^0.\n2) Ota gametalari: I^A va I^B.\n3) Bolalar genotiplari: I^A I^0 (II guruh - 50%) va I^B I^0 (III guruh - 50%). I va IV guruhli bola tug'ilmaydi.",
                    "answer": "II guruh (50%) va III guruh (50%)"
                }
            ],
            "exercise": "AaBb genotipli organizm nechta turdagi gameta hosil qiladi?",
            "exercise_solution": "2^n formulaga ko'ra (n=2 geterozigotalar soni): 2^2 = 4 xil gameta: AB, Ab, aB, ab.",
            "check_questions": [
                {
                    "question": "Monogibrid chatishtirishda F2 avlodda fenotip bo'yicha qanday ajralish bo'ladi?",
                    "options": ["1:1", "3:1", "9:3:3:1", "1:2:1"],
                    "correct_index": 1,
                    "explanation": "Mendelning ikkinchi qonuniga ko'ra fenotip bo'yicha 3 ta dominant va 1 ta retsessiv (3:1) hosil bo'ladi."
                },
                {
                    "question": "Organizmning barcha genlari yig'indisi nima deyiladi?",
                    "options": ["Fenotip", "Genotip", "Genofond", "Kariotip"],
                    "correct_index": 1,
                    "explanation": "Genotip — organizm barcha genlarining yig'indisidir. Fenotip esa tashqi belgilar namoyon bo'lishi."
                },
                {
                    "question": "Bir xil allel genlarga ega organizm (masalan AA yoki aa) qanday ataladi?",
                    "options": ["Geterozigota", "Gomozigota", "Gemizigota", "Mutant"],
                    "correct_index": 1,
                    "explanation": "Allel genlari bir xil bo'lgan organizm gomozigota deyiladi."
                }
            ],
            "tags": ["genetika", "mendel", "genotip", "fenotip", "irsiylanish", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "bio-004",
            "slug": "fotosintez-va-hujayraviy-nafas-olish",
            "subject_id": "sub-08",
            "subject_name": "Biologiya",
            "title": "Moddalar almashinuvi: fotosintez va hujayraviy nafas olish biokimyosi",
            "grade_level": "10-sinf",
            "difficulty": "Murakkab",
            "objective": "Plastik va energetik almashinuv, fotosintezning yorug'lik va qorong'ulik fazalari, glikoliz va Krebs siklini tushunish.",
            "theory": "Metabolizm ikkita qarama-qarshi jarayondan iborat: anabolizm (assimilyatsiya, plastik almashinuv — moddalar sintezi va energiya sarflanishi) va katabolizm (dissimilyatsiya, energetik almashinuv — moddalarning parchalanishi va energiya ajralishi). Fotosintez — o'simlik va xlorofilli bakteriyalarda quyosh nuri energiyasi hisobiga noorganik moddalardan (CO2 va H2O) organik moddalar (glyukoza) sintezlanishi va O2 ajralishi: 6CO2 + 6H2O -> C6H12O6 + 6O2. Fotosintez bosqichlari: Yorug'lik fazasi (tilakoidlarda: suv fotolizi, O2 ajralishi, ATF va NADFH sintezi); Qorong'ulik fazasi (stromada: Kalvin sikli orqali CO2 dan glyukoza sintezi). Hujayraviy nafas olish 3 bosqichda boradi: 1) Tayyorgarlik (oshqozon-ichakda); 2) Glikoliz — kislorodsiz bosqich sitoplazmada (1 mol glyukozadan 2 mol ATF va 2 mol sut kislota); 3) Kislorodli bosqich — mitoxondriyada Krebs sikli (36 mol ATF). Jami 1 mol glyukoza to'liq parchalanganda 38 mol ATF hosil bo'ladi.",
            "examples": [
                {
                    "title": "Energetik almashinuvda ATF hisobi",
                    "problem": "Hujayrada 3 mol glyukoza to'liq kislorodli parchalanganda necha mol ATF hosil bo'ladi?",
                    "step_by_step": "1) 1 mol glyukoza to'liq parchalanganda 38 mol ATF hosil bo'ladi.\n2) 3 mol glyukoza uchun: 3 * 38 = 114 mol ATF.",
                    "answer": "114 mol ATF"
                },
                {
                    "title": "Fotosintezda kislorod manbasi",
                    "problem": "Fotosintez jarayonida ajralib chiqadigan kislorod CO2 dan kelib chiqadimi yoki H2O danmi?",
                    "step_by_step": "Izotopli nishonlash tajribalari isbotlaganidek, yorug'lik fazasida suv fotolizga (2H2O -> 4H+ + 4e- + O2) uchraydi, demak kislorod suv molekulasidan ajraladi.",
                    "answer": "Suv (H2O) fotolizi hisobiga"
                }
            ],
            "exercise": "Glikoliz jarayonida 10 mol glyukoza chala parchalanganda necha mol ATF hosil bo'ladi?",
            "exercise_solution": "Kislorodsiz bosqichda 1 mol glyukozadan 2 mol ATF hosil bo'ladi. 10 * 2 = 20 mol ATF.",
            "check_questions": [
                {
                    "question": "Fotosintezning yorug'lik fazasi xloroplastning qayerida sodir bo'ladi?",
                    "options": ["Stromada", "Tilakoid membranalarida", "Tashqi membranada", "Ribosomada"],
                    "correct_index": 1,
                    "explanation": "Xlorofill pigmentlari tilakoid membranalarida joylashgan bo'lib, yorug'lik reaksiyalari shu yerda o'tadi."
                },
                {
                    "question": "1 mol glyukoza to'liq (aerob) parchalanganda jami necha mol ATF sintezlanadi?",
                    "options": ["2 mol", "36 mol", "38 mol", "42 mol"],
                    "correct_index": 2,
                    "explanation": "2 mol glikolizda + 36 mol mitoxondriyada = jami 38 mol ATF hosil bo'ladi."
                },
                {
                    "question": "ATF molekulasidagi yuqori energiyali bog'lar nima deb ataladi?",
                    "options": ["Kovalent bog'", "Makroergik bog'", "Peptid bog'", "Gidrofob bog'"],
                    "correct_index": 1,
                    "explanation": "Fosfat guruhlari orasidagi yuqori energiyaga ega bog'lar makroergik bog'lar deyiladi (~40 kJ/mol)."
                }
            ],
            "tags": ["fotosintez", "metabolizm", "glikoliz", "ATF", "krebs sikli", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "bio-005",
            "slug": "evolyutsiya-talimoti-va-tabiiy-tanlanish",
            "subject_id": "sub-08",
            "subject_name": "Biologiya",
            "title": "Evolyutsiya nazariyasi: Darvin ta'limoti va mikroevolyutsiya omillari",
            "grade_level": "11-sinf",
            "difficulty": "Murakkab",
            "objective": "Charlz Darvinning evolyutsion nazariyasi, yashash uchun kurash turlari, tabiiy tanlanish shakllari va turlarning paydo bo'lish yo'llarini bilish.",
            "theory": "Tirik tabiatning tarixiy rivojlanishi evolyutsiya deyiladi. Charlz Darvin evolyutsiyaning 3 ta asosiy harakatlantiruvchi kuchini ko'rsatgan: 1) Irsiy o'zgaruvchanlik (mutatsion va kombinativ); 2) Yashash uchun kurash (tur ichidagi, turlararo va noqulay muhit omillariga qarshi); 3) Tabiiy tanlanish — foydali o'zgarishlarga ega organizmlarning saqlanib qolishi va nasl qoldirishi. Tabiiy tanlanish shakllari: Harakatlantiruvchi (muhit o'zgarganda yangi me'yor yuzaga keladi), Turg'unlashtiruvchi (o'zgarmas muhitda o'rtacha belgilar saqlanadi), Dizruptiv (ajratuvchi — chekka belgilar afzallik oladi). Mikroevolyutsiya — populyatsiya ichida yangi turlarning paydo bo'lishiga olib keluvchi jarayonlar (izolyatsiya, mutatsiyalar, genlar dreyfi, tabiiy tanlanish).",
            "examples": [
                {
                    "title": "Yashash uchun kurash turlari",
                    "problem": "Qayin o'rmonida yorug'lik va oziq uchun bir xil yoshdagi qayin daraxtlari orasidagi raqobat qaysi kurash turiga kiradi?",
                    "step_by_step": "Bu bitta turning individlari o'rtasida bo'layotgani sababli tur ichidagi kurash hisoblanadi (bu kurash eng keskin kechadi).",
                    "answer": "Tur ichidagi kurash"
                },
                {
                    "title": "Turg'unlashtiruvchi tanlanish",
                    "problem": "Nima uchun qadimgi relikt baliq Latimeriya million yillar davomida deyarli o'zgarmasdan saqlanib qolgan?",
                    "step_by_step": "Okeanning chuqur qatlamlaridagi muhit sharoitlari millionlab yillar davomida barqaror qolgan, bunday sharoitda turg'unlashtiruvchi tanlanish ta'sir qiladi.",
                    "answer": "Turg'unlashtiruvchi tabiiy tanlanish natijasida"
                }
            ],
            "exercise": "Allopatrik (geografik) tur hosil bo'lishining simpatrik (ekologik) tur hosil bo'lishidan asosiy farqini tushuntiring.",
            "exercise_solution": "Allopatrik tur hosil bo'lishida populyatsiyalar geografik to'siqlar (tog'lar, daryolar) orqali ajraladi; simpatrikda esa bitta areal ichida ekologik yoki xromosoma tafovutlari hisobiga yuzaga keladi.",
            "check_questions": [
                {
                    "question": "Evolyutsiyaning boshlang'ich elementar birligi nima?",
                    "options": ["Alohida organizm", "Populyatsiya", "Tur", "Biogeotsenoz"],
                    "correct_index": 1,
                    "explanation": "Evolyutsiya alohida individ darajasida emas, balki erkin chatishadigan populyatsiya darajasida kechadi."
                },
                {
                    "question": "Tirik tabiatda eng keskin kechadigan yashash uchun kurash qaysi?",
                    "options": ["Tur ichidagi kurash", "Turlararo kurash", "Noqulay sharoitga qarshi kurash", "Parazitlik"],
                    "correct_index": 0,
                    "explanation": "Bitta tur vakillarining hayotiy ehtiyojlari bir xil bo'lgani sababli tur ichidagi kurash eng shafqatsiz bo'ladi."
                },
                {
                    "question": "Sanoat melanizmi (oq qayin kapalaqlarining qorayishi) tabiiy tanlanishning qaysi shakliga misol?",
                    "options": ["Turg'unlashtiruvchi", "Harakatlantiruvchi", "Dizruptiv", "Sun'iy"],
                    "correct_index": 1,
                    "explanation": "Muhit o'zgarganda belgi me'yorining siljishi harakatlantiruvchi tanlanish hisoblanadi."
                }
            ],
            "tags": ["evolyutsiya", "darvin", "tabiiy tanlanish", "populyatsiya", "11-sinf"],
            "duration_minutes": 35
        },

        # BOTANIKA (4)
        {
            "id": "bio-006",
            "slug": "osimliklar-anatomiyasi-ildiz-poya-va-barg",
            "subject_id": "sub-09",
            "subject_name": "Botanika",
            "title": "O'simliklarning vegetativ organlari: ildiz, poya va barg tuzilishi",
            "grade_level": "5-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Ildiz turlari va zonalari, poyaning anatomik qavatlari, barg tuzilishi va o'tkazuvchi to'qimalar (ksilema va floema) funksiyasini bilish.",
            "theory": "O'simlik tanasi vegetativ (ildiz, poya, barg) va generativ (gul, meva, urug') organlardan iborat. Ildiz — o'simlikni tuproqqa mustahkamlovchi, suv va mineral moddalarni so'ruvchi organ. Ildiz zonalari: ildiz qinchasi, bo'linish zonasi, o'sish zonasi, so'rish zonasi (ildiz tukchalari) va o'tkazuvchi zona. Poya — barg va kurtaklarni tutib turuvchi o'q organ. Ko'ndalang kesimida: po'stloq (probka va lub/floema), kambiy (hosil qiluvchi to'qima), yog'ochlik (ksilema — suv va tuzlarni yuqoriga o'tkazadi), o'zak (zaxira oziq to'playdi). Barg — fotosintez, gaz almashinuvi va transpiratsiya (suv bug'latish) vazifasini bajaruvchi organ.",
            "examples": [
                {
                    "title": "Ildiz tizimlari farqi",
                    "problem": "O'q ildiz va popuk ildiz tizimlarining farqini ayting va misollar keltiring.",
                    "step_by_step": "1) O'q ildizda asosiy ildiz yaqqol ko'rinadi (ikki urug'pallalilarda: burchak, loviya, olma).\n2) Popuk ildizda asosiy ildiz yaxshi rivojlanmaydi, qo'shimcha va yon ildizlar tutam hosil qiladi (bir urug'pallalilarda: bug'doy, makkajo'xori, piyoz).",
                    "answer": "O'q ildiz (loviya) va popuk ildiz (bug'doy)"
                },
                {
                    "title": "Transpiratsiya ahamiyati",
                    "problem": "O'simliklar so'rgan suvining 90% dan ortig'ini nega barglari orqali bug'latib yuboradi?",
                    "step_by_step": "1) Transpiratsiya o'simlikni quyosh issig'ida qizib ketishdan saqlaydi (sovitadi);\n2) Ildizdan barglargacha uzluksiz suv va mineral moddalar oqimini ta'minlovchi so'ruvchi kuch hosil qiladi.",
                    "answer": "Sovutish va suv oqimini harakatlantirish uchun"
                }
            ],
            "exercise": "Kambiy qavatining yillik faoliyati natijasida daraxt poyasida nima hosil bo'ladi?",
            "exercise_solution": "Kambiy hujayralarining bo'linishi hisobiga yog'ochlikda yillik halqalar hosil bo'ladi va daraxt tanasi yo'g'onlashadi.",
            "check_questions": [
                {
                    "question": "Suv va mineral tuzlar o'simlik bo'ylab qaysi to'qima orqali yuqoriga ko'tariladi?",
                    "options": ["Ksilema (yog'ochlik naylari)", "Floema (elaksimon naylar)", "Po'kak", "Kambiy"],
                    "correct_index": 0,
                    "explanation": "Ksilema naylari orqali suv va erigan moddalar ildizdan barglarga yuqoriga qarab harakatlanadi."
                },
                {
                    "question": "Bargda gaz almashinuvi va suv bug'lanishi qaysi tuzilma orqali boshqariladi?",
                    "options": ["Tomirlar", "Og'izchalar (ustitsa)", "Kutikula", "Barg bandi"],
                    "correct_index": 1,
                    "explanation": "Barg epidermasidagi og'izchalar ochilib-yopilib transpiratsiya va gaz almashinuvini tartibga soladi."
                },
                {
                    "question": "O'simlik ildizining suv va tuzlarni so'ruvchi asosiy qismi qaysi?",
                    "options": ["Ildiz qinchasi", "So'rish zonasi (ildiz tukchalari)", "O'sish zonasi", "Bo'linish zonasi"],
                    "correct_index": 1,
                    "explanation": "So'rish zonasida yuzlab mikroskopik ildiz tukchalari suvni faol o'zlashtiradi."
                }
            ],
            "tags": ["botanika", "ildiz", "poya", "barg", "ksilema", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "bio-007",
            "slug": "gul-changlanish-va-uruglanish",
            "subject_id": "sub-09",
            "subject_name": "Botanika",
            "title": "Gulning tuzilishi, changlanish turlari va yopiq urug'lilarda qo'sh urug'lanish",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Gul a'zolari (urug'chi, changchi), shamol va hasharotlar yordamida changlanish hamda S.G. Navashin kashf etgan qo'sh urug'lanish mexanizmini o'rganish.",
            "theory": "Gul — yopiq urug'li (gulli) o'simliklarning jinsiy ko'payish generativ organidir. Gul a'zolari: gulband, gulo'rni, gulkosachabarglar, gultojibarglar, changchi (erkaklik a'zosi) va urug'chi (urg'ochilik a'zosi). Changlanish — chang donachasining changchidan urug'chi tumshuqchasiga tushishi (o'z-o'zidan va chetdan changlanish: shamol, hasharotlar, qushlar orqali). Qo'sh urug'lanish (S.G. Navashin, 1898): Chang naychasidan murtak xaltasiga 2 ta spermiy kiradi: 1-spermiy (n) tuxumhujayra (n) bilan qo'shilib urug' murtagini (2n zigota) hosil qiladi; 2-spermiy (n) markaziy hujayra (2n) bilan qo'shilib zaxira oziq to'qimasi — triploid endospermni (3n) hosil qiladi. Urug'kurtakdan urug', tugunchadan meva shakllanadi.",
            "examples": [
                {
                    "title": "Qo'sh urug'lanish formulasi",
                    "problem": "Yopiq urug'li o'simliklarda endospermning xromosoma to'plami necha n ga teng?",
                    "step_by_step": "1) Markaziy hujayra diploid (2n).\n2) Unga qo'shiluvchi spermiy gaploid (1n).\n3) 2n + 1n = 3n (triploid).",
                    "answer": "Triploid (3n)"
                },
                {
                    "title": "Hasharotlar vositasida changlanish belgilari",
                    "problem": "Hasharotlar yordamida changlanuvchi gullarning asosiy xususiyatlarini sanang.",
                    "step_by_step": "Yorqin rangli gultoj, xushbo'y hid, shirin nektar, yopishqoq va yirik chang donachalari.",
                    "answer": "Yorqin tojibarg, nektar va xushbo'y hid"
                }
            ],
            "exercise": "Ochiq urug'lilar (qarag'ay, archa) bilan yopiq urug'lilarning urug'lanishidagi asosiy farq nimada?",
            "exercise_solution": "Ochiq urug'lilarda qo'sh urug'lanish bo'lmaydi, ularning endospermi urug'lanishdan oldin hosil bo'ladi va gaploid (n) to'plamga ega.",
            "check_questions": [
                {
                    "question": "Gulli o'simliklarda qo'sh urug'lanish hodisasini kim kashf etgan?",
                    "options": ["Charlz Darvin", "Gregor Mendel", "S.G. Navashin", "Robert Guk"],
                    "correct_index": 2,
                    "explanation": "Rus olimi Sergey Navashin 1898-yilda lolaguldoshlar misolida qo'sh urug'lanishni kashf etgan."
                },
                {
                    "question": "Gulning changchisi qaysi qismlardan iborat?",
                    "options": ["Tumshuqcha, ustuncha, tuguncha", "Changchi ipi va changdon", "Gulkosacha va gultoj", "Murtak va endosperm"],
                    "correct_index": 1,
                    "explanation": "Changchi changchi ipi va unda joylashgan changdondan tashkil topgan."
                },
                {
                    "question": "Urug'lanishdan so'ng tugunchadan nima rivojlanadi?",
                    "options": ["Urug'", "Meva", "Barg", "Ildiz"],
                    "correct_index": 1,
                    "explanation": "Urug'chining tugunchasi o'sib meva hosil qiladi, ichidagi urug'kurtakdan esa urug' yetiladi."
                }
            ],
            "tags": ["botanika", "gul", "changlanish", "qo'sh urug'lanish", "navashin", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "bio-008",
            "slug": "tuban-va-yuksak-osimliklar-suvotlar-va-qirqquloqlar",
            "subject_id": "sub-09",
            "subject_name": "Botanika",
            "title": "O'simliklar sistematikasi: suv o'tlari, yo'sinlar, qirqquloqlar va ochiq urug'lilar",
            "grade_level": "6-sinf",
            "difficulty": "O'rta",
            "objective": "Tuban o'simliklar (tallomli) va yuksak o'simliklar (sporalilar va urug'lilar) rivojlanish bosqichlari hamda nasllar gallanishini o'rganish.",
            "theory": "O'simliklar dunyosi ikki katta guruhga bo'linadi: 1) Tuban o'simliklar — tanasi a'zolarga (ildiz, poya, barg) ajralmagan, qatlam (tallom)dan iborat (yashil, qo'ng'ir va qizil suv o'tlari: xlorella, spirogira, ulotriks, laminariya); 2) Yuksak o'simliklar — haqiqiy to'qima va organlarga ega. Yuksak sporalilar: Yo'sinlar (moxlar) — ildizi yo'q, rizoidlari bor, hayotiy siklida gametofit (jinsiy nasl) ustunlik qiladi (funariya, sfagnum); Qirqquloqlar, qirqbo'g'imlar va plavunlar — o'tkazuvchi to'qimalarga ega, hayotiy siklida sporofit (jinssiz nasl) ustunlik qiladi, ko'payishi uchun suv zarur. Urug'li o'simliklar: Ochiq urug'lilar (qarag'ay, archa, qoraqarag'ay) — urug'lari qubbalarda ochiq holda yetiladi, suvga bog'liq bo'lmagan changlanishga ega.",
            "examples": [
                {
                    "title": "Nasllar gallanishi",
                    "problem": "Yo'sinlar va qirqquloqlarning hayot siklidagi asosiy farq nimada?",
                    "step_by_step": "Yo'sinlarda yashil barg-poyali o'simlik gametofit hisoblanadi (ustun nasl); qirqquloqlarda esa ko'zga ko'ringan yirik o'simlik sporofitdir, gametofit esa mayda yuraksimon o'simtadan iborat.",
                    "answer": "Yo'sinlarda gametofit, qirqquloqlarda sporofit ustunlik qiladi"
                },
                {
                    "title": "Sfagnum torf yo'sini",
                    "problem": "Sfagnum yo'sini botqoqliklarda qanday qilib torf qatlamlarini hosil qiladi?",
                    "step_by_step": "Sfagnum poyasi va bargida suv shimuvchi o'lik havoli hujayralar va bakteritsid moddalar (sfagnol) bor. Kislorod yetishmasligi va mikroblar o'lishi tufayli chirimasdan torfga aylanadi.",
                    "answer": "Chirimay to'planishi hisobiga torf hosil bo'ladi"
                }
            ],
            "exercise": "Bir hujayrali yashil suv o'ti xlorellaning oziq-ovqat va kosmonavtikada qo'llanilish sababi nima?",
            "exercise_solution": "Xlorella tez ko'payadi, fotosintez orqali ko'p kislorod ajratadi va quruq massasining 50% dan ortig'i yuqori sifatli oqsildan iborat.",
            "check_questions": [
                {
                    "question": "Tuban o'simliklarning a'zolarga ajralmagan tanasi nima deyiladi?",
                    "options": ["Kurtak", "Tallom (qatlam)", "Murtak", "Rizoid"],
                    "correct_index": 1,
                    "explanation": "Suv o'tlarining ildiz, poya, bargga ajralmagan tanasi tallom deb ataladi."
                },
                {
                    "question": "Qarag'ayning urug'i qayerda yetiladi?",
                    "options": ["Meva ichida", "Urg'ochi qubba tangachalari ustida ochiq holda", "Gultojida", "Ildizida"],
                    "correct_index": 1,
                    "explanation": "Ochiq urug'lilarda tuguncha bo'lmagani uchun urug'lar qubba tangachasida ochiq yetiladi."
                },
                {
                    "question": "Sporali o'simliklar (yo'sinlar, qirqquloqlar) urug'lanishi uchun nima mutlaqo zarur?",
                    "options": ["Shamol", "Hasharotlar", "Tomchi holidagi suv", "Quyosh qorong'uligi"],
                    "correct_index": 2,
                    "explanation": "Harakatlanuvchi spermatozoidlar tuxumhujayraga yetib borishi uchun suv tomchisi shart."
                }
            ],
            "tags": ["botanika", "suv o'tlari", "yo'sinlar", "qirqquloqlar", "ochiq urug'lilar", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "bio-009",
            "slug": "dorivor-va-qishloq-xojaligi-osimliklari",
            "subject_id": "sub-09",
            "subject_name": "Botanika",
            "title": "O'zbekistonning madaniy qishloq xo'jaligi va dorivor o'simliklari",
            "grade_level": "6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "G'o'za, bug'doy, poliz ekinlari va O'zbekiston florasidagi mashhur dorivor o'simliklar (kiyiko't, shirinmiya, dalachoy) biologiyasini o'rganish.",
            "theory": "O'zbekiston boy va xilma-xil o'simliklar dunyosiga ega bo'lib, 4500 dan ortiq yovvoyi o'simlik turlari o'sadi. Asosiy qishloq xo'jalik ekinlari: G'o'za (gulxayridoshlar oilasi) — tolasi to'qimachilikda, chigiti yog' sanoatida ishlatiladi; Bug'doy (bug'doydoshlar/g'alladoshlar) — donli oziq-ovqat ekini; Poliz ekinlari (qovun, tarvuz, qovoq — qovoqdoshlar oilasi). Dorivor o'simliklar: Shirinmiya (ildizida glitsirrizin bo'lib, nafas yo'llari va shamollashda qo'llaniladi); Kiyiko't (efir moylariga boy, oshqozon-ichak va asabni tinchlantirishda); Namatak (C vitaminiga boy, immunitetni ko'taradi); Dalachoy (zveroboy — antiseptik va yallig'lanishga qarshi vosita). O'zbekiston Qizil kitobiga ko'plab noyob va yo'qolib borayotgan o'simliklar (lola turlari, sallagul) kiritilgan.",
            "examples": [
                {
                    "title": "G'o'za o'simligi biologiyasi",
                    "problem": "G'o'za hosil beruvchi shoxlarining qanday turlari mavjud?",
                    "step_by_step": "G'o'zada o'suvchi (monopodial) shoxlar poyaning pastki qismidan chiqadi va bo'yiga o'sadi; hosil beruvchi (simpodial) shoxlarda esa bevosita g'uncha, gul va ko'saklar shakllanadi.",
                    "answer": "Monopodial (o'suvchi) va simpodial (hosil beruvchi)"
                },
                {
                    "title": "Shirinmiya (Solodka) eksport salohiyati",
                    "problem": "Nima uchun O'zbekistonda shirinmiya yetishtirish va qayta ishlashga katta e'tibor qaratilmoqda?",
                    "step_by_step": "Shirinmiya ildizidagi glitsirrizin kislotasi farmatsevtika, oziq-ovqat va kosmetikada qimmatbaho xomashyo hisoblanadi va jahon bozorida yuqori talabga ega.",
                    "answer": "Qimmatli farmatsevtik va eksportbop xomashyo bo'lgani uchun"
                }
            ],
            "exercise": "Namatak mevasidan xalq tabobati va zamonaviy tibbiyotda qanday maqsadda foydalaniladi?",
            "exercise_solution": "Namatak mevasi multivitamin manbai (ayniqsa askorbin kislota - C vitamini) bo'lib, shamollash, avitaminoz va jigarni davolashda damlama sifatida ichiladi.",
            "check_questions": [
                {
                    "question": "G'o'za qaysi o'simliklar oilasiga mansub?",
                    "options": ["Bug'doydoshlar", "Gulxayridoshlar", "Burchoqdoshlar", "Ituzumdoshlar"],
                    "correct_index": 1,
                    "explanation": "Paxta beruvchi g'o'za o'simligi gulxayridoshlar (Malvaceae) oilasiga kiradi."
                },
                {
                    "question": "Yo'tal va nafas yo'llari xastaliklarida ildizidan damlama tayyorlanadigan dorivor o'simlik qaysi?",
                    "options": ["Shirinmiya", "G'o'za", "Makkajo'xori", "Shohbaliq"],
                    "correct_index": 0,
                    "explanation": "Shirinmiya (Glycyrrhiza glabra) ildizi balg'am ko'chiruvchi mashhur dorivor vositadir."
                },
                {
                    "question": "Bug'doy doni qanday meva turiga kiradi?",
                    "options": ["Pista", "Donmeva", "Dukkak", "Rezavor"],
                    "correct_index": 1,
                    "explanation": "G'alladoshlar oilasi vakillarining mevasi yupqa qobiqli quruq donmeva deyiladi."
                }
            ],
            "tags": ["botanika", "dorivor o'simliklar", "g'o'za", "shirinmiya", "namatak", "6-sinf"],
            "duration_minutes": 25
        },

        # ZOOLOGIYA (4)
        {
            "id": "bio-010",
            "slug": "bir-hujayrali-va-soddalashgan-hayvonlar",
            "subject_id": "sub-10",
            "subject_name": "Zoologiya",
            "title": "Soddaxonalar: amyoba, yashil evglena, tufelka va parazit bir hujayralilar",
            "grade_level": "7-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Bir hujayrali hayvonlarning harakati (soxta oyoqlar, xivchinlar, kiprikchalar), oziqlanishi, bezgak plazmodiyasi va parazitlik xususiyatlarini bilish.",
            "theory": "Soddaxonalar (bir hujayralilar) tanasi bitta mustaqil eukariot hujayradan iborat bo'lib, barcha tiriklik vazifalarini bajaradi. Asosiy vakillari: 1) Oddiy amyoba — doimiy tana shakliga ega emas, soxta oyoqlari (psevdopodiyalar) yordamida fagotsitoz usulida oziqlanadi va harakatlanadi; 2) Yashil evglena — aralash (miksotrof) oziqlanadi: yorug'likda xloroplastlari yordamida fotosintez qiladi, qorong'uda tayyor organik moddalarni so'radi, stigma (qizil ko'zcha) yordamida yorug'likka intiladi; 3) Infuzoriya tufelka — doimiy poyafzal shaklidagi tanaga, minglab kiprikchalarga, ikkita yadroga (katta vegetativ makronukleus va kichik generativ mikronukleus) ega; 4) Parazit bir hujayralilar: Bezgak plazmodiyasi (bezgak chivinlari orqali yuqadi, odam qonidagi eritrotsitlarni parchalaydi), dizenteriya amyobasi.",
            "examples": [
                {
                    "title": "Yashil evglenaning o'ziga xosligi",
                    "problem": "Nima uchun yashil evglena o'simliklar va hayvonlar orasidagi bog'lovchi zanjir hisoblanadi?",
                    "step_by_step": "Chunki u o'simliklar kabi xloroplastga ega bo'lib fotosintez qiladi, lekin shu bilan birga hayvonlar kabi faol harakatlanadi (xivchin bilan) va tayyor organik moddalar bilan ham oziqlana oladi (miksotrof).",
                    "answer": "Ham avtotrof, ham geterotrof (miksotrof) oziqlangani uchun"
                },
                {
                    "title": "Noqulay sharoitda saqlanish",
                    "problem": "Hovuz yoki ko'lmak qurib qolganda bir hujayralilar qanday jon saqlaydi?",
                    "step_by_step": "Noqulay sharoitda ular qalin himoya qobig'i bilan o'ralib sistaga aylanadi va shamol orqali boshqa suv havzalariga tarqaladi.",
                    "answer": "Sista hosil qilish orqali"
                }
            ],
            "exercise": "Infuzoriya tufelkaning ayirish sistemasi qaysi organoidlardan iborat?",
            "exercise_solution": "Ikkita qisqaruvchi vakuola va ularga tutash radial kanallardan iborat bo'lib, ortiqcha suv va suyuq chiqindilarni tashqariga chiqaradi.",
            "check_questions": [
                {
                    "question": "Doimiy tana shakliga ega bo'lmagan bir hujayrali jonivor qaysi?",
                    "options": ["Yashil evglena", "Infuzoriya tufelka", "Oddiy amyoba", "Xlorella"],
                    "correct_index": 2,
                    "explanation": "Amyoba sitoplazmasining siljishi hisobiga soxta oyoqlar chiqarib shaklini doim o'zgartiradi."
                },
                {
                    "question": "Bezgak kasalligini qo'zg'atuvchi organizm qaysi?",
                    "options": ["Bakteriya", "Bezgak plazmodiyasi", "Qon so'ruvchi kana", "Virus"],
                    "correct_index": 1,
                    "explanation": "Bezgak plazmodiyasi (Plasmodium) parazit bir hujayrali jonivor hisoblanadi."
                },
                {
                    "question": "Infuzoriya tufelkada kichik yadro (mikronukleus) qanday vazifani bajaradi?",
                    "options": ["Oziq hazm qilish", "Jinsiy jarayon (konyugatsiya) va irsiy axborotni uzatish", "Harakatlanish", "Ayirish"],
                    "correct_index": 1,
                    "explanation": "Kichik yadro generativ yadro bo'lib, jinsiy ko'payish (konyugatsiya) uchun javobgardir."
                }
            ],
            "tags": ["zoologiya", "amyoba", "infuzoriya", "evglena", "soddaxonalar", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "bio-011",
            "slug": "chuvalchanglar-va-parazit-gijjalarning-rivojlanish-sikli",
            "subject_id": "sub-10",
            "subject_name": "Zoologiya",
            "title": "Chuvalchanglar: yassi, to'garak va halqali chuvalchanglar biologiyasi",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Yassi, to'garak va halqali chuvalchanglar anatomiyasi, jigar qurti va qoramol tasmasimon chuvalchangi rivojlanish sikli hamda gelmintozlar profilaktikasi.",
            "theory": "Chuvalchanglar uchta tipga bo'linadi: 1) Yassi chuvalchanglar — tana bo'shlig'i yo'q, parenxima bilan to'lgan, orqa-qorin tomondan yassilangan. Erkin yashovchi (oq planariya) va parazitlar: Jigar qurti (oraliq xo'jayini — kichik suv shillig'i, asosiy xo'jayini — tuyoqli hayvonlar va odam), Qoramol tasmasimon chuvalchangi (soliter — oraliq xo'jayini qoramol, asosiy xo'jayini odam, uzunligi 4-10 metr); 2) To'garak chuvalchanglar — birlamchi tana bo'shlig'iga va orqa chiqaruv teshigiga ega (Odam askaridasi, bolalar gijjasi / ostritsa). Askarida tuxumi tuproqda yetiladi, lichinkasi qon orqali o'pka va nafas yo'llarini aylanib chiqadi; 3) Halqali chuvalchanglar — ikkilamchi tana bo'shlig'i (tselom), segmentli tana va berk qon aylanish sistemasiga ega (Yomg'ir chuvalchangi, tibbiyot zulugi).",
            "examples": [
                {
                    "title": "Jigar qurtining oraliq xo'jayini",
                    "problem": "Nima uchun jigar qurti bilan zararlanish botqoqlashgan yaylovlarda ko'p uchraydi?",
                    "step_by_step": "Jigar qurtining tuxumidan chiqqan miratsidiy lichinkasi faqat chuchuk suv shillig'i (kichik prundovik) tanasida rivojlanadi, bu shillik esa botqoq va zax joylarda yashaydi.",
                    "answer": "Oraliq xo'jayin (kichik suv shillig'i) botqoqlarda yashagani uchun"
                },
                {
                    "title": "Yomg'ir chuvalchangining tuproqdagi o'rni",
                    "problem": "Charlz Darvin yomg'ir chuvalchanglarini nima sababdan tuproqning eng muhim biologik ishlovchilari deb atagan?",
                    "step_by_step": "Ular tuproqni kovlab yumshatadi, havo va suv o'tishini yaxshilaydi, o'simlik qoldiqlarini chirindiga (gumusga) aylantirib tuproq unumdorligini oshiradi.",
                    "answer": "Tuproqni yumshatib chirindi hosil qilgani uchun"
                }
            ],
            "exercise": "Qoramol tasmasimon chuvalchangi (soliter) bilan odam qanday yo'l bilan zararlanadi?",
            "exercise_solution": "Yaxshi pishirilmagan yoki xom finnali (finna — pufaksimon lichinka) qoramol go'shtini iste'mol qilish orqali zararlanadi.",
            "check_questions": [
                {
                    "question": "Berk qon aylanish sistemasi dastlab qaysi guruhda paydo bo'lgan?",
                    "options": ["Yassi chuvalchanglar", "To'garak chuvalchanglar", "Halqali chuvalchanglar", "Ichakbo'shliqlilar"],
                    "correct_index": 2,
                    "explanation": "Halqali chuvalchanglarda (masalan, yomg'ir chuvalchangi) dastlabki berk qon aylanish sistemasi mavjud."
                },
                {
                    "question": "Odam askaridasi lichinkasi organizmda qanday migratsiya qiladi?",
                    "options": ["Faqat ichakda qoladi", "Ichakdan qonga o'tib, jigar, yurak va o'pka orqali yana ichakka tushadi", "Bosh miyaga o'tadi", "Buyraklarda yashaydi"],
                    "correct_index": 1,
                    "explanation": "Askarida lichinkasi rivojlanishi uchun kislorod kerak, shuning uchun qon oqimi bilan o'pkaga borib, so'ng qayta yutiladi."
                },
                {
                    "question": "Jigar qurtining oraliq xo'jayini kim?",
                    "options": ["Qoramol", "Kichik suv shillig'i", "Odam", "Baliq"],
                    "correct_index": 1,
                    "explanation": "Lichinkalik davrini chuchuk suv shillig'i (Galba truncatula) tanasida o'taydi."
                }
            ],
            "tags": ["zoologiya", "chuvalchanglar", "parazitlar", "askarida", "yomg'ir chuvalchangi", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "bio-012",
            "slug": "bogimoyoqlilar-hasharotlar-va-ularning-rivojlanishi",
            "subject_id": "sub-10",
            "subject_name": "Zoologiya",
            "title": "Bo'g'imoyoqlilar: qisqichbaqasimonlar, o'rgimchaksimonlar va hasharotlar",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Xitin qoplami, bo'g'imli oyoqlar, ochiq qon aylanish sistemasi, to'liq va chala o'zgarishli (metamorfoz) hasharotlar biologiyasini o'rganish.",
            "theory": "Bo'g'imoyoqlilar — hayvonot olamidagi eng ko'p sonli tip (1.5 milliondan ortiq tur). Asosiy belgilari: xitinli tashqi skelet (tullash orqali o'sadi), bo'g'imli oyoqlar, bo'g'imlarga ajralgan tana, ochiq qon aylanish sistemasi. 3 ta asosiy sinf: 1) Qisqichbaqasimonlar — boshko'krak va qorin, 2 juft mo'ylov, 5 juft yurish oyog'i, jabralar bilan nafas oladi (daryo qisqichbaqasi, dafniya, siklop); 2) O'rgimchaksimonlar — boshko'krak va qorin, mo'ylovsiz, 4 juft yurish oyog'i, o'rgimchak bezlari, o'pka xaltalari va traxeyalar (butli o'rgimchak, chayon, qoraqurt, kanalar); 3) Hasharotlar — tana 3 qismdan (bosh, ko'krak, qorin), 1 juft mo'ylov, 3 juft oyoq (ko'krakda), qanotlar, traxeyalar orqali nafas oladi. Hasharotlar rivojlanishi: Chala o'zgarish (tuxum -> lichinka -> voyaga yetgan hasharot: chigirtka, ninachi, suvarak); To'liq o'zgarish (tuxum -> lichinka -> g'umbak -> voyaga yetgan hasharot: kapalak, qo'ng'iz, pashsha, ari, ipak qurti).",
            "examples": [
                {
                    "title": "To'liq va chala o'zgarish farqi",
                    "problem": "Ipak qurti (tut ipak qurti) qaysi rivojlanish turiga kiradi va ipak qaysi bosqichda olinadi?",
                    "step_by_step": "Ipak qurti to'liq o'zgarish bilan rivojlanadi (tuxum -> qurt -> g'umbak -> kapalak). Qurt g'umbakka aylanishdan oldin o'z atrofiga ipak ipidan pilla o'raydi. Ipak aynan shu pilladan olinadi.",
                    "answer": "To'liq o'zgarish; pilla (g'umbak) bosqichida"
                },
                {
                    "title": "O'rgimchaksimonlar va hasharotlar oyoqlari",
                    "problem": "O'rgimchak va ari nechta yurish oyog'iga ega?",
                    "step_by_step": "O'rgimchaksimonlarda 4 juft (8 ta), hasharotlarda (ari) esa 3 juft (6 ta) yurish oyog'i bo'ladi.",
                    "answer": "O'rgimchakda 8 ta, arida 6 ta"
                }
            ],
            "exercise": "Qoraqurt va chayon chaqqanda birinchi tibbiy yordam choralari qanday?",
            "exercise_solution": "Qoraqurt chaqqan zahoti (1-2 minut ichida) gugurt alangasida chaqilgan joy kuydiriladi (zahar oqsili termik parchalanadi) va zudlik bilan shifoxonaga yetkaziladi.",
            "check_questions": [
                {
                    "question": "Hasharotlarning ko'krak qismida nechta yurish oyog'i joylashgan?",
                    "options": ["2 juft (4 ta)", "3 juft (6 ta)", "4 juft (8 ta)", "5 juft (10 ta)"],
                    "correct_index": 1,
                    "explanation": "Barcha hasharotlarda qat'iy 3 juft (6 ta) bo'g'imli oyoqlar bo'ladi."
                },
                {
                    "question": "Chala o'zgarish bilan rivojlanuvchi hasharotlarda qaysi bosqich bo'lmaydi?",
                    "options": ["Tuxum", "Lichinka", "G'umbak", "Imago (voyaga yetgan)"],
                    "correct_index": 2,
                    "explanation": "Chala o'zgarishda g'umbak bosqichi bo'lmaydi, lichinka to'g'ridan-to'g'ri voyaga yetgan hasharotga aylanadi."
                },
                {
                    "question": "Bo'g'imoyoqlilarning qon aylanish sistemasi qanday tuzilgan?",
                    "options": ["Berk", "Ochiq", "Qon aylanish sistemasi yo'q", "Faqat venalardan iborat"],
                    "correct_index": 1,
                    "explanation": "Bo'g'imoyoqlilarning qoni (gemolimfa) tomirlardan tana bo'shlig'iga quyiladi, ya'ni qon aylanish sistemasi ochiq."
                }
            ],
            "tags": ["bo'g'imoyoqlilar", "hasharotlar", "o'rgimchaklar", "metamorfoz", "ipak qurti", "7-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "bio-013",
            "slug": "umurtqali-hayvonlar-evolyutsiyasi-baliqlardan-sutemizuvchilargacha",
            "subject_id": "sub-10",
            "subject_name": "Zoologiya",
            "title": "Umurtqali hayvonlar: baliqlar, suvda va quruqda yashovchilar, sudralib yuruvchilar, qushlar va sutemizuvchilar",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Xordalilar tipi belgilari, yurak tuzilishi va qon aylanish doiralari evolyutsiyasi, sovuqqonli va issiqqonli hayvonlar xususiyatlarini bilish.",
            "theory": "Xordalilar tipi ichki o'q skelet — xorda (umurtqa pog'onasi), nerv naychasi va halqumida jabra yoriqlariga ega bo'lishi bilan ajralib turadi. Umurtqalilar evolyutsiyasi: 1) Baliqlar — 2 kamerali yurak (1 bo'lmacha, 1 qorincha), 1 ta qon aylanish doirasi, jabralar, suzgich pufagi, sovuqqonli; 2) Suvda va quruqda yashovchilar (amfibiyalar: baqa, triton) — 3 kamerali yurak, 2 ta qon aylanish doirasi, o'pka va teri orqali nafas oladi, sovuqqonli, ko'payishi suvda kechadi (itbaliq); 3) Sudralib yuruvchilar (reptiliyalar: kaltakesak, ilon, toshbaqa, timsoh) — 3 kamerali yurak (qorinchada chala to'siq bor, timsohda 4 kamerali), quruqlikda tuxum qo'yadi, quruq muguz tangachalar; 4) Qushlar — 4 kamerali yurak, to'liq ajralgan arterial va venoz qon, havo xaltalari bilan qo'sh nafas olish, issiqqonli (gomoyoterm); 5) Sutemizuvchilar — 4 kamerali yurak, chap aorta yoyi, diafragma, sut bezlari, tirik tug'ish, tana harorati doimiy (issiqqonli), bosh miya yarimsharlari po'stlog'i yuksak rivojlangan.",
            "examples": [
                {
                    "title": "Yurak evolyutsiyasini taqqoslash",
                    "problem": "Baliq, baqa, kaltakesak va qushning yurak kameralari sonini ko'rsating.",
                    "step_by_step": "Baliq — 2 kamerali (1 bo'lmacha, 1 qorincha);\nBaqa — 3 kamerali (2 bo'lmacha, 1 qorincha);\nKaltakesak — 3 kamerali (qorinchada chala to'siq);\nQush — 4 kamerali (2 bo'lmacha, 2 qorincha).",
                    "answer": "2, 3, 3 (chala to'siq bilan) va 4 kamerali"
                },
                {
                    "title": "Issiqqonlilikning afzalligi",
                    "problem": "Nima sababdan qushlar va sutemizuvchilar sovuq iqlim sharoitlarida ham faol hayot kechira oladi?",
                    "step_by_step": "Yurak 4 kamerali bo'lib to'qimalarga sof kislorodga boy arterial qon boradi, moddalar almashinuvi juda tez kechadi va tana harorati doimiy (issiqqonli) saqlanadi.",
                    "answer": "Doimiy tana harorati (issiqqonlilik) tufayli"
                }
            ],
            "exercise": "Qushlarning uchishga moslashgan 3 ta asosiy anatomik belgisini sanang.",
            "exercise_solution": "1) Oldingi oyoqlarning qanotga aylanishi va pat qoplami; 2) Suyaklarning ichi g'ovak va yengilligi, to'sh suyagi qirining (kil) borligi; 3) O'pka bilan bog'langan havo xaltachalari (qo'sh nafas olish).",
            "check_questions": [
                {
                    "question": "Qaysi hayvonlar sinfida tana harorati atrof-muhitga bog'liq bo'lmagan doimiy (issiqqonli) hisoblanadi?",
                    "options": ["Baliqlar va amfibiyalar", "Sudralib yuruvchilar va qushlar", "Qushlar va sutemizuvchilar", "Barcha umurtqalilar"],
                    "correct_index": 2,
                    "explanation": "Faqat qushlar va sutemizuvchilar 4 kamerali yurak va tez moddalar almashinuvi hisobiga issiqqonli hayvonlardir."
                },
                {
                    "question": "Baliqlarda harakat yo'nalishi va suv oqimini sezuvchi o'ziga xos organ nima?",
                    "options": ["Suzgich pufagi", "Yon chiziq organi", "Ko'krak suzgichlari", "Quloq pardasi"],
                    "correct_index": 1,
                    "explanation": "Yon chiziq organi suvning bosimi, oqim yo'nalishi va tebranishlarini sezuvchi organdir."
                },
                {
                    "question": "Ko'krak bo'shlig'ini qorin bo'shlig'idan ajratib turuvchi muskul to'sig'i — diafragma qaysi sinfga xos?",
                    "options": ["Qushlar", "Sudralib yuruvchilar", "Sutemizuvchilar", "Amfibiyalar"],
                    "correct_index": 2,
                    "explanation": "Diafragma faqat sutemizuvchilar sinfiga xos bo'lib, nafas olish mexanizmida faol qatnashadi."
                }
            ],
            "tags": ["zoologiya", "umurtqalilar", "baliqlar", "qushlar", "sutemizuvchilar", "evolyutsiya", "7-sinf"],
            "duration_minutes": 35
        },

        # ANATOMIYA (3)
        {
            "id": "bio-014",
            "slug": "odam-qon-aylanish-sistemasi-va-yurak",
            "subject_id": "sub-11",
            "subject_name": "Anatomiya",
            "title": "Odam qon aylanish sistemasi: yurak tuzilishi, qon tomirlari va qon guruhlari",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Yurak kameralari va klapanlari, katta va kichik qon aylanish doiralari, qon tarkibi (eritrotsit, leykotsit, trombotsit) hamda qon bosimini o'rganish.",
            "theory": "Odamning qon aylanish sistemasi berk bo'lib, yurak va qon tomirlaridan (arteriyalar, venalar, kapillarlar) iborat. Yurak 4 kamerali: o'ng bo'lmacha, o'ng qorincha, chap bo'lmacha, chap qorincha. Bo'lmacha va qorinchalar orasida tavaqali klapanlar, qorinchalardan chiquvchi tomirlar boshida yarimoysimon klapanlar joylashgan bo'lib, qonning faqat bir yo'nalishda oqishini ta'minlaydi. Katta qon aylanish doirasi: chap qorinchadan boshlanadi -> aorta -> butun tana a'zolari kapillarlari -> yuqori va pastki kovak venalar -> o'ng bo'lmachada tugaydi (to'qimalarga O2 va oziq yetkazadi). Kichik (o'pka) qon aylanish doirasi: o'ng qorinchadan boshlanadi -> o'pka arteriyasi -> o'pka alveolalari kapillarlari -> o'pka venalari -> chap bo'lmachada tugaydi (qon O2 bilan to'yinadi). Qon hujayralari: Eritrotsitlar (gemoglobin orqali gaz tashuvchi yadrosiz hujayralar), Leykotsitlar (immunitet va fagotsitoz), Trombotsitlar (qon ivishi).",
            "examples": [
                {
                    "title": "Qon aylanish doiralarini aniqlash",
                    "problem": "O'pka arteriyasida qanday qon oqadi: arterialmi yoki venozmi?",
                    "step_by_step": "O'pka arteriyasi o'ng qorinchadan o'pkaga boruvchi tomir bo'lib, unda kislorodga kambag'al venoz qon oqadi. O'pkadan qaytuvchi o'pka venalarida esa kislorodga boy arterial qon oqadi.",
                    "answer": "Venoz qon oqadi"
                },
                {
                    "title": "Normal qon bosimi",
                    "problem": "Sog'lom katta yoshli odamda normal arterial qon bosimi qanday me'yorga ega?",
                    "step_by_step": "Sistolik (yurak qisqarganda) bosim: 110-120 mm simob ustuni; Diastolik (yurak bo'shashganda) bosim: 70-80 mm simob ustuni (120/80 mm sim.ust.).",
                    "answer": "120/80 mm simob ustuni"
                }
            ],
            "exercise": "Qon ketish turlarini (kapillar, vena, arteriya) tashqi belgilariga qarab qanday farqlash mumkin?",
            "exercise_solution": "Kapillar — sekin sizib chiqadi; Vena — to'q qizil qon bir tekis oqadi; Arteriya — yorqin qizil rangli qon favvora kabi kuchli zarb bilan otilib chiqadi.",
            "check_questions": [
                {
                    "question": "Yurakning eng qalin va baquvvat muskul devoriga ega kamerasi qaysi?",
                    "options": ["O'ng bo'lmacha", "O'ng qorincha", "Chap bo'lmacha", "Chap qorincha"],
                    "correct_index": 3,
                    "explanation": "Chap qorincha qonni butun tanaga (katta doiraga) katta bosim bilan haydashi sababli eng baquvvat muskul devoriga ega."
                },
                {
                    "question": "Qon ivishida ishtirok etuvchi qon plastinkalari qanday ataladi?",
                    "options": ["Eritrotsitlar", "Leykotsitlar", "Trombotsitlar", "Limfotsitlar"],
                    "correct_index": 2,
                    "explanation": "Trombotsitlar qon tomiri shikastlanganda fibrin laxtasi hosil qilib qon ketishini to'xtatadi."
                },
                {
                    "question": "Katta qon aylanish doirasi yurakning qaysi kamerasidan boshlanadi?",
                    "options": ["O'ng qorincha", "Chap qorincha", "O'ng bo'lmacha", "Chap bo'lmacha"],
                    "correct_index": 1,
                    "explanation": "Katta qon aylanish doirasi chap qorinchadan aortaga chiqish bilan boshlanadi."
                }
            ],
            "tags": ["anatomiya", "yurak", "qon aylanish", "eritrotsit", "aorta", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "bio-015",
            "slug": "asab-sistemasi-va-oliy-asab-faoliyati",
            "subject_id": "sub-11",
            "subject_name": "Anatomiya",
            "title": "Odam asab sistemasi, bosh miya tuzilishi va refleks yoyi",
            "grade_level": "8-sinf",
            "difficulty": "Murakkab",
            "objective": "Neyron tuzilishi, markaziy va periferik asab sistemasi, bosh miya bo'limlari funksiyalari va I.P. Pavlovning shartli va shartsiz reflekslar ta'limotini bilish.",
            "theory": "Asab sistemasi organizm a'zolari faoliyatini boshqaradi va tashqi muhit bilan bog'laydi. Asab to'qimasining asosiy hujayrasi — neyron (tanasi, qisqa o'simtalari — dendritlar va bitta uzun o'simtasi — akson). Asab sistemasi: Markaziy (bosh miya va orqa miya) va Periferik (nervlar, nerv tugunlari, nerv chigallari). Bosh miya 5 bo'limdan iborat: 1) Uzunchoq miya (nafas, yurak, yutish, aksa urish kabi hayotiy markazlar); 2) Ko'prik; 3) Miyacha (harakat koordinatsiyasi va muvozanat); 4) O'rta miya (ko'rish va eshitish birlamchi markazlari, muskul tonusi); 5) Oraliq miya (gipotalamus — gomeostaz va moddalar almashinuvi markazi); 6) Katta yarimsharlar po'stlog'i (ong, tafakkur, xotira, so'zlashuv markazlari). Refleks — organizmning retseptorlar ta'sirlanishiga asab sistemasi orqali javob reaksiyasi. Refleks yoyi 5 zanjirdan iborat: retseptor -> sezuvchi nerv -> asab markazi -> harakatlantiruvchi nerv -> ishchi a'zo.",
            "examples": [
                {
                    "title": "Miyacha zararlanganda nima bo'ladi?",
                    "problem": "Miyachasi shikastlangan odamda qanday o'zgarishlar kuzatiladi?",
                    "step_by_step": "Miyacha harakatlar muvozanati va aniqligini boshqaradi. U zararlansa odam gandiraklab yuradi, harakatlar muvozanati buziladi (ataksiya) va nozik harakatlarni bajara olmaydi.",
                    "answer": "Muvozanat va harakat aniqligi yo'qoladi"
                },
                {
                    "title": "Shartli va shartsiz reflekslar",
                    "problem": "Ko'zga chang tushganda miltillash va limonni ko'rganda so'lak ajralishi qaysi refleks turiga kiradi?",
                    "step_by_step": "Ko'zni miltillatish — tug'ma, doimiy bo'lgani uchun shartsiz refleks; Limonni ko'rganda so'lak chiqishi esa shaxsiy hayotiy tajriba natijasida hosil bo'lgan shartli refleksdir.",
                    "answer": "Miltillash - shartsiz; Limonni ko'rganda - shartli refleks"
                }
            ],
            "exercise": "Tizza refleksi yoyining ketma-ket qismlarini yozing.",
            "exercise_solution": "1) Pay retseptori -> 2) Sezuvchi neyron -> 3) Orqa miya segmenti (markaz) -> 4) Harakatlantiruvchi neyron -> 5) Sonning to'rt boshli muskuli (ishchi a'zo).",
            "check_questions": [
                {
                    "question": "Harakatlarni muvofiqlashtirish va tana muvozanatini saqlash qaysi miya bo'limiga yuklatilgan?",
                    "options": ["Uzunchoq miya", "Miyacha", "O'rta miya", "Gipotalamus"],
                    "correct_index": 1,
                    "explanation": "Miyacha (cerebellum) fazodagi muvozanat va harakat aniqligi markazidir."
                },
                {
                    "question": "Nafas olish, yurak urishi va himoya reflekslari (yo'tal, aksirish) qaysi miyada joylashgan?",
                    "options": ["Uzunchoq miya", "Katta yarimsharlar", "Miyacha", "Orqa miya"],
                    "correct_index": 0,
                    "explanation": "Uzunchoq miyada hayot uchun muhim nafas, qon aylanish va himoya reflekslari markazlari joylashgan."
                },
                {
                    "question": "Neyrondan impulsni boshqa hujayraga uzatuvchi uzun o'simta nima deyiladi?",
                    "options": ["Dendrit", "Akson", "Sinaps", "Miyelin"],
                    "correct_index": 1,
                    "explanation": "Neyron tanasidan chiqadigan yagona uzun o'simta akson deyiladi."
                }
            ],
            "tags": ["anatomiya", "asab sistemasi", "bosh miya", "refleks", "neyron", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "bio-016",
            "slug": "ovqat-hazm-qilish-va-ayirish-sistemasi",
            "subject_id": "sub-11",
            "subject_name": "Anatomiya",
            "title": "Odam ovqat hazm qilish a'zolari va buyraklar orqali ayirish mexanizmi",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Hazm a'zolari ketma-ketligi, fermentlar ta'siri (ptialin, pepsin, tripsin, lipaza), so'rilish hamda buyrak nefronida birlamchi va ikkilamchi siydik hosil bo'lishini o'rganish.",
            "theory": "Ovqat hazm qilish sistemasi oziq moddalarni mexanik maydalash va fermentlar yordamida kimyoviy parchalab qonga so'rish vazifasini bajaradi. A'zolari: Og'iz bo'shlig'i (tishlar, til, so'lak bezlari — amilaza kraxmalni parchalaydi) -> Halqum -> Qizilo'ngach -> Oshqozon (oshqozon shirasi: xlorid kislota HCl va pepsin oqsillarni parchalaydi) -> O'n ikki barmoqli ichak (jigar o'ti yog'larni emulsiyalaydi, oshqozon osti bezi shirasi barcha moddalarni parchalaydi) -> Ingichka ichak (vorsinkalar orqali aminokislota va glyukoza qonga, yog' kislotalari limfaga so'riladi) -> Yo'g'on ichak (suv so'rilishi va najas shakllanishi). Ayirish sistemasi: Buyraklar, siydik yo'llari, siydik pufagi. Buyrakning strukturaviy birligi — nefron (har bir buyrakda 1 mln ta). Siydik hosil bo'lishi: 1) Buyrak koptokchasida filtrlash -> sutkasiga 150-180 litr birlamchi siydik (oqsil va qon hujayralarisiz plazma); 2) Nefron naychalarida reabsorbsiya (qayta so'rilish) -> sutkasiga 1.5-2 litr ikkilamchi (haqiqiy) siydik hosil bo'ladi.",
            "examples": [
                {
                    "title": "Oshqozon osti bezi (pankreas) roli",
                    "problem": "Nima sababdan oshqozon osti bezi aralash bez hisoblanadi?",
                    "step_by_step": "Tashqi sekretsiya sifatida u ingichka ichakka hazm shirasini (tripsin, lipaza, amilaza) chiqaradi; ichki sekretsiya sifatida esa bevosita qonga qand miqdorini boshqaruvchi insulin va glyukagon gormonlarini ajratadi.",
                    "answer": "Ham hazm fermentlari, ham gormonlar (insulin) ishlab chiqargani uchun"
                },
                {
                    "title": "Birlamchi va ikkilamchi siydik",
                    "problem": "Sog'lom odamning ikkilamchi siydigida glyukoza bormi?",
                    "step_by_step": "Birlamchi siydikdagi barcha glyukoza va kerakli tuzlar nefron naychalarida qayta qonga so'riladi (reabsorbsiya). Shuning uchun sog'lom odam siydigida glyukoza bo'lmaydi.",
                    "answer": "Bo'lmaydi (to'liq qayta so'riladi)"
                }
            ],
            "exercise": "Ingichka ichak shilliq qavatidagi mikroskopik vorsinkalarning asosiy vazifasi nima?",
            "exercise_solution": "Ichakning umumiy so'rish yuzasini yuzlab baravarga oshirib, parchalangan ozuqa moddalarni qon va limfa tomirlariga tezkor so'rilishini ta'minlaydi.",
            "check_questions": [
                {
                    "question": "Oqsilni oshqozonda parchalovchi asosiy ferment qaysi?",
                    "options": ["Amilaza", "Pepsin", "Lipaza", "Maltaza"],
                    "correct_index": 1,
                    "explanation": "Pepsin fermenti xlorid kislotali muhitda murakkab oqsillarni peptidlargacha parchalaydi."
                },
                {
                    "question": "Buyrakning strukturaviy va funksional birligi nima deb ataladi?",
                    "options": ["Neyron", "Nefron", "Alveola", "Kapsula"],
                    "correct_index": 1,
                    "explanation": "Buyrak nefroni filtrlovchi koptokcha va naychalardan iborat asosiy birlikdir."
                },
                {
                    "question": "Sog'lom odamda sutkasiga necha litr ikkilamchi siydik ajraladi?",
                    "options": ["0.5 litr", "1.5 - 2 litr", "10 litr", "150 litr"],
                    "correct_index": 1,
                    "explanation": "Kattalarda me'yorda sutkasiga taxminan 1.5 - 2 litr ikkilamchi siydik ajraladi."
                }
            ],
            "tags": ["anatomiya", "hazm qilish", "buyrak", "nefron", "siydik hosil bo'lishi", "8-sinf"],
            "duration_minutes": 30
        },

        # TABIIY FANLAR (2)
        {
            "id": "bio-017",
            "slug": "jonli-va-jonsiz-tabiat-suv-tuproq-va-havo",
            "subject_id": "sub-14",
            "subject_name": "Tabiiy fanlar",
            "title": "Atrofimizdagi olam: jonli va jonsiz tabiat, suv, tuproq va havo",
            "grade_level": "3-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Jonli va jonsiz tabiat farqi, suvning 3 xil holati va tabiatda aylanishi, havo tarkibi va tuproq xossalarini tushunish.",
            "theory": "Tabiat — bizni o'rab turgan barcha borliqdir. Tabiat ikkiga bo'linadi: 1) Jonsiz tabiat — Quyosh, yulduzlar, havo, suv, toshlar, tog'lar, tuproq; 2) Jonli tabiat — o'simliklar, qo'ziqorinlar, hayvonlar va odamlar. Jonli tabiat vakillari nafas oladi, oziqlanadi, o'sadi, ko'payadi va nobud bo'ladi. Jonli tabiat jonsiz tabiat bilan uzviy bog'langan: suvsiz, havosiz va quyosh nurisiz hayot bo'lmaydi. Suv tabiatda 3 xil holatda bo'ladi: qattiq (muz), suyuq (suv) va gaz (suv bug'i). Quyosh suv havzalarini isitganda suv bug'lanadi, yuqorida sovib bulutlarga aylanadi va yomg'ir hamda qor bo'lib yerga qaytadi — bu tabiatda suvning doimiy aylanishi deyiladi. Havo — gazlar aralashmasi (asosan azot va kislorod).",
            "examples": [
                {
                    "title": "Tabiat hodisalarini ajratish",
                    "problem": "Quyidagilardan qaysilari jonli, qaysilari jonsiz tabiatga kiradi: archa, daryo toshi, qaldirg'och, bulut, quyon?",
                    "step_by_step": "Jonli tabiat: archa (o'simlik), qaldirg'och (qush), quyon (hayvon).\nJonsiz tabiat: daryo toshi, bulut.",
                    "answer": "Jonli: archa, qaldirg'och, quyon; Jonsiz: tosh, bulut"
                },
                {
                    "title": "Suvning uch holati",
                    "problem": "Qishda ko'l muzlaganda, choynak qaynaganda va yomg'ir yoqqanda suv qaysi holatlarda bo'ladi?",
                    "step_by_step": "Muzlaganda — qattiq holat; Choynak bug'i — gazsimon holat; Yomg'ir tomchilari — suyuq holat.",
                    "answer": "Qattiq, gaz va suyuq"
                }
            ],
            "exercise": "Tuproq nima va uning eng muhim xossasi qaysi?",
            "exercise_solution": "Tuproq — yer yuzasining unumdor yuqori qatlami bo'lib, uning eng muhim xossasi unumdorlik (chirindi/gumus miqdori) hisoblanadi.",
            "check_questions": [
                {
                    "question": "Jonli organizmlarning jonsiz tabiatdan asosiy farqi nima?",
                    "options": ["Og'irlikka ega ekanligi", "Nafas olishi, oziqlanishi va ko'payishi", "Rangli bo'lishi", "Qattiq bo'lishi"],
                    "correct_index": 1,
                    "explanation": "Jonli mavjudotlar nafas olish, oziqlanish, o'sish va nasl qoldirish xususiyatlariga ega."
                },
                {
                    "question": "Nafas olish uchun barcha tirik mavjudotlarga havoning qaysi gazi zarur?",
                    "options": ["Karbonat angidrid", "Kislorod", "Azot", "Vodorod"],
                    "correct_index": 1,
                    "explanation": "Kislorod nafas olish jarayonida hayotiy energiya hosil qilish uchun zarurdir."
                },
                {
                    "question": "Suv necha gradus issiqlikda qaynaydi?",
                    "options": ["50 °C", "80 °C", "100 °C", "0 °C"],
                    "correct_index": 2,
                    "explanation": "Oddiy atmosfera bosimida toza suv 100 °C da qaynaydi va bug'ga aylanadi."
                }
            ],
            "tags": ["tabiiy fanlar", "jonli tabiat", "jonsiz tabiat", "suv aylanishi", "3-sinf"],
            "duration_minutes": 20
        },
        {
            "id": "bio-018",
            "slug": "fasllar-almashinuvi-va-ekologik-savodxonlik",
            "subject_id": "sub-14",
            "subject_name": "Tabiiy fanlar",
            "title": "Yil fasllari almashinuvi, tabiatni asrash va ekologik madaniyat",
            "grade_level": "4-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Yil fasllarining paydo bo'lish sabablari (Yerning o'z o'qi va Quyosh atrofida aylanishi), o'simlik va hayvonlarning mavsumiy o'zgarishlari hamda atrof-muhitni muhofaza qilish.",
            "theory": "Yer sharida to'rtta fasl bor: bahor, yoz, kuz va qish. Fasllar almashinuvining asosiy sababi — Yer o'qining o'z orbital tekisligiga nisbatan og'maligi (66.5°) va Yerning Quyosh atrofida yillik aylanishidir. Yer Quyoshga qaysi yarimshari bilan og'gan bo'lsa, o'sha yerda yoz, qarama-qarshi yarimsharda qish bo'ladi. Yil fasllariga qarab o'simlik va hayvonot olamida moslashuvlar sodir bo'ladi: bahorda daraxtlar kurtak yozadi, qushlar qaytadi; kuzda barglar to'kiladi, qushlar issiq o'lkalarga uchib ketadi; qishda ayrim hayvonlar qishki uyquga ketadi. Inson tabiatning ajralmas qismidir. Tabiatni asrash: daraxtlarni kesmaslik, suvni isrof qilmaslik, havoni ifoslamaslik va chiqindilarni saralash har bir insonning burchidir.",
            "examples": [
                {
                    "title": "Fasllar almashinuvi sababi",
                    "problem": "Nega yoz faslida kunlar uzun va iliq, qishda esa qisqa va sovuq bo'ladi?",
                    "step_by_step": "Yozda biz yashaydigan Shimoliy yarimshar Quyosh tomonga og'gan bo'ladi, quyosh nurlari tikroq tushadi va ko'proq isitadi, kunlar uzun bo'ladi. Qishda esa quyosh nurlari yotiq tushadi va kamroq isitadi.",
                    "answer": "Yer o'qining og'maligi va nurlarning tushish burchagi sababli"
                },
                {
                    "title": "Chiqindilarni saralash",
                    "problem": "Nima uchun chiqindilarni plastik, qog'oz va shishaga ajratib yig'ish kerak?",
                    "step_by_step": "Saralangan chiqindilar qayta ishlanadi (retsikl): o'rmonlar kesilishdan, yer esa yuzlab yillar davomida parchalanmaydigan plastikdan saqlanadi.",
                    "answer": "Qayta ishlash va tabiatni toza saqlash uchun"
                }
            ],
            "exercise": "Kuzda daraxt barglari nega sarg'ayadi va qizaradi?",
            "exercise_solution": "Kuzda havo sovib, yorug'lik kamayishi bilan bargdagi yashil pigment — xlorofill parchalanadi va sariq (ksantofill) hamda qizil (karotin) pigmentlar yuzaga chiqadi.",
            "check_questions": [
                {
                    "question": "Yer Quyosh atrofini to'liq necha kunda aylanib chiqadi?",
                    "options": ["24 soatda", "30 kunda", "365 kun 6 soatda", "100 kunda"],
                    "correct_index": 2,
                    "explanation": "Yer Quyosh atrofini 1 yilda (365 kun 6 soatda) aylanadi."
                },
                {
                    "question": "Qish faslida qishki uyquga ketadigan hayvon qaysi?",
                    "options": ["Bo'ri", "Qo'ng'ir ayiq", "Tulki", "Quyon"],
                    "correct_index": 1,
                    "explanation": "Qo'ng'ir ayiq, tipratikan va bo'rsiq qishda energiya tejash uchun qishki uyquga yotadi."
                },
                {
                    "question": "Plastik idish tabiatda chirishi uchun taxminan necha yil kerak bo'ladi?",
                    "options": ["1 yil", "5 yil", "10 yil", "100-400 yil"],
                    "correct_index": 3,
                    "explanation": "Plastik tabiatda yuzlab yillar davomida chirimasdan atrof-muhitga jiddiy zarar yetkazadi."
                }
            ],
            "tags": ["tabiiy fanlar", "fasllar", "ekologiya", "chiqindi saralash", "4-sinf"],
            "duration_minutes": 25
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_biology_nature_materials()
    print(f"Generated {len(mats)} Biology/Nature materials.")
