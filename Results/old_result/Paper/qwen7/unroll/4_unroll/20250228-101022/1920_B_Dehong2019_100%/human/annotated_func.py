#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n. The array a consists of n integers where 1 ≤ a_i ≤ 1000 for all 1 ≤ i ≤ n. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: t is now the number of test cases that have been processed, n and k are the last values read from input for the current test case, x is the last value read for the current test case, and a is the last sorted list of integers in descending order for the current test case. ans2 holds the maximum value calculated for the current test case after processing all the iterations of the inner loops.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads positive integers \( t \), \( n \), \( k \), and \( x \), and an array \( a \) of \( n \) integers. It then calculates and prints the maximum value of \( ans2 \) for each test case based on specific conditions involving the elements of \( a \). Specifically, it first calculates \( ans1 \) as the sum of the elements in \( a \), subtracts twice the first \( x \) elements from \( ans1 \), and then iteratively adjusts \( ans1 \) by adding the first \( k \) elements and subtracting twice the corresponding \( x \)-th elements, updating \( ans2 \) to be the maximum of these values.

