#State of the program right berfore the function call: The input string is a non-empty string consisting of lowercase Latin letters and the '/' character. The string starts with at least one '/' and represents a directory path. The length of the string does not exceed 100 characters.
def func():
    line = stdin.readline()
    array = line.split('/')
    str = ''
    for word in array:
        if word != '':
            str = str + '/' + word.strip()
        
    #State of the program after the  for loop has been executed: `line` is a non-empty string starting with at least one '/', `array` is a list of substrings from `line` split by '/', `str` is '/' + (the concatenated result of stripping each non-empty word in `array` with a '/' separator).
    stdout.write(str)
#Overall this is what the function does:The function reads a single line from standard input, which is expected to be a non-empty string representing a directory path consisting of lowercase Latin letters and '/' characters. It splits the input string by '/' and concatenates the non-empty parts with a '/' separator, trimming any leading or trailing whitespace. Finally, it writes the resulting string to standard output. Potential edge cases include empty strings or input strings without any '/'. The function does not return any value.

