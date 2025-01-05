#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000. ai and bi are lists of integers with length n, where each element is in the range from 0 to n - 1 and all elements are distinct.**
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
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 <= n <= 200,000; `ai` and `bi` are lists of integers with length n, where each element is in the range from 0 to n - 1 and all elements are distinct; `f` is a modified string after replacing ' 0 ' with ' ', `ff` is a character extracted from `f`, `ss` is the index of the first occurrence of `ff` in `s. If `s` is equal to `f`, the program does nothing. If `s` is not equal to `f`, the program prints 'NO'.
#Overall this is what the function does:The function `func` reads an integer `n`, two lists of integers `ai` and `bi` of length `n`, and performs a series of string manipulations on input strings `f` and `s`. It then checks if the modified `s` is equal to `f` and prints 'YES' if they are equal, 'NO' otherwise. The function does not return any specific value.

