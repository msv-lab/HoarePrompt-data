#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of type i initially.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        m = min(a)
        
        ans = 0
        
        if k >= n * m:
            ans = math.factorial(n)
        else:
            k -= n * m
            for i in range(n):
                a[i] = m + min(k, m + k // n - a[i])
                k -= min(k, m + k // n - a[i])
            ans = a[0]
            for i in range(1, n):
                ans *= a[i] - a[i - 1]
        
        print(ans)
        
    #State: t is an integer such that 1 ≤ t ≤ 100, `n` is the last positive integer input split from the input string, `k` is the second integer input split from the input string, `a` is a list of integers obtained by splitting the input string and converting each element to an integer, `m` is the minimum value in list `a`, `ans` is either `math.factorial(n)` if `k >= n * m`, or the product of the differences between consecutive elements in the list `a` from index 1 to `n-1`, and `i` is equal to `n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n` and `k`, and a list `a` of `n` integers. It calculates and prints a value based on the following conditions:
- If `k` is greater than or equal to `n * m` (where `m` is the minimum value in `a`), it returns the factorial of `n`.
- Otherwise, it adjusts the values in `a` to satisfy certain constraints and then computes the product of the differences between consecutive elements in the modified list `a`.

