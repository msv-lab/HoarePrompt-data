#State of the program right berfore the function call: The function should take two integers a and b as input, where 1 <= a, b <= 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
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
        
    #State: The values of `a` and `b` will be the last input values provided in the loop, and the loop will have printed 'Bob' if the sum of the last `a` and `b` was even, or 'Alice' if the sum was odd. The value of `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input, representing the number of coins in Alice's and Bob's wallets, respectively. It then checks if the sum of `a` and `b` is even or odd and prints 'Bob' if the sum is even, or 'Alice' if the sum is odd. The function does not return any values. After the function concludes, the values of `a` and `b` will be the last input values provided in the loop, and `t` will remain unchanged.

