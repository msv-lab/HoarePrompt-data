#State of the program right berfore the function call: **
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `c` is the input string from `raw_input()`, `flag` is True if there exists at least one pair of characters such that the character at index `i` is greater than the character at index `i + 1`, `pos` is the index of the last occurrence of such a pair in the string `c`. If no such pair exists, `flag` remains False
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is at least 2, `c` is the input string from `raw_input()`, `flag` is True if there exists at least one pair of characters such that the character at index `i` is greater than the character at index `i + 1`, `pos` is the index of the last occurrence of such a pair in the string `c`. If no such pair exists, `flag` remains False. If `flag` is True, the function prints(pos + 1, pos + 2). If `flag` is False, there is no pair of characters in the string where the character at index `i` is greater than the character at index `i + 1.
#Overall this is what the function does:The function `func` reads input from the user, processes the input string `c` to check if there exists at least one pair of characters where the character at index `i` is greater than the character at index `i + 1`. If such a pair exists, it prints 'YES' along with the indices of the last occurrence of this pair in the string `c`. If no such pair is found, it prints 'NO'. The function does not accept any parameters and does not return any value.

