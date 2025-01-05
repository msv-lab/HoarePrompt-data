#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200000; ai is a list of n distinct integers where each element is in the range 0 ≤ ai ≤ n - 1, and exactly one element is 0; bi is a list of n distinct integers where each element is in the range 0 ≤ bi ≤ n - 1, and exactly one element is 0.
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
    #State of the program after the if-else block has been executed: *`n` is an input integer; `ai` is a list of `n` distinct integers; `bi` is a list of `n` distinct integers; `f` is modified to remove ' 0 '; `s` is modified to replace ' 0 ' with ' '; `ff` is the second element of the modified list `f`; `ss` is the index of the first occurrence of `ff` in `s`; `s` is assigned the value ' ' + `s[ss:-1]` + `s[:ss]`. If `s` is equal to `f`, 'YES' is printed; otherwise, `s` is not equal to `f` and 'NO' is printed.
#Overall this is what the function does:The function accepts an integer `n` and two lists `ai` and `bi` of `n` distinct integers, where each list contains numbers in the range from 0 to `n-1` with exactly one element being 0. It processes these lists by removing the 0 and checking if the modified list `s` can be rotated to match the modified list `f`. If the modified list `s` is equal to the modified list `f`, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value.

