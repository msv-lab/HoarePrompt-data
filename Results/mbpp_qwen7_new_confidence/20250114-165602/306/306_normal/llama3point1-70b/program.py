import re

def check_str(s):
    return bool(re.match('^[aeiouAEIOU]', s))
