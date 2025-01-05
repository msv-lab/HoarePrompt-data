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
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `flag` is True if at least one pair was found where `c[i] > c[i + 1]`, `pos` is the index of the last such pair, otherwise `flag` is False and `pos` is undefined.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is at least 2. If `flag` is True, it indicates that at least one pair was found where `c[i] > c[i + 1]`, so 'YES' is printed along with `pos + 1` and `pos + 2`. If `flag` is False, it indicates that no pairs were found where `c[i] > c[i + 1]`, and `pos` is undefined.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300000) and a string `c` of length `n` consisting only of lowercase Latin letters. It checks for any pair of adjacent characters in the string where the first character is greater than the second. If such a pair exists, it prints 'YES' along with the 1-based indices of the pair; otherwise, it prints 'NO'.

