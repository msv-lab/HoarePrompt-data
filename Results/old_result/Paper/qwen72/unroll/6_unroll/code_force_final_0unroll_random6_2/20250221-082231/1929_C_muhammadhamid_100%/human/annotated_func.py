#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, k, x, and a are integers such that 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: For each test case, the value of `s` is calculated based on the given `k`, `x`, and `a`. The loop iterates `x` times, updating `s` in each iteration. After all iterations, the loop prints 'Yes' if `a` is greater than or equal to `s`, otherwise it prints 'No'. The values of `t`, `k`, `x`, and `a` remain unchanged for each test case, but `s` is reset to 1 for each new test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `k`, `x`, and `a` where `2 <= k <= 30`, `1 <= x <= 100`, and `1 <= a <= 10^9`. For each test case, it calculates a value `s` by iterating `x` times and updating `s` in each iteration. After the iterations, it prints 'Yes' if `a` is greater than or equal to `s`, otherwise it prints 'No'. The values of `t`, `k`, `x`, and `a` remain unchanged for each test case, but `s` is reset to 1 for each new test case.

