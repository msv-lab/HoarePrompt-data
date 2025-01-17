import re

def extract_values(s):
    # Use a regular expression to find all substrings within double quotes
    return re.findall(r'"(.*?)"', s)

# Test cases to validate the solution
assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
assert extract_values('"python","program","language"') == ['python', 'program', 'language']
assert extract_values('"red","blue","green","yellow"') == ['red', 'blue', 'green', 'yellow']
