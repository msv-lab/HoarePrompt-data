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
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 2, `c` is a string input, `flag` is True, `pos` is the index of the last occurrence where `c[i]` is greater than `c[i + 1]`
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is greater than or equal to 2, `c` is a string input, `flag` is True, `pos` is the index of the last occurrence where `c[i]` is greater than `c[i + 1]`. If flag is True, the program prints the values of `pos + 1` and `pos + 2`. If flag is False, the program prints 'NO' and does not affect the initial state variables.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `c` from the user input. It then iterates over the characters of the string and checks if there is a decreasing trend. If such a trend is found, it sets a flag to True and stores the index of the last occurrence of this trend in `pos`. After the loop, if the flag is True, it prints 'YES' along with the indices of the characters causing the trend. If the flag is False, it prints 'NO'. The function does not accept any parameters and does not return any value.

