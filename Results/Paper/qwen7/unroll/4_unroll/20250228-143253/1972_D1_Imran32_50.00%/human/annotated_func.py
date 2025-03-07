#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `k` is an input integer, `ans` is equal to `n + sum((n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 1))`, `root` is `int(math.sqrt(n)) + 1`.
    #
    #This output state describes the final value of `ans` after the loop has executed all its iterations. The variable `ans` is updated in each iteration of the loop by adding `(n + i) // (i * i)` to its current value, where `i` ranges from 2 to `root` (inclusive), and `root` is defined as `int(math.sqrt(n)) + 1`.
    print(ans)
    #This is printed: n + sum((n + i) // (i * i) for i in range(2, int(math.sqrt(n)) + 1))
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( m \). For each valid test case, it calculates the value of \( ans \) as \( n + \sum_{i=2}^{\text{int}(\sqrt{n})+1} \left\lfloor \frac{n + i}{i^2} \right\rfloor \), where \( \left\lfloor x \right\rfloor \) denotes the floor function (rounding down to the nearest integer). After processing all test cases, it prints the final value of \( ans \) for the last test case. If any test case fails to meet the conditions (i.e., \( n \) and \( m \) are not within the specified range or their sums exceed the limit), the function still processes the valid part and prints the result accordingly.

