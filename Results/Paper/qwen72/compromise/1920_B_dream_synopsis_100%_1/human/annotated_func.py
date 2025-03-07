#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, and x are integers where 1 ≤ n ≤ 2 · 10^5, 1 ≤ x, k ≤ n, representing the number of elements in the array, the maximum number of elements Alice can remove, and the maximum number of elements Bob can multiply by -1, respectively. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 1000, representing the elements of the array. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations of the loop, `t` is an integer where 1 ≤ t ≤ 10^4, `n` is the first integer read from the input, `k` is the second integer read from the input and must be at least 0, `x` is the third integer read from the input, `a` is a list of integers read from the input and now sorted in descending order, `sum1` is the sum of the elements in the list `a`, `i` is equal to `k + 1`, `ans` is a list containing the final values of `sums` after each iteration of the loop, and `t` iterations have been completed.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the number of elements in an array `n`, the maximum number of elements Alice can remove `k`, and the maximum number of elements Bob can multiply by -1 `x`. It reads these inputs from the standard input. For each test case, it calculates the maximum possible sum of the array after applying the allowed operations by Alice and Bob. The function prints the optimal result for each test case. After processing all test cases, the function has no return value, but the state includes the completion of `t` iterations, with `a` sorted in descending order, and `ans` containing the results of the calculations for each iteration.

