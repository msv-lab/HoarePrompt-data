import re

def text_match_three(text):
    return bool(re.search("abbbb", text))
