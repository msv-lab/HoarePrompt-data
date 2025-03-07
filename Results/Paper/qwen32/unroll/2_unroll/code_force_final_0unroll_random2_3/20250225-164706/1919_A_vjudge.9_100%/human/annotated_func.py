#State of the program right berfore the function call: The function takes no arguments but reads from standard input. The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9) representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: After processing all test cases, the program will have printed 'Bob' if the absolute difference between the number of coins Alice and Bob have is even, and 'Alice' if the difference is odd for each test case. The values of `t`, `a`, and `b` will reflect the last test case processed.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers representing the number of coins Alice and Bob have. For each test case, it prints 'Bob' if the absolute difference between the number of coins Alice and Bob have is even, and 'Alice' if the difference is odd.

