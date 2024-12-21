#State of the program right berfore the function call: The input consists of two integers h and n, where 1 ≤ h ≤ 50 and 1 ≤ n ≤ 2^h.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `h` is an integer between 1 and 50 (inclusive), `n` is 1, and `ans` is the sum of the increments calculated based on the original value of `n`, which is the sum of the integer divisions of the original `n` by powers of 2, minus the number of times the original `n` is even in the iterations.
    print(ans)
#Overall this is what the function does:Functionality: The function accepts two integers `h` and `n` as input from the user, where `h` is an integer between 1 and 50 (inclusive) and `n` is an integer between 1 and 2^h (inclusive). The function calculates and prints the sum of increments based on the original value of `n`, which is the sum of the integer divisions of the original `n` by powers of 2, minus the number of times the original `n` is even in the iterations. The final state of the program after execution is that it has printed the calculated sum, with `n` being 1 at the end of the loop, and the original value of `h` remaining unchanged throughout the function's execution. The function handles all potential edge cases, including when `n` is a power of 2 and when `n` is an odd number, correctly calculating and printing the sum.

