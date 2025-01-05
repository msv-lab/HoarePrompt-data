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
        
    #State of the program after the  for loop has been executed: `n` is greater than 1, `flag` is True if there exists at least one index `i` such that `c[i]` is greater than `c[i + 1]`, otherwise `flag` is False. `pos` is the last index `i` where `c[i]` is greater than `c[i + 1]` if `flag` is True, otherwise `pos` remains undefined.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is greater than 1. If `flag` is True, then `pos` is defined as the last index `i` where `c[i]` is greater than `c[i + 1]`, and 'YES' is printed with the output (pos + 1, pos + 2). Otherwise, if `flag` is False, `pos` remains undefined, and 'NO' is printed.
#Overall this is what the function does:The function accepts an integer `n` (where \(2 \leq n \leq 300000\)) and a string `s` of length `n` consisting of lowercase Latin letters. It checks if there exists any index `i` such that the character at index `i` is greater than the character at index `i + 1`. If such an index exists, it prints 'YES' and the 1-based positions of these characters (pos + 1 and pos + 2). If no such index exists, it prints 'NO'. The function does not return any value; instead, it directly prints the output.

