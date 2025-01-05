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
        
    #State of the program after the  for loop has been executed: `n` is at least 1, `flag` is True if at least one character in `c` is greater than the next, otherwise False, `pos` is the last index where `c[i] > c[i + 1]` or remains undefined if `flag` is False, `c` is a string input from the user.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is at least 1, if `flag` is True indicating that at least one character in `c` is greater than the next, then `pos` is the last index where `c[i] > c[i + 1]`, and 'YES' is printed along with the output `pos + 1, pos + 2`. If `flag` is False, then `pos` remains undefined, and 'NO' is printed.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300000) and a string `c` consisting of lowercase Latin letters of length `n`. It checks if there is at least one character in `c` that is greater than the next character in the string. If such a character exists, it prints 'YES' and the 1-based positions of the two characters; otherwise, it prints 'NO'. The function does not handle cases where the input string is shorter than `n` or if `n` is less than 2, although it is stated to be at least 2 in the precondition.

