#State of the program right berfore the function call: The function should take two parameters, a and b, which are integers such that 1 <= a, b <= 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
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
        
    #State: The values of `a` and `b` will be the last pair of integers read from the input during the final iteration of the loop. The value of `t` remains unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` from the input, representing the number of test cases. For each test case, it reads a pair of integers `a` and `b` from the input, representing the number of coins in Alice's and Bob's wallets, respectively. It then prints 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd. After processing all test cases, the values of `a` and `b` will be the last pair of integers read during the final iteration of the loop, and the value of `t` remains unchanged. The function does not return any value.

