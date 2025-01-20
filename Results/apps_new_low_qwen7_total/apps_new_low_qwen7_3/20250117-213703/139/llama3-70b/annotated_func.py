#State of the program right berfore the function call: n, a, b, c are non-negative integers such that 1 ≤ n, a, b, c ≤ 10^9.
def func():
    n, a, b, c = map(int, input().split())

k = 4 - n % 4
    if (k == 4) :
        k = 0
    #State of the program after the if block has been executed: *`n` is a non-negative integer such that 1 ≤ n ≤ 10^9, `a` is a non-negative integer such that 1 ≤ a ≤ 10^9, `b` is a non-negative integer such that 1 ≤ b ≤ 10^9, `c` is a non-negative integer such that 1 ≤ c ≤ 10^9, `k` equals 4 - n % 4. If `k` equals 4, then `k` is set to 0. Otherwise, `k` remains unchanged.
    ans = float('inf')
    for i in range(k // 3 + 1):
        j = (k - 3 * i) // 2
        
        if 3 * i + 2 * j <= k:
            ans = min(ans, 3 * i * c + j * b + (k - 3 * i - 2 * j) * a)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer such that \(1 \leq n \leq 10^9\), `a` is a non-negative integer such that \(1 \leq a \leq 10^9\), `b` is a non-negative integer such that \(1 \leq b \leq 10^9\), `c` is a non-negative integer such that \(1 \leq c \leq 10^9\), `k = 4 - n \% 4` (with `k` being 0 if `n \% 4` equals 4), `ans` is the minimum value among all expressions `3 * i * c + j * b + (k - 3 * i - 2 * j) * a` where `i` and `j` are integers satisfying `3 * i + 2 * j <= k`, `i` starts from 0 and increases by 1 each iteration until it reaches the maximum possible value such that `3 * i + 2 * j <= k` holds.
    print(ans)
#Overall this is what the function does:The function processes four non-negative integers \(n\), \(a\), \(b\), and \(c\) (where \(1 \leq n, a, b, c \leq 10^9\)) internally. It calculates the remainder \(k\) of \(n\) divided by 4, setting \(k\) to 0 if it equals 4. Then, it iterates over possible values of \(i\) and \(j\) to find the minimum value of the expression \(3i \cdot c + j \cdot b + (k - 3i - 2j) \cdot a\), where \(3i + 2j \leq k\). Finally, it prints the minimum value found. Potential edge cases include when \(n \% 4 = 4\), in which case \(k\) is set to 0. The function does not return any value directly but modifies and uses the internal variables \(n\), \(a\), \(b\), \(c\), and \(k\) to compute and print the result.

