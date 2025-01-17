import re

def text_starta_endb(text):
    return bool(re.match(r'a.*b$', text))