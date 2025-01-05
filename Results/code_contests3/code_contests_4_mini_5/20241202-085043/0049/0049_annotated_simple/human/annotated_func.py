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
        
    #State of the program after the  for loop has been executed: `n` is the first element of the input list greater than 1, `i` is `n - 2`, `s` is a string of length `n`, `c` is the string input from the user, `flag` is True if at least one character in `c` is found to be greater than the next character during the iterations; `pos` is assigned the index of the last character found to be greater than the next character, or remains undefined if no such character is found.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is the first element of the input list greater than 1; `i` is `n - 2`; `s` is a string of length `n`; `c` is the string input from the user. If `flag` is True, `pos` is assigned the index of the last character found to be greater than the next character, 'YES' is printed along with `pos + 1` and `pos + 2`. Otherwise, if `flag` is False, `pos` remains undefined and 'NO' is printed.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300000) and a string `c` of length `n` consisting only of lowercase Latin letters. It checks if there exists at least one character in the string that is greater than the next character in the sequence. If such a character is found, it prints 'YES' along with the indices of the two characters involved (1-based indexing). If no such character is found, it prints 'NO'.

