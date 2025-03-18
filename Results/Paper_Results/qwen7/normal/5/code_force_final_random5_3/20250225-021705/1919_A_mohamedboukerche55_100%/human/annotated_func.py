#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: After all iterations of the loop have finished, `t` is a positive integer such that 1 ≤ t ≤ 1000, `i` is equal to t-1, `s` is the last input string provided, `a` is the first integer from the split string `s`, and `b` is the second integer from the split string `s`. The loop has printed 'Bob' for every pair `(a, b)` where `(a + b) % 2 == 0` and 'Alice' otherwise.
#Overall this is what the function does:The function processes `t` test cases, where `t` is a positive integer between 1 and 1000. For each test case, it reads two positive integers `a` and `b` (both between 1 and 10^9), and prints 'Bob' if the sum of `a` and `b` is even, otherwise it prints 'Alice'. After processing all test cases, the function does not return any value.

