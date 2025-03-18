#State of the program right berfore the function call: The function should accept two integers a and b as inputs, where 1 ≤ a, b ≤ 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
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
        
    #State: The values of `a` and `b` will be the last input values provided during the `t` iterations of the loop. The value of `t` remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads a string `s` from user input, splits the string into two integers `a` and `b`, and prints 'Bob' if the sum of `a` and `b` is even, otherwise it prints 'Alice'. The function does not return any value. After the function concludes, the value of `t` remains unchanged, and `a` and `b` will hold the values from the last test case.

