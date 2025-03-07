#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, a and b are integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: t is an input integer such that 1 <= t <= 1000, and for each of the t test cases, a and b are integers such that 1 <= a, b <= 10^9. The loop has printed 'Bob' for test cases where the absolute difference between a and b is even, and 'Alice' for test cases where the absolute difference between a and b is odd.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer between 1 and 1000. For each test case, it reads two integers `a` and `b` (both between 1 and 10^9). It then prints 'Bob' if the absolute difference between `a` and `b` is even, and 'Alice' if the absolute difference is odd. The function does not return any value. After the function concludes, `t` test cases have been processed, and the appropriate result ('Bob' or 'Alice') has been printed for each test case.

