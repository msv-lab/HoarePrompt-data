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
    #State of the program after the if-else block has been executed: *`n` is an integer input within the range [2, \(10^9\)]. If `n` equals 2, the function does not change the value of `n`. Otherwise, the function prints '1' followed by `n` and `n` is set to 2.
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` from the user. It then checks if `n` is equal to 2. If `n` is 2, it prints 'NO'. Otherwise, it prints 'YES', sets `k` to 2, and prints `k`, followed by '1' and `n`, and finally sets `n` to 2. The function does not return anything but modifies the value of `n` to 2 if `n` was not 2 initially.

