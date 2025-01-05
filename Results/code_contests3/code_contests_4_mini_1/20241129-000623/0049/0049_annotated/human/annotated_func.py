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
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `flag` is True or False, `pos` is the index of the last occurrence where `c[i]` is greater than `c[i + 1]` if `flag` is True; otherwise, `pos` is undefined.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is at least 2. If `flag` is True, `pos` is the index of the last occurrence where `c[i]` is greater than `c[i + 1]`, and 'YES' is printed along with the output `pos + 1` and `pos + 2`. If `flag` is False, `pos` is undefined, and 'NO' is printed.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300000) and a string `c` of length `n` consisting only of lowercase Latin letters. It checks if there is any index `i` in the string such that the character at index `i` is greater than the character at index `i + 1`. If such an index exists, it prints 'YES' along with the positions (1-based index) of the characters at `i` and `i + 1`. If no such index exists, it prints 'NO'. The function does not handle cases where the input format is invalid or where `s` is not of the specified length.

