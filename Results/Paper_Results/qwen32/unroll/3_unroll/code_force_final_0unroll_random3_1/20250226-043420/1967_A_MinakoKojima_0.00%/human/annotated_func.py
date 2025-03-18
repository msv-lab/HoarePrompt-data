#State of the program right berfore the function call: Each test case consists of two integers n and k, where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12. Additionally, there is a list of n integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^12, representing the number of cards of type i initially available. The number of test cases t satisfies 1 ≤ t ≤ 100, and the sum of n across all test cases does not exceed 5 · 10^5.
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
        
    #State: 6 24
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` (number of card types), an integer `k` (target value), and a list of `n` integers `a_1, a_2, ..., a_n` (number of cards of each type). For each test case, it calculates and prints a specific value `ans` based on the given inputs. The value `ans` is derived from either the factorial of `n` or a product of differences between adjusted card counts, depending on the relationship between `k` and the minimum card count across all types.

