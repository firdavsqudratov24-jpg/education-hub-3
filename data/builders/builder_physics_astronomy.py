# -*- coding: utf-8 -*-
"""
Builder for Fizika va Astronomiya (15 materials)
- sub-05: Fizika (10 materials: phy-001 to phy-010)
- sub-06: Astronomiya (5 materials: phy-011 to phy-015)
"""

def get_physics_astronomy_materials():
    materials = [
        # FIZIKA (10)
        {
            "id": "phy-001",
            "slug": "mexanik-harakat-tezlik-va-tezlanish",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "Mexanik harakat, to'g'ri chiziqli tekis va tekis o'zgaruvchan harakat",
            "grade_level": "7-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Moddiy nuqta, sanoq sistemasi, tezlik va tezlanish tushunchalarini o'rganish hamda harakat tenglamalarini tuzish.",
            "theory": "Vaqt o'tishi bilan jismning boshqa jismlarga nisbatan fazodagi vaziyatining o'zgarishi mexanik harakat deyiladi. O'lchamlari berilgan sharoitda hisobga olinmasa bo'ladigan jism moddiy nuqta deyiladi. To'g'ri chiziqli tekis harakatda jism teng vaqt oraliqlarida bir xil masofalarni bosib o'tadi: v = s / t. To'g'ri chiziqli tekis o'zgaruvchan harakatda esa tezlik teng vaqt oraliqlarida bir xil miqdorga o'zgaradi. Tezlanish a = (v - v_0) / t (birligi m/s^2). Bosib o'tilgan yo'l formulasi: s = v_0*t + (a*t^2)/2.",
            "examples": [
                {
                    "title": "Tekis harakatda yo'lni topish",
                    "problem": "Poyezd 72 km/soat tezlik bilan tekis harakatlanib, 20 sekundda qancha masofani bosib o'tadi?",
                    "step_by_step": "1) Tezlikni SI sistemasiga (m/s) o'tkazamiz: 72 km/soat = 72 * (1000 m / 3600 s) = 20 m/s.\n2) s = v * t = 20 m/s * 20 s = 400 m.",
                    "answer": "400 metr"
                },
                {
                    "title": "Tezlanuvchan harakatda tezlik va yo'l",
                    "problem": "Tinch holatdan (v_0 = 0) 2 m/s^2 tezlanish bilan harakat boshlagan avtomobilning 5-sekunddagi tezligi va bosib o'tgan yo'lini toping.",
                    "step_by_step": "1) v = v_0 + a*t = 0 + 2 * 5 = 10 m/s.\n2) s = (a * t^2) / 2 = (2 * 5^2) / 2 = 25 m.",
                    "answer": "Tezlik: 10 m/s, Yo'l: 25 m"
                }
            ],
            "exercise": "Avtomobil tormozlanib, 4 m/s^2 tezlanish bilan 3 sekundda to'xtadi. Uning boshlang'ich tezligi qancha bo'lgan?",
            "exercise_solution": "v = v_0 - a*t => 0 = v_0 - 4*3 => v_0 = 12 m/s (yoki 43.2 km/soat).",
            "check_questions": [
                {
                    "question": "SI sistemasida tezlanish birligi qaysi?",
                    "options": ["m/s", "m/s^2", "km/soat", "N/kg"],
                    "correct_index": 1,
                    "explanation": "Tezlanish tezlikning vaqtga nisbati bo'lib, SI da m/s^2 bilan o'lchanadi."
                },
                {
                    "question": "36 km/soat necha m/s ga teng?",
                    "options": ["5 m/s", "10 m/s", "15 m/s", "20 m/s"],
                    "correct_index": 1,
                    "explanation": "36 * 1000 / 3600 = 10 m/s."
                },
                {
                    "question": "Tezlanish nolga teng bo'lsa, harakat qanday harakat bo'ladi?",
                    "options": ["Tekis o'zgaruvchan", "Tekis harakat", "Tinch holat yoki to'xtash", "Aylanma harakat"],
                    "correct_index": 1,
                    "explanation": "a = 0 bo'lganda tezlik o'zgarmas doimiy bo'lib, harakat tekis harakat deyiladi."
                }
            ],
            "tags": ["mexanika", "tezlik", "tezlanish", "fizika", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "phy-002",
            "slug": "nyuton-qonunlari-va-kuchlar",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "Nyutonning dinamika qonunlari va tabiatdagi asosiy kuchlar",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Nyutonning I, II, III qonunlarini, inersiya hodisasini hamda og'irlik, elastiklik va ishqalanish kuchlarini hisoblash.",
            "theory": "Dinamika jismlarning o'zaro ta'siri va harakat sabablarini o'rganadi. Nyutonning I qonuni (inersiya qonuni): Jismga boshqa jismlar ta'sir etmasa yoki ularning ta'siri kompensatsiyalansa, jism o'zining tinch holatini yoki to'g'ri chiziqli tekis harakatini saqlaydi. Nyutonning II qonuni: Jism olgan tezlanish unga ta'sir etuvchi natijaviy kuchga to'g'ri, massasiga teskari proporsional: a = F / m yoki F = m * a. Nyutonning III qonuni: Ikki jism bir-biriga doimo moduli jihatidan teng, yo'nalishi bo'yicha qarama-qarshi kuchlar bilan ta'sir qiladi: F_12 = -F_21. Tabiatdagi kuchlar: Og'irlik kuchi (F_og = m*g), Guk qonuni bo'yicha elastiklik kuchi (F_el = -k*x), Ishqalanish kuchi (F_ishq = mu * N).",
            "examples": [
                {
                    "title": "Nyutonning II qonunini qo'llash",
                    "problem": "Massasi 1200 kg bo'lgan avtomobil 1.5 m/s^2 tezlanish bilan harakatlanishi uchun unga qanday kuch ta'sir qilishi kerak?",
                    "step_by_step": "1) F = m * a.\n2) F = 1200 kg * 1.5 m/s^2 = 1800 N (1.8 kN).",
                    "answer": "1800 N"
                },
                {
                    "title": "Guk qonuni bo'yicha prujina bikrligini topish",
                    "problem": "Prujinaga 20 N kuch bilan ta'sir etilganda u 4 sm ga cho'zildi. Prujinaning bikrligini (k) toping.",
                    "step_by_step": "1) Cho'zilish x = 4 sm = 0.04 m.\n2) F = k * x => k = F / x.\n3) k = 20 N / 0.04 m = 500 N/m.",
                    "answer": "500 N/m"
                }
            ],
            "exercise": "Massasi 5 kg bo'lgan jism gorizontal sirtda yotibdi. Sirt va jism orasidagi ishqalanish koeffitsiyenti mu = 0.2. Sirpanish ishqalanish kuchini toping (g = 10 m/s^2).",
            "exercise_solution": "N = m*g = 5 * 10 = 50 N. F_ishq = mu * N = 0.2 * 50 = 10 N.",
            "check_questions": [
                {
                    "question": "Nyutonning II qonuni matematik ifodasi qaysi?",
                    "options": ["F = m / a", "F = m * a", "a = m * F", "F_1 = -F_2"],
                    "correct_index": 1,
                    "explanation": "Kuch jism massasi bilan tezlanishining ko'paytmasiga teng: F = m*a."
                },
                {
                    "question": "Kuch birligi qaysi olim sharafiga Nyuton (N) deb nomlangan?",
                    "options": ["Galiley", "Isaak Nyuton", "Albert Eynshteyn", "Blez Paskal"],
                    "correct_index": 1,
                    "explanation": "Kuch birligi ingliz fizigi Isaak Nyuton sharafiga atalgan."
                },
                {
                    "question": "Bir jism ikkinchi jismga 100 N kuch bilan ta'sir etsa, ikkinchi jism birinchisiga qanday kuch bilan ta'sir qiladi?",
                    "options": ["50 N", "100 N qarama-qarshi yo'nalishda", "0 N", "200 N"],
                    "correct_index": 1,
                    "explanation": "Nyutonning III qonuniga ko'ra ta'sir aks ta'sirga teng va qarama-qarshi yo'nalgan."
                }
            ],
            "tags": ["nyuton qonunlari", "kuch", "dinamika", "og'irlik kuchi", "7-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "phy-003",
            "slug": "mexanik-ish-quvvat-va-energiya",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "Mexanik ish, quvvat, kinetik va potensial energiya",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Mexanik ish (A = F*s*cos(alpha)), quvvat (N = A/t) va mexanik energiyaning saqlanish qonunini to'liq o'rganish.",
            "theory": "Jism kuch ta'sirida ma'lum masofaga ko'chsa, mexanik ish bajariladi: A = F * s * cos(alpha). Agar kuch ko'chish yo'nalishida bo'lsa (alpha = 0°), A = F * s. Ishning SI dagi birligi Joul (J). Birlik vaqt ichida bajarilgan ish quvvat deyiladi: N = A / t (birligi Vatt, Vt). Energiya - jismning ish bajara olish qobiliyati. Kinetik energiya (harakat energiyasi): E_k = (m * v^2) / 2. Potensial energiya (o'zaro ta'sir energiyasi, yer yuzasidan balandlikda): E_p = m * g * h. To'la mexanik energiyaning saqlanish qonuni: Yopiq konservativ sistemada to'la mexanik energiya doimiy qoladi: E_to'la = E_k + E_p = const.",
            "examples": [
                {
                    "title": "Mexanik ishni hisoblash",
                    "problem": "Kran massasi 2 tonna bo'lgan yukni 15 metr balandlikka tekis ko'tardi. Kran qancha ish bajargan (g = 10 m/s^2)?",
                    "step_by_step": "1) m = 2000 kg, h = 15 m.\n2) Ko'taruvchi kuch og'irlik kuchiga teng: F = m*g = 2000 * 10 = 20 000 N.\n3) A = F * h = 20 000 N * 15 m = 300 000 J = 300 kJ.",
                    "answer": "300 kJ"
                },
                {
                    "title": "Mexanik energiyaning saqlanishi",
                    "problem": "Massasi 0.5 kg bo'lgan jism 20 m balandlikdan erkin tushmoqda. Jism yerga urilish paytidagi tezligini toping (havo qarshiligi hisobga olinmasin).",
                    "step_by_step": "1) Boshlang'ich potensial energiya yerga yetganda to'liq kinetik energiyaga aylanadi: m*g*h = (m*v^2)/2.\n2) v^2 = 2*g*h => v = sqrt(2 * 10 * 20) = sqrt(400) = 20 m/s.",
                    "answer": "20 m/s"
                }
            ],
            "exercise": "Dvigatel 2 minutda 360 kJ ish bajardi. Dvigatelning quvvatini toping.",
            "exercise_solution": "t = 2 min = 120 s. A = 360 000 J. N = A / t = 360 000 / 120 = 3000 Vt = 3 kVt.",
            "check_questions": [
                {
                    "question": "1 Joul (J) qaysi birliklarning ko'paytmasiga teng?",
                    "options": ["1 N * 1 m", "1 N / 1 m", "1 kg * 1 m", "1 Vt * 1 s^2"],
                    "correct_index": 0,
                    "explanation": "Ish kuchning ko'chishga ko'paytmasiga teng: 1 J = 1 N * 1 m."
                },
                {
                    "question": "Jismning tezligi 2 marta oshsa, uning kinetik energiyasi necha marta ortadi?",
                    "options": ["2 marta", "4 marta", "O'zgarmaydi", "8 marta"],
                    "correct_index": 1,
                    "explanation": "E_k = (m*v^2)/2 formulada tezlik kvadrat bo'lgani uchun 2^2 = 4 marta ortadi."
                },
                {
                    "question": "Quvvatning SI dagi birligi nima?",
                    "options": ["Joul", "Paskal", "Vatt", "Nyuton"],
                    "correct_index": 2,
                    "explanation": "Quvvat J/s bo'lib, Jeyms Vatt sharafiga Vatt (Vt) deb ataladi."
                }
            ],
            "tags": ["mexanik ish", "quvvat", "energiya", "saqlanish qonuni", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "phy-004",
            "slug": "bosim-paskal-qonuni-va-arximed-kuchi",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "Bosim, suyuqlik va gazlar gidrostatikasi, Arximed kuchi",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Qattiq jismlar bosimi (p = F/S), suyuqliklar gidrostatik bosimi (p = rho*g*h) va Arximed kuchi hamda jismlarning suzish shartlarini o'rganish.",
            "theory": "Sirtga tik ta'sir etuvchi kuchning shu sirt yuziga nisbati bosim deyiladi: p = F / S (birligi Paskal, Pa = N/m^2). Paskal qonuni: Suyuqlik yoki gazga berilgan tashqi bosim barcha yo'nalishlar bo'yicha o'zgarishsiz uzatiladi. Suyuqlik ustunining tubiga ko'rsatadigan gidrostatik bosimi: p = rho * g * h (bu yerda rho - zichlik, h - balandlik). Arximed qonuni: Suyuqlik yoki gazga botirilgan jismga suyuqlik tomonidan pastdan yuqoriga yo'nalgan itaruvchi kuch ta'sir qiladi. Bu kuch jism siqib chiqargan suyuqlik og'irligiga teng: F_A = rho_suyuqlik * g * V_botgan. Suzish shartlari: rho_jism < rho_suyuqlik bo'lsa jism suzadi, rho_jism = rho_suyuqlik bo'lsa muallaq turadi, rho_jism > rho_suyuqlik bo'lsa cho'kadi.",
            "examples": [
                {
                    "title": "Gidrostatik bosimni hisoblash",
                    "problem": "Suv tubining 5 metr chuqurligidagi gidrostatik bosimini toping (suv zichligi rho = 1000 kg/m^3, g = 10 m/s^2).",
                    "step_by_step": "1) p = rho * g * h.\n2) p = 1000 kg/m^3 * 10 m/s^2 * 5 m = 50 000 Pa = 50 kPa.",
                    "answer": "50 kPa"
                },
                {
                    "title": "Arximed kuchini topish",
                    "problem": "Hajmi 0.02 m^3 bo'lgan tosh suvga to'liq botirilganda unga qanday Arximed kuchi ta'sir qiladi?",
                    "step_by_step": "1) F_A = rho_suv * g * V.\n2) F_A = 1000 kg/m^3 * 10 m/s^2 * 0.02 m^3 = 200 N.",
                    "answer": "200 N"
                }
            ],
            "exercise": "Gidravlik press kichik porshenining yuzi 5 sm^2, katta porshenining yuzi 200 sm^2. Kichik porshenga 100 N kuch berilsa, katta porshen qanday kuch hosil qiladi?",
            "exercise_solution": "F_2 / F_1 = S_2 / S_1 => F_2 = F_1 * (S_2 / S_1) = 100 * (200 / 5) = 100 * 40 = 4000 N (4 kN).",
            "check_questions": [
                {
                    "question": "Bosimning SI sistemasidagi birligi nima?",
                    "options": ["Nyuton", "Joul", "Paskal", "Bar"],
                    "correct_index": 2,
                    "explanation": "Bosim birligi N/m^2 bo'lib, Blez Paskal sharafiga Paskal (Pa) deb ataladi."
                },
                {
                    "question": "Jism zichligi suv zichligidan kichik bo'lsa (rho_j < rho_s), jism nima bo'ladi?",
                    "options": ["Cho'kadi", "Suv sirtida suzadi", "Tubga yopishadi", "Erib ketadi"],
                    "correct_index": 1,
                    "explanation": "Arximed kuchi og'irlik kuchidan katta bo'lgani sababli jism yuqoriga qalqib chiqib suzadi."
                },
                {
                    "question": "Suyuqlik ichida chuqurlik ortgan sari gidrostatik bosim qanday o'zgaradi?",
                    "options": ["Kamayadi", "O'zgarmaydi", "Chiziqli ravishda ortadi", "Nolga teng bo'ladi"],
                    "correct_index": 2,
                    "explanation": "p = rho*g*h formulasiga ko'ra chuqurlik h ortishi bilan bosim to'g'ri mutanosib ortadi."
                }
            ],
            "tags": ["bosim", "paskal qonuni", "arximed kuchi", "gidrostatika", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "phy-005",
            "slug": "termodinamika-asoslari-va-issiqlik-miqdori",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "Termodinamika asoslari, ichki energiya va issiqlik miqdori",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Ichki energiya o'zgarishi, issiqlik uzatish turlari (o'tkazuvchanlik, konveksiya, nurlanish) va issiqlik balansi tenglamasini yechish.",
            "theory": "Jismni tashkil qiluvchi barcha zarralarning tartibsiz harakati kinetik energiyasi va ularning o'zaro ta'sir potensial energiyalari yig'indisi jismning ichki energiyasi deyiladi. Ichki energiyani o'zgartirishning 2 ta usuli bor: mexanik ish bajarish va issiqlik uzatish. Issiqlik miqdori formulalari: 1) Isitish/sovutishda: Q = c * m * (t_2 - t_1) (bu yerda c - solishtirma issiqlik sig'imi); 2) Yoqilg'i yonganda: Q = q * m (q - solishtirma yonish issiqligi); 3) Erish/qotishda: Q = lambda * m (lambda - solishtirma erish issiqligi); 4) Bug'lanish/kondensatsiyada: Q = L * m (L - solishtirma bug'lanish issiqligi). Termodinamikaning I qonuni: Q = Delta_U + A (sistemaga berilgan issiqlik uning ichki energiyasini oshirishga va tashqi kuchlarga qarshi ish bajarishga sarflanadi).",
            "examples": [
                {
                    "title": "Suvni isitish uchun issiqlik miqdori",
                    "problem": "Massasi 2 kg bo'lgan suvni 20 °C dan 100 °C gacha isitish uchun qancha issiqlik miqdori kerak (c_suv = 4200 J/(kg*°C))?",
                    "step_by_step": "1) Delta_t = 100 - 20 = 80 °C.\n2) Q = c * m * Delta_t = 4200 * 2 * 80 = 672 000 J = 672 kJ.",
                    "answer": "672 kJ"
                },
                {
                    "title": "Issiqlik balansi tenglamasi",
                    "problem": "80 °C li 1 kg suvga 20 °C li 1 kg suv aralashtirilsa, aralashmaning oxirgi temperaturasi qanday bo'ladi (issiqlik yo'qotilishi hisobga olinmasin)?",
                    "step_by_step": "1) Q_berilgan = Q_olingan.\n2) c * m_1 * (t_1 - theta) = c * m_2 * (theta - t_2).\n3) Massalar va issiqlik sig'imlari teng bo'lgani uchun: 80 - theta = theta - 20 => 2*theta = 100 => theta = 50 °C.",
                    "answer": "50 °C"
                }
            ],
            "exercise": "Massasi 3 kg bo'lgan quruq o'tin to'liq yonganda qancha issiqlik ajraladi (q = 1.0 * 10^7 J/kg)?",
            "exercise_solution": "Q = q * m = 1.0 * 10^7 J/kg * 3 kg = 3.0 * 10^7 J = 30 MJ.",
            "check_questions": [
                {
                    "question": "Solishtirma issiqlik sig'imining o'lchov birligi qaysi?",
                    "options": ["J / kg", "J / (kg * °C)", "J * kg", "Vt / °C"],
                    "correct_index": 1,
                    "explanation": "Q = c*m*Delta_t dan c = Q / (m * Delta_t), birligi J/(kg * °C)."
                },
                {
                    "question": "Moddaning suyuq holatdan gaz holatga o'tish jarayoni nima deyiladi?",
                    "options": ["Erish", "Kondensatsiya", "Bug'lanish", "Sublimatsiya"],
                    "correct_index": 2,
                    "explanation": "Suyuqlikning gazga aylanish jarayoni bug'lanish deb ataladi."
                },
                {
                    "question": "Termodinamikaning birinchi qonuni qaysi fundamental qonunning ifodasidir?",
                    "options": ["Massa saqlanishi", "Energiyaning saqlanish va aylanish qonuni", "Inersiya qonuni", "Paskal qonuni"],
                    "correct_index": 1,
                    "explanation": "Termodinamikaning I qonuni issiqlik jarayonlarida energiyaning saqlanish qonunidir."
                }
            ],
            "tags": ["termodinamika", "issiqlik miqdori", "ichki energiya", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "phy-006",
            "slug": "elektr-zaryadi-va-kulon-qonuni",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "Elektr zaryadi, zaryadning saqlanish qonuni va Kulon qonuni",
            "grade_level": "8-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Musbat va manfiy zaryadlar, elementar zaryad e, zaryad saqlanish qonuni va ikki nuqtaviy zaryad orasidagi Kulon o'zaro ta'sir kuchini hisoblash.",
            "theory": "Elektrostatika qo'zg'almas elektr zaryadlarining xossalarini o'rganadi. Tabiatda ikki turdagi zaryad mavjud: musbat (+) va manfiy (-). Bir xil ishorali zaryadlar itarishadi, har xil ishorali zaryadlar tortishadi. Zaryadning saqlanish qonuni: Yopiq tizimdagi barcha zaryadlarning algebraik yig'indisi o'zgarmas qoladi: q_1 + q_2 + ... + q_n = const. Elementar zaryad eng kichik bo'linmas zaryad bo'lib, e = 1.6 * 10^(-19) Kulon (elektron zaryadi -e). Kulon qonuni: Vakuumda ikki qo'zg'almas nuqtaviy zaryadning o'zaro ta'sir kuchi zaryadlar modullari ko'paytmasiga to'g'ri, ular orasidagi masofaning kvadratiga teskari proporsionaldir: F = k * (|q_1| * |q_2|) / r^2 (bu yerda k = 9 * 10^9 N*m^2/C^2).",
            "examples": [
                {
                    "title": "Kulon kuchini hisoblash",
                    "problem": "Vakuumda bir-biridan 30 sm masofada joylashgan q_1 = 2 * 10^(-6) C va q_2 = 5 * 10^(-6) C zaryadlar orasidagi o'zaro itarish kuchini toping.",
                    "step_by_step": "1) r = 30 sm = 0.3 m. r^2 = 0.09 m^2.\n2) F = 9 * 10^9 * (2 * 10^(-6) * 5 * 10^(-6)) / 0.09.\n3) F = 9 * 10^9 * 10 * 10^(-12) / 0.09 = 9 * 10^(-2) / 0.09 = 1 N.",
                    "answer": "1 N"
                },
                {
                    "title": "Zaryadlangan sharchalarning teginishi",
                    "problem": "q_1 = +8 nC va q_2 = -2 nC li ikkita bir xil metall shar tekkizilib, yana dastlabki masofaga ajratildi. Har bir sharda qanday zaryad qoladi?",
                    "step_by_step": "1) Zaryad saqlanish qonuniga ko'ra umumiy zaryad: q_umum = +8 + (-2) = +6 nC.\n2) Sharchalar bir xil bo'lgani uchun zaryad teng ikkiga bo'linadi: q' = 6 / 2 = +3 nC.",
                    "answer": "+3 nC dan"
                }
            ],
            "exercise": "Zaryadlar orasidagi masofa 2 marta oshirilsa, Kulon kuchi necha marta kamayadi?",
            "exercise_solution": "F ~ 1 / r^2 bo'lgani sababli, r 2 marta oshsa, kuch 2^2 = 4 marta kamayadi.",
            "check_questions": [
                {
                    "question": "Elektr zaryadining SI sistemasidagi birligi nima?",
                    "options": ["Amper", "Volt", "Kulon", "Om"],
                    "correct_index": 2,
                    "explanation": "Zaryad birligi Sharl Kulon sharafiga Kulon (C) deb ataladi."
                },
                {
                    "question": "Elementar elektr zaryadi e qiymati qanchaga teng?",
                    "options": ["1.6 * 10^(-19) C", "9 * 10^9 C", "3 * 10^8 C", "6.67 * 10^(-11) C"],
                    "correct_index": 0,
                    "explanation": "Elementar zaryad (elektron va proton zaryadi moduli) 1.6 * 10^(-19) Kulonga teng."
                },
                {
                    "question": "Ikki musbat zaryadlangan jism o'zaro qanday ta'sirlashadi?",
                    "options": ["Tortishadi", "Bir-birini itaradi", "Ta'sirlashmaydi", "Neytrallanadi"],
                    "correct_index": 1,
                    "explanation": "Bir xil ishorali zaryadlar elektrostatik jihatdan itarishadi."
                }
            ],
            "tags": ["kulon qonuni", "elektr zaryadi", "elektrostatika", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "phy-007",
            "slug": "om-qonuni-va-elektr-zanjirlari",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "O'zgarmas tok, zanjir qismi uchun Om qonuni va o'tkazgichlarni ulash",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Tok kuchi (I), kuchlanish (U), qarshilik (R) tushunchalari, Om qonuni (I = U/R) hamda o'tkazgichlarni ketma-ket va parallel ulash sxemalarini hisoblash.",
            "theory": "Zaryadlangan zarralarning tartibli yo'nalgan harakati elektr toki deyiladi. Tok kuchi: I = q / t (birligi Amper, A). Elektr kuchlanishi: U = A / q (birligi Volt, V). O'tkazgich qarshiligi uning o'lchamlariga va materialiga bog'liq: R = rho * (l / S) (rho - solishtirma qarshilik). Zanjir qismi uchun Om qonuni: Zanjir qismidagi tok kuchi shu qism uchlaridagi kuchlanishga to'g'ri, qarshilikka teskari proporsional: I = U / R. Ketma-ket ulash: I = const, U = U_1 + U_2, R = R_1 + R_2. Parallel ulash: U = const, I = I_1 + I_2, 1/R = 1/R_1 + 1/R_2 (yoki R = (R_1 * R_2)/(R_1 + R_2)).",
            "examples": [
                {
                    "title": "Om qonunini hisoblash",
                    "problem": "Qarshiligi 44 Om bo'lgan elektr choynak 220 V kuchlanish tarmog'iga ulanganda undan qanday tok o'tadi?",
                    "step_by_step": "1) I = U / R.\n2) I = 220 V / 44 Om = 5 A.",
                    "answer": "5 Amper"
                },
                {
                    "title": "Parallel ulangan rezistorlar qarshiligi",
                    "problem": "Qarshiliklari R_1 = 6 Om va R_2 = 12 Om bo'lgan ikkita o'tkazgich parallel ulangan. Umumiy qarshilikni toping.",
                    "step_by_step": "1) R = (R_1 * R_2) / (R_1 + R_2).\n2) R = (6 * 12) / (6 + 12) = 72 / 18 = 4 Om.",
                    "answer": "4 Om"
                }
            ],
            "exercise": "R_1 = 10 Om va R_2 = 15 Om bo'lgan ikkita rezistor ketma-ket ulangan. Umumiy kuchlanish 50 V bo'lsa, zanjirdagi tok kuchini toping.",
            "exercise_solution": "R_umum = 10 + 15 = 25 Om. I = U / R_umum = 50 / 25 = 2 A.",
            "check_questions": [
                {
                    "question": "Om qonunining matematik ifodasi qaysi?",
                    "options": ["I = U * R", "I = U / R", "U = I / R", "R = I * U"],
                    "correct_index": 1,
                    "explanation": "Zanjir qismi uchun Om qonuni: I = U / R."
                },
                {
                    "question": "Parallel ulangan zanjirda qaysi kattalik barcha tarmoqlarda bir xil bo'ladi?",
                    "options": ["Tok kuchi", "Qarshilik", "Kuchlanish", "Quvvat"],
                    "correct_index": 2,
                    "explanation": "Parallel ulashda barcha o'tkazgichlar bitta tugun juftligiga ulanganligi sababli ulardagi kuchlanish teng bo'ladi (U = const)."
                },
                {
                    "question": "Ampermetr elektr zanjiriga qanday ulanadi?",
                    "options": ["Ketma-ket", "Parallel", "Aralash", "Ulanmaydi"],
                    "correct_index": 0,
                    "explanation": "Ampermetr o'zidan barcha tokni o'tkazishi uchun zanjirga doimo ketma-ket ulanadi."
                }
            ],
            "tags": ["om qonuni", "elektr toki", "qarshilik", "kuchlanish", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "phy-008",
            "slug": "magnit-maydoni-amper-va-lorents-kuchlari",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "Magnit maydoni, magnit induksiyasi, Amper va Lorents kuchlari",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Tokli o'tkazgichning magnit maydoni, o'ng qo'l va chap qo'l qoidalari, Amper kuchi (F_A) va harakatlanayotgan zaryadga ta'sir etuvchi Lorents kuchini hisoblash.",
            "theory": "Harakatlanayotgan zaryadlar (elektr toki) atrofida magnit maydoni vujudga keladi. Magnit maydonining asosiy kuch xarakteristikasi magnit induksiya vektori B deyiladi (birligi Tesla, Tl). Magnit maydonida tokli o'tkazgichga ta'sir qiluvchi kuch Amper kuchi deyiladi: F_A = I * B * L * sin(alpha) (L - o'tkazgich uzunligi, alpha - B va o'tkazgich orasidagi burchak). Magnit maydonida v tezlik bilan harakatlanayotgan q zaryadga ta'sir etuvchi kuch Lorents kuchi deyiladi: F_L = |q| * v * B * sin(alpha). Amper va Lorents kuchlarining yo'nalishi chap qo'l qoidasi yordamida aniqlanadi: chap qo'l kaftiga magnit induksiya chiziqlari kirsa, to'rtta cho'zilgan barmoq musbat zaryad harakati (yoki tok) yo'nalishini ko'rsatsa, 90° ga ochilgan bosh barmoq kuch yo'nalishini ko'rsatadi.",
            "examples": [
                {
                    "title": "Amper kuchini topish",
                    "problem": "Induksiyasi B = 0.5 Tl bo'lgan bir jinsli magnit maydoniga maydon chiziqlariga perpendikulyar qilib uzunligi L = 0.4 m bo'lgan o'tkazgich joylashtirilgan. Undan I = 3 A tok o'tganda ta'sir etuvchi Amper kuchini toping.",
                    "step_by_step": "1) alpha = 90°, sin(90°) = 1.\n2) F_A = I * B * L * sin(alpha) = 3 * 0.5 * 0.4 * 1 = 0.6 N.",
                    "answer": "0.6 N"
                },
                {
                    "title": "Lorents kuchi ta'sirida harakat",
                    "problem": "Proton 0.2 Tl induksiyali magnit maydoniga chiziqlarga perpendikulyar ravishda 10^6 m/s tezlik bilan uchib kirdi. Unga ta'sir etuvchi Lorents kuchini toping (q_p = 1.6 * 10^(-19) C).",
                    "step_by_step": "1) F_L = q * v * B * sin(90°).\n2) F_L = 1.6 * 10^(-19) * 10^6 * 0.2 * 1 = 3.2 * 10^(-14) N.",
                    "answer": "3.2 * 10^(-14) N"
                }
            ],
            "exercise": "Tokli o'tkazgich magnit induksiya chiziqlariga parallel joylashtirilgan (alpha = 0°). Unga ta'sir etuvchi Amper kuchi nimaga teng?",
            "exercise_solution": "sin(0°) = 0 bo'lgani uchun F_A = I * B * L * 0 = 0 N.",
            "check_questions": [
                {
                    "question": "Magnit induksiyasining SI dagi birligi nima?",
                    "options": ["Veber", "Genri", "Tesla", "Ersted"],
                    "correct_index": 2,
                    "explanation": "Magnit induksiya birligi Nikola Tesla sharafiga Tesla (Tl) deb ataladi."
                },
                {
                    "question": "Amper kuchining yo'nalishi qaysi qoida bilan aniqlanadi?",
                    "options": ["O'ng qo'l qoidasi", "Chap qo'l qoidasi", "Parallelogramm qoidasi", "Burama qoidasi"],
                    "correct_index": 1,
                    "explanation": "Amper va Lorents kuchlari yo'nalishi chap qo'l qoidasi orqali topiladi."
                },
                {
                    "question": "Tinch turgan zaryadga bir jinsli doimiy magnit maydoni qanday kuch bilan ta'sir qiladi?",
                    "options": ["F = q*B", "F = 0", "F = q/B", "Cheksiz katta kuch bilan"],
                    "correct_index": 1,
                    "explanation": "v = 0 bo'lganda F_L = q*v*B*sin(alpha) = 0 bo'ladi. Magnit maydoni faqat harakatdagi zaryadga ta'sir qiladi."
                }
            ],
            "tags": ["magnit maydoni", "amper kuchi", "lorents kuchi", "tesla", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "phy-009",
            "slug": "geometrik-optika-va-yoruglik-qonunlari",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "Geometrik optika: yorug'likning qaytishi, sinishi va yupqa linza",
            "grade_level": "9-sinf",
            "difficulty": "O'rta",
            "objective": "Yorug'likning to'g'ri chiziqli tarqalishi, qaytish va sinish qonunlari (Snellius) hamda yupqa linza formulasini (1/F = 1/d + 1/f) qo'llash.",
            "theory": "Yorug'lik bir jinsli shaffof muhitda to'g'ri chiziq bo'ylab tarqaladi. Qaytish qonuni: Tushuvchi nur, qaytgan nur va tushish nuqtasiga o'tkazilgan perpendikulyar bitta tekislikda yotadi; qaytish burchagi tushish burchagiga teng (alpha = beta). Sinish qonuni (Snellius): sin(alpha) / sin(gamma) = n_2 / n_1 = n_21 (bu yerda n - muhitning sindirish ko'rsatkichi, n = c / v). Yupqa linza: Qavariq (yig'uvchi) va botiq (sochuvchi) linzalar. Yupqa linza formulasi: +- 1/F = 1/d +- 1/f (bu yerda F - fokus masofasi, d - buyumdan linzagacha masofa, f - tasvirdan linzagacha masofa). Linza optik kuchi: D = 1 / F (birligi Dioptriya, dptr).",
            "examples": [
                {
                    "title": "Yupqa linza formulasini qo'llash",
                    "problem": "Fokus masofasi F = 20 sm bo'lgan yig'uvchi linzadan buyum d = 30 sm masofada turibdi. Tasvir linzadan qanday masofada hosil bo'ladi?",
                    "step_by_step": "1) 1/F = 1/d + 1/f => 1/f = 1/F - 1/d.\n2) 1/f = 1/20 - 1/30 = (3 - 2) / 60 = 1/60.\n3) f = 60 sm.",
                    "answer": "60 sm"
                },
                {
                    "title": "Linzaning optik kuchi",
                    "problem": "Fokus masofasi 50 sm bo'lgan yig'uvchi linzaning optik kuchini toping.",
                    "step_by_step": "1) F = 50 sm = 0.5 m.\n2) D = 1 / F = 1 / 0.5 m = +2 dptr.",
                    "answer": "+2 dioptriya"
                }
            ],
            "exercise": "Suvning sindirish ko'rsatkichi n = 4/3. Yorug'likning suvdagi tezligini toping (c = 3 * 10^8 m/s).",
            "exercise_solution": "v = c / n = 3 * 10^8 / (4/3) = 2.25 * 10^8 m/s.",
            "check_questions": [
                {
                    "question": "Linza optik kuchining birligi nima?",
                    "options": ["Metr", "Fokus", "Dioptriya", "Lyuks"],
                    "correct_index": 2,
                    "explanation": "Optik kuch birligi dioptriya (dptr = 1/m) dir."
                },
                {
                    "question": "Yassi ko'zguda hosil bo'lgan tasvir qanday xususiyatga ega?",
                    "options": ["Haqiqiy, to'ntarilgan, kattalashgan", "Mavhum, to'g'ri, o'lchami teng", "Haqiqiy, to'g'ri, kichraygan", "Mavhum, to'ntarilgan"],
                    "correct_index": 1,
                    "explanation": "Yassi ko'zgu doimo o'lchami jismga teng bo'lgan mavhum va to'g'ri tasvir beradi."
                },
                {
                    "question": "Vakuumda yorug'lik tezligi qanchaga teng?",
                    "options": ["300 km/s", "300 000 km/s", "150 000 km/s", "3 000 000 km/s"],
                    "correct_index": 1,
                    "explanation": "c = 3 * 10^8 m/s = 300 000 km/s."
                }
            ],
            "tags": ["optika", "linza", "yorug'lik", "sinish qonuni", "9-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "phy-010",
            "slug": "atom-va-yadro-fizikasi-radioaktivlik",
            "subject_id": "sub-05",
            "subject_name": "Fizika",
            "title": "Atom va yadro fizikasi, radioaktiv yemirilish qonuni",
            "grade_level": "11-sinf",
            "difficulty": "Murakkab",
            "objective": "Atomning Rezerford planetar modeli, yadro tuzilishi (proton va neytronlar), bog'lanish energiyasi va radioaktiv yemirilish qonunini o'zlashtirish.",
            "theory": "Rezerford tajribalari asosida atomning planetar modeli yaratilgan: markazda musbat zaryadlangan og'ir yadro, uning atrofida orbitallarda elektronlar harakatlanadi. Atom yadrosi nuklonlardan — musbat zaryadli protonlar (Z) va zaryadsiz neytronlardan (N) tashkil topgan. Massa soni: A = Z + N. Yadro massasi uni tashkil etuvchi alohida nuklonlar massalari yig'indisidan kichik bo'ladi (massa defekti): Delta_m = Z*m_p + N*m_n - M_yadro. Eynshteyn formulasi bo'yicha yadro bog'lanish energiyasi: E_bog' = Delta_m * c^2. Radioaktiv yemirilish qonuni: N(t) = N_0 * 2^(-t / T) (bu yerda T - yarim yemirilish davri, N_0 - dastlabki yadrolar soni).",
            "examples": [
                {
                    "title": "Radioaktiv yemirilish masalasi",
                    "problem": "Radioaktiv izotopning yarim yemirilish davri 4 kun. 16 kundan keyin dastlabki atom yadrolarining necha foizi parchalanmay qoladi?",
                    "step_by_step": "1) t = 16 kun, T = 4 kun. t / T = 16 / 4 = 4 ta yarim yemirilish davri o'tgan.\n2) N = N_0 * (1/2)^4 = N_0 / 16.\n3) Foizda: (1/16) * 100% = 6.25%.",
                    "answer": "6.25%"
                },
                {
                    "title": "Yadro tarkibini aniqlash",
                    "problem": "Uran-235 (92_U_235) atomi yadrosida nechta proton va nechta neytron bor?",
                    "step_by_step": "1) Z = 92 (protonlar soni).\n2) A = 235 (massa soni).\n3) N = A - Z = 235 - 92 = 143 ta neytron.",
                    "answer": "92 ta proton, 143 ta neytron"
                }
            ],
            "exercise": "Alfa yemirilishda uran yadrosi (92_U_238) alfa zarracha (2_He_4) chiqarib qaysi elementga aylanadi?",
            "exercise_solution": "Z_yangi = 92 - 2 = 90 (Toriy - Th). A_yangi = 238 - 4 = 234. Hosil bo'ladi: 90_Th_234.",
            "check_questions": [
                {
                    "question": "Eynshteynning massa va energiya bog'liqlik formulasi qaysi?",
                    "options": ["E = m * v", "E = m * c^2", "E = (m * c^2) / 2", "E = h * v"],
                    "correct_index": 1,
                    "explanation": "E = m*c^2 zamonaviy fizikaning eng mashhur tenglamalaridan biridir."
                },
                {
                    "question": "Yadroda neytronlar qanday zaryadga ega?",
                    "options": ["Musbat (+)", "Manfiy (-)", "Zaryadsiz (neytral)", "O'zgaruvchan"],
                    "correct_index": 2,
                    "explanation": "Neytron elektr jihatdan neytral zarracha bo'lib, uning zaryadi nolga teng."
                },
                {
                    "question": "Yarim yemirilish davri T o'tganda dastlabki yadrolarning qancha qismi parchalanadi?",
                    "options": ["25%", "50%", "75%", "100%"],
                    "correct_index": 1,
                    "explanation": "Yarim yemirilish davrida dastlabki radioaktiv yadrolarning 50% i parchalanadi."
                }
            ],
            "tags": ["yadro fizikasi", "radioaktivlik", "eynshteyn", "11-sinf"],
            "duration_minutes": 35
        },

        # ASTRONOMIYA (5)
        {
            "id": "phy-011",
            "slug": "quyosh-tizimi-va-sayyoralar-tasnifi",
            "subject_id": "sub-06",
            "subject_name": "Astronomiya",
            "title": "Quyosh tizimining tuzilishi, yer guruhi va gigant sayyoralar",
            "grade_level": "10-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Quyosh tizimi arxitekturasi, sayyoralarning tasnifi (Yer guruhi va Gaz gigantlari) hamda asteroidlar va kometalarni o'rganish.",
            "theory": "Quyosh tizimi markaziy yulduz — Quyosh va uning atrofida aylanuvchi 8 ta katta sayyora, mitti sayyoralar, asteroidlar, kometalar va meteoroidlardan iborat. Sayyoralar ikki guruhga bo'linadi: 1) Yer guruhi sayyoralari (Merkuriy, Venera, Yer, Mars) — qattiq toshli sirtga, kichik o'lchamga, yuqori zichlikka va kam sonli yo'ldoshlarga ega; 2) Gigant sayyoralar (Yupiter, Saturn, Uran, Neptun) — asosan vodorod, geliy va muzlardan tashkil topgan, katta o'lchamli, past zichlikli, ko'plab yo'ldoshlar va halqalarga ega. Mars va Yupiter orbitalari oralig'ida Asosiy asteroidlar belbog'i, Neptun orbitasidan tashqarida esa Koyper belbog'i joylashgan.",
            "examples": [
                {
                    "title": "Astronomik birlik (a.b.) tushunchasi",
                    "problem": "Yer va Quyosh orasidagi o'rtacha masofa 150 mln km ga teng. Quyosh nuri Yergacha qancha vaqtda yetib keladi (c = 300 000 km/s)?",
                    "step_by_step": "1) Masofa: S = 150 000 000 km.\n2) Vaqt: t = S / c = 150 000 000 / 300 000 = 500 sekund.\n3) 500 sekund = 8 minut 20 sekund.",
                    "answer": "8 minut 20 sekund"
                },
                {
                    "title": "Sayyoralar ketma-ketligi",
                    "problem": "Quyoshdan uzoqlashish tartibida 8 ta sayyorani joylashtiring.",
                    "step_by_step": "1. Merkuriy, 2. Venera, 3. Yer, 4. Mars, 5. Yupiter, 6. Saturn, 7. Uran, 8. Neptun.",
                    "answer": "Merkuriy, Venera, Yer, Mars, Yupiter, Saturn, Uran, Neptun"
                }
            ],
            "exercise": "Quyosh tizimidagi eng katta va eng kichik sayyoralarni ko'rsating.",
            "exercise_solution": "Eng katta sayyora — Yupiter (gaz giganti), eng kichik sayyora — Merkuriy.",
            "check_questions": [
                {
                    "question": "Quyosh tizimida nechta asosiy sayyora mavjud?",
                    "options": ["7 ta", "8 ta", "9 ta", "10 ta"],
                    "correct_index": 1,
                    "explanation": "2006-yilda Xalqaro Astronomiya Ittifoqi Plutonni mitti sayyora toifasiga o'tkazgach, 8 ta sayyora qoldi."
                },
                {
                    "question": "Qaysi sayyora o'zining ajoyib yorqin halqalari bilan mashhur?",
                    "options": ["Mars", "Saturn", "Merkuriy", "Venera"],
                    "correct_index": 1,
                    "explanation": "Saturn sayyorasi muz va chang zarralaridan iborat keng ko'lamli halqalar tizimiga ega."
                },
                {
                    "question": "1 Astronomik Birlik (a.b.) nimaga teng?",
                    "options": ["Oy va Yer orasidagi masofa", "Yer va Quyosh orasidagi o'rtacha masofa", "Yorug'likning 1 yilda bosib o'tgan yo'li", "Quyosh diametri"],
                    "correct_index": 1,
                    "explanation": "1 a.b. Yer bilan Quyosh orasidagi o'rtacha masofa bo'lib, taxminan 149.6 mln km ga teng."
                }
            ],
            "tags": ["astronomiya", "quyosh tizimi", "sayyoralar", "yupiter", "10-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "phy-012",
            "slug": "kepler-qonunlari-va-osmon-mexanikasi",
            "subject_id": "sub-06",
            "subject_name": "Astronomiya",
            "title": "Kepler qonunlari va osmon jismlarining harakati",
            "grade_level": "11-sinf",
            "difficulty": "O'rta",
            "objective": "Iogann Kepler tomonidan kashf etilgan 3 ta osmon mexanikasi qonunini va sayyoralarning orbital davrlarini hisoblashni bilish.",
            "theory": "Keplerning I qonuni: Barcha sayyoralar Quyosh atrofida ellipslar bo'ylab harakatlanadi, Quyosh bu ellipsning fokuslaridan birida joylashgan. Sayyoraning Quyoshga eng yaqin nuqtasi perigeliy, eng uzoq nuqtasi afeliy deyiladi. Keplerning II qonuni (yuzalar qonuni): Sayyoraning radius-vektori teng vaqt oraliqlarida teng yuzalarni chizib o'tadi (buning natijasida sayyora perigeliyda eng tez, afeliyda eng sekin harakatlanadi). Keplerning III qonuni: Sayyoralarning Quyosh atrofida to'liq aylanish davrlarining kvadratlari ularning orbitalari katta yarim o'qlarining kublariga to'g'ri proporsionaldir: (T_1^2 / T_2^2) = (a_1^3 / a_2^3).",
            "examples": [
                {
                    "title": "Keplerning III qonunini qo'llash",
                    "problem": "Sayyoraning Quyoshgacha bo'lgan o'rtacha masofasi Yernikidan 4 marta katta bo'lsa (a = 4 a.b.), uning Quyosh atrofida aylanish davri necha Yer yiliga teng?",
                    "step_by_step": "1) (T^2 / 1^2) = (4^3 / 1^3).\n2) T^2 = 64.\n3) T = sqrt(64) = 8 yil.",
                    "answer": "8 yil"
                },
                {
                    "title": "Orbital tezlik o'zgarishi",
                    "problem": "Yer Quyoshga qish faslida (yanvar oyida) yaqinroq, yoz faslida (iyul oyida) uzoqroq bo'ladi. Yer qachon tezroq harakatlanadi?",
                    "step_by_step": "Keplerning II qonuniga ko'ra Quyoshga yaqin (perigeliy) bo'lganda orbital tezlik maksimal bo'ladi, demak yanvar oyida tezroq harakatlanadi.",
                    "answer": "Yanvar oyida (perigeliyda)"
                }
            ],
            "exercise": "Agar sayyora Quyoshdan 9 a.b. masofada joylashgan bo'lsa, uning aylanish davrini toping.",
            "exercise_solution": "T^2 = a^3 = 9^3 = 729 => T = sqrt(729) = 27 yil.",
            "check_questions": [
                {
                    "question": "Sayyoraning Quyoshga eng yaqin orbital nuqtasi nima deb ataladi?",
                    "options": ["Afeliy", "Perigeliy", "Zenit", "Nadir"],
                    "correct_index": 1,
                    "explanation": "Quyosh atrofidagi orbitaning Quyoshga eng yaqin nuqtasi perigeliy deyiladi."
                },
                {
                    "question": "Keplerning III qonuni qaysi nisbatni ifodalaydi?",
                    "options": ["T_1 / T_2 = a_1 / a_2", "T_1^2 / T_2^2 = a_1^3 / a_2^3", "T_1^3 / T_2^3 = a_1^2 / a_2^2", "T_1 * a_1 = T_2 * a_2"],
                    "correct_index": 1,
                    "explanation": "Davrlar kvadratlari nisbati katta yarim o'qlar kublari nisbatiga teng: T^2 ~ a^3."
                },
                {
                    "question": "Keplerning birinchi qonuniga ko'ra sayyoralar qanday trayektoriya bo'ylab harakatlanadi?",
                    "options": ["Aylana", "Ellips", "Parabola", "To'g'ri chiziq"],
                    "correct_index": 1,
                    "explanation": "Kepler I qonuniga ko'ra sayyoralar ellipssimon orbita bo'ylab harakatlanadi."
                }
            ],
            "tags": ["kepler qonunlari", "osmon mexanikasi", "orbital davr", "11-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "phy-013",
            "slug": "yulduzlar-evolyutsiyasi-va-gershprung-rassell-diagrammasi",
            "subject_id": "sub-06",
            "subject_name": "Astronomiya",
            "title": "Yulduzlar evolyutsiyasi, spektral sinflar va Gershprung-Rassell diagrammasi",
            "grade_level": "11-sinf",
            "difficulty": "Murakkab",
            "objective": "Yulduzlarning paydo bo'lishi (gravitatsion siqilish), bosh ketma-ketlik, qizil gigantlar, oq mitti, neytron yulduzlar va qora tuynuklarni tushunish.",
            "theory": "Yulduzlar gaz va chang bulutlarining (tumanliklarning) gravitatsion siqilishi natijasida paydo bo'ladi. Yadroda termoyadroviy reaksiya (vodorodning geliyga aylanishi) boshlanishi bilan yulduz bosh ketma-ketlikka o'tadi. Gershprung-Rassell (G-R) diagrammasi yulduzlarning yorqinligi (absolyut yulduz kattaligi) va ularning sirt temperaturasi (spektral sinfi: O, B, A, F, G, K, M) orasidagi bog'liqlikni aks ettiradi. Quyosh — G2V sinfidagi sariq mitti yulduz. Yulduz evolyutsiyasi uning massasiga bog'liq: Quyosh massasidagi yulduzlar qizil gigantga aylanib, oxirida oq mittiga aylanadi; massasi juda katta yulduzlar esa o'ta yangi yulduz (Supernova) sifatida portlab, neytron yulduz (pulsar) yoki qora tuynuk hosil qiladi.",
            "examples": [
                {
                    "title": "Quyoshning kelajakdagi evolyutsiyasi",
                    "problem": "Quyosh taxminan 5 milliard yildan keyin qanday bosqichlarni bosib o'tadi?",
                    "step_by_step": "1) Yadroda vodorod tugagach, Quyosh kengayib qizil gigant bosqichiga o'tadi.\n2) Tashqi qatlamlarini tashlab, sayyorasimon tumanlik hosil qiladi.\n3) Yadrosi siqilib, Yer kattaligidagi oq mittiga aylanadi va asta-sekin soviydi.",
                    "answer": "Qizil gigant -> Sayyorasimon tumanlik -> Oq mitti"
                },
                {
                    "title": "Yulduzlar spektral sinfi",
                    "problem": "Eng issiq (ko'k) va eng sovuq (qizil) yulduzlar qaysi spektral sinfga kiradi?",
                    "step_by_step": "Klassik shkala: O - B - A - F - G - K - M. Eng issiq: O sinfi (30 000 K dan yuqori, ko'k), eng sovuq: M sinfi (3000 K atrofida, qizil).",
                    "answer": "O (eng issiq) va M (eng sovuq)"
                }
            ],
            "exercise": "Massasi Quyoshnikidan 20 marta katta bo'lgan o'ta og'ir yulduz umri oxirida nimaga aylanadi?",
            "exercise_solution": "O'ta yangi yulduz portlashidan so'ng uning yadrosi gravitatsion kollapsga uchrab qora tuynuk (Black Hole) hosil qiladi.",
            "check_questions": [
                {
                    "question": "Quyosh qaysi spektral sinfga tegishli?",
                    "options": ["O", "A", "G", "M"],
                    "correct_index": 2,
                    "explanation": "Quyosh G sinfidagi (aniqrog'i G2V) sariq mitti yulduzdir."
                },
                {
                    "question": "Gershprung-Rassell diagrammasida yulduzlarning qaysi xarakteristikalari solishtiriladi?",
                    "options": ["Massa va radius", "Yorqinlik va sirt temperaturasi", "Yoshi va masofasi", "Tezligi va zichligi"],
                    "correct_index": 1,
                    "explanation": "G-R diagrammasi yulduz yorqinligi (yoki absolyut kattaligi) bilan uning spektral sinfi (temperaturasi) bog'lanishidir."
                },
                {
                    "question": "O'ta yangi yulduz portlashidan so'ng hosil bo'ladigan o'ta zich aylanuvchi yulduz nima deyiladi?",
                    "options": ["Oq mitti", "Neytron yulduz (pulsar)", "Qizil mitti", "Protoyulduz"],
                    "correct_index": 1,
                    "explanation": "Neytron yulduzlar atom yadrosi zichligiga ega bo'lgan o'ta ixcham va kuchli magnit maydonli yulduzlardir."
                }
            ],
            "tags": ["yulduzlar", "evolyutsiya", "gershprung rassell", "qora tuynuk", "11-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "phy-014",
            "slug": "galaktikalar-somon-yoli-va-koinot-tuzilishi",
            "subject_id": "sub-06",
            "subject_name": "Astronomiya",
            "title": "Bizning Galaktika — Somon yo'li va koinotning yirik masshtabli tuzilishi",
            "grade_level": "11-sinf",
            "difficulty": "O'rta",
            "objective": "Somon yo'lining spiralli tuzilishi, yulduzlar to'dalari, galaktikalar turlari (Xabbl klassifikatsiyasi) va mahalliy guruhni o'rganish.",
            "theory": "Gravitatsiya kuchi orqali bog'langan milliardlab yulduzlar, gaz va chang to'plami galaktika deyiladi. Biz yashaydigan Somon yo'li galaktikasi to'siqli spiral (SBbc) galaktika bo'lib, diametri taxminan 100 000 yorug'lik yiliga teng va unda 200-400 milliard yulduz bor. Markazida massasi 4 million Quyosh massasiga teng bo'lgan o'ta massiv qora tuynuk (Sagittarius A*) joylashgan. Edvin Xabbl galaktikalarni shakliga ko'ra 3 ta asosiy turga ajratgan: 1) Elliptik (E), 2) Spiral (S va SB), 3) Noto'g'ri (Irr). Somon yo'li, Andromeda galaktikasi (M31) va Uchburchak galaktikasi (M33) 50 dan ortiq mitti galaktikalar bilan birga Mahalliy Galaktikalar Guruhini tashkil etadi.",
            "examples": [
                {
                    "title": "Yorug'lik yili masofasi",
                    "problem": "1 yorug'lik yili taxminan necha kilometrga teng (c = 300 000 km/s, 1 yil = 365.25 kun)?",
                    "step_by_step": "1) 1 yil = 365.25 * 24 * 3600 s = 31 557 600 sekund.\n2) S = c * t = 300 000 km/s * 31 557 600 s = 9.46 * 10^12 km (taxminan 9.5 trillion km).",
                    "answer": "9.46 trillion km"
                },
                {
                    "title": "Andromeda galaktikasi bilan to'qnashuv",
                    "problem": "Bizga eng yaqin yirik spiral galaktika qaysi va u necha yorug'lik yili uzoqlikda joylashgan?",
                    "step_by_step": "Eng yaqin spiral galaktika — Andromeda (M31), u taxminan 2.5 million yorug'lik yili masofada joylashgan va Somon yo'liga qarab yaqinlashmoqda.",
                    "answer": "Andromeda galaktikasi (2.5 mln yorug'lik yili)"
                }
            ],
            "exercise": "Somon yo'li markazidagi o'ta massiv qora tuynuk qaysi yulduz turkumida joylashgan?",
            "exercise_solution": "Qavs (Sagittarius) yulduz turkumi yo'nalishida joylashgan bo'lib, Sagittarius A* deb nomlanadi.",
            "check_questions": [
                {
                    "question": "Somon yo'li qaysi turdagi galaktikalarga kiradi?",
                    "options": ["Elliptik", "Spiral (to'siqli spiral)", "Noto'g'ri", "Sferik"],
                    "correct_index": 1,
                    "explanation": "Somon yo'li markaziy to'siqqa ega bo'lgan spiral galaktika (SB) turiga kiradi."
                },
                {
                    "question": "Galaktikalarni morfologik tasniflagan olim kim?",
                    "options": ["Galiley", "Isaak Nyuton", "Edvin Xabbl", "Iogann Kepler"],
                    "correct_index": 2,
                    "explanation": "Edvin Xabbl galaktikalarning mashhur 'kameron' (tyuning-fork) klassifikatsiyasini ishlab chiqqan."
                },
                {
                    "question": "Somon yo'li diametri taxminan qancha?",
                    "options": ["10 000 yorug'lik yili", "100 000 yorug'lik yili", "1 000 000 yorug'lik yili", "1000 a.b."],
                    "correct_index": 1,
                    "explanation": "Bizning Galaktikamiz diskining diametri taxminan 100 000 yorug'lik yiliga teng."
                }
            ],
            "tags": ["galaktika", "somon yo'li", "andromeda", "xabbl", "11-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "phy-015",
            "slug": "zamonaviy-kosmologiya-va-katta-portlash-nazariyasi",
            "subject_id": "sub-06",
            "subject_name": "Astronomiya",
            "title": "Zamonaviy kosmologiya, Katta portlash va koinotning kengayishi",
            "grade_level": "11-sinf",
            "difficulty": "Murakkab",
            "objective": "Xabbl qonuni (v = H_0 * r), qizilga siljish hodisasi, relikt nurlanish va qorong'u energiya hamda qorong'u materiya mohiyatini tushunish.",
            "theory": "Kosmologiya butun Koinotning paydo bo'lishi, tuzilishi va evolyutsiyasini o'rganadigan fandir. 1929-yilda Edvin Xabbl uzoq galaktikalar spektrida qizilga siljishni kashf etdi, bu esa barcha galaktikalar bir-biridan uzoqlashayotganini (Koinot kengayayotganini) ko'rsatdi. Xabbl qonuni: v = H_0 * r (bu yerda v - uzoqlashish tezligi, r - masofa, H_0 - Xabbl doimiysi, taxminan 70 km/(s*Mpk)). Katta portlash (Big Bang) nazariyasiga ko'ra, Koinot bundan taxminan 13.8 milliard yil oldin cheksiz yuqori zichlik va haroratga ega singulyarlik holatidan vujudga kelgan. Katta portlashning asosiy isbotlari: 1) Galaktikalarning qizilga siljishi (kengayish), 2) Relikt (kosmik mikroto'lqinli fon) nurlanishi (T = 2.7 K), 3) Birlamchi elementlar (vodorod va geliy) nisbati. Zamonaviy koinot tarkibi: ~68% qorong'u energiya, ~27% qorong'u materiya, faqat ~5% odatiy (barion) modda.",
            "examples": [
                {
                    "title": "Xabbl qonuni bo'yicha masofani topish",
                    "problem": "Bizdan v = 14 000 km/s tezlik bilan uzoqlashayotgan galaktikagacha bo'lgan masofani toping (H_0 = 70 km/(s * Mpk)).",
                    "step_by_step": "1) v = H_0 * r => r = v / H_0.\n2) r = 14 000 / 70 = 200 Megaparsek (Mpk).\n3) 1 Mpk taxminan 3.26 million yorug'lik yili, demak r = 652 million yorug'lik yili.",
                    "answer": "200 Mpk (652 mln yorug'lik yili)"
                },
                {
                    "title": "Koinotning yoshi",
                    "problem": "Xabbl doimiysiga ko'ra Koinot yoshi t_0 qanday baholanadi?",
                    "step_by_step": "Xabbl vaqti: t_H = 1 / H_0. H_0 = 70 km/(s*Mpk) o'tkazilganda t_H taxminan 13.8 - 14 milliard yilni tashkil qiladi.",
                    "answer": "Taxminan 13.8 milliard yil"
                }
            ],
            "exercise": "Relikt nurlanish qanday haroratga ega bo'lgan qora jism nurlanishiga mos keladi?",
            "exercise_solution": "Relikt nurlanish harorati taxminan 2.725 Kelvin (-270.4 °C) ga teng.",
            "check_questions": [
                {
                    "question": "Koinotning yoshi taxminan necha milliard yil?",
                    "options": ["4.5 milliard", "13.8 milliard", "20 milliard", "100 milliard"],
                    "correct_index": 1,
                    "explanation": "Zamonaviy astrofizik o'lchovlar (Planck missiyasi) bo'yicha Koinot yoshi 13.787 +- 0.020 milliard yil."
                },
                {
                    "question": "Uzoq galaktikalar spektridagi chiziqlarning qizil tomonga siljishi nimani anglatadi?",
                    "options": ["Galaktikalar bizga yaqinlashayotganini", "Galaktikalar bizdan uzoqlashayotganini", "Yulduzlar sovuqlashayotganini", "Yorug'lik yutilayotganini"],
                    "correct_index": 1,
                    "explanation": "Doppler effekti bo'yicha manba uzoqlashganda to'lqin uzunligi ortadi va spektr qizil tomonga siljiydi."
                },
                {
                    "question": "Koinotning tezlanuvchan kengayishiga sababchi bo'lgan noma'lum substansiya nima deyiladi?",
                    "options": ["Qorong'u materiya", "Qorong'u energiya", "Antimateriya", "Efir"],
                    "correct_index": 1,
                    "explanation": "Koinotning tezlanuvchan kengayishini ta'minlovchi manfiy bosimli omil qorong'u energiya deb ataladi."
                }
            ],
            "tags": ["kosmologiya", "katta portlash", "xabbl qonuni", "relikt nurlanish", "11-sinf"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_physics_astronomy_materials()
    print(f"Generated {len(mats)} Physics/Astronomy materials.")
