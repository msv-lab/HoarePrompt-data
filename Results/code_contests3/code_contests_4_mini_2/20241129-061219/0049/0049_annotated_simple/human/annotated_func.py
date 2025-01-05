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
        
    #State of the program after the  for loop has been executed: `n` is at least 1, `s` is a string of length 2 to 300000 consisting only of lowercase Latin letters, `c` is an input string, `flag` is True if there exists at least one index `i` such that `c[i] > c[i + 1]`, otherwise `flag` is False, and `pos` is the last index where this condition was met or undefined if `flag` is False.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is at least 1, `s` is a string of length 2 to 300000 consisting only of lowercase Latin letters, and `c` is an input string. If `flag` is True, indicating that there exists at least one index `i` such that `c[i] > c[i + 1]`, then 'YES' is printed along with `pos + 1` and `pos + 2`. If `flag` is False, indicating that there does not exist any index `i` such that `c[i] > c[i + 1]`, then 'NO' is printed and `pos` is undefined.
#Overall this is what the function does:The function reads an integer `n` and a string `c` of length `n`, where `n` is between 2 and 300000, and `c` consists only of lowercase Latin letters. It checks if there is at least one index `i` such that `c[i] > c[i + 1]`. If such an index exists, it prints 'YES' and the indices of the characters that form this pair (1-based). If no such index exists, it prints 'NO'. The function does not handle input errors or cases where the string length does not match `n`.

