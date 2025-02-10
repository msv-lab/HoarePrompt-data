#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, a and b are integers such that 1 ≤ a, b ≤ 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    t = int(input())
    for _rep in range(t):
        n, k = list(map(int, input().split()))
        
        if n > k:
            print('Bob')
        elif n < k:
            print('Alice')
        else:
            print('Bob')
        
    #State: _rep is t-1, t is the initial value of t, and for each iteration, n and k were integers provided by user input. The loop has completed all its iterations, and the final value of _rep is one less than the initial value of t. No changes were made to the variables n and k within the loop, but their values were used to determine the output for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` (1 ≤ t ≤ 1000) indicating the number of test cases. For each test case, it reads two integers `n` and `k` (1 ≤ n, k ≤ 10^9). It then compares `n` and `k` and prints 'Bob' if `n` is greater than or equal to `k`, and 'Alice' if `n` is less than `k`. After processing all test cases, the function completes without returning any value. The state of the program after the function concludes includes the completion of all test cases, with no modifications to the input variables `n` and `k` beyond their use in the comparison.

