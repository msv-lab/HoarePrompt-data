#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^7.**
def func():
    n = input()
    memo = 0, 3
    MOD = 10 ** 9 + 7
    for i in range(n - 2):
        x, y = memo
        
        value = 2 * y + 3 * x
        
        memo = y, value % MOD
        
    #State of the program after the  for loop has been executed: `n` is 3, `memo` is a tuple containing 24 and 66, `MOD` is 1000000007, `x` is 6, `y` is 24, `value` is 66
    if (n > 2) :
        print(memo[1])
    else :
        print(0 if n == 1 else 3)
    #State of the program after the if-else block has been executed: *`n` is 3, `memo` is a tuple containing 24 and 66, `MOD` is 1000000007, `x` is 6, `y` is 24, `value` is 66. If `n` is greater than 2, the function prints 66. If `n` is not larger than 2, the function prints 3.
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, then iterates through a loop to calculate a specific value based on the previous values in `memo`. If `n` is greater than 2, it prints the second element of `memo`, otherwise, it prints 0 if `n` is 1 and 3 if `n` is 2. The function does not accept any parameters and does not return any value.

