#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains three integers a, b, and m such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: The loop has executed `t` times, where `t` is the initial integer input such that 1 <= t <= 10^4. For each iteration, integers `a`, `b`, and `m` are read from input, and based on the conditions involving `a`, `b`, and `m`, the program prints a specific value: 2 if `m` is less than both `a` and `b`; 2 + m // b if `m` is less than `a` and greater than `b`; 2 + m // a if `m` is less than `b` and greater than `a`; or m // a + m // b + 2 otherwise. The variable `i` has been incremented from 0 to `t-1` during these iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each of the `t` test cases, it reads three integers `a`, `b`, and `m`. Based on the values of `a`, `b`, and `m`, it prints a specific value: 2 if `m` is less than both `a` and `b`; 2 plus the integer division of `m` by `b` if `m` is less than `a` and greater than `b`; 2 plus the integer division of `m` by `a` if `m` is less than `b` and greater than `a`; or the sum of the integer divisions of `m` by `a` and `m` by `b` plus 2 otherwise.

