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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 300000, `i` is `n - 2`, `flag` is True if at least one `c[i]` is greater than `c[i + 1]`, `pos` is the index of the last occurrence where `c[i]` is greater than `c[i + 1]`, or `flag` is False and `pos` is undefined if no such occurrence exists.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 300000. If `flag` is True, then "YES" is printed along with the outputs `pos + 1` and `pos + 2`, where `pos` is defined as the index of the last occurrence where `c[i]` is greater than `c[i + 1]`. If `flag` is False, then "NO" is printed, and `pos` is either undefined or represents the index of the last occurrence where `c[i]` is not greater than `c[i + 1]`.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300000) and a string `s` of length `n` consisting only of lowercase Latin letters. It checks if there exists at least one index `i` such that `s[i]` is greater than `s[i + 1]`. If such an index exists, it prints "YES" and the 1-based indices of that pair (i + 1, i + 2). If no such occurrences exist, it prints "NO". The function does not handle input errors or cases where the string is not of the specified length.

