#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5·10^4. For each test case, n and l are integers such that 1 ≤ n ≤ 2000 and 1 ≤ l ≤ 10^9. Additionally, a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for each message i, where 1 ≤ i ≤ n.
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
        
    #State of the program after the loop has been executed: `t` is an integer such that \( 1 \leq t \leq 5 \times 10^4 \), `n` is an integer such that \( 1 \leq n \leq 2000 \), `a` is a list of `n` sublists, each containing integers, and is sorted based on the second element of each sublist, `ans` is the maximum length of a subarray within `a` such that the cumulative reduction in the sum of elements from the start of the array to the end of the subarray does not exceed `t`, `l` is the left boundary index of the valid subarray, `r` is the right boundary index of the valid subarray, `res` is the sum of elements from `a[l]` to `a[r]` that satisfies the condition `res \leq t`.
    return ans
    #The program returns `ans`, which is the maximum length of a subarray within `a` such that the cumulative reduction in the sum of elements from the start of the array to the end of the subarray does not exceed `t`.
#Overall this is what the function does:The function accepts an integer `t` and a list `a` of `n` sublists, each containing two integers `a_i` and `b_i`. It first sorts the list `a` based on the second element of each sublist. Then, it iterates through the list to find the longest subarray such that the cumulative reduction in the sum of elements from the start of the array to the end of the subarray does not exceed `t`. If the cumulative sum exceeds `t`, it adjusts the subarray boundaries accordingly. Finally, it returns the maximum length of such a subarray. Potential edge cases include scenarios where no subarray meets the condition, resulting in a length of 0.

