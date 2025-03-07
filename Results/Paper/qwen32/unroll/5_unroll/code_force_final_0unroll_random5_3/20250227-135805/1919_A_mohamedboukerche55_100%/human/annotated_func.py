#State of the program right berfore the function call: Each test case contains two integers a and b (1 ≤ a, b ≤ 10^9) representing the number of coins in Alice's and Bob's wallets, respectively. The input consists of multiple test cases, with the first line containing a single integer t (1 ≤ t ≤ 1000) indicating the number of test cases.
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
        if (a + b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The output state consists of `t` lines, each indicating either 'Bob' or 'Alice' based on whether the sum of `a` and `b` for each test case is even or odd, respectively. The values of `t`, `a`, and `b` from the initial state are not changed and remain as inputs.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b` representing the number of coins in Alice's and Bob's wallets, respectively. It then prints 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd.

