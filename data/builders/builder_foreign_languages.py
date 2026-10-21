# -*- coding: utf-8 -*-
"""
Builder for Ingliz va boshqa xorijiy tillar (20 materials: lng-001 to lng-020)
- sub-17: Ingliz tili (8: lng-001 to lng-008)
- sub-18: Rus tili (4: lng-009 to lng-012)
- sub-19: Qoraqalpoq tili va adabiyoti (2: lng-013 to lng-014)
- sub-20: Nemis tili (2: lng-015 to lng-016)
- sub-21: Fransuz tili (2: lng-017 to lng-018)
- sub-22: Chet tili grammatikasi (2: lng-019 to lng-020)
"""

def get_foreign_languages_materials():
    materials = [
        # INGLIZ TILI (8)
        {
            "id": "lng-001",
            "slug": "present-simple-tense-and-daily-routines",
            "subject_id": "sub-17",
            "subject_name": "Ingliz tili",
            "title": "Present Simple Tense: Grammar, Daily Routines and Adverbs of Frequency",
            "grade_level": "5-sinf / A1",
            "difficulty": "Boshlang'ich",
            "objective": "Present Simple zamonining tuzilishi, 3-shaxs birlikda -s/-es qo'shimchasi, inkor va so'roq shakllari (do/does) hamda kundalik odatlarni ifodalash.",
            "theory": "Present Simple (Oddiy hozirgi zamon) doimiy takrorlanuvchi harakatlar, umumiy haqiqatlar va odatlarni ifodalash uchun ishlatiladi. Formulalar:\n- Darak gap: I / You / We / They + V1 (fe'lning asosiy shakli); He / She / It + V1 + -s / -es (masalan: He plays, She watches).\n- Inkor gap: I / You / We / They + do not (don't) + V1; He / She / It + does not (doesn't) + V1.\n- So'roq gap: Do + I / you / we / they + V1? Does + he / she / it + V1?\nVaqt ko'rsatkichlari (Frequency adverbs): always (doimo), usually (odatda), often (tez-tez), sometimes (ba'zan), never (hech qachon), every day/week (har kuni/hafta). Odatda fe'ldan oldin keladi: 'I always wake up at 7 AM'. 'To be' fe'lidan keyin keladi: 'She is always happy'.",
            "examples": [
                {
                    "title": "3-shaxs birlikda fe'l o'zgarishi",
                    "problem": "'He (go) to school by bus every morning' gapini to'g'ri shaklga keltiring.",
                    "step_by_step": "Ega 'He' (3-shaxs birlik) bo'lgani uchun 'go' fe'liga -es qo'shiladi: 'goes'.\nNatija: 'He goes to school by bus every morning'.",
                    "answer": "He goes to school by bus every morning"
                },
                {
                    "title": "Inkor va so'roq shakl",
                    "problem": "'She likes ice cream' gapini inkor va so'roq shaklga aylantiring.",
                    "step_by_step": "Inkor: 'She does not (doesn't) like ice cream' (asosiy fe'ldagi -s tushib qoladi).\nSo'roq: 'Does she like ice cream?'",
                    "answer": "Doesn't like / Does she like...?"
                }
            ],
            "exercise": "Qavslarni oching: 'They (not / play) football on rainy days, but Tom always (watch) matches on TV.'",
            "exercise_solution": "'They don't play football on rainy days, but Tom always watches matches on TV.'",
            "check_questions": [
                {
                    "question": "He/She/It olmoshlaridan keyin Present Simple da qaysi yordamchi fe'l qo'llanadi?",
                    "options": ["do", "does", "is", "have"],
                    "correct_index": 1,
                    "explanation": "3-shaxs birlikda inkor va so'roqda 'does' (doesn't) ishlatiladi."
                },
                {
                    "question": "'Water ... at 100 degrees Celsius' gapidagi nuqtalar o'rniga qaysi fe'l mos keladi?",
                    "options": ["boil", "boils", "boiling", "is boiling"],
                    "correct_index": 1,
                    "explanation": "Tabiat qonuni va ilmiy haqiqat bo'lgani uchun Present Simple qo'llanadi: Water boils."
                },
                {
                    "question": "'Never' so'zi qatnashgan gapda inkor 'not' yuklamasi ishlatiladimi?",
                    "options": ["Ha, doimo", "Yo'q, chunki 'never' ning o'zi inkor ma'noga ega", "Faqat so'roq gapda", "Farqi yo'q"],
                    "correct_index": 1,
                    "explanation": "Ingliz tilida bitta gapda ikkita inkor bo'lmaydi: 'I never drink coffee' (not kerak emas)."
                }
            ],
            "tags": ["english", "grammar", "present simple", "verbs", "A1", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "lng-002",
            "slug": "present-continuous-vs-present-simple",
            "subject_id": "sub-17",
            "subject_name": "Ingliz tili",
            "title": "Present Continuous Tense and State Verbs (Stative vs Dynamic)",
            "grade_level": "6-sinf / A2",
            "difficulty": "Boshlang'ich",
            "objective": "Ayni paytda sodir bo'layotgan harakatlar (am/is/are + V-ing), vaqtinchalik holatlar hamda davomli zamonda ishlatilmaydigan holat fe'llari (Stative verbs)ni o'rganish.",
            "theory": "Present Continuous (Hozirgi davomli zamon) nutq paytida davom etayotgan harakatlar yoki ayni kunlardagi vaqtinchalik jarayonlar uchun ishlatiladi. Formulalar:\n- Darak: Subject + am / is / are + Verb-ing (I am studying, He is reading, They are playing).\n- Inkor: Subject + am not / isn't / aren't + Verb-ing.\n- So'roq: Am / Is / Are + Subject + Verb-ing?\nVaqt ko'rsatkichlari: now (hozir), at the moment (ayni paytda), currently, right now, Look!, Listen!\nMUHIM: State verbs (holat fe'llari) his-tuyg'u, aqliy faoliyat va egalikni bildirib, odatda Continuous zamonlarda ISHLATILMAYDI: know, understand, believe, love, like, hate, want, need, remember, belong, see, hear. Masalan: 'I understand you' (I am understanding emas).",
            "examples": [
                {
                    "title": "Present Continuous qo'llanishi",
                    "problem": "'Listen! Somebody (sing) in the garden' gapini to'ldiring.",
                    "step_by_step": "'Listen!' ayni daqiqadagi harakatga e'tiborni qaratmoqda. Somebody (3-shaxs birlik) -> is singing.",
                    "answer": "Listen! Somebody is singing in the garden"
                },
                {
                    "title": "State verbs qoidasi",
                    "problem": "'I (not / believe) this strange story' gapini to'g'ri zamonda yozing.",
                    "step_by_step": "'Believe' fe'li aqliy ishonchni bildiruvchi holat fe'li bo'lib, Continuous bo'lmaydi. Present Simple ishlatiladi: 'I don't believe'.",
                    "answer": "I don't believe this strange story"
                }
            ],
            "exercise": "Taqqoslang: 'Look! It (rain)' vs 'It usually (rain) in autumn.'",
            "exercise_solution": "'Look! It is raining' (ayni paytda) va 'It usually rains in autumn' (odatdagi holat).",
            "check_questions": [
                {
                    "question": "Qaysi fe'l odatda Present Continuous zamonida ishlatilmaydi?",
                    "options": ["run", "know", "eat", "write"],
                    "correct_index": 1,
                    "explanation": "'Know' (bilmoq) aqliy holat fe'li bo'lib, davomli zamon qo'shimchasini olmaydi."
                },
                {
                    "question": "'They ... dinner right now' gapiga qaysi shakl to'g'ri keladi?",
                    "options": ["have", "are having", "is having", "has"],
                    "correct_index": 1,
                    "explanation": "'Right now' davomli zamon talab qiladi, 'They' bilan 'are having' qo'llanadi."
                },
                {
                    "question": "Present Continuous zamonining so'roq shakli qanday yasaladi?",
                    "options": ["Do/Does + ega + V1", "Am/Is/Are + ega + V-ing", "Did + ega + V1", "Have + ega + V3"],
                    "correct_index": 1,
                    "explanation": "To be (am/is/are) yordamchi fe'li egadan oldinga o'tadi."
                }
            ],
            "tags": ["english", "grammar", "present continuous", "stative verbs", "A2", "6-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lng-003",
            "slug": "past-simple-regular-and-irregular-verbs",
            "subject_id": "sub-17",
            "subject_name": "Ingliz tili",
            "title": "Past Simple Tense: Regular and Irregular Verbs, Wh- Questions",
            "grade_level": "7-sinf / A2",
            "difficulty": "Boshlang'ich",
            "objective": "O'tgan oddiy zamon, to'g'ri fe'llarga -ed qo'shilishi, noto'g'ri fe'llar (Irregular verbs V2) jadvali va did yordamida savol va inkor tuzish.",
            "theory": "Past Simple (O'tgan oddiy zamon) o'tmishda tugallangan aniq harakatlarni ifodalaydi. Fe'llar 2 turga bo'linadi:\n1) Regular verbs (to'g'ri fe'llar): fe'lga -ed qo'shiladi (work -> worked, play -> played, study -> studied);\n2) Irregular verbs (noto'g'ri fe'llar): maxsus o'zgaradi (go -> went, see -> saw, buy -> bought, have -> had, write -> wrote).\nFormulalar:\n- Darak: Subject + V2 (I visited London last year; She bought a new car);\n- Inkor: Subject + did not (didn't) + V1 (fe'l 1-shaklga qaytadi: She didn't buy);\n- So'roq: Did + Subject + V1? (Did you see that movie?).\nVaqt ko'rsatkichlari: yesterday (kecha), last week/month/year (o'tgan hafta/yil), in 2015, two days ago (ikki kun oldin).",
            "examples": [
                {
                    "title": "Inkor va so'roqqa aylantirish",
                    "problem": "'He wrote a letter yesterday' gapini inkor va maxsus so'roq shakliga o'tkazing.",
                    "step_by_step": "1) Inkor: He didn't write a letter yesterday (wrote -> write bo'ladi).\n2) So'roq: What did he write yesterday?",
                    "answer": "He didn't write... / What did he write yesterday?"
                },
                {
                    "title": "To be fe'lining o'tgan zamoni",
                    "problem": "'They (be) at the museum on Sunday' gapini to'ldiring.",
                    "step_by_step": "'To be' ning o'tgan zamoni I/he/she/it uchun WAS, we/you/they uchun WERE bo'ladi. 'They were at the museum...'",
                    "answer": "They were at the museum on Sunday"
                }
            ],
            "exercise": "Noto'g'ri fe'llarning V2 shaklini yozing: eat, make, take, leave, fly.",
            "exercise_solution": "ate, made, took, left, flew.",
            "check_questions": [
                {
                    "question": "'Go' fe'lining Past Simple (V2) shakli qaysi?",
                    "options": ["goed", "gone", "went", "goes"],
                    "correct_index": 2,
                    "explanation": "'Go' noto'g'ri fe'l bo'lib, o'tgan zamoni 'went' dir."
                },
                {
                    "question": "Past Simple inkorda 'didn't' dan keyin fe'l qaysi shaklda keladi?",
                    "options": ["V2 (o'tgan zamon)", "V1 (boshlang'ich shakl)", "V-ing", "V3"],
                    "correct_index": 1,
                    "explanation": "'Did' o'tgan zamon yukini o'ziga olgani sababli asosiy fe'l V1 (infinitive) ga qaytadi."
                },
                {
                    "question": "I, He, She, It uchun 'to be' ning o'tgan zamoni qaysi?",
                    "options": ["were", "was", "been", "are"],
                    "correct_index": 1,
                    "explanation": "Birlik shaxslar uchun 'was', ko'plik uchun 'were' ishlatiladi."
                }
            ],
            "tags": ["english", "past simple", "irregular verbs", "grammar", "A2", "7-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lng-004",
            "slug": "present-perfect-tense-and-experience",
            "subject_id": "sub-17",
            "subject_name": "Ingliz tili",
            "title": "Present Perfect Tense: Life Experience, Result and Signal Words",
            "grade_level": "8-sinf / B1",
            "difficulty": "O'rta",
            "objective": "Present Perfect (have/has + V3) tuzilishi, o'tmishdagi harakatning hozirgi paytdagi natijasi, ever, never, just, already, yet, since, for so'zlari bilan qo'llanishi.",
            "theory": "Present Perfect Tense o'tmishda sodir bo'lgan, ammo natijasi yoki ta'siri hozirgi paytda ko'rinib turgan harakatlarni hamda hayotiy tajribani (life experience) ifodalaydi. Harakatning qachon bo'lgani aniq aytilmaydi.\nFormulalar:\n- Darak: Subject + have / has + V3 (Past Participle) (I have seen, He has finished);\n- Inkor: Subject + haven't / hasn't + V3;\n- So'roq: Have / Has + Subject + V3?\nSignal so'zlar:\n- just (hozirgina), already (allaqachon) — darak gapda;\n- yet (hali) — faqat inkor va so'roq gap oxirida;\n- ever (hech/umringda) — so'roqda; never (hech qachon) — inkorda;\n- for (davomida: for 5 years) va since (berli, boshlanish vaqti: since 2018).",
            "examples": [
                {
                    "title": "Hayotiy tajriba haqida so'rash",
                    "problem": "'Siz hech qachon samolyotda uchganmisiz?' jumlasini ingliz tiliga tarjima qiling.",
                    "step_by_step": "Hayotiy tajriba uchun 'Have you ever + V3' qolipi ishlatiladi. Fly fe'lining V3 shakli 'flown'.\nNatija: 'Have you ever flown by plane?'",
                    "answer": "Have you ever flown by plane?"
                },
                {
                    "title": "Since va for farqi",
                    "problem": "'I have lived in Tashkent (for / since) 10 years' gapida qaysi ko'rsatkich to'g'ri?",
                    "step_by_step": "'10 years' bu vaqt davomiyligi (muddat), shuning uchun 'for' ishlatiladi. Agar boshlang'ich yil (masalan: 2014) bo'lsa 'since' bo'lardi.",
                    "answer": "for 10 years"
                }
            ],
            "exercise": "'I (already / finish) my homework, but my brother (not / do) his yet' gapini to'ldiring.",
            "exercise_solution": "'I have already finished my homework, but my brother hasn't done his yet.'",
            "check_questions": [
                {
                    "question": "'Yet' so'zi qanday gaplarda va gapning qaysi qismida ishlatiladi?",
                    "options": ["Faqat darak gap o'rtasida", "Inkor va so'roq gap oxirida", "Faqat o'tgan zamonda", "Gap boshida"],
                    "correct_index": 1,
                    "explanation": "'Yet' faqat inkor va so'roq gaplarning eng oxirida keladi: 'I haven't eaten yet'."
                },
                {
                    "question": "Present Perfect da 'see' fe'lining 3-shakli (Past Participle) qaysi?",
                    "options": ["saw", "seen", "seeing", "sees"],
                    "correct_index": 1,
                    "explanation": "see (V1) - saw (V2) - seen (V3)."
                },
                {
                    "question": "Past Simple va Present Perfect ning asosiy farqi nima?",
                    "options": ["Hech qanday farqi yo'q", "Past Simple da vaqt aniq ko'rsatiladi (yesterday), Present Perfect da natija muhim", "Past Simple faqat savollarda ishlatiladi", "Present Perfect faqat kelasi zamonda"],
                    "correct_index": 1,
                    "explanation": "Past Simple da o'tmishdagi aniq vaqt aytiladi, Present Perfect da esa harakatning hozirgi kundagi natijasi/tajribasi muhim."
                }
            ],
            "tags": ["english", "present perfect", "grammar", "since", "for", "B1", "8-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lng-005",
            "slug": "passive-voice-and-modal-verbs",
            "subject_id": "sub-17",
            "subject_name": "Ingliz tili",
            "title": "Passive Voice (Majhul nisbat) and Modal Verbs (Can, Must, Should)",
            "grade_level": "9-sinf / B1",
            "difficulty": "O'rta",
            "objective": "Active Voice dan Passive Voice ga o'tkazish formulasi (to be + V3), turli zamonlarda qo'llanilishi hamda modal fe'llar ma'nolari (ruxsat, majburiyat, maslahat).",
            "theory": "Passive Voice (Majhul nisbat) harakatning bajaruvchisi emas, balki harakat obyekti muhim yoki noma'lum bo'lganda ishlatiladi.\nUmumiy formula: Object + TO BE (mos zamonda) + V3 (Past Participle) (+ by Subject).\nZamonlar bo'yicha:\n- Present Simple Passive: am / is / are + V3 (English is spoken all over the world);\n- Past Simple Passive: was / were + V3 (The bridge was built in 1995);\n- Future Simple Passive: will be + V3 (The work will be finished tomorrow);\n- Present Perfect Passive: have / has been + V3 (The car has been repaired).\nModal fe'llar: can/could (qobiliyat), must (qat'iy qonuniy majburiyat), have to (zaruriyat), should (maslahat: 'You should see a doctor'), may/might (ehtimollik/ruxsat). Modal fe'llardan keyin 'to' siz sof fe'l (bare infinitive) keladi.",
            "examples": [
                {
                    "title": "Active dan Passive ga o'tkazish",
                    "problem": "'Alexander Bell invented the telephone in 1876' gapini Passive Voice ga aylantiring.",
                    "step_by_step": "1) Obyekt: 'The telephone' gap boshiga chiqadi;\n2) Zamon: Past Simple -> was invented;\n3) Bajaruvchi: by Alexander Bell;\nNatija: 'The telephone was invented by Alexander Bell in 1876'.",
                    "answer": "The telephone was invented by Alexander Bell in 1876"
                },
                {
                    "title": "Must vs Should farqi",
                    "problem": "'You (must / should) stop when the traffic light is red' — qaysi modal fe'l to'g'ri?",
                    "step_by_step": "Qizil chiroqda to'xtash bu tavsiya emas, qat'iy yo'l harakati qoidasi (majburiyat), shuning uchun 'must' ishlatiladi.",
                    "answer": "must"
                }
            ],
            "exercise": "Passive Voice ga aylantiring: 'They clean the rooms every day.'",
            "exercise_solution": "'The rooms are cleaned every day.'",
            "check_questions": [
                {
                    "question": "Passive Voice hosil qilishning umumiy formulasi qaysi?",
                    "options": ["have + V3", "to be + V3 (Past Participle)", "to be + V-ing", "will + V1"],
                    "correct_index": 1,
                    "explanation": "Majhul nisbat har doim 'to be' ning tegishli zamon shakli va fe'lning 3-shakli (V3) bilan yasaladi."
                },
                {
                    "question": "Maslahat berishda qaysi modal fe'l ishlatiladi?",
                    "options": ["must", "can", "should", "may"],
                    "correct_index": 2,
                    "explanation": "'Should' do'stona maslahat va tavsiya berish uchun qo'llanadi ('You should sleep more')."
                },
                {
                    "question": "'The Mona Lisa ... painted by Leonardo da Vinci' — nuqtalar o'rniga nima qo'yiladi?",
                    "options": ["is", "was", "were", "has"],
                    "correct_index": 1,
                    "explanation": "Rasm o'tmishda bitta jism sifatida yaratilgani uchun 'was painted' bo'ladi."
                }
            ],
            "tags": ["english", "passive voice", "modal verbs", "grammar", "B1", "9-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lng-006",
            "slug": "conditionals-zero-first-second-and-third",
            "subject_id": "sub-17",
            "subject_name": "Ingliz tili",
            "title": "Conditionals (Shart ergash gaplar): Zero, First, Second and Third Conditionals",
            "grade_level": "10-sinf / B2",
            "difficulty": "Murakkab",
            "objective": "4 ta shart mayli turi (ilmiy haqiqatlar, real kelajak sharti, noreal hozirgi shart va o'tmishdagi afsuslanish) formulalarini va farqlarini o'zlashtirish.",
            "theory": "Conditionals (Shart gaplar) 'If' (agar) bog'lovchisi yordamida tuziladi va 4 ta asosiy turga bo'linadi:\n1) Zero Conditional (100% haqiqat, tabiiy qonunlar):\n   If + Present Simple, Present Simple. ('If you heat ice, it melts' — Muzni qizdirsangiz, u eriydi).\n2) First Conditional (Kelajakdagi real ehtimoliy shart):\n   If + Present Simple, will + V1. ('If it rains tomorrow, we will stay at home' — Agar ertaga yomg'ir yog'sa, biz uyda qolamiz).\n3) Second Conditional (Hozirgi paytdagi xayoliy, noreal orzu-istak):\n   If + Past Simple, would + V1. (Barcha shaxslar uchun 'were' afzal: 'If I were you, I would study harder' — Sizning o'rningizda bo'lganimda ko'proq o'qirdim; 'If I won a million dollars, I would travel').\n4) Third Conditional (O'tmishda bajarilmagan noreal shart va afsus):\n   If + Past Perfect (had + V3), would have + V3. ('If I had studied harder, I would have passed the exam' — Ko'proq o'qiganimda edi, imtihondan o'tgan bo'lardim).",
            "examples": [
                {
                    "title": "First Conditional vs Second Conditional",
                    "problem": "'If I have free time tonight, I (watch) a movie' va 'If I had a spaceship, I (fly) to Mars' gaplarini oching.",
                    "step_by_step": "1) Bugun oqshomda vaqt bo'lishi real ehtimol -> First Conditional: will watch;\n2) Kosmik kema bo'lishi hozir noreal orzu -> Second Conditional: would fly.",
                    "answer": "will watch / would fly"
                },
                {
                    "title": "Third Conditional (o'tmishdagi afsus)",
                    "problem": "'We missed the train because we woke up late' vaziyatiga Third Conditional tuzing.",
                    "step_by_step": "Formula: If + had + V3, would have + V3.\nNatija: 'If we hadn't woken up late, we wouldn't have missed the train'.",
                    "answer": "If we hadn't woken up late, we wouldn't have missed the train"
                }
            ],
            "exercise": "Qavslarni oching: 'If she (know) the truth back then, she (not / make) that mistake.'",
            "exercise_solution": "'If she had known the truth back then, she wouldn't have made that mistake' (Third Conditional).",
            "check_questions": [
                {
                    "question": "First Conditional da 'If' li qismda qaysi zamon ishlatiladi?",
                    "options": ["Future Simple (will)", "Present Simple", "Past Simple", "Present Perfect"],
                    "correct_index": 1,
                    "explanation": "Qoidaga ko'ra 'If' li shart ergash qismida 'will' ishlatilmaydi, Present Simple qo'llanadi."
                },
                {
                    "question": "Hozirgi zamondagi noreal orzu-istakni ifodalovchi shart turi qaysi?",
                    "options": ["Zero Conditional", "First Conditional", "Second Conditional", "Third Conditional"],
                    "correct_index": 2,
                    "explanation": "Second Conditional (If + Past Simple, would + V1) xayoliy noreal vaziyatlar uchun qo'llanadi."
                },
                {
                    "question": "'If I were a bird, I would fly' gapida nima uchun 'was' o'rniga 'were' ishlatiladi?",
                    "options": ["Chunki bu qoida xatosi", "Subjunctive mood (istak mayli) da barcha shaxslar uchun 'were' qo'llanishi adabiy me'yordir", "Chunki 'I' ko'plik olmoshi", "Faqat qushlar bilan shunday"],
                    "correct_index": 1,
                    "explanation": "Second Conditional da rasmiy va adabiy me'yorda 'I' va 'He/She' bilan ham 'were' qo'llanadi."
                }
            ],
            "tags": ["english", "conditionals", "if clauses", "grammar", "B2", "10-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lng-007",
            "slug": "ielts-writing-task-2-essay-structure",
            "subject_id": "sub-17",
            "subject_name": "Ingliz tili",
            "title": "Academic English: IELTS Writing Task 2 Essay Structures and Cohesive Devices",
            "grade_level": "11-sinf / B2-C1",
            "difficulty": "Murakkab",
            "objective": "IELTS Writing Task 2 mezonlari (TR, CC, LR, GRA), insho turlari (Opinion, Discussion, Problem-Solution) va 4 qismli akademik insho tuzilishini egallash.",
            "theory": "IELTS Academic Writing Task 2 da talabgor 40 daqiqa ichida kamida 250 ta so'zdan iborat akademik insho yozishi kerak. 4 ta baholash mezoni (har biri 25%): 1) Task Response (savolga to'liq va asosli javob); 2) Coherence and Cohesion (paragraflar mantiqi va bog'lovchilar); 3) Lexical Resource (akademik so'z boyligi va kollokatsiyalar); 4) Grammatical Range and Accuracy (murakkab grammatik tuzilmalar xatosizligi).\nKlassik 4 qismli struktura:\n1. Introduction (2 gap): Paraphrase the prompt (savolni o'z so'zlari bilan qayta yozish) + Thesis Statement (shaxsiy pozitsiya va inshoning qisqacha maqsadi);\n2. Body Paragraph 1 (Topic sentence + Explanation + Concrete Example);\n3. Body Paragraph 2 (Topic sentence + Explanation + Concrete Example);\n4. Conclusion (Summary of main points + Final recommendation). Bog'lovchi vositalar (Cohesive devices): Furthermore, However, Consequently, For instance, In contrast, On the other hand.",
            "examples": [
                {
                    "title": "Savolni parafraz qilish (Paraphrasing)",
                    "problem": "Mavzu: 'Some people think that universities should provide graduates with knowledge and skills for their future jobs.' Ushbu gapni kirish qismida parafraz qiling.",
                    "step_by_step": "Sinonimlar va struktura o'zgarishi: Some people believe -> It is often argued; provide with skills -> equip students with practical competencies; future jobs -> prospective careers.\nParafraz: 'It is widely argued that higher education institutions ought to equip learners with the practical competencies necessary for their prospective careers.'",
                    "answer": "It is widely argued that higher education institutions ought to equip learners with practical competencies..."
                },
                {
                    "title": "Thesis Statement tuzish",
                    "problem": "'To what extent do you agree or disagree?' savoliga qat'iy fikrli (strong thesis) gap yozing.",
                    "step_by_step": "'This essay completely agrees with this perspective, as vocational preparedness enhances graduate employability and directly stimulates economic growth.'",
                    "answer": "This essay completely agrees with this perspective, as..."
                }
            ],
            "exercise": "Body paragraf uchun 'Topic Sentence' ning vazifasi nima va u qanday yoziladi?",
            "exercise_solution": "Topic Sentence paragrafning birinchi gapi bo'lib, butun paragrafda qanday asosiy g'oya muhokama qilinishini aniq va lo'nda e'lon qiladi.",
            "check_questions": [
                {
                    "question": "IELTS Writing Task 2 da insho hajmi kamida nechta so'zdan iborat bo'lishi shart?",
                    "options": ["150 ta", "200 ta", "250 ta", "300 ta"],
                    "correct_index": 2,
                    "explanation": "Task 2 uchun minimal hajm 250 ta so'z; kam bo'lsa Task Response dan ball tushiriladi."
                },
                {
                    "question": "Kirish (Introduction) paragrafining eng muhim gapi nima deyiladi?",
                    "options": ["Topic sentence", "Thesis statement", "Example", "Conclusion"],
                    "correct_index": 1,
                    "explanation": "Thesis statement muallifning mavzuga nisbatan bosh pozitsiyasini bildiruvchi asosiy gapdir."
                },
                {
                    "question": "Insho oxiridagi Conclusion (xulosa) qismida yangi g'oyalar yoki dalillar kiritilishi to'g'rimi?",
                    "options": ["Ha, albatta", "Yo'q, xulosada faqat oldingi fikrlar umumlashtiriladi", "Ixtiyoriy", "Faqat muammoli mavzuda"],
                    "correct_index": 1,
                    "explanation": "Xulosada hech qachon yangi g'oya berilmaydi, faqat tana paragraflaridagi fikrlar yakunlanadi."
                }
            ],
            "tags": ["english", "ielts", "writing task 2", "academic essay", "B2-C1", "11-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lng-008",
            "slug": "academic-vocabulary-collocations-and-phrasal-verbs",
            "subject_id": "sub-17",
            "subject_name": "Ingliz tili",
            "title": "Advanced Vocabulary: Academic Collocations and Essential Phrasal Verbs",
            "grade_level": "11-sinf / C1",
            "difficulty": "Murakkab",
            "objective": "Akademik so'z birikmalari (Collocations), iborali fe'llar (Phrasal verbs) va yuqori darajadagi so'z boyligini nutqda to'g'ri qo'llash.",
            "theory": "Kollokatsiyalar (Collocations) — bir-biri bilan tabiiy bog'lanib keluvchi so'z juftliklaridir. Ingliz tilida xatosiz va ravon gapirish uchun so'zlarni alohida emas, balki birikma holida yodlash zarur. Misollar:\n- 'make' bilan: make a decision, make progress, make an effort, make a mistake;\n- 'do' bilan: do research, do homework, do business, do someone a favor;\n- Sifat + Ot: heavy rain (kuchli yomg'ir, strong rain emas), rapid growth, significant impact, vital role.\nPhrasal Verbs (Iborali fe'llar) — fe'l va predlog/ravishdan iborat bo'lib, yangi ko'chma ma'no hosil qiladi: carry out (amalga oshirmoq / to conduct: carry out research), bring about (sabab bo'lmoq / to cause), look forward to (intiqlik bilan kutmoq), turn down (rad etmoq / to reject), give up (tashlamoq / to quit), run out of (tugab qolmoq).",
            "examples": [
                {
                    "title": "Do va Make kollokatsiyalari",
                    "problem": "'Scientists are (making / doing) research on renewable energy' — qaysi fe'l to'g'ri?",
                    "step_by_step": "'Research' so'zi bilan har doim 'do' ishlatiladi (do research, conduct research). 'Make research' grammatik xato hisoblanadi.",
                    "answer": "doing research"
                },
                {
                    "title": "Phrasal verb ma'nosini ochish",
                    "problem": "'The government decided to call off the strike' gapidagi 'call off' nimani anglatadi?",
                    "step_by_step": "'Call off' iborali fe'li bekor qilmoq (to cancel) ma'nosini bildiradi.",
                    "answer": "Bekor qilmoq (to cancel)"
                }
            ],
            "exercise": "Bo'sh o'rinni to'ldiring: 'Education plays a ... role in personal development.' (vital / strong / heavy)",
            "exercise_solution": "'vital role' (juda muhim rol o'ynamoq; play a vital/pivotal role).",
            "check_questions": [
                {
                    "question": "'Xatoga yo'l qo'ymoq' birikmasi ingliz tilida qanday bo'ladi?",
                    "options": ["do a mistake", "make a mistake", "create a mistake", "take a mistake"],
                    "correct_index": 1,
                    "explanation": "Qat'iy kollokatsiya qoidasiga ko'ra 'make a mistake' ishlatiladi."
                },
                {
                    "question": "'Carry out' iborali fe'lining ma'nosi nima?",
                    "options": ["Yuk ko'tarmoq", "Amalga oshirmoq, o'tkazmoq (to conduct)", "Tashqariga chiqmoq", "Rad etmoq"],
                    "correct_index": 1,
                    "explanation": "'Carry out an experiment/research' — tadqiqot yoki tajriba o'tkazmoq degan ma'noni beradi."
                },
                {
                    "question": "'Give up' iborasi nimani anglatadi?",
                    "options": ["Sovg'a qilmoq", "Tashlab yubormoq, taslim bo'lmoq", "Davom ettirmoq", "Boshlamoq"],
                    "correct_index": 1,
                    "explanation": "'Give up' biror odatni tashlash yoki kurashdan voz kechishni bildiradi."
                }
            ],
            "tags": ["english", "vocabulary", "collocations", "phrasal verbs", "C1", "11-sinf"],
            "duration_minutes": 30
        },

        # RUS TILI (4)
        {
            "id": "lng-009",
            "slug": "rus-tili-rod-va-otlar-turlanishi",
            "subject_id": "sub-18",
            "subject_name": "Rus tili",
            "title": "Rus tili grammatikasi: otlarning rodi (jinsi) va 3 ta turlanish tizimi",
            "grade_level": "5-6-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Rus tilida otlarning erkak (мужской), ayol (женский) va o'rta (средний) jinslarini aniqlash hamda 1, 2, 3-turlanish qoidalarini o'rganish.",
            "theory": "Rus tilida barcha otlar 3 ta jinsdan biriga tegishli bo'ladi:\n1) Мужской род (он, мой): qattiq undoshga yoki -й ga tugaydi (стол, дом, музей, учитель);\n2) Женский род (она, моя): -а, -я yoki yumshatish belgili asoslarga tugaydi (книга, земля, песня, ночь);\n3) Средний род (оно, моё): -о, -е, -мя ga tugaydi (окно, поле, море, время, имя).\nTurlanish (склонение):\n- 1-склонение: -а, -я bilan tugaydigan ayol va erkak jinsidagi otlar (мама, папа, книга, земля);\n- 2-склонение: nol qo'shimchali erkak jinsi va -о, -е li o'rta jins otlari (стол, конь, окно, море);\n- 3-склонение: -ь (yumshatish belgisi) bilan tugaydigan ayol jinsidagi otlar (ночь, мышь, тетрадь, радость).",
            "examples": [
                {
                    "title": "Otning rodini aniqlash",
                    "problem": "'Время', 'словарь' va 'тетрадь' so'zlarining jinsini (род) aniqlang.",
                    "step_by_step": "1) Время — -мя bilan tugagan, demak средний род (оно моё);\n2) Словарь — erkak jinsidagi ot (он мой, родительный: словаря — 2-склонение);\n3) Тетрадь — ayol jinsidagi ot (она моя, родительный: тетради — 3-склонение).",
                    "answer": "Время - ср.р., Словарь - м.р., Тетрадь - ж.р."
                },
                {
                    "title": "Mening (мой/моя/моё) olmoshini moslashtirish",
                    "problem": "'(Мой) семья', '(мой) брат' va '(мой) пальто' birikmalarini to'g'rilang.",
                    "step_by_step": "Семья (ж.р.) -> моя семья; Брат (м.р.) -> мой брат; Пальто (ср.р., o'zgarmas) -> моё пальто.",
                    "answer": "Моя семья, мой брат, моё пальто"
                }
            ],
            "exercise": "So'zlarni turlanishlar (склонение) bo'yicha ajrating: школа, город, дочь, дядя, озеро.",
            "exercise_solution": "1-склонение: школа, дядя; 2-склонение: город, озеро; 3-склонение: дочь.",
            "check_questions": [
                {
                    "question": "-о va -е bilan tugaydigan otlar odatda qaysi jinsga kiradi?",
                    "options": ["Мужской род", "Женский род", "Средний род", "Umumiy rod"],
                    "correct_index": 2,
                    "explanation": "-о va -е bilan tugovchi otlar sredniy rod hisoblanadi (masalan: окно, море)."
                },
                {
                    "question": "3-склонение ga qaysi otlar kiradi?",
                    "options": ["-а, -я li otlar", "Undoshga tugaydigan erkak jinsi", "-ь bilan tugaydigan ayol jinsi otlari", "Barcha o'rta jins"],
                    "correct_index": 2,
                    "explanation": "3-skloneniyaga faqat yumshatish belgisi (-ь) bilan tugovchi ayol jinsidagi otlar kiradi (ночь, мать)."
                },
                {
                    "question": "'Кофе' so'zi rus adabiy tilida qaysi jinsda qo'llanadi?",
                    "options": ["Средний род", "Мужской род", "Женский род", "Ko'plikda"],
                    "correct_index": 1,
                    "explanation": "Qat'iy adabiy normaga ko'ra 'чёрный кофе' erkak jinsidadir (он мой)."
                }
            ],
            "tags": ["rus tili", "род", "склонение", "грамматика", "5-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "lng-010",
            "slug": "rus-tili-padejlar-tizimi",
            "subject_id": "sub-18",
            "subject_name": "Rus tili",
            "title": "Rus tilida 6 ta padej (kelishik) tizimi va predloglar bilan qo'llanishi",
            "grade_level": "7-sinf",
            "difficulty": "O'rta",
            "objective": "Rus tilidagi 6 ta padej so'roqlari, asosiy ma'nolari, qo'shimchalari va predloglar bilan moslashuvini o'zlashtirish.",
            "theory": "Rus tilida 6 ta padej bor:\n1) Именительный (Bosh kelishik: Кто? Что?) — gapda doimo ega bo'ladi (Студент читает);\n2) Родительный (Kimning? Nimaning? Kim/nima yo'q? Кого? Чего?) — predloglar: без, для, до, из, от, у, около (нет книги, стакан воды);\n3) Дательный (Jo'nalish: Кому? Чему?) — predloglar: к, по (подарить другу, подойти к окну);\n4) Винительный (Tushum: Кого? Что?) — predloglar: в, на, через (читать книгу, вижу друга);\n5) Творительный (Birgalik/qurol: Кем? Чем?) — predloglar: с, под, над, за, перед (писать ручкой, гулять с другом);\n6) Предложный (O'rin-payt: О ком? О чём? Где?) — doimo predlog bilan keladi: о/об, в, на (думать о родине, жить в Ташкенте).",
            "examples": [
                {
                    "title": "Padejni to'g'ri qo'llash",
                    "problem": "'Я живу в (Ташкент) и учусь в (школа)' gapidagi qavslarni oching.",
                    "step_by_step": "'Где?' savoliga javob beruvchi o'rin ma'nosi Предложный падеж talab qiladi (qo'shimcha -е):\nТашкент -> в Ташкенте; школа -> в школе.",
                    "answer": "Я живу в Ташкенте и учусь в школе"
                },
                {
                    "title": "Родительный падеж inkorda",
                    "problem": "'У меня есть время' gapini inkor shaklga o'giring.",
                    "step_by_step": "Inkor qilinganda 'нет' so'zidan keyin Родительный падеж ishlatiladi: время -> времени.\nNatija: 'У меня нет времени'.",
                    "answer": "У меня нет времени"
                }
            ],
            "exercise": "'Друг' so'zini Творительный падежда 'с' predlogi bilan ishlating.",
            "exercise_solution": "с другом (гулять с другом).",
            "check_questions": [
                {
                    "question": "Faqat predloglar bilan ishlatiladigan yagona padej qaysi?",
                    "options": ["Родительный", "Дательный", "Творительный", "Предложный"],
                    "correct_index": 3,
                    "explanation": "Предложный падеж hech qachon predlogsiz (о, в, на, при) qo'llanmaydi."
                },
                {
                    "question": "'Кому? Чему?' qaysi padejning so'roqlari?",
                    "options": ["Дательный", "Винительный", "Родительный", "Творительный"],
                    "correct_index": 0,
                    "explanation": "Дательный падеж jo'nalish va berish harakatini bildiradi (дать кому?)."
                },
                {
                    "question": "Jonli otlarda Винительный падеж shakli qaysi padej bilan bir xil bo'ladi?",
                    "options": ["Именительный", "Родительный", "Дательный", "Предложный"],
                    "correct_index": 1,
                    "explanation": "Jonli erkak jinsidagi otlarda Винительный shakli Родительный bilan bir xil (вижу студента = нет студента)."
                }
            ],
            "tags": ["rus tili", "падежи", "грамматика", "предлоги", "7-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lng-011",
            "slug": "rus-tili-fel-vidlari-sovershenniy-nesovershenniy",
            "subject_id": "sub-18",
            "subject_name": "Rus tili",
            "title": "Rus tilida fe'l vidlari: совершенный va несовершенный вид",
            "grade_level": "8-sinf",
            "difficulty": "O'rta",
            "objective": "Fe'l vidlari farqi (что делать? — несовершенный vs что сделать? — совершенный), natija va jarayonni to'g'ri ifodalash.",
            "theory": "Rus tilidagi har bir fe'l ikki vidning biriga kiradi:\n1) Несовершенный вид (НСВ) — savoli: Что делать? Harakatning davomiyligini, jarayonini yoki doimiy takrorlanishini bildiradi (читать, писать, делать). Bu fe'llar 3 ta zamonga ega: o'tgan (читал), hozirgi (читаю) va murakkab kelasi (буду читать);\n2) Совершенный вид (СВ) — savoli: Что сделать? Harakatning tugallanganligini, bir martalikligini va natijaga erishilganini bildiradi (прочитать, написать, сделать). Bu fe'llarning hozirgi zamoni YO'Q, faqat o'tgan (прочитал) va oddiy kelasi zamoni (прочитаю) bo'ladi.\nVid juftliklari ko'pincha prefikslar (yondash qo'shimchalar) yordamida yasaladi: писать -> написать, учить -> выучить, делать -> сделать.",
            "examples": [
                {
                    "title": "Vidni to'g'ri tanlash",
                    "problem": "'Я вчера два часа (читал / прочитал) книгу' — qaysi fe'l to'g'ri?",
                    "step_by_step": "'Два часа' (ikki soat davomida) harakatning davomiy jarayon ekanligini ko'rsatmoqda, shuning uchun НСВ kerak: 'читал'.",
                    "answer": "читал"
                },
                {
                    "title": "Natijani ifodalash",
                    "problem": "'Men uy vazifamni bajarib bo'ldim' jumlasini tarjima qiling.",
                    "step_by_step": "Harakat yakunlangan va natija bor. 'Сделать' (СВ) fe'li ishlatiladi: 'Я сделал домашнее задание'.",
                    "answer": "Я сделал домашнее задание"
                }
            ],
            "exercise": "Fe'llarni vid juftliklariga ajrating: решать — ..., открывать — ..., повторять — ...",
            "exercise_solution": "решать — решить, открывать — открыть, повторять — повторить.",
            "check_questions": [
                {
                    "question": "Совершенный вид fe'llarining qaysi zamon shakli mavjud emas?",
                    "options": ["O'tgan zamon", "Hozirgi zamon", "Kelasi zamon", "Hech qaysi"],
                    "correct_index": 1,
                    "explanation": "Совершенный вид tugallanganlikni bildirgani uchun unda hozirgi zamon shakli umuman bo'lmaydi."
                },
                {
                    "question": "Harakatning jarayonini va takrorlanishini qaysi vid bildiradi?",
                    "options": ["Совершенный вид", "Несовершенный вид", "Har ikkalasi", "Hech biri"],
                    "correct_index": 1,
                    "explanation": "Несовершенный вид (что делать?) jarayon va takrorlanishni ifodalaydi."
                },
                {
                    "question": "'Буду писать' qaysi zamon va qaysi vid shakli?",
                    "options": ["Совершенный вид kelasi zamon", "Несовершенный вид murakkab kelasi zamon", "O'tgan zamon", "Hozirgi zamon"],
                    "correct_index": 1,
                    "explanation": "'Буду + infinitiv' faqat несовершенный вид ning murakkab kelasi zamonida ishlatiladi."
                }
            ],
            "tags": ["rus tili", "вид глагола", "совершенный", "несовершенный", "8-sinf"],
            "duration_minutes": 30
        },
        {
            "id": "lng-012",
            "slug": "rus-tili-harakat-fellari-idti-yehat",
            "subject_id": "sub-18",
            "subject_name": "Rus tili",
            "title": "Rus tilida harakat fe'llari (Глаголы движения: идти — ходить, ехать — ездить)",
            "grade_level": "9-sinf",
            "difficulty": "Murakkab",
            "objective": "Bir yo'nalishli va ko'p yo'nalishli harakat fe'llari farqi, transport vositasida va piyoda harakatlanish hamda prefiksli harakat fe'llarini o'rganish.",
            "theory": "Rus tilida harakat fe'llari o'ziga xos juftliklar hosil qiladi:\n1) Piyoda harakatlanish: идти (bir tomonga, ayni daqiqada: 'Я иду в школу') — ходить (har doim, har xil tomonga yoki borib-kelish: 'Я каждый день хожу в школу');\n2) Transportda harakatlanish: ехать (bir tomonga ayni paytda: 'Мы едем в Самарканд') — ездить (muntazam: 'Мы часто ездим в горы');\nPrefikslar bilan ma'no o'zgarishi:\n- по- (harakat boshlanishi: пойти, поехать);\n- при- (yetib kelish: прийти, приехать);\n- у- (ketish, jo'nash: уйти, уехать);\n- в- / во- (ichkariga kirish: войти в комнату);\n- вы- (tashqariga chiqish: выйти из класса);\n- пере- (kesib o'tish: перейти улицу).",
            "examples": [
                {
                    "title": "Идти va ходить farqi",
                    "problem": "'Смотри, куда он ...?' va 'Он каждую субботу ... в бассейн' gaplarini to'ldiring.",
                    "step_by_step": "1) 'Смотри, куда он идёт?' (ayni paytdagi aniq bir yo'nalish);\n2) 'Он каждую субботу ходит в бассейн' (muntazam takrorlanuvchi harakat).",
                    "answer": "идёт / ходит"
                },
                {
                    "title": "Prefiksli harakat fe'li",
                    "problem": "'Poyezd soat 8 da Toshkentga yetib keldi' jumlasini rus tiliga o'giring.",
                    "step_by_step": "Transportda yetib kelish uchun 'при-' prefiksi va 'ехать' fe'li ishlatiladi: 'Поезд прибыл (приехал) в Ташкент в 8 часов'.",
                    "answer": "Поезд приехал в Ташкент в 8 часов"
                }
            ],
            "exercise": "Prefikslar ma'nosini moslang: войти, выйти, перейти (chiqmoq, kirmoq, kesib o'tmoq).",
            "exercise_solution": "войти — kirmoq; выйти — chiqmoq; перейти — kesib o'tmoq.",
            "check_questions": [
                {
                    "question": "Piyoda bir yo'nalishda ayni paytda borayotganda qaysi fe'l ishlatiladi?",
                    "options": ["ходить", "идти", "ехать", "ездить"],
                    "correct_index": 1,
                    "explanation": "'Идти' ayni daqiqadagi bir yo'nalishli piyoda harakatni bildiradi."
                },
                {
                    "question": "Ko'chani kesib o'tishda qaysi prefiksli fe'l qo'llanadi?",
                    "options": ["войти", "уйти", "перейти", "прийти"],
                    "correct_index": 2,
                    "explanation": "'Пере-' prefiksi bir tarafdan ikkinchi tarafga kesib o'tishni bildiradi (перейти дорогу)."
                },
                {
                    "question": "Transport vositasida muntazam qatnashni qaysi fe'l ifodalaydi?",
                    "options": ["ехать", "ездить", "идти", "ходить"],
                    "correct_index": 1,
                    "explanation": "'Ездить' transportda doimiy yoki ikki tomonga qatnashni bildiradi."
                }
            ],
            "tags": ["rus tili", "глаголы движения", "идти", "ехать", "префиксы", "9-sinf"],
            "duration_minutes": 35
        },

        # QORAQALPOQ TILI VA ADABIYOTI (2)
        {
            "id": "lng-013",
            "slug": "qoraqalpoq-tili-grammatikasi-fonetika-va-morfologiya",
            "subject_id": "sub-19",
            "subject_name": "Qoraqalpoq tili va adabiyoti",
            "title": "Qoraqalpoq tili: fonetik xususiyatlar, singarmonizm va kelishik tizimi",
            "grade_level": "7-8-sinf",
            "difficulty": "Boshlang'ich",
            "objective": "Qoraqalpoq tilining turkiy tillar qipchoq guruhiga mansubligi, unlilar singarmonizmi, o'ziga xos tovushlar (á, ó, ú, g', j, w) va 6 ta kelishik tizimini o'rganish.",
            "theory": "Qoraqalpoq tili — turkiy tillar oilasining qipchoq guruhiga (qozoq va no'g'ay tillariga yaqin) mansub bo'lib, Qoraqalpog'iston Respublikasining davlat tilidir. Fonetik xususiyatlari: Qoraqalpoq tilida qat'iy ohangdoshlik (singarmonizm / lab garmoniyasi) mavjud: so'zdagi unlilar yo yoppasiga yo'g'on (a, o, u, ı), yo yoppasiga ingichka (e, ó, ú, i, á) bo'ladi. O'zbek tili bilan muhim farqi: o'zbek tilidagi 'sh' tovushi o'rnida qoraqalpoq tilida ko'pincha 's' tovushi keladi (bosh -> bas, tosh -> tas, qosh -> qas); o'zbek tilidagi 'ch' o'rnida 'sh' keladi (uch -> úsh, kecha -> keshe). Kelishik tizimi (seplikler — 6 ta): 1) Ataw sepligi (kim? ne?); 2) Iyelik sepligi (-nıń / -niń); 3) Barıs sepligi (-ǵa / -ge, -qa / -ke); 4) Tabıs sepligi (-nı / -ni); 5) Shıǵıs sepligi (-nan / -nen, -dan / -den); 6) Orın sepligi (-da / -de, -ta / -te).",
            "examples": [
                {
                    "title": "O'zbek va qoraqalpoq so'zlarini qiyoslash",
                    "problem": "'Bosh', 'uchta tosh' va 'yaxshi kishi' so'z birikmalarining qoraqalpoqcha shaklini toping.",
                    "step_by_step": "1) Bosh -> Bas;\n2) Uchta tosh -> Úsh tas;\n3) Yaxshi kishi -> Jaqsı kisi (y -> j, x -> q, sh -> s).",
                    "answer": "Bas, úsh tas, jaqsı kisi"
                },
                {
                    "title": "Kelishik qo'shimchasini qo'shish",
                    "problem": "'Mektep' (maktab) so'ziga barıs (jo'nalish) sepligi qo'shilganda qanday bo'ladi?",
                    "step_by_step": "Mektep ingichka unlilarga ega va p jarangsiz bilan tugagan, shuning uchun -ke qo'shiladi: 'mektepke'.",
                    "answer": "Mektepke"
                }
            ],
            "exercise": "Qoraqalpoq tilidagi 6 ta kelishik (seplik) nomlarini sanang.",
            "exercise_solution": "Ataw, Iyelik, Barıs, Tabıs, Orın, Shıǵıs seplikleri.",
            "check_questions": [
                {
                    "question": "Qoraqalpoq tili turkiy tillarning qaysi guruhiga kiradi?",
                    "options": ["O'g'uz guruhi", "Qipchoq guruhi", "Qarluq guruhi", "Sibir guruhi"],
                    "correct_index": 1,
                    "explanation": "Qoraqalpoq tili qipchoq tarmog'iga mansub bo'lib, singarmonizm qonuniyati juda kuchli."
                },
                {
                    "question": "O'zbek tilidagi 'bosh' so'zi qoraqalpoq tilida qanday talaffuz qilinadi?",
                    "options": ["Bosh", "Bas", "Posh", "Bax"],
                    "correct_index": 1,
                    "explanation": "Qipchoq fonetik qonuniyatiga ko'ra o'zbekcha 'sh' o'rnida qoraqalpoqchada 's' keladi (bas)."
                },
                {
                    "question": "Qoraqalpoq alifbosidagi 'á', 'ó', 'ú' harflari qanday unlilarni bildiradi?",
                    "options": ["Yo'g'on unlilar", "Yumshoq (ingichka) unlilar", "Cho'ziq unlilar", "Differensial tovushlar"],
                    "correct_index": 1,
                    "explanation": "Apostrofli bu belgilar ingichka yumshoq unli tovushlarni ifodalaydi."
                }
            ],
            "tags": ["qoraqalpoq tili", "singarmonizm", "qipchoq", "kelishiklar", "seplik", "7-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "lng-014",
            "slug": "berdaq-ijodi-va-qoraqalpoq-adabiyoti",
            "subject_id": "sub-19",
            "subject_name": "Qoraqalpoq tili va adabiyoti",
            "title": "Qoraqalpoq mumtoz adabiyoti: Berdaq G'arg'abay o'g'li va Ajiniyoz ijodi",
            "grade_level": "8-9-sinf",
            "difficulty": "O'rta",
            "objective": "Berdaqning xalqparvar she'riyati ('Xalq uchun', 'Ahmoq bo'lma'), dostonlari hamda Ajiniyoz Qo'siboy o'g'lining 'Ellarim bordir' qasidasi va lirik merosini o'rganish.",
            "theory": "Qoraqalpoq adabiyoti boy folklor merosi ('Qirq qiz', 'Alpamıs', 'Qoblan' dostonlari) va XIX asr mumtoz adabiyotiga ega. Berdaq (Berdimurod) G'arg'abay o'g'li (1827-1900) — qoraqalpoq adabiyotining klassigi va asoschisi. Shoir butun hayotini o'z xalqining dardi, ozodligi va ma'rifatiga bag'ishlagan. Mashhur asarlari: 'Xalq uchun' ('Dardim ko'pdir, g'amim bisyor, Mehnat tortdim xalqim uchun...'), 'Ahmoq bo'lma', 'Bo'lgan emas', 'Izlar edim', 'Omongeldi' dostoni. Ajiniyoz Qo'siboy o'g'li (Ziyvar, 1824-1878) — qoraqalpoq lirik she'riyatining yorqin vakili. Xivadagi Sherg'ozixon madrasasida tahsil olgan. Uning 'Ellarim bordir' qo'shig'i vatanparvarlikning yuksak madhiyasidir. Shuningdek, qoraqalpoq xalq eposi 'Qirq qiz' (Guloyim va uning 40 nafar botir qizlari jasorati) jahon miqyosidagi qahramonlik dostonidir.",
            "examples": [
                {
                    "title": "Berdaqning 'Xalq uchun' she'ri g'oyasi",
                    "problem": "Berdaq 'Xalq uchun' she'rida o'z hayotiy burchini nimalarda ko'radi?",
                    "step_by_step": "Shoir boylik yoki amaldorlikni emas, balki qora mehnatda ezilgan qoraqalpoq xalqining himoyachisi bo'lishni, odamlarni birlikka va adolatga chaqirishni o'zining eng oliy maqsadi deb biladi.",
                    "answer": "Xalqqa fidokorona xizmat qilish va adolatni himoyalash"
                },
                {
                    "title": "'Qirq qiz' dostoni o'ziga xosligi",
                    "problem": "Nima sababdan 'Qirq qiz' dostoni jahon eposlari ichida noyob hisoblanadi?",
                    "step_by_step": "Chunki doston qahramonlari erkak botirlar emas, balki Guloyim boshchiligidagi 40 nafar mard, vatanparvar jangchi qizlar bo'lib, o'z yurtini chet el bosqinchilaridan mardonavor himoya qiladilar.",
                    "answer": "Ayol jangchilar qahramonligiga bag'ishlangan noyob epos bo'lgani uchun"
                }
            ],
            "exercise": "Ajiniyozning vatan madhiga bag'ishlangan mashhur she'ri qaysi?",
            "exercise_solution": "'Ellarim bordir' ('Bo'zotov' dostonida ham vatan mavzusi keng yoritilgan).",
            "check_questions": [
                {
                    "question": "Qoraqalpoq mumtoz adabiyotining asoschisi deb kim e'tirof etiladi?",
                    "options": ["Ajiniyoz", "Berdaq", "Kunxo'ja", "Ibroyim Yusupov"],
                    "correct_index": 1,
                    "explanation": "Berdaq G'arg'abay o'g'li qoraqalpoq xalqining eng buyuk mutafakkir shoiridir."
                },
                {
                    "question": "'Qirq qiz' qahramonlik dostonidagi bosh qahramon qizning ismi nima?",
                    "options": ["Oltinoy", "Guloyim", "Barchin", "Qunduz"],
                    "correct_index": 1,
                    "explanation": "Dostonning bosh qahramoni mard sarkarda qiz Guloyimdir."
                },
                {
                    "question": "Ajiniyoz Ziyvar qayerdagi madrasada tahsil olgan?",
                    "options": ["Buxoroda Mir Arabda", "Xivada Sherg'ozixon madrasasida", "Samarqandda Tillakori madrasasida", "Qo'qonda"],
                    "correct_index": 1,
                    "explanation": "Ajiniyoz Xivadagi mashhur Sherg'ozixon madrasasida o'qib, sharq tillari va falsafasini o'rgangan."
                }
            ],
            "tags": ["qoraqalpoq adabiyoti", "berdaq", "ajiniyoz", "qirq qiz", "ellarim bordir", "8-sinf"],
            "duration_minutes": 30
        },

        # NEMIS TILI (2)
        {
            "id": "lng-015",
            "slug": "nemis-tili-artikllar-va-otlar-turlanishi",
            "subject_id": "sub-20",
            "subject_name": "Nemis tili",
            "title": "Nemis tili grammatikasi: artikllar (der, die, das) va 4 ta kelishik (Kasus)",
            "grade_level": "5-6-sinf / A1",
            "difficulty": "Boshlang'ich",
            "objective": "Nemis tilida rodlar (maskulin, feminin, neytral), aniq va noaniq artikllar hamda 4 ta kelishik (Nominativ, Akkusativ, Dativ, Genitiv) turlanishini bilish.",
            "theory": "Nemis tilida har bir ot bosh harf bilan yoziladi va o'z artikliga ega bo'ladi:\n1) Maskulin (erkak jinsi) — der Tisch, der Mann (noaniq: ein);\n2) Feminin (ayol jinsi) — die Frau, die Lampe (noaniq: eine);\n3) Neytral (o'rta jins) — das Buch, das Kind (noaniq: ein);\n4) Ko'plik (Plural) — die Bücher, die Tische (noaniq artikl yo'q).\n4 ta kelishik (Kasus):\n- Nominativ (Bosh kelishik: Wer? Was?) — der, die, das, die;\n- Akkusativ (Tushum: Wen? Was?) — faqat erkak jinsi o'zgaradi: den (einen), die (eine), das (ein), die;\n- Dativ (Jo'nalish: Wem? Wo?): dem (einem), der (einer), dem (einem), den...n;\n- Genitiv (Qaratqich: Wessen?): des...s, der, des...s, der.",
            "examples": [
                {
                    "title": "Akkusativ kelishigida artikl o'zgarishi",
                    "problem": "'Ich habe ... (der Hund)' gapida qaysi artikl bo'ladi?",
                    "step_by_step": "Haben fe'li doimo Akkusativ (tushum) talab qiladi. Der Hund erkak jinsida 'den Hund' yoki noaniq 'einen Hund' ga aylanadi.\nNatija: 'Ich habe einen Hund'.",
                    "answer": "einen Hund (den Hund)"
                },
                {
                    "title": "Dativ kelishigida o'rin bildirish",
                    "problem": "'Das Buch liegt auf ... (der Tisch)' — kitob stol ustida yotibdi (qayerda? — Dativ).",
                    "step_by_step": "'Wo?' (qayerda?) savoliga javob berganda 'auf' predlogi Dativ talab qiladi. Der Tisch -> dem Tisch.\nNatija: 'Das Buch liegt auf dem Tisch'.",
                    "answer": "auf dem Tisch"
                }
            ],
            "exercise": "Nemis tilida 'die Schule' (maktab) so'zini 4 ta kelishikda aniq artikl bilan yozing.",
            "exercise_solution": "Nom: die Schule, Akk: die Schule, Dat: der Schule, Gen: der Schule.",
            "check_questions": [
                {
                    "question": "Akkusativ kelishigida qaysi jinsdagi aniq artikl 'den' ga o'zgaradi?",
                    "options": ["Feminin (die)", "Maskulin (der)", "Neutral (das)", "Plural (die)"],
                    "correct_index": 1,
                    "explanation": "Akkusativda faqat erkak jinsi 'der' -> 'den' (yoki ein -> einen) ga o'zgaradi."
                },
                {
                    "question": "Nemis tilida otlar qanday harf bilan yoziladi?",
                    "options": ["Faqat gap boshida bosh harf bilan", "Doimo bosh (katta) harf bilan", "Kichik harf bilan", "Ixtiyoriy"],
                    "correct_index": 1,
                    "explanation": "Nemis tili orfografiyasiga ko'ra barcha otlar gapning qayerida kelishidan qat'i nazar bosh harf bilan yoziladi."
                },
                {
                    "question": "'Wem?' (kimgacha?) qaysi nemischa kelishikning so'rog'i?",
                    "options": ["Nominativ", "Akkusativ", "Dativ", "Genitiv"],
                    "correct_index": 2,
                    "explanation": "'Wem?' Dativ (uchinchi kelishik) so'rog'idir."
                }
            ],
            "tags": ["nemis tili", "artikl", "kasus", "akkusativ", "dativ", "A1", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "lng-016",
            "slug": "nemis-tili-perfekt-va-modal-fellar",
            "subject_id": "sub-20",
            "subject_name": "Nemis tili",
            "title": "Nemis tili og'zaki nutqi: Perfekt zamoni va modalfeller (können, müssen, wollen)",
            "grade_level": "7-8-sinf / A2",
            "difficulty": "O'rta",
            "objective": "Nemis tilida og'zaki o'tgan zamon — Perfekt (haben/sein + Partizip II), ramka konstruksiyasi (Satzklammer) va modal fe'llarni to'g'ri qo'llash.",
            "theory": "Perfekt — nemis tilida so'zlashuv nutqida eng ko'p ishlatiladigan o'tgan zamondir. Formula: Ega + haben / sein (2-o'rinda tuslanadi) + ... + Partizip II (gapning eng oxirida!).\n- 'Sein' yordamchi fe'li bilan: joy o'zgarishi (harakat fe'llari: gehen, fahren, fliegen, kommen) va holat o'zgarishi (aufstehen, sterben) hamda sein, bleiben fe'llari ishlatiladi: 'Ich bin nach Berlin gefahren';\n- Qolgan barcha holatlarda 'haben' ishlatiladi: 'Ich habe ein Buch gelesen'.\nPartizip II yasalishi: ge- + o'zak + -(e)t (to'g'ri fe'llarda: gemacht, gespielt); ge- + o'zak + -en (noto'g'ri fe'llarda: gelesen, geschrieben).\nModal fe'llar: können (qila olmoq), müssen (majbur bo'lmoq), wollen (xohlamoq), dürfen (ruxsat bo'lmoq), sollen (kerak bo'lmoq). Gapda modal fe'l 2-o'rinda keladi, asosiy fe'l esa infintiv shaklda gap oxiriga suriladi: 'Ich kann Deutsch sprechen'.",
            "examples": [
                {
                    "title": "Perfektda jumla tuzish",
                    "problem": "'Er (machen) seine Hausaufgaben gestern' gapini Perfektda tuzing.",
                    "step_by_step": "1) Machen harakat yoki holat o'zgarishi emas, demak yordamchi fe'l: haben -> er hat;\n2) Partizip II: gemacht;\n3) Gap oxiriga suriladi: 'Er hat gestern seine Hausaufgaben gemacht'.",
                    "answer": "Er hat gestern seine Hausaufgaben gemacht"
                },
                {
                    "title": "Harakat fe'lida 'sein'",
                    "problem": "'Wir (fahren) nach Deutschland' gapini Perfektda tuzing.",
                    "step_by_step": "Fahren transportda joy o'zgarishi, shuning uchun 'sein' olinadi: wir sind. Partizip II: gefahren.\nNatija: 'Wir sind nach Deutschland gefahren'.",
                    "answer": "Wir sind nach Deutschland gefahren"
                }
            ],
            "exercise": "Modal fe'l bilan gap tuzing: 'Ich / wollen / ein neues Auto / kaufen'.",
            "exercise_solution": "'Ich will ein neues Auto kaufen' (modal fe'l will 2-o'rinda, kaufen gap oxirida).",
            "check_questions": [
                {
                    "question": "Perfekt zamonida asosiy ma'noli fe'l (Partizip II) gapning qayerida joylashadi?",
                    "options": ["Yordamchi fe'lning yonida", "Gap boshida", "Gapning eng oxirida", "Ixtiyoriy joyda"],
                    "correct_index": 2,
                    "explanation": "Nemis tilidagi ramka (Satzklammer) qoidasiga ko'ra Partizip II gapning eng oxirida turadi."
                },
                {
                    "question": "'Gehen' (bormoq) fe'li Perfektda qaysi yordamchi fe'l bilan qo'llanadi?",
                    "options": ["haben", "sein", "werden", "können"],
                    "correct_index": 1,
                    "explanation": "Piyoda joy o'zgarishi bo'lgani sababli 'sein' bilan keladi: 'Ich bin gegangen'."
                },
                {
                    "question": "'Können' modal fe'lining 'ich' (men) shaxsi uchun hozirgi zamon shakli qaysi?",
                    "options": ["kann", "könne", "konnte", "kannst"],
                    "correct_index": 0,
                    "explanation": "Modal fe'llarda 1- va 3-shaxs birlik bir xil va qo'shimchasiz bo'ladi: ich kann, er kann."
                }
            ],
            "tags": ["nemis tili", "perfekt", "modalverben", "haben sein", "A2", "8-sinf"],
            "duration_minutes": 30
        },

        # FRANSUZ TILI (2)
        {
            "id": "lng-017",
            "slug": "fransuz-tili-artikllar-va-fellar-guruhlari",
            "subject_id": "sub-21",
            "subject_name": "Fransuz tili",
            "title": "Fransuz tili: artikllar (le, la, les), unlilar ulanishi (liaison) va I guruh fe'llari",
            "grade_level": "5-6-sinf / A1",
            "difficulty": "Boshlang'ich",
            "objective": "Fransuz tili jinslari (masculin, féminin), aniq/noaniq artikllar, fe'llarning 3 ta guruhi va -er bilan tugovchi I guruh fe'llari tuslanishini o'rganish.",
            "theory": "Fransuz tilida 2 ta jins mavjud: Masculin (erkak: le livre, un livre) va Féminin (ayol: la table, une table). Ko'plikda: les livres, des livres. Agar so'z unli tovush bilan boshlansa, artikl qisqaradi: l'ami, l'école. Fe'llar 3 ta guruhga bo'linadi:\n1) I guruh (-er bilan tugovchi to'g'ri fe'llar: parler, aimer, habiter, travailler — 80% fe'llar). Tuslanish qo'shimchalari: je -e, tu -es, il/elle -e, nous -ons, vous -ez, ils/elles -ent (oxirgi -ent talaffuz qilinmaydi! Parler: je parle, tu parles, il parle, nous parlons, vous parlez, ils parlent);\n2) II guruh (-ir bilan tugovchi to'g'ri fe'llar: finir, choisir);\n3) III guruh (noto'g'ri fe'llar: être, avoir, aller, faire, prendre).\nLiaison (ulanish): so'z oxiridagi o'qilmaydigan undosh keyingi unli bilan boshlangan so'z bilan birikib o'qiladi (les amis -> le-zami).",
            "examples": [
                {
                    "title": "I guruh fe'lini tuslash",
                    "problem": "'Habiter' (yashamoq) fe'lini 'nous' va 'ils' shaxslarida tuslang.",
                    "step_by_step": "O'zak: habit-.\nNous habitons (biz yashaymiz);\nIls habitent (ular yashaydilar — -ent o'qilmaydi).",
                    "answer": "Nous habitons, ils habitent"
                },
                {
                    "title": "Être (bo'lmoq) fe'li hozirgi zamonda",
                    "problem": "'Men talabaman' va 'Biz do'stlarmiz' jumlalarini yozing.",
                    "step_by_step": "Être tuslanishi: je suis, tu es, il est, nous sommes, vous êtes, ils sont.\nNatija: 'Je suis étudiant', 'Nous sommes amis'.",
                    "answer": "Je suis étudiant, nous sommes amis"
                }
            ],
            "exercise": "'Aimer' (sevmoq/yoqtirmoq) fe'lini 'je' olmoshi bilan qo'llang.",
            "exercise_solution": "J'aime (unli bilan boshlangani uchun 'je' dagi e tushib qoladi: J'aime).",
            "check_questions": [
                {
                    "question": "Fransuz tilida -er bilan tugaydigan fe'llar qaysi guruhga kiradi?",
                    "options": ["I guruh", "II guruh", "III guruh", "Noto'g'ri guruh"],
                    "correct_index": 0,
                    "explanation": "Fransuz tilidagi fe'llarning aksariyati -er bilan tugovchi I guruh muntazam fe'llaridir."
                },
                {
                    "question": "Ils/Elles shaxsida I guruh fe'llarining -ent qo'shimchasi qanday talaffuz qilinadi?",
                    "options": ["-ent deb eshitiladi", "Umuman talaffuz qilinmaydi (o'qilmaydi)", "-on deb o'qiladi", "-e deb o'qiladi"],
                    "correct_index": 1,
                    "explanation": "Uchinchi shaxs ko'plikdagi -ent fe'l qo'shimchasi o'qilmaydi (masalan: ils parlent talaffuzda 'il parl')."
                },
                {
                    "question": "Unli bilan boshlangan so'zlar oldida 'le' va 'la' artikli qanday yoziladi?",
                    "options": ["O'zgarmaydi", "l' ko'rinishida apostrof bilan", "les bo'ladi", "tushib qoladi"],
                    "correct_index": 1,
                    "explanation": "Eliziya (qisqarish) hodisasiga ko'ra unli oldida l' yoziladi (l'ami, l'hôtel)."
                }
            ],
            "tags": ["fransuz tili", "artikl", "parler", "I guruh", "liaison", "A1", "6-sinf"],
            "duration_minutes": 25
        },
        {
            "id": "lng-018",
            "slug": "fransuz-tili-passe-compose-va-futur-simple",
            "subject_id": "sub-21",
            "subject_name": "Fransuz tili",
            "title": "Fransuz tili zamonlari: Passé Composé va Futur Simple",
            "grade_level": "7-8-sinf / A2",
            "difficulty": "O'rta",
            "objective": "Passé Composé (avoir/être + participe passé), harakat fe'llarida jins va sonda moslashuv hamda Futur Simple (kelasi zamon) shakllarini bilish.",
            "theory": "Passé Composé — fransuz tilida o'tgan tugallangan harakatlarni ifodalovchi asosiy zamondir. Formula: Ega + avoir / être (hozirgi zamonda) + Participe passé.\n- 'Être' yordamchi fe'li bilan: 14 ta asosiy harakat fe'li (aller, venir, arriver, partir, entrer, sortir, monter, descendre, naître, mourir...) va barcha o'zlik (pronominaux: se laver) fe'llari ishlatiladi. MUHIM: Être bilan kelganda Participe passé ega bilan jins va sonda moslashadi (Elle est allée — e qo'shiladi; Ils sont allés — s qo'shiladi);\n- Qolgan barcha fe'llar 'avoir' bilan ishlatiladi (moslashmaydi: J'ai mangé, elle a mangé).\nParticipe passé yasalishi: I guruh -er -> -é (parlé); II guruh -ir -> -i (fini); III guruh: fait, pris, vu, bu.\nFutur Simple (Oddiy kelasi zamon): Infinitivga -ai, -as, -a, -ons, -ez, -ont qo'shimchalari qo'shiladi (je parlerai, tu parleras, nous parlerons).",
            "examples": [
                {
                    "title": "Passé Composé da moslashuv",
                    "problem": "'Marie (aller) à Paris hier' gapini Passé Composé da yozing.",
                    "step_by_step": "1) Aller fe'li 'être' bilan keladi: Marie est...\n2) Marie ayol jinsida bo'lgani uchun Participe passé ga -e qo'shiladi: allée.\nNatija: 'Marie est allée à Paris hier'.",
                    "answer": "Marie est allée à Paris hier"
                },
                {
                    "title": "Futur Simple da jumlalar",
                    "problem": "'Ertaga men yangi kitob o'qiyman' jumlasini fransuzcha yozing (lire).",
                    "step_by_step": "Demain, je lirai un nouveau livre (lire -> lir-ai).",
                    "answer": "Demain, je lirai un nouveau livre"
                }
            ],
            "exercise": "Passé Composé ga aylantiring: 'Nous (finir) le travail' (avoir bilan).",
            "exercise_solution": "'Nous avons fini le travail'.",
            "check_questions": [
                {
                    "question": "Passé Composé da 'aller' (bormoq) fe'li qaysi yordamchi fe'l bilan ishlatiladi?",
                    "options": ["avoir", "être", "faire", "aller"],
                    "correct_index": 1,
                    "explanation": "Joy o'zgarishini bildiruvchi 'aller' fe'li har doim 'être' bilan tuslanadi."
                },
                {
                    "question": "'Être' yordamchi fe'li bilan kelganda Participe passé nima bilan moslashadi?",
                    "options": ["Obyekt bilan", "Eganing jinsi va soni bilan", "Moslashmaydi", "Vaqt bilan"],
                    "correct_index": 1,
                    "explanation": "Être bilan kelganda ayol jinsi uchun -e, ko'plik uchun -s qo'shimchasi qo'shiladi."
                },
                {
                    "question": "Futur Simple kelasi zamoni odatda nimanining asosida yasaladi?",
                    "options": ["Fe'l infinitiviga maxsus qo'shimchalar qo'shish orqali", "Hozirgi zamon orqali", "Avoir + V3", "Yordamchi fe'l bilan"],
                    "correct_index": 0,
                    "explanation": "Futur Simple fe'lning to'liq infinitiviga -ai, -as, -a, -ons, -ez, -ont qo'shish orqali hosil qilinadi."
                }
            ],
            "tags": ["fransuz tili", "passé composé", "futur simple", "avoir être", "A2", "8-sinf"],
            "duration_minutes": 30
        },

        # CHET TILI GRAMMATIKASI (2)
        {
            "id": "lng-019",
            "slug": "taqqoslashli-grammatika-zamonlar-uygunligi",
            "subject_id": "sub-22",
            "subject_name": "Chet tili grammatikasi",
            "title": "Taqqoslama grammatika: zamonlar moslashuvi (Sequence of Tenses) va ko'chirma gap",
            "grade_level": "10-11-sinf",
            "difficulty": "Murakkab",
            "objective": "Bosh gap o'tgan zamonda bo'lganda ergash gap zamonlarining orqaga surilishi (Direct to Indirect Speech) va o'zbek tili bilan qiyosiy tahlili.",
            "theory": "Ingliz va boshqa g'arbiy chet tillarida Zamonlar uyg'unligi (Sequence of Tenses) qoidasi mavjud: agar bosh gapdagi fe'l o'tgan zamonda (Past Simple: said, told, thought) kelsa, ergash gapdagi zamonlar ham bir pog'ona o'tmishga suriladi:\n- Present Simple -> Past Simple (am/is/are -> was/were, play -> played);\n- Present Continuous -> Past Continuous (is playing -> was playing);\n- Past Simple va Present Perfect -> Past Perfect (went/has gone -> had gone);\n- Future Simple (will) -> Future-in-the-Past (would).\nKo'rsatkichlarning o'zgarishi: today -> that day, tomorrow -> the next day, yesterday -> the day before, now -> then, here -> there, this -> that. O'zbek tilida bunday majburiy zamon siljishi yo'q ('U ertaga kelishini aytdi' — mazmun saqlanadi).",
            "examples": [
                {
                    "title": "Ko'chirma gapni o'zlashtirma gapga aylantirish",
                    "problem": "Direct: Tom said: 'I am learning German now'. Ushbu gapni Indirect Speech ga o'tkazing.",
                    "step_by_step": "1) Bosh gap: Tom said that...\n2) I -> he;\n3) am learning (Present Cont.) -> was learning (Past Cont.);\n4) now -> then.\nNatija: 'Tom said that he was learning German then'.",
                    "answer": "Tom said that he was learning German then"
                },
                {
                    "title": "Kelasi zamonning o'zgarishi",
                    "problem": "'She said: I will help you tomorrow' gapini o'zlashtiring.",
                    "step_by_step": "will -> would; tomorrow -> the next/following day.\nNatija: 'She said that she would help me the following day'.",
                    "answer": "She said that she would help me the following day"
                }
            ],
            "exercise": "Indirect ga o'giring: 'He said: I have lost my keys'.",
            "exercise_solution": "'He said that he had lost his keys' (have lost -> had lost).",
            "check_questions": [
                {
                    "question": "Bosh gap o'tgan zamonda bo'lsa, 'will' yordamchi fe'li ko'chirma gapda nimaga aylanadi?",
                    "options": ["shall", "would", "had been", "will be"],
                    "correct_index": 1,
                    "explanation": "Zamonlar moslashuviga ko'ra 'will' o'rniga 'would' (Future-in-the-Past) qo'llanadi."
                },
                {
                    "question": "O'zlashtirma gapda 'yesterday' so'zi nimaga o'zgaradi?",
                    "options": ["tomorrow", "the day before (the previous day)", "that day", "now"],
                    "correct_index": 1,
                    "explanation": "'Yesterday' o'rniga 'the day before' yoki 'the previous day' ishlatiladi."
                },
                {
                    "question": "Qaysi holatda zamonlar moslashuvi qoidasi qo'llanilmaydi va zamon o'zgarmaydi?",
                    "options": ["Har doim o'zgaradi", "Tabiat qonuni va doimiy haqiqat ifodalanganda ('The teacher said that water boils at 100 C')", "Faqat savollarda", "Inkor gaplarda"],
                    "correct_index": 1,
                    "explanation": "Umumiy ilmiy haqiqatlar va tabiat qonunlari ifodalanganda zamon o'zgarmasdan Present Simple da qoladi."
                }
            ],
            "tags": ["chet tili", "reported speech", "sequence of tenses", "zamonlar moslashuvi", "B2", "11-sinf"],
            "duration_minutes": 35
        },
        {
            "id": "lng-020",
            "slug": "inversion-cleft-sentences-va-stilistik-vositalar",
            "subject_id": "sub-22",
            "subject_name": "Chet tili grammatikasi",
            "title": "Murakkab sintaktik tuzilmalar: Inversiya va Cleft Sentences (Ajratilgan gaplar)",
            "grade_level": "11-sinf / C1",
            "difficulty": "Murakkab",
            "objective": "Ingliz tilida urg'u berish usullari: Inversiya (inkor so'zlari gap boshida kelganda) va Cleft sentences (It is/was... that...) sintaktik tahlili.",
            "theory": "Akademik va badiiy ingliz tilida biror fikrni kuchaytirish yoki hissiy urg'u berish uchun maxsus sintaktik tuzilmalardan foydalaniladi:\n1) Inversion (Inversiya — so'z tartibining teskari aylanishi): Inkor yoki cheklovchi so'zlar gap boshiga chiqqanda yordamchi fe'l egadan oldinga o'tadi (so'roq gap shaklidek):\n- Never, Rarely, Seldom, Barely, Scarcely, Little, Hardly... when, No sooner... than;\nMasalan: 'I have never seen such beauty' -> 'Never have I seen such beauty'; 'Hardly had he arrived when the rain started'.\n- Only after / Not only... but also: 'Not only did he win, but he also broke the record'.\n2) Cleft Sentences (Ajratilgan gaplar): Fikrning bir bo'lagiga alohida urg'u berish uchun 'It is / It was ... that / who' yoki 'What ... is / was' konstruksiyasi ishlatiladi:\n- 'John broke the window yesterday' -> 'It was John who broke the window' (Aynan Jon sindirdi);\n- 'I need a cup of hot coffee' -> 'What I need is a cup of hot coffee'.",
            "examples": [
                {
                    "title": "Inversiya hosil qilish",
                    "problem": "'He little knew about the upcoming danger' gapini inversiya bilan qayta yozing.",
                    "step_by_step": "'Little' so'zini gap boshiga chiqaramiz. Knew (Past Simple) -> yordamchi fe'l 'did':\nNatija: 'Little did he know about the upcoming danger'.",
                    "answer": "Little did he know about the upcoming danger"
                },
                {
                    "title": "Cleft sentence tuzish",
                    "problem": "'His kindness impressed me most' gapiga 'What' bilan boshlanuvchi cleft sentence tuzing.",
                    "step_by_step": "Natija: 'What impressed me most was his kindness'.",
                    "answer": "What impressed me most was his kindness"
                }
            ],
            "exercise": "Inversiyaga aylantiring: 'We had scarcely started the journey when the car broke down.'",
            "exercise_solution": "'Scarcely had we started the journey when the car broke down.'",
            "check_questions": [
                {
                    "question": "'Rarely' so'zi gap boshida kelganda gap tuzilishi qanday bo'ladi?",
                    "options": ["Oddiy darak gap tartibi saqlanadi", "Yordamchi fe'l egadan oldinga o'tadi (inversiya)", "Fe'l oxiriga suriladi", "Inkor yuklamasi qo'shiladi"],
                    "correct_index": 1,
                    "explanation": "Inkor va cheklov ma'nosidagi ravishlar gap boshida kelganda inversiya (yordamchi fe'l + ega) talab qilinadi."
                },
                {
                    "question": "'No sooner had I closed my eyes ... the phone rang' — nuqtalar o'rniga qaysi bog'lovchi qo'yiladi?",
                    "options": ["when", "than", "then", "that"],
                    "correct_index": 1,
                    "explanation": "'No sooner ... than' qat'iy korrelyativ juftlikdir ('Hardly ... when' bilan adashtirmaslik kerak)."
                },
                {
                    "question": "Cleft sentences nima maqsadda qo'llaniladi?",
                    "options": ["Faqat savol berish uchun", "Gapning ma'lum bir bo'lagiga kuchli urg'u va ta'kid berish uchun", "Matnni qisqartirish uchun", "Faqat o'tgan zamonda"],
                    "correct_index": 1,
                    "explanation": "Cleft gaplar (masalan: It was Ali who...) aynan ma'lum shaxs yoki voqeani alohida ajratib ko'rsatish uchun ishlatiladi."
                }
            ],
            "tags": ["chet tili", "inversion", "cleft sentences", "advanced grammar", "C1", "11-sinf"],
            "duration_minutes": 35
        }
    ]
    return materials

if __name__ == "__main__":
    mats = get_foreign_languages_materials()
    print(f"Generated {len(mats)} Foreign Languages materials.")
