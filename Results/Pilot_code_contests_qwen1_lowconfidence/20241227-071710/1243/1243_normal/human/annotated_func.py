#State of the program right berfore the function call: The input string is a path consisting of lowercase Latin letters and the '/' character. The path starts with at least one '/' and the length does not exceed 100 characters.
def func():
    line = stdin.readline()
    array = line.split('/')
    str = ''
    for word in array:
        if word != '':
            str = str + '/' + word.strip()
        
    #State of the program after the  for loop has been executed: `line` is the original input string, `path` starts with at least one `/` and the length does not exceed 100 characters, `array` is the list of substrings obtained by splitting `line` using the delimiter `/`, and `str` is the concatenation of `'/'+word.strip()` for each non-empty `word` in `array`. If no words in `array` are non-empty, `str` remains an empty string.
    stdout.write(str)
#Overall this is what the function does:The function processes an input string representing a path, which consists of lowercase Latin letters and the '/' character, ensuring the path starts with at least one '/' and its length does not exceed 100 characters. It splits the input string by the '/' delimiter, strips leading and trailing whitespace from each segment, and then concatenates these segments back into a single string, adding a leading '/' if necessary. If no non-empty segments are found, the function outputs an empty string. The function reads the input string from standard input, modifies it according to the specified rules, and writes the result to standard output. Potential edge cases include paths with multiple consecutive '/' characters, paths with leading or trailing slashes, and empty paths.

