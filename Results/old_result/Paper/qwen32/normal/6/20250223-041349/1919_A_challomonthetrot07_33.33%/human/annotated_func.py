#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it receives two integers a and b (1 ≤ a, b ≤ 10^9) representing the number of coins in Alice's and Bob's wallets, respectively.
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
        
    #State: The loop has executed `T` times, where `T` is the number of test cases. For each test case, the values of `a` and `b` are read from the input and a winner is determined based on the given conditions. The values of `a` and `b` are not altered after each iteration; they are only used to print the result ('Alice' or 'Bob'). The variable `i` ranges from 0 to `T-1` as the loop iterates through each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b` representing the number of coins in Alice's and Bob's wallets, respectively. It then determines and prints the winner based on specific conditions: if `a` equals `b`, it prints 'Bob'; if `a` is 1, it prints 'Alice'; if `b` is 1, it prints 'Bob'; if `a` is odd, it prints 'Bob'; if `a` is even and `b` is odd, it prints 'Alice'; if `a` is greater than `b`, it prints 'Bob'; otherwise, it prints 'Alice'. The function does not return any value; it only prints the results.

