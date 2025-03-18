#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, and m, where 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: Output State: `t` must be greater than 0, `i` is equal to `t-1`, `a`, `b`, and `m` are input integers whose values are updated to the last set of integers obtained from the input split by spaces. The loop has executed `t` times, and for each iteration, the values of `a`, `b`, and `m` remain unchanged based on the input provided for that iteration. Depending on the condition `m < a or m < b`, the loop prints either `2` or `m // a + m // b + 2`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it checks if `m` is less than both `a` and `b`. If true, it prints `2`; otherwise, it calculates and prints `m // a + m // b + 2`. After processing all test cases, the function does not return any value but outputs the results for each test case.

