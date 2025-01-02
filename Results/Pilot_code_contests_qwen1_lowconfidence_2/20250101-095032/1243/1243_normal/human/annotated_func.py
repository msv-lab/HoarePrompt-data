#State of the program right berfore the function call: The input string is a non-empty string containing only lowercase Latin letters and the character '/', starting with at least one '/'. The length of the string does not exceed 100 characters.
def func():
    line = stdin.readline()
    array = line.split('/')
    str = ''
    for word in array:
        if word != '':
            str = str + '/' + word.strip()
        
    #State of the program after the  for loop has been executed: `word` is the last element in `array`, `str` is the original value of `str` plus `'/'` plus the stripped version of each non-empty word in `array`. If there are no non-empty words in `array`, `str` remains the original value of `str`.
    stdout.write(str)
#Overall this is what the function does:The function processes a non-empty input string containing only lowercase Latin letters and the character '/', ensuring the string starts with at least one '/'. It then splits the string by '/', strips any leading or trailing whitespace from each resulting substring, and concatenates them back together with '/' in between. The final result, which is the processed string, is written to standard output. Potential edge cases include strings with no non-empty substrings after splitting, where the output remains unchanged. The function does not return any value but modifies and outputs the string directly.

