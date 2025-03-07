#State of the program right berfore the function call: t is an integer such that 1 \leq t \leq 10^4, n, k, and x are integers such that 1 \leq n \leq 2 \cdot 10^5, 1 \leq x, k \leq n, and a_1, a_2, \ldots, a_n are integers such that 1 \leq a_i \leq 1000. The sum of n over all test cases does not exceed 2 \cdot 10^5.
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
            ans = max(ans1, ans2)
        
        print(ans)
        
    #State: The loop iterates t times, and for each iteration, it processes the input values n, k, x, and the list a. The final output for each iteration is the maximum value between ans1 and ans2, where ans1 is modified by subtracting the top x elements of the sorted list a (in descending order) and then adding and subtracting elements based on the values of k and x. The state of t, n, k, x, and a remains unchanged after each iteration, but the values of ans1 and ans2 are recalculated for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases, each defined by integers `n`, `k`, `x`, and a list of integers `a`. For each test case, it calculates the sum of the elements in `a`, modifies this sum by subtracting twice the value of the top `x` elements, and then further modifies the sum by adding and subtracting elements based on the values of `k` and `x`. The function prints the maximum value between the modified sum and the initial modified sum for each test case. The state of `t`, `n`, `k`, `x`, and `a` remains unchanged after each iteration, but the values of the intermediate sums (`ans1` and `ans2`) are recalculated for each test case.

