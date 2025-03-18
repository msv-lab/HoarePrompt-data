#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, a and b are integers where 1 ≤ a, b ≤ 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: After the loop has executed all its iterations, `t` is an integer provided by the user input (1 ≤ t ≤ 1000), `a` and `b` are specific integers provided by the user input (1 ≤ a, b ≤ 10^9), and `i` is `t-1`. The loop has printed "Bob" for each pair of `a` and `b` where the absolute difference between them is even, and "Alice" for each pair where the absolute difference is odd.
#Overall this is what the function does:The function reads an integer `t` from user input, representing the number of test cases. For each test case, it reads two integers `a` and `b` from user input, representing the number of coins in Alice's and Bob's wallets, respectively. It then checks if the absolute difference between `a` and `b` is even. If it is, the function prints "Bob"; otherwise, it prints "Alice". After processing all test cases, the function completes without returning any value. The final state of the program is that `t` test cases have been processed, and for each test case, either "Bob" or "Alice" has been printed based on the condition described.

