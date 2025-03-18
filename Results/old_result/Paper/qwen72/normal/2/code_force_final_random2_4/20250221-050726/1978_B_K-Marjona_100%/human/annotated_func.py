#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, a, and b are integers where 1 ≤ n, a, b ≤ 10^9, representing the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price, respectively.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The loop has executed `t` times, where `t` is the initial number of test cases. For each test case, `n`, `a`, and `b` are input integers, and `k` is the minimum of `n` and `b - a`. If `b` is less than or equal to `a`, the total cost for the buns is `a * n`. If `b` is greater than `a`, the total cost for the buns is `b * k - k * (k - 1) // 2 + (n - k) * a`. The loop variable `_` is now equal to `t - 1`.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers: `n` (number of buns), `a` (usual price of a bun), and `b` (price of the first bun). For each test case, it calculates and prints the total cost for buying `n` buns. If `b` is less than or equal to `a`, the total cost is `a * n`. If `b` is greater than `a`, the total cost is calculated as `b * k - k * (k - 1) // 2 + (n - k) * a`, where `k` is the minimum of `n` and `b - a`. After processing all test cases, the function completes without returning any value.

