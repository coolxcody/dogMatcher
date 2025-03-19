import google.generativeai as genai
import pandas as pd
import os
from dotenv import load_dotenv
from prompts import *

"""
# Dostosowanie bazy do projektu

df = pd.read_csv('akc-data-latest.csv')
df = df.drop(columns=["popularity"])
df = df.dropna()
df['avg_weight'] = (df['min_weight'] + df['max_weight']) / 2
df = df[df['avg_weight'] != 0]
df.to_csv('dog_breeds.csv', index=False)
"""

# Konfiguracja klucza API
load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')

# Konfiguracja Gemini
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

dogs = pd.read_csv('dog_breeds.csv')

def interpret_input(user_input, prompt_temp):
    """
    Uniwersalny interpreter zapytań użytkownika
    """
    prompt = prompt_temp.format(user_input=user_input)
    try:
        response = model.generate_content(contents=prompt)
        print(response.text)
        return response.text.strip()
    except Exception as e:
        print(f"Błąd podczas interpretacji zapytania: {e}")
        return "0"

def filter_weight(user_input, data):
    """
    Filtracja według wielkości
    """
    options = interpret_input(user_input, WEIGHT_PROMPT).split(",")
    filtered = pd.DataFrame()

    if "1" in options:
        filtered = pd.concat([filtered, data[data['avg_weight'] < 10]])
    if "2" in options:
        filtered = pd.concat([filtered, data[(data['avg_weight'] >= 10) & (data['avg_weight'] <= 25)]])
    if "3" in options:
        filtered = pd.concat([filtered, data[data['avg_weight'] > 25]])

    return filtered if not filtered.empty else None

def filter_grooming(user_input, data):
    """
    Filtracja według częstotliwości pielęgnacji
    """
    options = interpret_input(user_input, GROOMING_PROMPT)
    filtered = pd.DataFrame()

    if "2" in options:
        filtered = data[data['grooming_frequency_value'] <= 0.2]
    elif "4" in options:
        filtered = data[data['grooming_frequency_value'] <= 0.4]
    elif "6" in options:
        filtered = data[data['grooming_frequency_value'] <= 0.6]
    elif "8" in options:
        filtered = data[data['grooming_frequency_value'] <= 0.8]
    elif "10" in options:
        filtered = data[data['grooming_frequency_value'] <= 1.0]

    return filtered if not filtered.empty else None

def filter_shedding(user_input, data):
    """
    Filtracja według linienia
    """
    options = interpret_input(user_input, SHEDDING_PROMPT)
    filtered = pd.DataFrame()

    if "2" in options:
        filtered = data[data['shedding_value'] <= 0.2]
    elif "4" in options:
        filtered = data[data['shedding_value'] <= 0.4]
    elif "6" in options:
        filtered = data[data['shedding_value'] <= 0.6]
    elif "8" in options:
        filtered = data[data['shedding_value'] <= 0.8]
    elif "10" in options:
        filtered = data[data['shedding_value'] <= 1.0]

    return filtered if not filtered.empty else None

def process_filters(filter_list, dog_list):
    for question, filter_func in filter_list:
        answer = input(question)
        dog_list = filter_func(answer, dog_list)

        if dog_list is None:
            return None

        print("\nFiltracja zakończona, wyniki:")
        print(dog_list)

    return dog_list

filters = [
    ("Jak duży powinien być Twój idealny pies? ", filter_weight),
    ("Jak często możesz zajmować się pielęgnacją swojego zwierzaka? ", filter_grooming),
    ("Jak często może linieć Twój idealny pies? ", filter_shedding)]

filtered_dogs = process_filters(filters, dogs)

if filtered_dogs is None:
    print("\nBrak wyników po filtracji.")