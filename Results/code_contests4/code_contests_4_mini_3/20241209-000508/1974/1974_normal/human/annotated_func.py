#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200,000; ai is a list of n distinct integers where each integer is in the range 0 to n - 1, and exactly one integer is 0; bi is a list of n distinct integers where each integer is in the range 0 to n - 1, and exactly one integer is 0.
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
    #State of the program after the if-else block has been executed: *`n` is an input integer; `f` has had occurrences of '0' replaced with ' '; `s` is the updated value after the replacement operation; `ff` is the character at index 1 of `f`; `ss` is the index of the first occurrence of `ff` in `s`; if `s` is equal to `f`, 'YES' has been printed. Otherwise, if `s` is not equal to `f`, 'NO' is printed.
#Overall this is what the function does:The function accepts an integer input `n` (between 2 and 200,000) and two lists of distinct integers `ai` and `bi` (both containing integers from 0 to n-1, with one integer being 0 in each list). It reads these lists as strings, removes occurrences of '0', and then checks if the modified second list `s` matches the modified first list `f`. It prints 'YES' if they are equal and 'NO' if they are not. However, the function does not explicitly return any values.

