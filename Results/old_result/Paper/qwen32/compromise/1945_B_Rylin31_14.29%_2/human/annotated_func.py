#State of the program right berfore the function call: Each test case consists of three integers a, b, and m where 1 ≤ a, b, m ≤ 10^18. There are t test cases where 1 ≤ t ≤ 10^4.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: The output state consists of `t` lines, each containing the result of the computation for each test case. The variables `a`, `b`, and `m` are unchanged from their initial values provided in each test case input, and `t` remains the same as the number of test cases.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it computes and prints a result based on these integers. The result is the sum of the integer divisions of `mn` (which is the minimum of `a` and `b` plus `m`) by `a` and `b`, with an additional `1` added to the result if `m` is divisible by both `a` and `b` and neither `a` nor `b` is `1`. The function outputs `t` lines, each corresponding to the result of one test case.

