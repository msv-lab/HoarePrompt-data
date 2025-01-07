#State of the program right berfore the function call: s is a string consisting of only lowercase English letters.**
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` does not contain any character from `alphabet`, `res` is a string consisting of all characters from `alphabet` in order
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` does not contain any character from `alphabet`, `res` is a string consisting of all characters from `alphabet` in order. If the length of `res` is 26, `res` is printed to the console. Otherwise, -1 is printed.
#Overall this is what the function does:The function `func` reads a string consisting of only lowercase English letters. It then iterates over the alphabet and for each character, it appends it to a result string in order by replacing occurrences of that character in the input string with the next character in the alphabet. After processing all characters in the alphabet, if the result string contains all 26 letters, it is printed; otherwise, -1 is printed. The function does not accept any parameters and does not return any value.

