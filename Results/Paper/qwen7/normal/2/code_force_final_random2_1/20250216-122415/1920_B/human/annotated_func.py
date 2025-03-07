#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n. The array a consists of n integers where 1 ≤ a_i ≤ 1000 for all i. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state after the loop executes all the iterations is a list `ans` containing `k + 1` elements. Each element in `ans` represents the maximum value of `sums` after each iteration of the loop. The loop processes the array `a` by sorting it in descending order, calculating a preliminary sum `sum1`, and then iteratively adjusting `sums` based on the conditions provided. The final value in `ans` will be the maximum value of `sums` obtained after `k + 1` iterations.
    #
    #To summarize, the final output state is a list `ans` with `k + 1` elements, where each element is the result of the `sums` calculation after each iteration of the loop, and the last element is the maximum value among these calculations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( n \), \( k \), and \( x \), along with an array \( a \) of \( n \) integers. For each test case, it sorts the array \( a \) in descending order, calculates a series of sums based on specific conditions involving \( x \) and \( k \), and stores these sums in a list \( ans \). Finally, it prints the maximum value from this list \( ans \).

