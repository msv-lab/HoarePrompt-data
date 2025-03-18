#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, a and b are integers where 1 ≤ a, b ≤ 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
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
        
    #State: _rep is t-1, t is greater than or equal to 1, a and b remain as integers where 1 ≤ a, b ≤ 10^9, and n and k are updated to the input integers for each iteration. For each iteration, if the current n is greater than the current k, the condition n > k holds true. If the current n is less than or equal to the current k, the condition n ≤ k holds true.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where 1 ≤ t ≤ 1000. For each test case, it reads two integers `n` and `k`, where 1 ≤ n, k ≤ 10^9. It then compares `n` and `k` and prints 'Bob' if `n` is greater than or equal to `k`, and 'Alice' if `n` is less than `k`. After processing all test cases, the function completes, and the state of the program remains unchanged except for the printed output.

