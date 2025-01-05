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
        
    #State of the program after the  for loop has been executed: `n` is an integer, `c` is an input string, `flag` is True if there is any character in `c` that is greater than the following character, otherwise `flag` is False, and `pos` is the index of the last such occurrence if `flag` is True, otherwise `pos` is undefined.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer and `c` is an input string. If `flag` is True, 'YES' is printed along with `pos + 1` and `pos + 2`, indicating that there is at least one character in `c` that is greater than the following character. If `flag` is False, 'NO' is printed, and `pos` is undefined, indicating that there are no such characters in `c`.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300000) and a string `c` of length `n` consisting only of lowercase Latin letters. It checks for any occurrence in the string where a character is greater than the next character. If such an occurrence exists, it prints 'YES' and the 1-based indices of the two characters involved; otherwise, it prints 'NO'. If there are no characters greater than the following character, it indicates that the string is sorted in non-decreasing order. The function does not return a value but directly outputs the result.

