#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 \cdot 10^5, 1 ≤ x, k ≤ n. Additionally, a list of n integers a_1, a_2, \ldots, a_n where 1 ≤ a_i ≤ 1000 represents the elements of the array. The sum of n across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: After the loop executes all iterations, `i` will be `k + 1`, `x` and `n` will remain unchanged, and `ans` will be a list of length `k + 1` containing the sequence of `sums` values calculated during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the values of \( n \), \( k \), and \( x \), along with an array of \( n \) integers. It sorts the array in descending order, calculates a series of sums based on specific conditions involving \( x \) and \( k \), and stores these sums in a list. Finally, it prints the maximum value from this list for each test case.

