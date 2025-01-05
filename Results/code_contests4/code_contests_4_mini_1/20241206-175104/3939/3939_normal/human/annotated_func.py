#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^7.
def func():
    n = input()
    memo = 0, 3
    MOD = 10 ** 9 + 7
    for i in range(n - 2):
        x, y = memo
        
        value = 2 * y + 3 * x
        
        memo = y, value % MOD
        
    #State of the program after the  for loop has been executed: `memo` is the result after `n - 2` iterations, `MOD` is 1000000007, `n` is an integer greater than or equal to 2.
    if (n > 2) :
        print(memo[1])
    else :
        print(0 if n == 1 else 3)
    #State of the program after the if-else block has been executed: *`memo` is the result after `n - 2` iterations, `MOD` is 1000000007, and `n` is an integer greater than or equal to 2. If `n` is greater than 2, `memo[1]` is printed. If `n` is equal to 2, the printed value is 3.
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` from input, which must be in the range of 1 to 10^7. If `n` is equal to 1, it prints 0. If `n` is equal to 2, it prints 3. For values of `n` greater than 2, it performs a calculation using a loop that executes `n - 2` times and prints the second value of the `memo` tuple after the loop, which is derived from a specific recurrence relation. The function does not return any value; it only prints the results based on the value of `n`.

