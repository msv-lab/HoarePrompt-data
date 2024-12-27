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
        
    #State of the program after the loop has been executed: `n` is 1, `h` remains unchanged, and `ans` is a value accumulated based on the divisions and parities of the original `n` during the loop executions, specifically tailored to how many times `n` was halved and its parity at each halving step.
    print(ans)
#Overall this is what the function does:The function accepts two parameters, `h` and `n`, where `h` is a positive integer between 1 and 50, and `n` is a positive integer between 1 and 2^h. It calculates and returns a value, `ans`, which is accumulated based on the divisions and parities of the original `n` during the loop executions, specifically tailored to how many times `n` was halved and its parity at each halving step. The final state of the program is that `n` is reduced to 1, `h` remains unchanged, and the calculated `ans` value is printed out, providing the result based on the input parameters `h` and `n`. The function handles all potential edge cases, including when `n` is a power of 2 and when `n` is an odd number, as the loop condition and the calculations within it ensure that `n` is progressively halved until it reaches 1, accumulating the `ans` value accordingly.

