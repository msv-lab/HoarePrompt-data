#State of the program right berfore the function call: t is an integer such that 1 \leq t \leq 1000, and for each test case, a and b are integers such that 1 \le a, b \le 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop has executed t times, and for each iteration, it has read two integers a and b from the input. If the absolute difference between a and b is even, it has printed 'Bob'. If the absolute difference between a and b is odd, it has printed 'Alice'. The values of t, a, and b are unchanged after the loop, but the loop has completed its execution and produced the specified output for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 ≤ t ≤ 1000`. It then reads `t` pairs of integers `a` and `b` (where `1 ≤ a, b ≤ 10^9`) from the input. For each pair, the function checks if the absolute difference between `a` and `b` is even. If it is, the function prints 'Bob'. If the absolute difference is odd, the function prints 'Alice'. After processing all `t` test cases, the function completes its execution without returning any value. The values of `t`, `a`, and `b` are not modified and are not accessible outside the function.

