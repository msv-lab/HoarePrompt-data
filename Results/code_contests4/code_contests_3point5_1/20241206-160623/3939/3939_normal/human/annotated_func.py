#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^7.**
def func():
    n = input()
    memo = 0, 3
    MOD = 10 ** 9 + 7
    for i in range(n - 2):
        x, y = memo
        
        value = 2 * y + 3 * x
        
        memo = y, value % MOD
        
    #State of the program after the  for loop has been executed: Output State: `n` is an integer such that 3 <= n <= 10^7, `memo` is 0, `i` is equal to n - 2, `x` is 0, `y` is 0, `memo` is assigned the value of `y`, value % MOD is calculated, `x` is 0, `y` is 0, `value` is assigned the value of 2 * y + 3 * x, `memo` is 0, value % MOD is calculated, `x` is 0, `y` is 0, value is assigned the value of 2 * y + 3 * x, `memo` is assigned the value of `y`, value % MOD.
    if (n > 2) :
        print(memo[1])
    else :
        print(0 if n == 1 else 3)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 3 <= n <= 10^7, `memo` is 0, `i` is equal to n - 2, `x` is 0, `y` is 0, `memo` is assigned the value of `y`, value % MOD is calculated, `x` is 0, `y` is 0, `value` is assigned the value of 2 * y + 3 * x, `memo` is 0, value % MOD is calculated, `x` is 0, `y` is 0, value is assigned the value of 2 * y + 3 * x, `memo` is assigned the value of `y`, value % MOD. If `n` is greater than 2, we print memo[1]. If `n` is not greater than 2, `n` is an integer such that 3 <= n <= 10^7, `memo` is 0, `i` is equal to n - 2, `x` is 0, `y` is 0, `memo` is assigned the value of `y`, value % MOD is calculated, `x` is 0, `y` is 0, `value` is assigned the value of 2 * y + 3 * x, `memo` is 0, value % MOD is calculated, `x` is 0, `y` is 0, value is assigned the value of 2 * y + 3 * x, `memo` is assigned the value of `y`, value % MOD, `n` is an integer such that 3 <= n <= 10^7; 0 if n == 1 else 3
#Overall this is what the function does:The function `func` reads an integer `n` as input within the range 1 <= n <= 10^7. It then iterates through a for loop updating the values of `memo` based on the previous values of `x` and `y`. After the loop, if `n` is greater than 2, it prints the second value in `memo`, otherwise, it prints 0 if `n` is 1 and 3 if `n` is 2.

