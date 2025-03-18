#State of the program right berfore the function call: h is a positive integer such that 1 ≤ h ≤ 50, and n is a positive integer such that 1 ≤ n ≤ 2^h.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `n` is 1, `ans` is the total accumulation from the original value of `n` through the loop's iterations, which adds either `n // 2 - 1` if `n` was even or `n // 2` if `n` was odd for each iteration before `n` became 1. `h` remains a positive integer such that 1 ≤ `h` ≤ 50.
    print(ans)
#Overall this is what the function does:The function accepts two positive integers `h` and `n`, where `1 ≤ h ≤ 50` and `1 ≤ n ≤ 2^h`. It computes a value `ans` based on the value of `n` while halving `n` until it reaches 1. In each iteration of the loop, it accumulates either `n // 2 - 1` if `n` is even or `n // 2` if `n` is odd into `ans`. The function then prints the final value of `ans`. It inherently assumes that `n` starts from a valid positive integer within the specified range and does not handle cases where input may violate the stated constraints, nor does it account for invalid or negative values for `h` or `n`. Therefore, `h` remains unchanged during execution while `n` will be reduced to 1 after the loop. In summary, the function summarizes a computed result based on the evolution of `n` and outputs that result.

