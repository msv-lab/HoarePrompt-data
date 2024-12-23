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
        
    #State of the program after the loop has been executed: `h` is an integer input from the user, `n` is 1 (since `n` will eventually become 1 due to the loop condition), `ans` is updated based on the value of `n` at each iteration: if `n` was even, `ans` is updated by adding `n // 2 - 1`; otherwise, `ans` is updated by adding `n // 2`. The final value of `ans` is the sum of these updates.
    print(ans)
#Overall this is what the function does:The function `func` accepts two parameters: `h` and `n`, where `h` is an integer between 1 and 50 inclusive, and `n` is an integer between 1 and \(2^h\) inclusive. It calculates and returns an integer value based on the following process:

