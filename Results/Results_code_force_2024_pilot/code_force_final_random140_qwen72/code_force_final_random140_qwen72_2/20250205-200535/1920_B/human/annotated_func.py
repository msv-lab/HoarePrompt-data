#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, and x are integers where 1 ≤ n ≤ 2 × 10^5, 1 ≤ k, x ≤ n, representing the number of elements in the array, the maximum number of elements Alice can remove, and the maximum number of elements Bob can multiply by -1, respectively. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 1000, representing the elements of the array. The sum of n over all test cases does not exceed 2 × 10^5.
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
                sums = sum1 - 2 * sum(a[:x + 1])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: After the loop has executed all iterations, `_` is equal to the initial value of `t` (the number of test cases), `n`, `k`, and `x` retain their values from the last test case, `a` is a sorted list of integers from the last test case in descending order, `sum1` is the sum of all elements in the list `a` from the last test case, `ans` is a list containing `k + 1` elements for each test case, where each element is the result of the calculations performed within the loop. The variable `i` has been incremented through the loop from 0 to `k` for each test case, and `sums` holds the final value after the last iteration of the loop for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, and `x`, and an array `a` of length `n`. It calculates the maximum possible sum of the array after performing two operations: removing up to `k` elements and multiplying up to `x` elements by -1. The function prints the maximum sum for each test case. After processing all test cases, the function leaves the variables `n`, `k`, and `x` with their values from the last test case, `a` as a sorted list in descending order from the last test case, and `sum1` as the sum of the elements in `a` from the last test case. The list `ans` contains the results of the calculations for the last test case, and the loop variable `i` and the sum `sums` hold their final values from the last iteration of the inner loop for the last test case.

