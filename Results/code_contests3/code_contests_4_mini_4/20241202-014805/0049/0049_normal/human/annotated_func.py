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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 300000, `flag` is True if at least one character in `c` is greater than its next character, otherwise `flag` is False, and `pos` is the last index where `c[i] > c[i + 1]` or undefined if `flag` is False.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 300000. If `flag` is True, indicating that at least one character in `c` is greater than its next character, then `pos` is defined as the last index where `c[i] > c[i + 1]`, and the output is 'YES' along with the values `pos + 1` and `pos + 2`. If `flag` is False, indicating no such character exists, `pos` is undefined and 'NO' is printed.
#Overall this is what the function does:The function reads an integer `n` (where 2 ≤ n ≤ 300000) and a string `c` of length `n` consisting of lowercase Latin letters. It checks if there exists at least one character in `c` that is greater than the following character. If such a character exists, it prints 'YES' and the 1-based positions of the two characters; otherwise, it prints 'NO'. The function does not return any value but outputs results directly.

