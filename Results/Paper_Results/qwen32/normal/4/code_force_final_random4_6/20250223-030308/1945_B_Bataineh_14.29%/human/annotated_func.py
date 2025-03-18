#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18), where a is the frequency of launching for the first installation, b is the frequency of launching for the second installation, and m is the time the firework is visible in the sky. The input begins with an integer t (1 ≤ t ≤ 10^4) indicating the number of test cases.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: The loop has executed `t` times, and for each iteration, the values of `a`, `b`, and `m` were read from the input. If `m` was less than either `a` or `b`, the output was `2`. Otherwise, the output was `m // a + m // b + 2`. The values of `t`, `a`, `b`, and `m` remain unchanged after each iteration except for the loop index `i`, which increments from `0` to `t-1`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints a result based on the conditions: if `m` is less than either `a` or `b`, it prints `2`; otherwise, it prints `m // a + m // b + 2`.

