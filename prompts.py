"""
Prompty dla różnych kategorii
"""

WEIGHT_PROMPT = """
Użytkownik wprowadził następujące zdanie: "{user_input}".
Twoim zadaniem jest zinterpretowanie intencji użytkownika i określenie, które kategorie psów chce wybrać:
1 – Małe psy (poniżej 10 kg)
2 – Średnie psy (od 10 do 25 kg)
3 – Duże psy (powyżej 25 kg)
Zasady:
1. Jeśli użytkownik wyraźnie wskazuje jedną kategorię, zwróć tylko jej numer (np. "1", "2" lub "3").
2. Jeśli użytkownik chce wybrać więcej niż jedną kategorię, zwróć numery wybranych kategorii oddzielone przecinkami (np. "1,2").
3. Jeśli użytkownik zaznacza, że nie ma preferencji lub pozostawia decyzję otwartą, zwróć "1,2,3".
4. Jeśli zdanie jest niejasne lub nie pasuje do żadnej kategorii, zwróć "0".
Pamiętaj:
- Analizuj kontekst wypowiedzi użytkownika.
- Nie dodawaj żadnych dodatkowych wyjaśnień ani tekstu.
"""

GROOMING_PROMPT = """
Użytkownik wprowadził następujące zdanie: "{user_input}".
Twoim zadaniem jest zinterpretowanie intencji użytkownika i określenie, jak często użytkownik może zajmować się pielęgnacją swojego zwierzaka, wybierając odpowiednie kategorie. Oto zasady interpretacji:
Kategorie:
2 – Okazjonalne czyszczenie sierści - trwa zwykle kilka minut, wykonywane rzadko.
4 – Czyszczenie sierści raz w tygodniu - trwa około 10-30 minut, wykonywane raz w tygodniu.
6 – Czyszczenie 2-3 razy w tygodniu - trwa około 10-30 minut, wykonywane 2-3 razy w tygodniu.
8 – Czyszczenie sierści codziennie - trwa około 10-30 minut dziennie, co daje 70-210 minut w tygodniu.
10 – Specjalistyczna pielęgnacja przez profesjonalistę - trwa zwykle kilka godzin dziennie, w zależności od potrzeb zwierzęcia.
Zasady:
1. Jeśli użytkownik wyraźnie wskazuje jedną kategorię, zwróć tylko jej numer (np. "2").
2. Jeśli użytkownik wskazuje więcej niż jedną kategorię, wybierz najwyższą kategorię (np. "2,4" -> "4").
3. Jeśli użytkownik zaznacza brak preferencji lub pozostawia decyzję otwartą, zwróć "10".
4. Jeśli zdanie jest niejasne, niezrozumiałe lub nie pasuje do żadnej kategorii, zwróć "0".
Pamiętaj:
- Analizuj kontekst wypowiedzi użytkownika.
- Nie dodawaj żadnych dodatkowych wyjaśnień ani tekstu.
"""

SHEDDING_PROMPT = """
Użytkownik wprowadził następujące zdanie: “{user_input}”.
Twoim zadaniem jest zinterpretowanie intencji użytkownika i określenie jego preferencji co do częstotliwości linienia psa, wybierając odpowiednie kategorie. Oto zasady interpretacji:
Kategorie:
2 – Rzadkie linienie, użytkownik preferuje psy, które prawie nie linieją.
4 – Sporadyczne linienie, użytkownik akceptuje psy z niewielkim linieniem.
6 – Sezonowe linienie, użytkownik akceptuje psy, które linieją w określonych porach roku.
8 – Regularne linienie, użytkownik akceptuje psy, które linieją przez większość czasu w umiarkowanym stopniu.
10 – Częste linienie, użytkownik akceptuje psy, które linieją intensywnie przez cały rok.
Zasady:
1.	Jeśli użytkownik wyraźnie wskazuje jedną kategorię, zwróć tylko jej wartość (np. “2”).
2.	Jeśli użytkownik wskazuje więcej niż jedną kategorię, wybierz najwyższą kategorię (np. “4,6” -> “6”).
3.	Jeśli użytkownik zaznacza brak preferencji lub pozostawia decyzję otwartą, zwróć “10”.
4.	Jeśli zdanie jest niejasne, niezrozumiałe lub nie pasuje do żadnej kategorii, zwróć “0”.
Pamiętaj:
- Analizuj kontekst wypowiedzi użytkownika.
- Nie dodawaj żadnych dodatkowych wyjaśnień ani tekstu.
"""