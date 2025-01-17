#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; each test case consists of two integers n and k such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even.
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
        
    #State of the program after the  for loop has been executed: `i` is `k`, `j` is `n`, `n` is an integer such that \(2 \leq k \leq n \leq 2 \cdot 10^5\) and `k` is an even integer, `l` is `1 + (n // 2)`, `r` is `n - (n // 2)`, and `ans[j]` is either `l` (if `i % 2 == 0`) or `r` (if `i % 2 != 0`) for each `j` in the sequence `i, i+k, i+2k, ..., n-1`
    print(*ans)
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers \(n\) and \(k\). For each test case, the function initializes two pointers \(l\) and \(r\) to 1 and \(n\), respectively. It then iterates over a range defined by \(k\) and updates an array `ans` such that for every index \(j\) in the sequence \(i, i+k, i+2k, \ldots, n-1\), if the iteration index \(i\) is even, `ans[j]` is set to \(l\) and \(l\) is incremented, otherwise `ans[j]` is set to \(r\) and \(r\) is decremented. After processing all test cases, the function prints the contents of the `ans` array. This process ensures that the values in `ans` are alternately assigned based on the parity of the iteration index, starting from the left and right ends of the array. The function handles up to \(10^4\) test cases, and for each test case, it processes integers \(n\) and \(k\) such that \(2 \leq k \leq n \leq 2 \cdot 10^5\) and \(k\) is even.

