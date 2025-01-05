#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200000. ai and bi are lists of integers with length n, where each element is in the range from 0 to n-1 and distinct.**
def func():
    n = input()
    f = ' ' + raw_input() + ' '
    f = f.replace(' 0 ', ' ')
    s = ' ' + raw_input() + ' '
    s = s.replace(' 0 ', ' ')
    ff = f[1]
    ss = s.find(ff)
    s = ' ' + s[ss:-1] + s[:ss]
    if (s == f) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *n is an integer such that 2 <= n <= 200000, ai and bi are lists of integers with length n, where each element is in the range from 0 to n-1 and distinct, f is a string with spaces added before and after the input, s is a modified string after replacing ' 0 ' with ' ', ff is a character extracted from f, ss is the index of ff in s or -1 if ff is not found. If s is equal to f, the program retains the initial state. Otherwise, the modified string s is not equal to the original string f.
#Overall this is what the function does:The function `func` takes user input for a positive integer `n`, two lists `ai` and `bi` of length `n`, and performs string manipulation operations on the input strings `f` and `s`. It then checks if the modified string `s` is equal to the original string `f`, and prints 'YES' if they are equal, 'NO' otherwise. The function does not have a return value.

