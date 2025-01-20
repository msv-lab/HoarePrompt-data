#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^8, c_0 and c_1 are integers such that 0 ≤ c_0, c_1 ≤ 10^8.
def func():
    n, c0, c1 = map(int, input().split())

ans = 0

i = 0
    while 1 << i < n:
        ans += (1 << i) * min(c0, c1)
        
        i += 1
        
    #State of the program after the loop has been executed: n is an integer from input and must be greater than 1, c0 is an integer from input, c1 is an integer from input, ans is (2^k - 1) * min(c0, c1) where k is the largest integer such that 2^k < n, i is k.
    if (1 << i > n) :
        ans += (n - (1 << i - 1)) * min(c0, c1)
    #State of the program after the if block has been executed: *`n` is an integer greater than 1, `c0` and `c1` are integers from input, `i` is `k` which is the largest integer such that `2^k < n`. If `1 << i` (which is `2^i`) is greater than `n`, `ans` is `(2^k - 1) * min(c0, c1) + (n - (1 << i - 1)) * min(c0, c1)`. Otherwise, `ans` remains `(2^k - 1) * min(c0, c1)`.
    print(ans)
#Overall this is what the function does:The function `func` reads three integers `n`, `c0`, and `c1` from the input, where `2 ≤ n ≤ 10^8` and `0 ≤ c0, c1 ≤ 10^8`. It calculates the sum of the series `(2^0 + 2^1 + ... + 2^(k-1)) * min(c0, c1)` plus the remaining part `(n - 2^k) * min(c0, c1)` if `2^k < n`, where `k` is the largest integer such that `2^k < n`. The final result, `ans`, is printed to the console. The function does not return any value. The state after the function execution is that `ans` holds the calculated value, and the input values `n`, `c0`, and `c1` remain unchanged. Edge cases include when `n` is a power of 2, in which case the loop will still execute correctly, and the final addition will be zero.

