#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, and x are integers where 1 ≤ n ≤ 2·10^5, 1 ≤ k, x ≤ n, representing the number of elements in the array, the maximum number of elements Alice can remove, and the maximum number of elements Bob can multiply by -1, respectively. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 1000, representing the elements of the array. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: After the loop executes all the iterations, `t` is an integer where 1 ≤ t ≤ 10^4, `_` is `t - 1`, `n` is an input integer, `k` is an input integer, `x` is an input integer, `a` is a reversed sorted list of integers read from the input, `sum1` is the sum of all elements in the original `a`, `i` is `k + 1`, and `ans` is a list containing `k + 1` elements. Each element in `ans` represents the value of `sums` after each iteration of the inner loop. The first element in `ans` is `sum1 - 2 * sum(a[:x])`, and subsequent elements are updated based on the conditions: if `i + x - 1 < n`, then `sums` is updated to `sums + a[i - 1] - 2 * a[i + x - 1]`; otherwise, if `i + x - 1 >= n`, then `sums` is updated to `sums + a[i - 1]`. The final output is the maximum value in the list `ans`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, and `x`, and an array `a` of integers. For each test case, it calculates the maximum possible sum of the array after allowing Alice to remove up to `k` elements and Bob to multiply up to `x` elements by -1. The function prints the maximum sum for each test case. After processing all test cases, the function completes without returning any value.

