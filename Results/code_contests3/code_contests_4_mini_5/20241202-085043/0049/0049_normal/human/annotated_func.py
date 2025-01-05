#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 300000, and s is a string of length n consisting only of lowercase Latin letters.
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than or equal to 1, `flag` is either True or False (indicating if any `c[i]` was greater than `c[i + 1]`), `pos` is the last index where `c[i]` was greater than `c[i + 1]` or remains uninitialized if `flag` is False.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer greater than or equal to 1. If `flag` is True, then 'YES' is printed, followed by `pos + 1` and `pos + 2`, where `pos` is the last index where `c[i]` was greater than `c[i + 1]`. If `flag` is False, 'NO' is printed, and `pos` remains uninitialized.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300000) and a string `c` of length `n` consisting only of lowercase Latin letters. It checks if there are any adjacent characters in the string such that the first character is greater than the second. If such a pair exists, it prints "YES" and the 1-based indices of the first pair found; otherwise, it prints "NO". If no such adjacent characters are found, the variable `pos` remains uninitialized.

