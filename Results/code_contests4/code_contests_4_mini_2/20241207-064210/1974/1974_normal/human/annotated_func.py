#State of the program right berfore the function call: n is an integer between 2 and 200,000, ai is a list of n distinct integers where each integer is between 0 and n-1, and bi is a list of n distinct integers where each integer is between 0 and n-1. Both lists contain exactly one occurrence of 0, indicating the position of the empty pedestal.
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
    #State of the program after the if-else block has been executed: *`n` is an input string; `ai` is a list of `n` distinct integers; `bi` is a list of `n` distinct integers; `f` has had '0' replaced with ' '; `s` is now a modified string; `ff` is the substring of `f` starting from index 1; `ss` is the index of the first occurrence of `ff` in `s` or -1 if not found. If `s` is equal to `f`, 'YES' is printed. Otherwise, if `s` is not equal to `f`, 'NO' is printed.
#Overall this is what the function does:The function reads an integer `n` and two lists of distinct integers `ai` and `bi`. It modifies these lists by removing the occurrence of the integer `0` and checks if the modified version of the second list `s` can be made equal to the modified version of the first list `f` by rotating it. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not handle inputs outside of the specified constraints and relies on the input format being correct, which may lead to unexpected behavior if the constraints are not met.

