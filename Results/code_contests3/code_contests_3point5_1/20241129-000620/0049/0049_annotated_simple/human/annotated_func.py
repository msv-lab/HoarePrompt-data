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
        
    #State of the program after the  for loop has been executed: `n` is the first integer from the original list of integers, `flag` is True, `n` is greater than or equal to 2, `i` is the last index of the list `c`, the last element of list `c` is greater than the second to last element of list `c`, and `pos` is assigned the value of the last index of the list `c`
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is the first integer from the original list of integers, `flag` is a boolean, `n` is greater than or equal to 2, `i` is the last index of the list `c`, the last element of list `c` is greater than the second to last element of list `c`, and `pos` is assigned the value of the last index of the list `c`. If `flag` is True, then `pos + 1` and `pos + 2` are printed. If `flag` is False, then 'NO' is printed.
#Overall this is what the function does:The function `func` reads a single integer `n` followed by a string `c`. It then iterates through the characters of `c` and checks if any character is greater than the next character. If such a character is found, it sets `flag` to True and records the position of that character. Finally, if `flag` is True, it prints 'YES' along with the positions of the characters, otherwise it prints 'NO'. The function does not accept any parameters and does not have any explicit return value.

