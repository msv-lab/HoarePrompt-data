#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, and x are integers where 1 ≤ n ≤ 2 · 10^5, 1 ≤ k, x ≤ n, representing the number of elements in the array, the maximum number of elements Alice can remove, and the maximum number of elements Bob can multiply by -1, respectively. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 1000, representing the elements of the array. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop executes all the iterations, `t` is an integer where 1 ≤ t ≤ 10^4, `_` is a placeholder, `n`, `k`, and `x` are integers read from the input, `a` is a reversed sorted list of integers read from the input, `sum1` is the sum of the elements in `a`, `ans` is a list containing `k + 1` elements, each element representing the updated value of `sums` at each iteration of the inner loop, `i` is `k + 1`, and `k` is at least 0. The first element in `ans` is `sum1 - 2 * sum(a[:x + 1])`. For each subsequent element in `ans` (from index 1 to `k`), if `i + x - 1 < n`, the element is updated to `sums + a[i - 1] - 2 * a[i + x - 1]`. If `i + x - 1 >= n`, the element is updated to `sums + a[i - 1]`. The maximum value in `ans` is printed for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by three integers `n`, `k`, and `x`, and an array `a` of integers. For each test case, it calculates the maximum possible sum of the array after performing two operations: removing up to `k` elements and multiplying up to `x` elements by -1. The function prints the maximum sum for each test case. After processing all test cases, the function completes without returning any value.

