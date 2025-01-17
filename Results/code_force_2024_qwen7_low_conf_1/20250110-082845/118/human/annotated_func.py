#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; each test case consists of two integers n and k (2 ≤ k ≤ n ≤ 2⋅10^5, k is even), and n - k + 1 is the number of continuous segments of length k in the permutation.
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
        
    #State of the program after the  for loop has been executed: `i` is `n`, `l` is `1 + floor((n-1)/2)` if `k` is even, or `1 + floor(n/2)` if `n` is odd, `r` is `n` if `k` is even, or `n - 1` if `n` is odd, and `ans[j]` is `l` if `i` was even, otherwise `ans[j]` is `r` for all `j` in the range `[n, n-1, k]`.
    print(*ans)
#Overall this is what the function does:Functionality: The function processes a permutation of integers from 1 to n and fills an array `ans` with alternating values based on the indices determined by `k`. Specifically, it alternates between incrementing and decrementing values starting from 1 and n respectively. After executing the nested loops, the array `ans` is printed. If `k` is even, `l` starts at 1 and `r` starts at `n`, and if `k` is odd, `l` starts at 1 and `r` starts at `n-1`. The function ensures that the values in `ans` are filled such that for every `j` in the range `[0, n-k+1, k]`, `ans[j]` is either `l` or `r` depending on whether the index `i` is even or odd. There are no explicit checks for edge cases within the provided code, but the loop and conditional statements handle the alternating logic correctly for the given constraints.

