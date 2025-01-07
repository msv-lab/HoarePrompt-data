#State of the program right berfore the function call: h is an integer such that 1 ≤ h ≤ 50, and n is an integer such that 1 ≤ n ≤ 2^{h}.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `n` is 1, `ans` is the sum of the series formed by the loop operations based on the initial value of `n`.
    print(ans)
#Overall this is what the function does:The function reads two integers `h` and `n` from input where `1 ≤ h ≤ 50` and `1 ≤ n ≤ 2^h`. It calculates a sum `ans` by iterating over the binary representation of `n`, halving `n` each time and adding either `n // 2 - 1` or `n // 2` to `ans` depending on whether `n` is even or odd. The function then prints the final value of `ans`.

