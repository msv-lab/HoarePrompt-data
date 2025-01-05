#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000. ai and bi are lists of integers representing the statues currently placed and desired statues on each island, respectively. Each list has n elements, and each element is in the range from 0 to n-1, and all elements in ai and bi are distinct.**
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
    #State of the program after the if-else block has been executed: *`n` is an input integer, `ai` and `bi` are lists of integers representing the statues currently placed and desired statues on each island, `s` is a rotated version of the original string, `ss` is the index of the first occurrence of `ff` in the rotated `s` or -1 if `ff` is not found. If `s` is equal to `f`, then 'YES' is printed. Otherwise, the string `s` is not equal to `f`.
#Overall this is what the function does:The function `func` reads an integer `n` as input, followed by two lists of integers `f` and `s`. It then modifies `s` by rotating it based on certain conditions. After that, it compares the modified `s` with `f` and prints 'YES' if they are equal, otherwise it prints 'NO'. The function does not accept any parameters and works with predefined constraints. The output of the function is not provided.

