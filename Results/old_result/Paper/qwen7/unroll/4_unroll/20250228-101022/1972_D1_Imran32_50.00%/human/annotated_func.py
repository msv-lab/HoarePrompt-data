#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2⋅10^6, `k` is an integer such that 1 ≤ k ≤ 2⋅10^6; `ans` is equal to `n + sum((n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 1))`, `root` is `int(math.sqrt(n)) + 1`.
    print(ans)
    #This is printed: n + sum((n + i) / (i * i) for i in range(2, int(math.sqrt(n)) + 1))
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers \( n \) and \( m \). For each test case, it calculates the value of \( ans \) as \( n + \sum_{i=2}^{\sqrt{n}} \left\lfloor \frac{n + i}{i^2} \right\rfloor \), and prints the final value of \( ans \). The function does not return any value but prints the calculated result for each test case.

