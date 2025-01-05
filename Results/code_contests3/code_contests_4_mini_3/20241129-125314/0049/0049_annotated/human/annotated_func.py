#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 300,000, and s is a string of length n consisting only of lowercase Latin letters.
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `s` is a string of length `n`, `c` is an input string, `flag` is True if there exists at least one `i` such that `c[i] > c[i + 1]`, otherwise `flag` is False, `pos` is the last index where `c[i] > c[i + 1]` occurred or remains undefined if `flag` is False.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is at least 2, `s` is a string of length `n`, and `c` is an input string. If `flag` is True, indicating that there exists at least one `i` such that `c[i] > c[i + 1]`, then `pos` is the last index where this condition occurred, 'YES' is printed along with the values `pos + 1` and `pos + 2`. If `flag` is False, `pos` remains undefined, and 'NO' is printed.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300,000) and a string `c` of length `n` consisting of lowercase Latin letters. It checks if there exists at least one index `i` such that the character at index `i` is greater than the character at index `i + 1`. If such an index exists, it prints 'YES' followed by the indices `pos + 1` and `pos + 2`, where `pos` is the last index where this condition is met. If no such index exists, it prints 'NO'. The function does not return a value, but prints results based on the conditions checked.

