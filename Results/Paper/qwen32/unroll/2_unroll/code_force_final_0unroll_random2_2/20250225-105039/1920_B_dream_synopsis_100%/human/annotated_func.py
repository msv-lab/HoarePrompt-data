#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, k, and x are integers such that 1 <= n <= 2 * 10^5, 1 <= k <= n, and 1 <= x <= n. The array a contains n integers such that 1 <= a_i <= 1000. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: a list of maximum sums for each test case, where each maximum sum is determined by the operations described in the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, and `x`, and an array `a` of `n` integers. For each test case, it calculates and prints the maximum possible sum after performing specific operations involving the elements of `a` and the values of `k` and `x`.

