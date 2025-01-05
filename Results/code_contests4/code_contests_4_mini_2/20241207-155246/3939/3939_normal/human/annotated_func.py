#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^7.
def func():
    n = input()
    memo = 0, 3
    MOD = 10 ** 9 + 7
    for i in range(n - 2):
        x, y = memo
        
        value = 2 * y + 3 * x
        
        memo = y, value % MOD
        
    #State of the program after the  for loop has been executed: `n` is a string that must be converted to an integer greater than or equal to 3, `memo` is the final computed tuple after (n - 2) iterations, `MOD` is 1000000007, `i` is (n - 3), `x` is the second last value from memo, `y` is the last value from memo, `value` is the last computed value.
    if (n > 2) :
        print(memo[1])
    else :
        print(0 if n == 1 else 3)
    #State of the program after the if-else block has been executed: *`n` is a string that must be converted to an integer greater than or equal to 3. If `n` is greater than 2, `memo[1]` is printed. Otherwise, if `n` is greater than 1, the result of the print statement is 3, while `memo` remains the final computed tuple after (n - 2) iterations, `MOD` is 1000000007, `i` is (n - 3), `x` is the second last value from memo, `y` is the last value from memo, and `value` is the last computed value.
#Overall this is what the function does:The function reads a positive integer `n` from input, computes a sequence based on `n` using a memoization technique, and prints the result based on the value of `n`. If `n` is 1, it prints 0; if `n` is 2, it prints 3; for `n` greater than 2, it prints the second element of the final computed tuple `memo` after `n - 2` iterations of the sequence calculation. The function does not accept any parameters and is constrained by the input value being a positive integer.

