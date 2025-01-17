#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 × 10^4. For each test case, n and l are integers such that 1 ≤ n ≤ 2000 and 1 ≤ l ≤ 10^9. Each of the next n lines contains two integers a_i and b_i such that 1 ≤ a_i, b_i ≤ 10^9.
def func_1():
    n, t = (int(i) for i in input().split())
    a = [[int(i) for i in input().split()] for i in range(n)]
    """q = int(input())
  while q:
    l, r = map(int, input().split())
    q -= 1
    """
    a.sort(key=lambda x: x[1])
    ans = 0
    l = r = 0
    res = 0
    while r < n:
        res += a[r][0]
        
        if r > 0:
            res += a[r][1] - a[r - 1][1]
        
        while res > t:
            res -= a[l][0]
            if l < n - 1:
                res -= a[l + 1][1] - a[l][1]
            l += 1
        
        ans = max(ans, r - l + 1)
        
        r += 1
        
    #State of the program after the loop has been executed: `ans` is the maximum value of `r - l + 1` encountered during the loop, `t` is an integer such that \(1 \leq t \leq 5 \times 10^4\), `n` is the same as the initial value, `a` is the same as the initial value, `l` is the last position where `res` was within the constraint, `r` is `n`, and `res` is the final value after all adjustments.
    return ans
    #The program returns `ans`, which is the maximum value of `r - l + 1` encountered during the loop
#Overall this is what the function does:The function processes a series of test cases, where each test case includes an integer `n` and a value `t`. For each test case, it also receives `n` pairs of integers `a_i` and `b_i`. The function sorts these pairs based on the second element `b_i`. It then iterates through the sorted list, maintaining a running sum `res` of the first elements `a_i` and calculating the difference between consecutive `b_i` values. During iteration, it adjusts the indices `l` and `r` to ensure that the running sum `res` does not exceed `t`. The function keeps track of the maximum value of `r - l + 1` encountered during the process and returns this maximum value. Potential edge cases include scenarios where the running sum `res` exceeds `t` early in the iteration, causing the indices `l` and `r` to be adjusted, and the function correctly handles these adjustments to find the maximum valid subarray length.

