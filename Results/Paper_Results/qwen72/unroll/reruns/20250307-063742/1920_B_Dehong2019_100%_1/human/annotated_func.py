#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, and x are integers where 1 ≤ n ≤ 2 · 10^5, 1 ≤ k, x ≤ n, representing the number of elements in the array, the limit on the number of elements Alice can remove, and the limit on the number of elements Bob can multiply by -1, respectively. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 1000, representing the elements of the array. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: For each test case, the output state is the maximum possible sum of the array after Alice removes up to k elements and Bob multiplies up to x elements by -1. The variables t, n, k, x, and the array a remain unchanged, but the computed value ans2 for each test case is printed.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the number of elements `n`, the limit on removals `k`, the limit on negations `x`, and an array `a` of integers. For each test case, it computes and prints the maximum possible sum of the array after simulating the removal of up to `k` elements and the negation of up to `x` elements. The function does not return any value; it only prints the result for each test case. The input variables `t`, `n`, `k`, `x`, and the array `a` are read from standard input and remain unchanged after the function concludes.

