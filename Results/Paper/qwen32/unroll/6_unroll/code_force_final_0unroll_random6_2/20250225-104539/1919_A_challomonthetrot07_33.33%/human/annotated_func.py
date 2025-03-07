#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, the function receives two integers a and b (1 ≤ a, b ≤ 10^9) representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        
        if a == b:
            print('Bob')
        elif a == 1:
            print('Alice')
        elif b == 1:
            print('Bob')
        elif a % 2 == 1:
            print('Bob')
        elif a % 2 == 0 and b % 2 == 1:
            print('Alice')
        elif a > b:
            print('Bob')
        else:
            print('Alice')
        
    #State: The output state consists of `T` lines, each containing either 'Alice' or 'Bob', determined by the comparisons of the input pairs `a` and `b` for each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b` representing the number of coins Alice and Bob have, respectively. It then prints "Alice" or "Bob" based on specific conditions related to the values of `a` and `b`. The final state of the program is that it outputs `t` lines, each indicating the winner ("Alice" or "Bob") for the corresponding test case.

