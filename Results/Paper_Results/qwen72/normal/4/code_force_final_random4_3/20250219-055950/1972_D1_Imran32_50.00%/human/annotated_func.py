#State of the program right berfore the function call: The function `func_1` is expected to take two positive integers `n` and `m` as input, where 1 ≤ n, m ≤ 2 × 10^6. The function should handle multiple test cases, with the number of test cases `t` being a positive integer such that 1 ≤ t ≤ 10^4. The sum of all `n` values and the sum of all `m` values across all test cases should not exceed 2 × 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: `n` is at least 1, `i` is `root + 1`, `root` is the integer part of the square root of `n` plus 1, `cnt` is `root * root`, `ans` is increased by the sum of `(n + i) // (i * i)` for all `i` from 2 to `root`.
    print(ans)
    #This is printed: ans (where ans is the sum of \((n + i) // (i * i)\) for all \(i\) from 2 to \(\text{root}\), and \(\text{root}\) is the integer part of the square root of \(n\) plus 1)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `k` from the input, where `1 ≤ n, k ≤ 2 × 10^6`. It calculates a value `ans` by starting with `n` and then adding to it the sum of \((n + i) // (i * i)\) for all integers `i` from 2 to the integer part of the square root of `n` plus 1. The function prints the final value of `ans` and does not return any value.

