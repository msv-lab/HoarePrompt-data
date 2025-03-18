#State of the program right berfore the function call: The function should take two parameters, a and b, which are integers such that 1 <= a, b <= 10^9. The function should also handle multiple test cases, where the number of test cases, t, is an integer such that 1 <= t <= 1000. However, the provided function definition does not include these parameters, so it should be revised to include them.
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
        
    #State: `a` is the integer value of the first word in the last input string `s`, `b` is the integer value of the second word in the last input string `s`, `t` is an integer such that 1 <= t <= 1000, `i` is `t-1`, `s` is the last input string. If `(a + b) % 2 == 0`, the program prints 'Bob'. If `(a + b) % 2 != 0`, the program prints 'Alice'.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases, where 1 <= t <= 1000. For each test case, it reads a string `s` from the input, splits it into two integers `a` and `b`, and checks if the sum of `a` and `b` is even. If the sum is even, it prints 'Bob'; if the sum is odd, it prints 'Alice'. After processing all test cases, the function concludes without returning any value.

