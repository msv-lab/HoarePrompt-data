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
        
    #State of the program after the  for loop has been executed: `n` is at least 1, `flag` is True if at least one character in `c` is greater than the next; otherwise, `flag` is False, `pos` is the index of the last occurrence of `c[i] > c[i + 1]` if `flag` is True, otherwise `pos` is undefined.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is at least 1. If `flag` is True, indicating that there is at least one character in `c` greater than the next, `pos` is the index of the last occurrence of `c[i] > c[i + 1]`, and the program prints 'YES' along with the values (pos + 1) and (pos + 2). If `flag` is False, meaning there are no characters in `c` that are greater than the next one, `pos` is undefined, and 'NO' is printed.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300000) and a string `c` of length `n` consisting of lowercase Latin letters. It checks if there is at least one character in `c` that is greater than the next character in the string. If such a character exists, it prints 'YES' along with the 1-based indices of the last occurrence of this condition (pos + 1 and pos + 2). If no such characters exist, it prints 'NO'. The function does not return any value but outputs the result directly.

