#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
def func():
    n = int(input())
    if (n == 2) :
        print('NO')
    else :
        print('YES')
        k = 2
        print(k)
        print('1', n // 2)
        print('1', n)
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 2 <= `n` <= 10^9. If `n` is equal to 2, the output is 'NO'. If `n` is greater than 2, the output is '1' followed by the value of `n`, and `k` is set to 2.
#Overall this is what the function does:The function reads an integer `n` from user input. If `n` is equal to 2, it prints 'NO'. If `n` is greater than 2, it prints 'YES', followed by the integer 2, the integer resulting from `n // 2`, and the integer `n`. The function does not return any value.

