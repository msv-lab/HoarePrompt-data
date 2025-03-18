#State of the program right berfore the function call: n is an integer between 0 and 2,000,000,000, and k is an integer between 1 and 9.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is the original value of `n` divided by 10 to the power of `w`, `w` is the smallest number such that `n` divided by 10 to the power of `w` is divisible by 10 to the power of `k`, and `k` remains the input integer.
    print(w)
#Overall this is what the function does:The function accepts two integers `n` and `k` as input, where `n` is divided by 10 repeatedly until it is divisible by 10 to the power of `k`, and it prints the number of divisions required to achieve this, handling cases where `n` becomes 0 or `k` exceeds the number of digits in `n`.

