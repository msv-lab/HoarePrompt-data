#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is the integer input value such that \(1 \leq t \leq 10^4\); `a`, `b`, and `m` are the integers from the last iteration such that \(1 \leq a, b, m \leq 10^{18}\).
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It then prints `2` if either `m` is less than `a` or `m` is less than `b`. Otherwise, it prints the result of the expression `m // a + m // b + 2`.

