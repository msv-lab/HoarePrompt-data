#State of the program right berfore the function call: n, a, b, c are non-negative integers such that 1 ≤ n, a, b, c ≤ 10^9.
def func():
    n, a, b, c = map(int, input().split())

k = 4 - n % 4
    if (k == 4) :
        k = 0
    #State of the program after the if block has been executed: *`n`, `a`, `b`, `c` are integers read from input. If `k` equals 4, then `k` is 0. Since there is no else part, the value of `k` remains unchanged (i.e., `k` will be `4 - n % 4`).
    ans = float('inf')
    for i in range(k // 3 + 1):
        j = (k - 3 * i) // 2
        
        if 3 * i + 2 * j <= k:
            ans = min(ans, 3 * i * c + j * b + (k - 3 * i - 2 * j) * a)
        
    #State of the program after the  for loop has been executed: `k` is between 0 and the original value of `k` inclusive; `i` is `k // 3`; `j` is `(k - 3 * (k // 3)) // 2` or `0` depending on the exact value of `k`; `ans` is the minimum value of `3 * i * c + j * b + (k - 3 * i - 2 * j) * a` for all valid `i` and `j` as described in the loop.
    print(ans)
#Overall this is what the function does:The function reads four integers \( n \), \( a \), \( b \), and \( c \) from the input, where \( 1 \leq n, a, b, c \leq 10^9 \). It then calculates the value of \( k \) as \( 4 - n \mod 4 \), ensuring \( k \) is between 0 and 3 inclusive. The function iterates over possible values of \( i \) and \( j \) derived from \( k \), computing the expression \( 3i \cdot c + j \cdot b + (k - 3i - 2j) \cdot a \) and updating the minimum value found in \( ans \). Finally, it prints the minimum value of the expression obtained. This process covers all possible values of \( k \) and ensures that \( 3i + 2j \leq k \).

