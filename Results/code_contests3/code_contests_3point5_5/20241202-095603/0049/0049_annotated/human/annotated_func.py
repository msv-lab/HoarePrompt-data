#State of the program right berfore the function call: **Precondition**: **n is an integer such that 2 ≤ n ≤ 3*10^5 and s is a string of length n consisting only of lowercase Latin letters.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `n` is an integer based on the first element of the user input list, `s` is a string of length `n`, `c` is a string based on the user input, `flag` is True if there exists at least one instance where `c[i]` is greater than `c[i + 1]`, `pos` is the index of the last occurrence where `c[i]` is greater than `c[i + 1]`. If no such occurrence exists, `flag` remains False.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer, `s` is a string of length `n`, `c` is a string based on user input. If `flag` is True, 'YES' is printed. If `flag` is False, `pos` is the index of the last occurrence where `c[i]` is greater than `c[i + 1]` if it exists, otherwise `pos` remains the same.
#Overall this is what the function does:The function `func` reads an integer `n` followed by a string `c` from the user input. It then iterates through the string to check if there exists a character in `c` that is greater than the next character. If such a case is found, it prints 'YES' along with the indices of the characters involved. If no such case is found, it prints 'NO'. The function does not accept any parameters explicitly, but works with the predefined values of `n` and `c`.

