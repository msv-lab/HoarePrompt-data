import re

def replace_specialchar(input_string: str) -> str:
    # Use regular expression to replace spaces, commas, and dots with a colon.
    return re.sub(r'[ ,.]', ':', input_string)

# Tests
assert replace_specialchar('Python language, Programming language.') == 'Python:language::Programming:language:'
assert replace_specialchar('a b c,d e f') == 'a:b:c:d:e:f'
assert replace_specialchar('ram reshma,ram rahim') == 'ram:reshma:ram:rahim'
