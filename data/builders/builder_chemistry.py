# -*- coding: utf-8 -*-
"""
Builder for Kimyo (12 materials: chm-001 to chm-012)
- sub-07: Kimyo
"""

def get_chemistry_materials():
    materials = [
        {
            "id": "chm-001",
            "slug": "moddalar-aralashmalar-va-tozalash-usullari",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Sof moddalar, aralashmalar va ularni ajratish usullari",
            "grade_level": "7-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Sof modda va aralashma farqini bilish, bir jinsli (gomogen) va har xil jinsli (geterogen) aralashmalarni ajratish usullarini amalda qo'llash.",
            "theory": "Muayyan doimiy fizik xossalarga (zichlik, erish va qaynash temperaturasi) ega bo'lgan moddalar sof moddalar deyiladi. Ikki yoki undan ortiq moddalarning o'zaro kimyoviy birikmasdan hosil qilgan sistemasi aralashma deyiladi. Geterogen aralashmalarda modda zarralarini mikroskop orqali ko'rish mumkin (masalan, qum va suv, loyqa suv). Ularni tindirish, filtrlash, magnit bilan ta'sir etish usullari bilan ajratiladi. Gomogen aralashmalarda modda zarralari molekulyar darajada aralashgan bo'ladi (shakarli suv, spirt va suv). Ularni bug'latish, haydash (distillash) va xromatografiya usullari orqali ajratiladi.",
            "examples": [
                {
                    "title": "Tuz va qum aralashmasini ajratish",
                    "problem": "Osh tuzi va daryo qumi aralashmasini qanday qilib toza qismlarga ajratish mumkin?",
                    "step_by_step": "1) Aralashmaga suv quyamiz: osh tuzi eriydi, qum erimaydi.\n2) Eritmani filtr qog'ozidan o'tkazamiz (filtrlash): qum filtrda qoladi.\n3) Tuzli suvni qizdirib suvni bug'latamiz (bug'latish): kristall osh tuzi idish tubida qoladi.",
                    "answer": "Eritish, filtrlash va bug'latish ketma-ketligi"
                },
                {
                    "title": "Suv va spirt aralashmasi",
                    "problem": "Suv va etil spirtining gomogen aralashmasini ajratish usuli qaysi?",
                    "step_by_step": "Spirt 78 °C da, suv 100 °C da qaynaydi. Har xil qaynash temperaturasiga asoslangan haydash (distillash) usuli qo'llaniladi.",
                    "answer": "Distillash (haydash)"
                }
            ],
            "exercise": "Temir qirindisi va oltingugurt kukunidan iborat quruq aralashmani qanday qilib oson ajratish mumkin?",
            "exercise_solution": "Aralashmaga magnit yaqinlashtiriladi: magnit temir qirindilarini o'ziga tortadi, oltingugurt kukuni qoladi.",
            "check_questions": [
                {
                    "question": "Quyidagilardan qaysi biri sof modda hisoblanadi?",
                    "options": ["Dengiz suvi", "Distillangan suv", "Havo", "Sut"],
                    "correct_index": 1,
                    "explanation": "Distillangan suv tarkibida erigan tuzlar bo'lmagan toza H2O sof moddadir."
                },
                {
                    "question": "Qattiq erimaydigan moddani suyuqlikdan ajratish usuli nima?",
                    "options": ["Distillash", "Filtrlash", "Xromatografiya", "Eritish"],
                    "correct_index": 1,
                    "explanation": "Erimaydigan qattiq zarralarni suyuqlikdan ajratish filtrlash deyiladi."
                },
                {
                    "question": "Neftdan benzin, kerosin va dizel yoqilg'isini ajratish qaysi usulga asoslangan?",
                    "options": ["Magnitlash", "Fraksiyali haydash (distillash)", "Tindirish", "Muzlatish"],
                    "correct_index": 1,
                    "explanation": "Uglevodorodlarning qaynash temperaturalari farqiga asoslangan fraksiyali haydash ishlatiladi."
                }
            ],
            "tags": ["kimyo", "sof modda", "aralashma", "filtrlash", "7-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "chm-002",
            "slug": "atom-tuzilishi-va-davriy-qonun",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Atom tuzilishi va D.I. Mendeleyev davriy qonuni",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Atomning elektron konfiguratsiyasi, proton, neytron, davr va guruhlar bo'yicha elementlar xossalarining davriy o'zgarishini tushunish.",
            "theory": "Atom musbat zaryadli yadro va manfiy zaryadli elektron qobiqdan iborat. Yadro zaryadi Mendeleyev davriy jadvalidagi tartib raqamiga (Z) teng. Elektronlar energetik pog'onalarda (qavatlarda) s, p, d, f orbitallar bo'ylab joylashadi (maksimal elektronlar soni N = 2n^2). D.I. Mendeleyev davriy qonuni: Kimyoviy elementlarning va ular hosil qilgan oddiy hamda murakkab moddalarning xossalari elementlar atom yadrosi zaryadiga davriy ravishda bog'liqdir. Davr bo'yicha chapdan o'ngga: atom radiusi kichrayadi, ionlanish energiyasi va elektromanfiylik ortadi, metallik xossasi susayib, nometallik kuchayadi. Guruh bo'yicha yuqoridan pastga: atom radiusi kattalashadi, metallik xossalari kuchayadi.",
            "examples": [
                {
                    "title": "Elektron formulani yozish",
                    "problem": "Natriy (11_Na) atomining elektron konfiguratsiyasini yozing.",
                    "step_by_step": "1) Z = 11, demak 11 ta elektron bor.\n2) 1-pog'ona: 1s^2 (2 ta).\n3) 2-pog'ona: 2s^2 2p^6 (8 ta).\n4) 3-pog'ona: 3s^1 (1 ta).\n5) To'liq konfiguratsiya: 1s^2 2s^2 2p^6 3s^1.",
                    "answer": "1s^2 2s^2 2p^6 3s^1"
                },
                {
                    "title": "Valent elektronlarni aniqlash",
                    "problem": "Xlor (17_Cl) atomining tashqi pog'onasida nechta elektron bor?",
                    "step_by_step": "1) Elektron formula: 1s^2 2s^2 2p^6 3s^2 3p^5.\n2) Tashqi pog'ona (n=3): 3s^2 3p^5 => 2 + 5 = 7 ta valent elektron.",
                    "answer": "7 ta elektron"
                }
            ],
            "exercise": "Fosfor (15_P) atomining elektron formulasini tuzing va toq elektronlar sonini ko'rsating.",
            "exercise_solution": "1s^2 2s^2 2p^6 3s^2 3p^3. 3p orbitalda 3 ta toq elektron mavjud.",
            "check_questions": [
                {
                    "question": "Elementning tartib raqami nimaga teng?",
                    "options": ["Neytronlar soniga", "Yadrodagi protonlar soniga", "Nisbiy atom massasiga", "Valetlikka"],
                    "correct_index": 1,
                    "explanation": "Tartib raqami yadro zaryadiga, ya'ni protonlar soniga teng."
                },
                {
                    "question": "Davriy jadvalda eng yuqori elektromanfiylikka ega element qaysi?",
                    "options": ["Kislorod", "Xlor", "Ftor", "Fransiy"],
                    "correct_index": 2,
                    "explanation": "Ftor (F) elementi eng kuchli elektromanfiy element hisoblanadi (Poling bo'yicha 4.0)."
                },
                {
                    "question": "3-davr elementlarining atomlarida nechta energetik qavat mavjud?",
                    "options": ["1 ta", "2 ta", "3 ta", "4 ta"],
                    "correct_index": 2,
                    "explanation": "Element joylashgan davr raqami atomdagi elektron qavatlar soniga teng bo'ladi."
                }
            ],
            "tags": ["davriy jadval", "mendeleyev", "atom tuzilishi", "elektron", "7-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "chm-003",
            "slug": "kimyoviy-boglanish-turlari",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Kimyoviy bog'lanish turlari: kovalent, ion, metall va vodorod bog'lanish",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Qutbsiz va qutbli kovalent bog'lanish, ion bog'lanish, metall bog'lanish hamda moddalarning kristall panjara turlarini o'rganish.",
            "theory": "Molekulada atomlarni bir-biriga tutashtiruvchi o'zaro ta'sir kimyoviy bog'lanish deyiladi. Turlari: 1) Kovalent bog'lanish — umumiy elektron juftlari hosil bo'lishi hisobiga vujudga keladi. Agar elektromanfiyligi bir xil nometallar orasida bo'lsa qutbsiz kovalent (H2, O2, N2, Cl2), har xil elektromanfiy nometallar orasida bo'lsa qutbli kovalent (HCl, H2O, NH3) deyiladi; 2) Ion bog'lanish — elektromanfiyligi keskin farq qiluvchi metall va nometall atomlari orasida elektron o'tishi natijasida hosil bo'lgan qarama-qarshi ionlarning elektrostatik tortishuvi (NaCl, CaCl2, K2O); 3) Metall bog'lanish — metall kristall panjarasida musbat ionlar va erkin harakatlanuvchi 'elektron gazi' orasidagi bog'lanish; 4) Vodorod bog'lanish — kuchli elektromanfiy atomlar (F, O, N) bilan bog'langan vodorod atomi va boshqa molekuladagi elektromanfiy atom orasidagi bog'lanish.",
            "examples": [
                {
                    "title": "Bog'lanish turini aniqlash",
                    "problem": "O2, H2O, NaCl va Fe moddalarida kimyoviy bog'lanish turlarini aniqlang.",
                    "step_by_step": "1) O2: bir xil nometallar — qutbsiz kovalent.\n2) H2O: har xil nometallar — qutbli kovalent.\n3) NaCl: metall (Na) va nometall (Cl) — ion bog'lanish.\n4) Fe: temir atomlari va erkin elektronlar — metall bog'lanish.",
                    "answer": "O2 - qutbsiz kovalent, H2O - qutbli kovalent, NaCl - ion, Fe - metall"
                },
                {
                    "title": "Ammiak molekulasida bog'lanish",
                    "problem": "NH3 molekulasida nechta va qanday kovalent bog' bor?",
                    "step_by_step": "Azot atomi 3 ta vodorod atomi bilan 3 ta umumiy elektron jufti hosil qiladi: 3 ta qutbli kovalent sigma-bog'.",
                    "answer": "3 ta qutbli kovalent bog'"
                }
            ],
            "exercise": "HF (vodorod ftorid) va N2 (azot) molekulalaridagi bog'lanish turini aniqlang.",
            "exercise_solution": "HF da qutbli kovalent va molekulalararo vodorod bog'lanish; N2 da kuchli uch karrali qutbsiz kovalent bog'lanish.",
            "check_questions": [
                {
                    "question": "NaCl kristall panjarasi qanday bog'lanish hisobiga hosil bo'ladi?",
                    "options": ["Kovalent qutbsiz", "Ion bog'lanish", "Metall bog'lanish", "Vodorod bog'lanish"],
                    "correct_index": 1,
                    "explanation": "Na+ va Cl- ionlari orasidagi elektrostatik tortishuv ion bog'lanishdir."
                },
                {
                    "question": "Azot (N2) molekulasida atomlar orasida nechta kovalent bog' bor?",
                    "options": ["1 ta", "2 ta", "3 ta", "4 ta"],
                    "correct_index": 2,
                    "explanation": "N2 molekulasida azot atomlari o'zaro 3 ta umumiy elektron jufti orqali mustahkam uch karrali bog' hosil qiladi."
                },
                {
                    "question": "Suvning o'ziga xos yuqori qaynash temperaturasiga sabab nima?",
                    "options": ["Kovalent bog'", "Molekulalararo vodorod bog'lanish", "Ion bog'", "Kichik molekulyar massa"],
                    "correct_index": 1,
                    "explanation": "Suv molekulalari orasidagi vodorod bog'lanishlar uning qaynash haroratini sezilarli oshiradi."
                }
            ],
            "tags": ["kimyoviy bog'lanish", "kovalent", "ion bog'", "vodorod bog'", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "chm-004",
            "slug": "modda-miqdori-mol-va-avogadro-qonuni",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Modda miqdori, molyar massa va Avogadro qonuni",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Mol, molyar massa (M), Avogadro soni (N_A = 6.02*10^23) va gazlarning molyar hajmi (V_m = 22.4 l/mol) bo'yicha stexiometrik hisoblashlarni bajarish.",
            "theory": "Modda miqdori (n) deb berilgan namunadagi tarkibiy zarrachalar (atom, molekula, ion) sonini ifodalovchi fizik kattalikka aytiladi (birligi mol). 1 mol har qanday moddada 0.012 kg uglerod-12 dagi atomlar sonicha zarra bo'ladi: N_A = 6.02 * 10^23 mol^(-1) (Avogadro soni). Asosiy formulalar: 1) n = N / N_A; 2) n = m / M (m - massa, M - molyar massa, g/mol); 3) Normal sharoitda (n.sh.: T = 0 °C, P = 101.3 kPa) har qanday gazning 1 moli 22.4 litr hajmni egallaydi (V_m = 22.4 l/mol): n = V / V_m.",
            "examples": [
                {
                    "title": "Molekulalar sonini va massani hisoblash",
                    "problem": "88 gramm karbonat angidrid (CO2) necha mol va uning tarkibida nechta molekula bor?",
                    "step_by_step": "1) M(CO2) = 12 + 2 * 16 = 44 g/mol.\n2) n = m / M = 88 g / 44 g/mol = 2 mol.\n3) N = n * N_A = 2 * 6.02 * 10^23 = 1.204 * 10^24 ta molekula.",
                    "answer": "2 mol, 1.204 * 10^24 ta molekula"
                },
                {
                    "title": "Gaz hajmini topish",
                    "problem": "Normal sharoitda 64 gramm kislorod (O2) qanday hajmni (litrda) egallaydi?",
                    "step_by_step": "1) M(O2) = 32 g/mol.\n2) n = 64 / 32 = 2 mol.\n3) V = n * V_m = 2 mol * 22.4 l/mol = 44.8 litr.",
                    "answer": "44.8 litr"
                }
            ],
            "exercise": "Normal sharoitda 11.2 litr metan (CH4) gazining massasini toping.",
            "exercise_solution": "n = 11.2 / 22.4 = 0.5 mol. M(CH4) = 12 + 4 = 16 g/mol. m = 0.5 * 16 = 8 gramm.",
            "check_questions": [
                {
                    "question": "Avogadro doimiysi N_A ning son qiymati nechaga teng?",
                    "options": ["6.02 * 10^21", "6.02 * 10^23", "3 * 10^8", "1.6 * 10^(-19)"],
                    "correct_index": 1,
                    "explanation": "Avogadro soni 1 moldagi zarrachalar soni bo'lib, 6.02 * 10^23 mol^(-1) ga teng."
                },
                {
                    "question": "Normal sharoitda 1 mol ixtiyoriy ideal gaz qanday hajmni egallaydi?",
                    "options": ["11.2 litr", "22.4 litr", "44.8 litr", "1.0 litr"],
                    "correct_index": 1,
                    "explanation": "Molyar hajm V_m = 22.4 l/mol normal sharoitdagi o'zgarmas kattalikdir."
                },
                {
                    "question": "1 mol suv (H2O) massasi necha gramm?",
                    "options": ["10 g", "16 g", "18 g", "20 g"],
                    "correct_index": 2,
                    "explanation": "M(H2O) = 2*1 + 16 = 18 g/mol."
                }
            ],
            "tags": ["mol", "avogadro qonuni", "molyar massa", "stexiometriya", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "chm-005",
            "slug": "anorganik-birikmalarning-asosiy-sinflari",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Anorganik moddalarning asosiy sinflari: oksidlar, asoslar, kislotalar va tuzlar",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Oksidlar, asoslar, kislotalar va tuzlarning tasnifi, olinishi, kimyoviy xossalari va genetik bog'lanishini o'rganish.",
            "theory": "Anorganik moddalar 4 ta asosiy sinfga bo'linadi: 1) Oksidlar — elementning kislorod bilan birikmasi (asosli: CaO, Na2O; kislotali: SO3, CO2; amfoter: ZnO, Al2O3); 2) Asoslar — metall atomi va gidroksid guruhlaridan iborat birikmalar (Me(OH)n). Suvda eriydigan asoslar ishqorlar deyiladi (NaOH, KOH, Ca(OH)2); 3) Kislotalar — vodorod atomi va kislota qoldig'idan iborat moddalar (HCl, H2SO4, HNO3). Lakmusni qizil rangga bo'yaydi; 4) Tuzlar — metall atomi va kislota qoldig'idan iborat murakkab moddalar (o'rta: NaCl; nordon: NaHCO3; asosli: Cu(OH)Cl). Neytrallanish reaksiyasi: Kislota + Asos = Tuz + Suv (masalan: HCl + NaOH = NaCl + H2O).",
            "examples": [
                {
                    "title": "Neytrallanish reaksiyasi",
                    "problem": "Sulfat kislota bilan kaliy gidroksid reaksiyasi tenglamasini yozing va tenglashtiring.",
                    "step_by_step": "1) Reagentlar: H2SO4 + KOH.\n2) Tuz va suv hosil bo'ladi: K2SO4 + H2O.\n3) Koeffitsiyentlarni tenglashtiramiz: H2SO4 + 2KOH = K2SO4 + 2H2O.",
                    "answer": "H2SO4 + 2KOH = K2SO4 + 2H2O"
                },
                {
                    "title": "Kislotali va asosli oksidlarning o'zaro ta'siri",
                    "problem": "Kalsiy oksid (CaO) va uglerod (IV) oksid (CO2) birikkanda nima hosil bo'ladi?",
                    "step_by_step": "Asosli oksid + Kislotali oksid = Tuz: CaO + CO2 = CaCO3 (kalsiy karbonat / ohaktosh).",
                    "answer": "CaCO3"
                }
            ],
            "exercise": "Rux gidroksid (Zn(OH)2) amfoter xossaga ega ekanligini kislota va ishqor bilan reaksiyalari misolida ko'rsating.",
            "exercise_solution": "1) Zn(OH)2 + 2HCl = ZnCl2 + 2H2O (asos sifatida); 2) Zn(OH)2 + 2NaOH = Na2[Zn(OH)4] (kislota sifatida).",
            "check_questions": [
                {
                    "question": "Ishqoriy muhitda fenolftalein indikatori qanday rangga kiradi?",
                    "options": ["Qizil", "Ko'k", "Malina rang (to'q pushti)", "Sariq"],
                    "correct_index": 2,
                    "explanation": "Fenolftalein faqat ishqoriy muhitda yorqin malina (pushti) rangga kiradi."
                },
                {
                    "question": "Quyidagi oksidlardan qaysi biri kislotali oksid?",
                    "options": ["Na2O", "CuO", "SO3", "BaO"],
                    "correct_index": 2,
                    "explanation": "SO3 oltingugurt (VI) oksidi bo'lib, suv bilan birikkanda sulfat kislota (H2SO4) hosil qiluvchi kislotali oksiddir."
                },
                {
                    "question": "Osh sodasining kimyoviy formulasi qaysi?",
                    "options": ["NaCl", "Na2CO3", "NaHCO3", "NaOH"],
                    "correct_index": 2,
                    "explanation": "Osh sodasi natriy gidrokarbonat bo'lib, NaHCO3 formulaga ega nordon tuzdir."
                }
            ],
            "tags": ["oksidlar", "asoslar", "kislotalar", "tuzlar", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "chm-006",
            "slug": "kimyoviy-reaksiyalar-tezligi-va-muvozanat",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Kimyoviy reaksiya tezligi va kimyoviy muvozanat (Le Shatelye prinsipi)",
            "grade_level": "9-sinf",
            "difficulty": "Murakkab",
            "objective": "Reaksiya tezligiga ta'sir etuvchi omillar (konsentratsiya, temperatura, katalizator) va Le Shatelye prinsipi bo'yicha muvozanat siljishini tushuntirish.",
            "theory": "Vaqt birligi ichida moddalar konsentratsiyasining o'zgarishi kimyoviy reaksiya tezligi deyiladi: v = +- Delta_C / Delta_t. Ta'sir etuvchi massalar qonuni: aA + bB = C reaksiyasi uchun v = k * [A]^a * [B]^b. Vant-Goff qoidasi: Temperatura har 10 °C ga ko'tarilganda reaksiya tezligi 2-4 marta ortadi: v_2 = v_1 * gamma^((T_2 - T_1)/10). Qaytar reaksiyalarda to'g'ri va teskari reaksiyalar tezligi tenglashgan holat kimyoviy muvozanat deyiladi. Le Shatelye prinsipi: Agar muvozanatda turgan sistemaga tashqi ta'sir (konsentratsiya, temperatura, bosim) ko'rsatilsa, muvozanat shu ta'sirni kamaytiradigan tomonga siljiydi. Bosim ortganda gazlar hajmi kamayadigan tomonga siljiydi.",
            "examples": [
                {
                    "title": "Le Shatelye prinsipini qo'llash",
                    "problem": "N2(g) + 3H2(g) <=> 2NH3(g) + Q (ammiak sintezi) reaksiyasida muvozanatni ammiak hosil bo'lish tomonga siljitish uchun nima qilish kerak?",
                    "step_by_step": "1) Reaksiya ekzotermik (+Q): haroratni pasaytirish muvozanatni o'ngga siljitadi.\n2) Chapda 1+3=4 hajm gaz, o'ngda 2 hajm gaz: bosimni oshirish muvozanatni hajm kam tomonga (o'ngga) siljitadi.\n3) N2 yoki H2 konsentratsiyasini oshirish ham muvozanatni o'ngga siljitadi.",
                    "answer": "Haroratni pasaytirish, bosimni oshirish va reagentlar qo'shish"
                },
                {
                    "title": "Vant-Goff qoidasi",
                    "problem": "Reaksiyaning harorat koeffitsiyenti gamma = 3 bo'lsa, harorat 20 °C dan 50 °C gacha ko'tarilganda tezlik necha marta ortadi?",
                    "step_by_step": "Delta_T = 50 - 20 = 30 °C. Delta_T / 10 = 3. Tezlik ortishi: gamma^3 = 3^3 = 27 marta.",
                    "answer": "27 marta"
                }
            ],
            "exercise": "Reaksiyada katalizatorning vazifasi nimadan iborat?",
            "exercise_solution": "Katalizator reaksiyaning aktivlanish energiyasini pasaytirib uning tezligini oshiradi, lekin reaksiya oxirida sarflanmaydi va muvozanat holatini o'zgartirmaydi.",
            "check_questions": [
                {
                    "question": "Gazlar ishtirokidagi reaksiyada bosim oshirilganda muvozanat qaysi tomonga siljiydi?",
                    "options": ["Gaz hajmi ko'p tomonga", "Gaz hajmi kam tomonga", "Muvozanat o'zgarmaydi", "Endotermik tomonga"],
                    "correct_index": 1,
                    "explanation": "Le Shatelye prinsipiga ko'ra bosim ortganda sistema bosimni kamaytirish uchun gaz molekulalari soni (hajmi) kam bo'lgan tomonga intiladi."
                },
                {
                    "question": "Ekzotermik reaksiyada harorat ko'tarilsa, muvozanat qayerga siljiydi?",
                    "options": ["To'g'ri reaksiya tomonga", "Teskari reaksiya (boshlang'ich moddalar) tomonga", "O'zgarmaydi", "Nolga tenglashadi"],
                    "correct_index": 1,
                    "explanation": "Ekzotermik reaksiyada issiqlik ajraladi (+Q), harorat oshirilsa muvozanat issiqlik yutiladigan (teskari) tomonga siljiydi."
                },
                {
                    "question": "Reaksiya tezligining birligi qaysi?",
                    "options": ["mol / litr", "mol / (litr * sekund)", "g / mol", "litr / sekund"],
                    "correct_index": 1,
                    "explanation": "Tezlik konsentratsiya o'zgarishining vaqtga nisbati: mol / (l * s)."
                }
            ],
            "tags": ["reaksiya tezligi", "kimyoviy muvozanat", "le shatelye", "katalizator", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "chm-007",
            "slug": "elektrolitik-dissotsiatsiya-va-gidroliz",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Elektrolitik dissotsiatsiya, ion almashinish reaksiyalari va tuzlar gidrolizi",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Eritmalarda ionlarga ajralish (dissotsiatsiya), qisqargan ionli tenglamalarni tuzish va tuzlar gidrolizida muhitni (pH) aniqlash.",
            "theory": "Moddalarning suvda erishi yoki suyuqlanishi natijasida ionlarga ajralishi elektrolitik dissotsiatsiya deyiladi. Kuchli elektrolitlar suvda to'liq ionlarga ajraladi (kuchli kislotalar, ishqorlar, deyarli barcha eriydigan tuzlar). Kuchsiz elektrolitlar qisman ajraladi (sirka kislota, H2S, suv). Ion almashinish reaksiyalari faqat 3 ta holda oxirigacha boradi: 1) Cho'kma tushsa (BaSO4, AgCl); 2) Gaz ajralsa (CO2, SO2, H2S); 3) Kuchsiz elektrolit (suv H2O) hosil bo'lsa. Tuzlar gidrolizi — tuz ionlarining suv bilan ta'sirlashib kuchsiz elektrolit hosil qilishi. Kuchli asos va kuchsiz kislota tuzi (Na2CO3) gidrolizlanganda asosiy muhit (pH > 7); Kuchsiz asos va kuchli kislota tuzi (NH4Cl) gidrolizlanganda kislotali muhit (pH < 7) hosil bo'ladi.",
            "examples": [
                {
                    "title": "Qisqargan ionli tenglama tuzish",
                    "problem": "Bariy xlorid va natriy sulfat eritmalarining o'zaro ta'siri to'liq va qisqargan ionli tenglamalarini yozing.",
                    "step_by_step": "1) Molekulyar: BaCl2 + Na2SO4 = BaSO4 v (oq cho'kma) + 2NaCl.\n2) To'liq ionli: Ba(2+) + 2Cl(-) + 2Na(+) + SO4(2-) = BaSO4 v + 2Na(+) + 2Cl(-).\n3) Qisqargan ionli: Ba(2+) + SO4(2-) = BaSO4 v.",
                    "answer": "Ba(2+) + SO4(2-) = BaSO4 v"
                },
                {
                    "title": "Tuz gidrolizida muhitni aniqlash",
                    "problem": "AlCl3 tuzining suvli eritmasida lakmus qog'ozi qanday rangga kiradi?",
                    "step_by_step": "AlCl3 - kuchsiz asos Al(OH)3 va kuchli kislota HCl dan hosil bo'lgan tuz. Kation bo'yicha gidrolizlanadi, eritmada H(+) ionlari to'planadi (kislotali muhit, pH < 7). Lakmus qizil rangga kiradi.",
                    "answer": "Qizil rang (kislotali muhit)"
                }
            ],
            "exercise": "AgNO3 va NaCl eritmalari aralashtirilganda hosil bo'ladigan oq cho'kmaning formulasini yozing.",
            "exercise_solution": "Ag(+) + Cl(-) = AgCl v (kumush xlorid oq tvorogsimon cho'kmasi).",
            "check_questions": [
                {
                    "question": "Neytral muhitda pH qiymati nechaga teng?",
                    "options": ["0", "7", "14", "1"],
                    "correct_index": 1,
                    "explanation": "Toza suvda [H+] = [OH-] = 10^(-7) mol/l bo'lib, neytral pH = 7 bo'ladi."
                },
                {
                    "question": "Quyidagi moddalardan qaysi biri kuchli elektrolit?",
                    "options": ["H2O", "H2SO4", "CH3COOH", "NH4OH"],
                    "correct_index": 1,
                    "explanation": "Sulfat kislota suvda to'liq dissotsiatsiyalanadigan kuchli elektrolitdir."
                },
                {
                    "question": "Osh tuzi (NaCl) suvda eritilganda gidrolizga uchraydimi?",
                    "options": ["Ha, kislotali muhit beradi", "Ha, ishqoriy muhit beradi", "Yo'q, gidrolizga uchramaydi (muhit neytral)", "Gaz ajraladi"],
                    "correct_index": 2,
                    "explanation": "Kuchli asos (NaOH) va kuchli kislotadan (HCl) hosil bo'lgan tuzlar gidrolizga uchramaydi, muhit neytral (pH=7) bo'ladi."
                }
            ],
            "tags": ["elektrolit", "dissotsiatsiya", "gidroliz", "pH", "ion tenglama", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "chm-008",
            "slug": "oksidlanish-qaytarilish-reaksiyalari-va-elektron-balans",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Oksidlanish-qaytarilish reaksiyalari (OQR) va elektron balans usuli",
            "grade_level": "9-sinf",
            "difficulty": "Murakkab",
            "objective": "Oksidlanish darajasini aniqlash, oksidlovchi va qaytaruvchini topish hamda elektron balans usuli yordamida tenglamalarni tenglashtirish.",
            "theory": "Atomlarning oksidlanish darajasi o'zgarishi bilan boradigan reaksiyalar oksidlanish-qaytarilish reaksiyalari (OQR) deyiladi. Oksidlanish darajasi — kimyoviy birikmada barcha bog'lar ionli deb hisoblanganda atom ega bo'ladigan shartli zaryaddir (oddiy moddalarda 0 ga teng, birikmalarda F doim -1, O odatda -2, H odatda +1). Qaytaruvchi — elektron beruvchi atom (oksidlanish darajasi ortadi, o'zi oksidlanadi). Oksidlovchi — elektron biriktirib oluvchi atom (oksidlanish darajasi kamayadi, o'zi qaytariladi). Elektron balans qoidasi: qaytaruvchi bergan elektronlar soni oksidlovchi olgan elektronlar soniga teng bo'lishi shart.",
            "examples": [
                {
                    "title": "Elektron balans usulida tenglashtirish",
                    "problem": "KMnO4 + HCl -> KCl + MnCl2 + Cl2 + H2O reaksiyasini elektron balans usulida tenglashtiring.",
                    "step_by_step": "1) Oksidlanish darajalari o'zgarishi: Mn(+7) -> Mn(+2); 2Cl(-1) -> Cl2(0).\n2) Balans:\n   Mn(+7) + 5e -> Mn(+2) | x 2 (oksidlovchi, qaytariladi)\n   2Cl(-1) - 2e -> Cl2(0)  | x 5 (qaytaruvchi, oksidlanadi)\n3) Koeffitsiyentlar: 2KMnO4 + 16HCl = 2KCl + 2MnCl2 + 5Cl2 + 8H2O.",
                    "answer": "2KMnO4 + 16HCl = 2KCl + 2MnCl2 + 5Cl2 + 8H2O"
                },
                {
                    "title": "Oksidlanish darajasini topish",
                    "problem": "K2Cr2O7 birikmasida xrom (Cr) atomining oksidlanish darajasini toping.",
                    "step_by_step": "1) K: +1, O: -2.\n2) 2*(+1) + 2*x + 7*(-2) = 0.\n3) 2 + 2x - 14 = 0 => 2x = 12 => x = +6.",
                    "answer": "+6"
                }
            ],
            "exercise": "Cu + 4HNO3 (kons) -> Cu(NO3)2 + 2NO2 + 2H2O reaksiyasida qaysi modda qaytaruvchi va qaysi modda oksidlovchi?",
            "exercise_solution": "Cu(0) -> Cu(+2) (2 elektron berib oksidlanadi, demak Cu - qaytaruvchi); N(+5) -> N(+4) (1 elektron olib qaytariladi, demak HNO3 - oksidlovchi).",
            "check_questions": [
                {
                    "question": "Qaytaruvchi modda reaksiyada nima qiladi?",
                    "options": ["Elektron oladi", "Elektron beradi", "Proton oladi", "O'zgarmaydi"],
                    "correct_index": 1,
                    "explanation": "Qaytaruvchi elektron berib, o'zining oksidlanish darajasini oshiradi."
                },
                {
                    "question": "Oddiy moddalarda (masalan, Fe, O2, H2) elementning oksidlanish darajasi nimaga teng?",
                    "options": ["+1", "-1", "0", "Valentligiga"],
                    "correct_index": 2,
                    "explanation": "Oddiy moddalarda elektron zichligi siljimaganligi sababli oksidlanish darajasi 0 ga teng."
                },
                {
                    "question": "H2SO4 birikmasida oltingugurtning (S) oksidlanish darajasi qanday?",
                    "options": ["+2", "+4", "+6", "-2"],
                    "correct_index": 2,
                    "explanation": "2*(+1) + S + 4*(-2) = 0 => 2 + S - 8 = 0 => S = +6."
                }
            ],
            "tags": ["OQR", "oksidlovchi", "qaytaruvchi", "elektron balans", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "chm-009",
            "slug": "organik-kimyoga-kirish-va-alkanlar",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Organik kimyoga kirish: uglerod valentligi va to'yingan uglevodorodlar (alkanlar)",
            "grade_level": "10-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "A.M. Butlerovning organik moddalar tuzilish nazariyasi, izomeriya, alkanlarning umumiy formulasi (CnH2n+2) va metanning xossalarini bilish.",
            "theory": "Organik kimyo uglerod birikmalarini o'rganadigan fandir. A.M. Butlerov tuzilish nazariyasining asosiy qoidalari: 1) Organik moddalarda uglerod doimo IV valentli; 2) Atomlar molekulada o'z valentliklariga muvofiq qat'iy ketma-ketlikda birikadi; 3) Moddalarning xossalari nafaqat tarkibiga, balki ularning tuzilishiga ham bog'liq (izomeriya hodisasi). To'yingan uglevodorodlar (alkanlar yoki parafinlar) — molekulasida uglerod atomlari faqat oddiy (bir karrali) sigma-bog'lar bilan bog'langan ochiq zanjirli birikmalar. Umumiy formulasi: C_n H_(2n+2). Gomologik qator: Metan (CH4), Etan (C2H6), Propan (C3H8), Butan (C4H10)... Xarakterli reaksiyalari: o'rin olish (galogenlanish, xlorlash yorug'lik ta'sirida) va yonish.",
            "examples": [
                {
                    "title": "Metanning xlorlanishi",
                    "problem": "Metanning ultrabinafsha nur ta'sirida bosqichma-bosqich xlorlanish reaksiyasini yozing.",
                    "step_by_step": "1) CH4 + Cl2 --(hv)--> CH3Cl (xlormetan) + HCl\n2) CH3Cl + Cl2 -> CH2Cl2 (dixlormetan) + HCl\n3) CH2Cl2 + Cl2 -> CHCl3 (trixlormetan / xloroform) + HCl\n4) CHCl3 + Cl2 -> CCl4 (tetraxlormetan) + HCl.",
                    "answer": "CH4 + Cl2 -> CH3Cl + HCl"
                },
                {
                    "title": "Alkanlarning yonishi",
                    "problem": "Propan (C3H8) gazining to'liq yonish tenglamasini tuzing.",
                    "step_by_step": "C3H8 + 5O2 -> 3CO2 + 4H2O + Q.",
                    "answer": "C3H8 + 5O2 -> 3CO2 + 4H2O"
                }
            ],
            "exercise": "Geksan (C6H14) ning nechta strukturaviy izomeri mavjud?",
            "exercise_solution": "Geksanning 5 ta izomeri bor: n-geksan, 2-metilpentan, 3-metilpentan, 2,2-dimetilbutan va 2,3-dimetilbutan.",
            "check_questions": [
                {
                    "question": "Alkanlarning umumiy formulasi qaysi?",
                    "options": ["CnH2n", "CnH2n+2", "CnH2n-2", "CnH2n-6"],
                    "correct_index": 1,
                    "explanation": "To'yingan uglevodorodlar umumiy formulasi C_n H_(2n+2) dir."
                },
                {
                    "question": "Organik birikmalarda uglerod atomi qanday valentlik namoyon qiladi?",
                    "options": ["II", "III", "IV", "O'zgaruvchan (I-VI)"],
                    "correct_index": 2,
                    "explanation": "Organik kimyoda uglerod har doim IV valentli bo'ladi."
                },
                {
                    "question": "Tarkibi bir xil, lekin tuzilishi va xossalari har xil bo'lgan moddalar nima deyiladi?",
                    "options": ["Gomologlar", "Izotoplar", "Izomerlar", "Allotroplar"],
                    "correct_index": 2,
                    "explanation": "Molekulyar formulasi bir xil, fazoviy/kimyoviy tuzilishi har xil bo'lgan moddalar izomerlar deyiladi."
                }
            ],
            "tags": ["organik kimyo", "alkanlar", "metan", "izomeriya", "10-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "chm-010",
            "slug": "toyinmagan-uglevodorodlar-alkenlar-va-alkinlar",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "To'yinmagan uglevodorodlar: alkenlar (etilen), alkadiyenlar va alkinlar (atsetilen)",
            "grade_level": "10-sinf",
            "difficulty": "O'rta",
            "objective": "Qo'shbog' va uchbog' tabiati, Markovnikov qoidasi, polimerlanish reaksiyasi va to'yinmaganlikning sifat reaksiyalarini (bromli suv va KMnO4) o'rganish.",
            "theory": "Molekulasida uglerod atomlari orasida karrali bog'lar (qo'shbog' yoki uchbog') bo'lgan uglevodorodlar to'yinmagan uglevodorodlar deyiladi. 1) Alkenlar (etilen qatori) — bitta qo'shbog' (sigma va pi) tutgan, umumiy formulasi C_n H_2n (Etilen C2H4, Propen C3H6). Xarakterli reaksiyalari: birikish (gidrogenlanish, galogenlanish, gidratlanish) va polimerlanish (polietilen hosil bo'lishi); 2) Markovnikov qoidasi: Vodorod galogenidlar yoki suv nosimmetrik alkenlarga birikkanda vodorod atomi vodorodi ko'proq uglerodga, galogen (yoki OH guruhi) vodorodi kamroq uglerodga birikadi; 3) Alkinlar (atsetilen qatori) — bitta uchbog' tutgan, formulasi C_n H_(2n-2) (Atsetilen C2H2). Sifat reaksiyalari: bromli suvni va kaliy permanganat eritmasini rangsizlantiradi.",
            "examples": [
                {
                    "title": "Markovnikov qoidasini qo'llash",
                    "problem": "Propen (CH2=CH-CH3) ga vodorod xlorid (HCl) birikkanda qanday asosiy mahsulot hosil bo'ladi?",
                    "step_by_step": "1) CH2=CH-CH3 molekulasida birinchi uglerodda 2 ta H, ikkinchisida 1 ta H bor.\n2) Markovnikov qoidasiga ko'ra H birinchi uglerodga, Cl ikkinchi uglerodga birikadi.\n3) Hosil bo'ladi: CH3-CH(Cl)-CH3 (2-xlorpropan).",
                    "answer": "2-xlorpropan"
                },
                {
                    "title": "Atsetilen olinishi",
                    "problem": "Kalsiy karbidga suv ta'sir ettirib atsetilen olish reaksiyasini yozing.",
                    "step_by_step": "CaC2 + 2H2O -> Ca(OH)2 + C2H2 ^ (atsetilen gazi).",
                    "answer": "CaC2 + 2H2O -> Ca(OH)2 + C2H2"
                }
            ],
            "exercise": "Etilenning polimerlanish reaksiyasi tenglamasini yozing.",
            "exercise_solution": "n CH2=CH2 --(t, p, kat)--> (-CH2-CH2-)n (polietilen).",
            "check_questions": [
                {
                    "question": "Alkenlarning umumiy formulasi qaysi?",
                    "options": ["CnH2n+2", "CnH2n", "CnH2n-2", "CnH2n-6"],
                    "correct_index": 1,
                    "explanation": "Bitta qo'shbog'li to'yinmagan uglevodorodlar umumiy formulasi C_n H_2n dir."
                },
                {
                    "question": "To'yinmagan uglevodorodlarni aniqlash uchun qaysi sifat reaksiyasidan foydalaniladi?",
                    "options": ["Lakmus qog'ozi", "Bromli suvning rangsizlanishi", "Ohakli suvning loyqalanishi", "Fenolftalein"],
                    "correct_index": 1,
                    "explanation": "Qo'shbog' va uchbog' bromli suv bilan oson birikish reaksiyasiga kirishib, qo'ng'ir rangni rangsizlantiradi."
                },
                {
                    "question": "Atsetilen (C2H2) molekulasida nechta pi-bog' bor?",
                    "options": ["1 ta", "2 ta", "3 ta", "0 ta"],
                    "correct_index": 1,
                    "explanation": "Uchbog' 1 ta mustahkam sigma-bog' va 2 ta zaifroq pi-bog'dan iborat."
                }
            ],
            "tags": ["alkenlar", "etilen", "alkinlar", "atsetilen", "markovnikov", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "chm-011",
            "slug": "kislorodli-organik-birikmalar-spirtlar-va-aldegidlar",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Kislorodli organik birikmalar: bir atomli va ko'p atomli spirtlar, aldegidlar",
            "grade_level": "10-sinf",
            "difficulty": "O'rta",
            "objective": "Spirtlarning funksional guruhi (-OH), metanol va etanol xossalari, glitserin hamda aldegidlarning sifat reaksiyalarini (kumush ko'zgu) bilish.",
            "theory": "Molekulasida uglevodorod radikali bilan bog'langan bitta yoki bir nechta gidroksil guruhi (-OH) bo'lgan organik birikmalar spirtlar deyiladi. Bir atomli spirtlar: C_n H_(2n+1) OH (Metanol CH3OH — zaharli, Etanol C2H5OH). Xossalari: faol metallar (Na) bilan reaksiyaga kirishib alkogolyatlar hosil qiladi, vodorod ajraladi; kislotalar bilan murakkab efirlar hosil qiladi (eterifikatsiya). Ko'p atomli spirtlar: etilenglikol (2 atomli) va glitserin (3 atomli, C3H5(OH)3 — mis (II) gidroksid bilan och ko'k rangli eritma hosil qiladi). Aldegidlar — tarkibida karbonil guruhi (-CH=O) bo'lgan birikmalar. Sifat reaksiyasi: 'Kumush ko'zgu' reaksiyasi — aldegidlarning kumush (I) oksidining ammiakli eritmasi bilan oksidlanishi natijasida erkin metall kumush ajralib chiqadi.",
            "examples": [
                {
                    "title": "Spirtlarning natriy bilan reaksiyasi",
                    "problem": "Etanolning metall natriy bilan reaksiyasini yozing.",
                    "step_by_step": "2C2H5OH + 2Na -> 2C2H5ONa (natriy etilat) + H2 ^.",
                    "answer": "2C2H5OH + 2Na -> 2C2H5ONa + H2"
                },
                {
                    "title": "Kumush ko'zgu reaksiyasi",
                    "problem": "Sirka aldegidi (CH3CHO) ning kumush (I) oksidi ammiakli eritmasi bilan reaksiyasini yozing.",
                    "step_by_step": "CH3CHO + Ag2O --(NH3*H2O, t)--> CH3COOH (sirka kislota) + 2Ag v (kumush qatlami).",
                    "answer": "CH3CHO + Ag2O -> CH3COOH + 2Ag v"
                }
            ],
            "exercise": "Glitserinni laboratoriyada qaysi reaktiv yordamida aniqlash mumkin?",
            "exercise_solution": "Yangi tayyorlangan mis (II) gidroksid Cu(OH)2 ta'sir ettirilganda yorqin ko'k rangli mis glitserati eritmasi hosil bo'ladi.",
            "check_questions": [
                {
                    "question": "Spirtlarning funksional guruhi qaysi?",
                    "options": ["-COOH", "-OH", "-CHO", "-NH2"],
                    "correct_index": 1,
                    "explanation": "Gidroksil guruhi (-OH) spirtlarning xarakterli funksional guruhidir."
                },
                {
                    "question": "Qaysi spirt o'ta zaharli bo'lib, hatto oz miqdori ko'rlik va o'limga olib keladi?",
                    "options": ["Etanol", "Metanol (yog'och spirti)", "Glitserin", "Butanol"],
                    "correct_index": 1,
                    "explanation": "Metanol (CH3OH) kuchli asab zahari hisoblanadi."
                },
                {
                    "question": "Aldegidlar oksidlanganda qanday moddalar hosil bo'ladi?",
                    "options": ["Oddiy efirlar", "Karboksil kislotalar", "Alkanlar", "Spirtlar"],
                    "correct_index": 1,
                    "explanation": "Aldegidlar (-CHO) oksidlanganda karboksil kislotalarga (-COOH) aylanadi."
                }
            ],
            "tags": ["spirtlar", "etanol", "glitserin", "aldegidlar", "kumush ko'zgu", "10-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "chm-012",
            "slug": "karboksil-kislotalar-aminokislotalar-va-oqsillar",
            "subject_id": "sub-07",
            "subject_name": "Kimyo",
            "title": "Karboksil kislotalar, murakkab efirlar, aminokislotalar va oqsillar",
            "grade_level": "11-sinf",
            "difficulty": "Murakkab",
            "objective": "Karboksil guruhi (-COOH), sirka kislota, murakkab efirlar va yog'lar, aminokislotalarning amfoterligi hamda oqsillarning peptid bog'i va tuzilishini tushunish.",
            "theory": "Karboksil kislotalar — molekulasida karboksil guruhi (-COOH) bo'lgan birikmalar (Chumoli kislota HCOOH, Sirka kislota CH3COOH). Kislotali xossalarga ega: metallar, asosli oksidlar, asoslar va tuzlar bilan reaksiyaga kirishadi. Eterifikatsiya reaksiyasi: Kislota + Spirt <=> Murakkab efir + Suv (masalan, CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O). Yog'lar — uch atomli spirt glitserin va yuqori yog' kislotalarining murakkab efirlaridir. Aminokislotalar — tarkibida ham amin guruhi (-NH2, asosli), ham karboksil guruhi (-COOH, kislotali) bo'lgan amfoter organik moddalardir (masalan, glitsin NH2-CH2-COOH). Oqsillar — alfa-aminokislota qoldiqlarining peptid bog'lari (-CO-NH-) orqali birikishidan hosil bo'lgan biopolimerlardir. Oqsilning 4 ta strukturasi mavjud (birlamchi, ikkilamchi, uchlamchi, to'rtlamchi) va denaturatsiya jarayoniga uchraydi.",
            "examples": [
                {
                    "title": "Eterifikatsiya reaksiyasi",
                    "problem": "Sirka kislotasi bilan etil spirtidan etilatsetat hosil bo'lish reaksiyasini yozing.",
                    "step_by_step": "CH3COOH + C2H5OH <=(H2SO4 kons, t)=> CH3COOC2H5 (etilatsitat) + H2O.",
                    "answer": "CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O"
                },
                {
                    "title": "Dipeptid hosil bo'lishi",
                    "problem": "Ikki molekula glitsindan (NH2-CH2-COOH) dipeptid hosil bo'lishini ko'rsating.",
                    "step_by_step": "NH2-CH2-COOH + NH2-CH2-COOH -> NH2-CH2-CO-NH-CH2-COOH + H2O (-CO-NH- peptid bog'i).",
                    "answer": "Glitsil-glitsin + H2O"
                }
            ],
            "exercise": "Oqsilning denaturatsiyasi nima va unga qanday omillar sabab bo'ladi?",
            "exercise_solution": "Denaturatsiya — tashqi omillar (yuqori harorat, og'ir metall tuzlari, kuchli kislota va ishqorlar, radiatsiya) ta'sirida oqsilning ikkilamchi, uchlamchi va to'rtlamchi fazoviy tuzilmasining buzilishi va biologik faolligini yo'qotishi.",
            "check_questions": [
                {
                    "question": "Aminokislotalar bir-biri bilan qanday kimyoviy bog' orqali bog'lanadi?",
                    "options": ["Vodorod bog'", "Peptid (amid) bog'i", "Ion bog'", "Glikozid bog'i"],
                    "correct_index": 1,
                    "explanation": "-CO-NH- guruhi peptid bog'i deyiladi va oqsillarning birlamchi strukturasini hosil qiladi."
                },
                {
                    "question": "Oqsillarga xos bo'lgan biuret reaksiyasi qanday rangli kompleks hosil qiladi?",
                    "options": ["Sariq", "Qizil", "Binafsha", "Yashil"],
                    "correct_index": 2,
                    "explanation": "Ishqoriy muhitda Cu(2+) ionlari peptid bog'lar bilan binafsha rangli kompleks hosil qiladi."
                },
                {
                    "question": "Aminokislotalarning qaysi xossasi ularning ikkala muhit bilan reaksiyaga kirishishini ta'minlaydi?",
                    "options": ["Kislotaliligi", "Asosliligi", "Amfoterligi", "Neytralligi"],
                    "correct_index": 2,
                    "explanation": "Molekulada ham asosli (-NH2), ham kislotali (-COOH) guruhlar bo'lgani sababli ular amfoterdir."
                }
            ],
            "tags": ["karboksil kislotalar", "efirlar", "aminokislotalar", "oqsillar", "peptid bog'", "11-sinf"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_chemistry_materials()
    print(f"Generated {len(mats)} Chemistry materials.")
