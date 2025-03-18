#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, a and b are integers where 1 ≤ a, b ≤ 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is an integer input by the user where 1 ≤ t ≤ 1000, `i` is `t`, `a` and `b` are integers input by the user. The loop has completed all `t` iterations, and for each iteration, if the absolute difference between `a` and `b` was even, "Bob" was printed; otherwise, "Alice" was printed.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 ≤ t ≤ 1000. For each test case, it reads two integers `a` and `b` (1 ≤ a, b ≤ 10^9), representing the number of coins in Alice's and Bob's wallets, respectively. The function then checks if the absolute difference between `a` and `b` is even. If it is, it prints "Bob"; otherwise, it prints "Alice". After processing all `t` test cases, the function completes its execution, and the final state is that `t` lines have been printed, each line containing either "Bob" or "Alice" based on the condition evaluated for each test case.

