#State of the program right berfore the function call: The function should take two positive integers n and m as inputs, where 1 <= n, m <= 2 * 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: `n` remains unchanged; `k` remains unchanged; `ans` is updated to `n` plus the sum of `(n + i) // (i * i)` for all `i` from 2 to `root` inclusive; `root` remains unchanged.
    print(ans)
    #This is printed: ans (where ans is the value of n plus the sum of (n + i) // (i * i) for all i from 2 to root inclusive)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `k` from the user input, where `1 <= n, m <= 2 * 10^6`. It calculates a new value `ans` by starting with `n` and adding the sum of `(n + i) // (i * i)` for all integers `i` from 2 to the square root of `n` (inclusive). The function then prints the final value of `ans`. The input variables `n` and `k` remain unchanged. The function does not return any value.

