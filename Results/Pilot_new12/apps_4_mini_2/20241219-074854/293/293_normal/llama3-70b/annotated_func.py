#State of the program right berfore the function call: h is an integer between 1 and 50 inclusive, and n is an integer between 1 and 2^h inclusive.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `h` is an integer between 1 and 50 inclusive, `n` is 1, `ans` is the sum of contributions from each iteration derived from the original value of `n` based on its parity during division
    print(ans)
#Overall this is what the function does:The function reads two integers, `h` and `n`, from user input, where `h` is between 1 and 50 inclusive and `n` is between 1 and \(2^h\) inclusive. It processes `n` in a loop, reducing it by half until `n` equals 1, during which it calculates a cumulative sum `ans` based on whether `n` is even or odd at each step. After the loop concludes, the function outputs the final value of `ans`, which represents the total contributions calculated from `n` during the iterations. The function does not return a value but prints `ans` directly. Note that it does not handle the case where `n` is 1, which means it anticipates that `n` will always be greater than 1 upon entering the loop.

