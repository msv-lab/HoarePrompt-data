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
        
    #State: The values of `a` and `b` will be the last pair of integers read from the input during the `t` iterations. The loop will print 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each of the `t` test cases, it reads a string `s` from the input, splits the string into two integers `a` and `b`, and checks if the sum of `a` and `b` is even or odd. If the sum is even, it prints 'Bob'; if the sum is odd, it prints 'Alice'. The function does not return any value. After the function concludes, the values of `a` and `b` will be the last pair of integers read from the input during the `t` iterations.

