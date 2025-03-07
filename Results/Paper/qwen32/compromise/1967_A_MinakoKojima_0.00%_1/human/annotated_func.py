#State of the program right berfore the function call: Each test case contains two integers n (1 ≤ n ≤ 2 · 10^5) and k (0 ≤ k ≤ 10^12), representing the number of distinct types of cards and the number of coins, respectively. Additionally, each test case contains a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^12), where a_i represents the number of cards of type i initially available. The total number of test cases t (1 ≤ t ≤ 100) is given at the start of the input, and the sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: All test cases have been processed, and for each test case, the value of `ans` has been computed and printed. The variable `t` is 0, indicating no more test cases remain to be processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of card types `n`, a number of coins `k`, and a list of integers representing the initial count of each card type. For each test case, it calculates and prints a value based on these inputs, which is either the factorial of `n` if `k` is sufficiently large, or a product of differences between modified card counts otherwise.

