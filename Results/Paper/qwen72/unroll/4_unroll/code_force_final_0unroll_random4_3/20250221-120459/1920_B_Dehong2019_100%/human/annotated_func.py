#State of the program right berfore the function call: The function should take three parameters: a list of integers `a` representing the array, and two integers `k` and `x` representing the limits on the number of elements Alice can remove and Bob can multiply by -1, respectively. The list `a` should contain at least 1 and at most 2 * 10^5 elements, each element `a_i` should be a positive integer (1 ≤ a_i ≤ 1000), and `k` and `x` should be non-negative integers such that 1 ≤ k, x ≤ len(a). Additionally, the function should handle multiple test cases, where the number of test cases `t` is a positive integer (1 ≤ t ≤ 10^4) and the sum of the lengths of the arrays across all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop iterates `t` times, each time processing a new test case. For each test case, the array `a` is sorted in descending order, and two sums `ans1` and `ans2` are calculated. `ans1` is initially the sum of the array, then adjusted by subtracting twice the value of the first `x` elements. `ans2` is then updated by adding the first `k` elements and subtracting twice the value of the elements from position `i + x` (if they exist). The maximum value between `ans1` and `ans2` is printed for each test case. After all iterations, the variables `t`, `n`, `k`, `x`, and `a` are reset for the next test case, and the final output is the sequence of maximum values printed for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by a list of integers `a` and two integers `k` and `x`. For each test case, it calculates the maximum possible sum of the array after performing two operations: removing the largest `k` elements and multiplying the largest `x` elements by -1. The function prints the maximum sum for each test case and does not return any value. After processing all test cases, the function concludes, and the final output is the sequence of maximum sums printed for each test case.

