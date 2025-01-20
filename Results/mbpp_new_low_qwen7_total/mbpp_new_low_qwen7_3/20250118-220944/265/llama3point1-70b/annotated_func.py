#State of the program right berfore the function call: s is a string and pattern is a valid regular expression pattern.
def func_1(s, pattern):
    match = re.search(pattern, s)
    if match :
        return match.group(), match.start(), match.end()
        #`The program returns match.group() which is the string matched by the regular expression, match.start() which is the start position of the match in the string s, and match.end() which is the end position of the match in the string s`
    else :
        return None
        #The program returns None
#Overall this is what the function does:The function `func_1` accepts two parameters: `s` (a string) and `pattern` (a valid regular expression pattern). It searches for a match of the regular expression pattern within the string `s`. If a match is found, the function returns a tuple containing three elements: `match.group()` (the matched substring), `match.start()` (the starting index of the match), and `match.end()` (the ending index of the match). If no match is found, the function returns `None`.

