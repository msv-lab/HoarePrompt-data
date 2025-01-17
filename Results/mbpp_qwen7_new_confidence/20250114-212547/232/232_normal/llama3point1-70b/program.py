import re

def extract_values(s):
    return re.findall(r'"(.*?)"', s)
