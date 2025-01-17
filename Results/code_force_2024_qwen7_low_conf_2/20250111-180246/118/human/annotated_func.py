#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
def func_1():
    n, k = map(int, input().split())
    l, r = 1, n
    ans = [0] * n
    for i in range(k):
        for j in range(i, n, k):
            if i % 2 == 0:
                ans[j] = l
                l += 1
            else:
                ans[j] = r
                r -= 1
        
    #State of the program after the  for loop has been executed: `i` is `n + k - 1`, `k` is a positive even integer, `n` is a positive integer, `l` is the initial value of `l` plus the number of times `i % 2 == 0` during the loop, `r` is the initial value of `r` minus the number of times `i % 2 != 0` during the loop, and `ans` is a list where if `j = i, i+k, i+2k, ..., n-1-k` (if applicable), `ans[j]` is `l + 1` if `i % 2 == 0`, and `ans[j]` is `r - 1` if `i % 2 != 0`.
    print(*ans)
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers \(n\) and \(k\) where \(2 \leq k \leq n \leq 2 \cdot 10^5\) and \(k\) is even. For each test case, it initializes a list `ans` of length \(n\) with all elements set to 0. It then uses a nested loop to fill the list `ans` based on the values of `i` and `j`. Specifically, for each \(i\) from 0 to \(n-1\) with a step size of \(k\), if \(i\) is even, the corresponding element in `ans` at index \(j\) is set to \(l\), and \(l\) is incremented by 1. If \(i\) is odd, the corresponding element in `ans` at index \(j\) is set to \(r\), and \(r\) is decremented by 1. After processing all test cases, the function prints the contents of `ans`.

The function handles the following edge cases:
1. If \(k = 2\), the loop will iterate over every other index, setting alternate elements in `ans` to `l` and `r`.
2. If \(k = n\), the loop will only run once, setting the first element in `ans` to `l` and the last element to `r`.
3. If \(n = 2 \cdot 10^5\), the function will handle the maximum possible value for \(n\).

However, the function does not handle the case where the input does not meet the specified constraints, such as \(n < 2\) or \(k\) being odd. Additionally, the function does not validate the input within the specified range, which could lead to incorrect behavior if the input is out of bounds.

