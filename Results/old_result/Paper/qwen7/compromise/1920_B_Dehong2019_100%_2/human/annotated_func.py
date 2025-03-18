#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n. Additionally, there is a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 1000 for all i. The sum of n across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: After the loop executes all its iterations, `i` will be equal to `k`, `k` must be greater than 0, `ans1` will be the result of applying the loop's operations up to `k` times starting from the initial value of `ans1` minus the sum of `2 * a[i]` for each `i` in the range of `x`, and `ans2` will hold the highest value that `ans1` has taken during any iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three integers \( n \), \( k \), and \( x \), and a list of \( n \) integers \( a_1, a_2, \ldots, a_n \). It then sorts the list in descending order and calculates two values, \( ans1 \) and \( ans2 \). \( ans1 \) is initially set to the sum of the sorted list. It subtracts twice the first \( x \) elements from \( ans1 \). Next, it iterates \( k \) times, each time adjusting \( ans1 \) by adding the current element and subtracting twice the element at position \( i + x \) (if within bounds). \( ans2 \) keeps track of the maximum value of \( ans1 \) during these iterations. Finally, it prints \( ans2 \) for each test case.

