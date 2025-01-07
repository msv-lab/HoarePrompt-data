#State of the program right berfore the function call: h is an integer such that 1 ≤ h ≤ 50, and n is an integer such that 1 ≤ n ≤ 2^h.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `h` is equal to input_h, `n` is 1, `ans` is the sum of (n // 2) for every `n` value encountered during the loop where `n` is even, and (n // 2) for odd `n` values before it became 1. If the original `n` was 1, then `ans` remains 0 since the loop does not execute.
    print(ans)
#Overall this is what the function does:The function accepts two integers `h` and `n` from input, processes them in a loop to calculate a sum `ans` based on the values of `n` as it is halved. Specifically, for every even `n`, it adds `n // 2 - 1` to `ans`, and for odd `n`, it adds `n // 2`. The process continues until `n` becomes 1, at which point the loop exits and `ans` is printed. If `n` begins as 1, the loop does not execute, leaving `ans` at 0. The function does not return any values, only printing the final result.

