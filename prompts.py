"""
Prompty dla różnych kategorii
"""

WEIGHT_PROMPT = """
Użytkownik wprowadził następujące zdanie: "{user_input}".
Twoim zadaniem jest określenie preferencji użytkownika dotyczących wielkości psa, stosując poniższe zasady:
Kategorie:
1 – Małe psy (poniżej 10 kg)
2 – Średnie psy (od 10 do 25 kg)
3 – Duże psy (powyżej 25 kg)
Zasady:
1. Jeśli użytkownik wyraźnie wskazuje jedną kategorię, zwróć tylko jej numer (np. "1", "2" lub "3").
2. Jeśli użytkownik chce wybrać więcej niż jedną kategorię, zwróć numery wybranych kategorii oddzielone przecinkami (np. "1,2").
3. Jeśli użytkownik zaznacza, że nie ma preferencji / brak znaczenia lub pozostawia decyzję otwartą, zwróć "1,2,3".
4. Jeśli zdanie jest niejasne lub nie pasuje do żadnej kategorii, zwróć "0".
Pamiętaj:
- Analizuj kontekst wypowiedzi użytkownika.
- Nie dodawaj żadnych dodatkowych wyjaśnień ani tekstu.
"""

GROOMING_PROMPT = """
Użytkownik wprowadził następujące zdanie: "{user_input}".
Twoim zadaniem jest zinterpretowanie intencji użytkownika i określenie, jak często użytkownik może zajmować się pielęgnacją swojego zwierzaka, wybierając odpowiednie kategorie. Oto zasady interpretacji:
Kategorie:
0.2 – Okazjonalne czyszczenie sierści - trwa zwykle kilka minut, wykonywane rzadko.
0.4 – Czyszczenie sierści raz w tygodniu - trwa około 10-30 minut, wykonywane raz w tygodniu.
0.6 – Czyszczenie 2-3 razy w tygodniu - trwa około 10-30 minut, wykonywane 2-3 razy w tygodniu.
0.8 – Czyszczenie sierści codziennie - trwa około 10-30 minut dziennie, co daje 70-210 minut w tygodniu.
1.0 – Specjalistyczna pielęgnacja przez profesjonalistę - trwa zwykle kilka godzin dziennie, w zależności od potrzeb zwierzęcia.
Zasady:
1. Jeśli użytkownik wyraźnie wskazuje jedną kategorię, zwróć tylko jej numer (np. "0.2").
2. Jeśli użytkownik wskazuje więcej niż jedną kategorię, wybierz najwyższą kategorię (np. "0.2,0.4" -> "0.4").
3. Jeśli użytkownik zaznacza brak preferencji / brak znaczenia lub pozostawia decyzję otwartą, zwróć "1.0".
4. Jeśli zdanie jest niejasne, niezrozumiałe lub nie pasuje do żadnej kategorii, zwróć "0".
Pamiętaj:
- Analizuj kontekst wypowiedzi użytkownika.
- Nie dodawaj żadnych dodatkowych wyjaśnień ani tekstu.
"""

SHEDDING_PROMPT = """
Użytkownik wprowadził następujące zdanie: "{user_input}".
Twoim zadaniem jest określenie preferencji użytkownika dotyczących częstotliwości linienia psa, stosując poniższe zasady:
Kategorie:
0.2 – Rzadkie linienie, użytkownik preferuje psy, które prawie nie linieją.
0.4 – Sporadyczne linienie, użytkownik akceptuje psy z niewielkim linieniem.
0.6 – Sezonowe linienie, użytkownik akceptuje psy, które linieją w określonych porach roku.
0.8 – Regularne linienie, użytkownik akceptuje psy, które linieją przez większość czasu w umiarkowanym stopniu.
1.0 – Częste linienie, użytkownik akceptuje psy, które linieją intensywnie przez cały rok.
Zasady:
1. Jeśli użytkownik wyraźnie wskazuje jedną kategorię, zwróć tylko jej wartość (np. "0.2").
2. Jeśli użytkownik wskazuje więcej niż jedną kategorię, wybierz najwyższą kategorię (np. "0.4,0.6" -> "0.6").
3. Jeśli użytkownik zaznacza brak preferencji / brak znaczenia lub pozostawia decyzję otwartą, zwróć "1.0".
4. Jeśli zdanie jest niejasne lub nie pasuje do żadnej kategorii, zwróć "0".
Pamiętaj:
- Analizuj kontekst wypowiedzi użytkownika.
- Nie dodawaj żadnych dodatkowych wyjaśnień ani tekstu.
"""

ENERGY_PROMPT = """
Użytkownik wprowadził następujące zdanie: "{user_input}".
Twoim zadaniem jest określenie preferencji użytkownika dotyczących zapotrzebowania energetycznego psa, stosując poniższe zasady:
Kategorie:
0.2 – Couch Potato, użytkownik preferuje psy o bardzo niskim poziomie aktywności.
0.4 – Calm, użytkownik akceptuje psy o spokojnym temperamencie i niskim zapotrzebowaniu na ruch.
0.6 – Regular Exercise, użytkownik akceptuje psy wymagające umiarkowanej ilości codziennego ruchu.
0.8 – Energetic, użytkownik akceptuje psy o wysokim poziomie energii, które potrzebują dużo aktywności.
1.0 – Needs Lots of Activity, użytkownik akceptuje psy o bardzo wysokim poziomie energii, wymagające intensywnego ruchu i zajęć.
Zasady:
1. Jeśli użytkownik wyraźnie wskazuje jedną kategorię, zwróć tylko jej wartość (np. "0.4").
2. Jeśli użytkownik wskazuje więcej niż jedną kategorię, wybierz najwyższą kategorię (np. "0.6, 0.8" -> "0.8").
3. Jeśli użytkownik zaznacza brak preferencji / brak znaczenia lub pozostawia decyzję otwartą, zwróć "1.0".
4. Jeśli zdanie jest niejasne lub nie pasuje do żadnej kategorii, zwróć "0".
Pamiętaj:
- Analizuj kontekst wypowiedzi użytkownika.
- Nie dodawaj żadnych dodatkowych wyjaśnień ani tekstu.
"""

TRAINABILITY_PROMPT = """
Użytkownik wprowadził następujące zdanie: "{user_input}".
Twoim zadaniem jest określenie preferencji użytkownika dotyczących zdolności psa do szkolenia, stosując poniższe zasady:
Kategorie:
0.2 – Może być uparty, użytkownik akceptuje psy, które mogą być trudne do szkolenia.
0.4 – Niezależny, użytkownik akceptuje psy o niezależnym charakterze, które wymagają większej cierpliwości podczas szkolenia.
0.6 – Chętny do współpracy, użytkownik preferuje psy, które są skłonne do współpracy i umiarkowanie łatwe w szkoleniu.
0.8 – Łatwy w szkoleniu, użytkownik preferuje psy, które są łatwe do szkolenia i szybko uczą się poleceń.
1.0 – Chętny do zadowolenia, użytkownik preferuje psy, które są wyjątkowo chętne do współpracy i bardzo łatwe w szkoleniu.
Zasady:
1. Jeśli użytkownik wyraźnie wskazuje jedną kategorię, zwróć tylko jej wartość (np. "0.2").
2. Jeśli użytkownik wskazuje więcej niż jedną kategorię, wybierz najwyższą kategorię (np. "0.4,0.6" -> "0.6").
3. Jeśli użytkownik zaznacza brak preferencji / brak znaczenia lub pozostawia decyzję otwartą, zwróć "1.0".
4. Jeśli zdanie jest niejasne lub nie pasuje do żadnej kategorii, zwróć "0".
Pamiętaj:
- Analizuj kontekst wypowiedzi użytkownika.
- Nie dodawaj żadnych dodatkowych wyjaśnień ani tekstu.
"""

DEMEANOR_PROMPT = """
Użytkownik wprowadził następujące zdanie: "{user_input}".
Twoim zadaniem jest określenie preferencji użytkownika dotyczących reakcji psa na obcych i inne zwierzęta, stosując poniższe zasady:
Kategorie:
0.2 – Zdystansowany/Ostrożny, użytkownik preferuje psy, które są bardzo powściągliwe wobec obcych i innych zwierząt.
0.4 – Powściągliwy wobec obcych, użytkownik akceptuje psy, które zachowują umiarkowany dystans wobec obcych.
0.6 – Czujny/Reagujący, użytkownik akceptuje psy, które są czujne i reagują na obecność obcych lub innych zwierząt.
0.8 – Przyjazny, użytkownik akceptuje psy, które są otwarte i przyjazne wobec obcych oraz innych zwierząt.
1.0 – Towarzyski, użytkownik preferuje psy, które są bardzo towarzyskie i uwielbiają kontakt z obcymi oraz innymi zwierzętami.
Zasady:
1. Jeśli użytkownik wyraźnie wskazuje jedną kategorię, zwróć tylko jej wartość (np. "0.2").
2. Jeśli użytkownik wskazuje więcej niż jedną kategorię, wybierz najwyższą kategorię (np. "0.4,0.6" -> "0.6").
3. Jeśli użytkownik zaznacza brak preferencji / brak znaczenia lub pozostawia decyzję otwartą, zwróć "1.0".
4. Jeśli zdanie jest niejasne lub nie pasuje do żadnej kategorii, zwróć "0".
Pamiętaj:
- Analizuj kontekst wypowiedzi użytkownika.
- Nie dodawaj żadnych dodatkowych wyjaśnień ani tekstu.
"""

TEMPERAMENT_PROMPT = """
Użytkownik wprowadził następujące zdanie: "{user_input}".
Twoim zadaniem jest określenie najbardziej zbliżonych cech charakteru psa z poniższej listy:
{prompt_data}
Jeśli podane przez użytkownika cechy nie pokrywają się z żadnym z temperamentów psów wybierz rasę, która jest najbardziej uniwersalna lub neutralna pod względem cech charakteru. 
Zwróć tylko jedną rasę psa - bez żadnych dodatkowych słów.
"""

TRANSLATE_PROMPT = """
Przetłumacz tekst na język polski:
"{text}"
"""
