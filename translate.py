from googletrans import Translator, LANGUAGES
import time
import re


def split_string(s):
    parts = re.split(r' (\(SW \d+\))', s)
    return [part.strip() for part in parts if part]

# List of similar strings
strings = [
    "Seawashed Glass (SW 9034)",
    "Ocean Blue (SW 8956)",
    "Beach Sand (SW 9123)"
]

# Split each string in the list
split_strings = [split_string(s) for s in strings]

for s in split_strings:
    print(s)
def format_langs():
    langs = list(LANGUAGES.values())
    capitalized_lst = [word.capitalize() for word in langs]
    return capitalized_lst

def translate_text(text, lang):
    lang_code = get_lang_code(lang)
    translator = Translator()
    translated = translator.translate(text, dest=lang_code)
    return translated.text

# Given a language name, find the language code:
def get_lang_code(lang_name):
    reversed_languages = {v: k for k, v in LANGUAGES.items()}
    return reversed_languages.get(lang_name.lower())

# Example
# lang_name = "English"
# lang_code = get_lang_code(lang_name)
# print(f"The language code for {lang_name} is {lang_code}.")

data = [{ "Name": "Seawashed Glass (SW 9034)", "RGB": [169, 192, 149] },  { "Name": "Frosted Emerald (SW 9035)", "RGB": [120, 177, 133] }]

def unpack(arg):
    data = {}
    for element in arg:
        data[element["Name"]] = element["RGB"]
    names, colors = data.keys(), data.values()
    return names, colors

names, colors = unpack(data)
split_strings = [split_string(s) for s in names]
print(split_strings)

