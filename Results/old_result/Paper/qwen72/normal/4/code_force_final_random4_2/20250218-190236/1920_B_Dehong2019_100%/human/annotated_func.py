#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, k, and x are integers such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ k, x ≤ n, and a_i are integers such that 1 ≤ a_i ≤ 1000 for each element in the array. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    """
    Created on Fri Sep  6 21:42:15 2024
     
    @author: dehon
    """
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        
        a = sorted(list(map(int, input().split())), reverse=True)
        
        ans1 = sum(a)
        
        for i in range(x):
            ans1 -= a[i] * 2
        
        ans2 = ans1
        
        for i in range(k):
            ans1 += a[i]
            if i + x < n:
                ans1 -= a[i + x] * 2
            ans2 = max(ans1, ans2)
        
        print(ans2)
        
    #State: `t` is an input integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `k` is an input integer that must be greater than or equal to 0, `x` is an input integer, `_` is a placeholder variable, `a` is a sorted list of integers in descending order, `ans1` is the sum of all integers in the list `a` minus 2 times the sum of the first `x` integers in the list `a` plus the sum of the first `k` integers in the list `a` minus 2 times the sum of the integers at indices `x` to `x + k - 1` in the list `a` (if these indices are within bounds), `ans2` is the maximum value of `ans1` observed during all iterations of the loop, and `i` is `k - 1` if `k > 0`, otherwise `i` is 0.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it takes an integer `n`, two integers `k` and `x`, and a list of `n` integers `a`. It then calculates and prints the maximum possible value of a modified sum of the elements in `a`. The modified sum is computed by initially summing all elements in `a`, then subtracting twice the sum of the first `x` elements, and finally adjusting this sum by adding the first `k` elements and subtracting twice the elements from index `x` to `x + k - 1` (if these indices are within bounds). The function does not return any value; it only prints the result for each test case.

