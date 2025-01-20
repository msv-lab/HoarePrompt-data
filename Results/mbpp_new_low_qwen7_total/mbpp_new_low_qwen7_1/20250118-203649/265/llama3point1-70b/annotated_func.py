#State of the program right berfore the function call: s is a string and pattern is a valid regular expression string.
def func_1(s, pattern):
    match = re.search(pattern, s)
    if match :
        return match.group(), match.start(), match.end()
        #The program returns match.group() which is the string matched by the pattern, match.start() which is the start index of the match, and match.end() which is the end index of the match
    else :
        return None
        #The program returns None
#Overall this is what the function does:The function `func_1` accepts two parameters: `s`, a string, and `pattern`, a valid regular expression string. It searches for a match of the regular expression `pattern` within the string `s`. If a match is found, the function returns a tuple containing the matched string (`match.group()`), the start index of the match (`match.start()`), and the end index of the match (`match.end()`). If no match is found, the function returns `None`.

