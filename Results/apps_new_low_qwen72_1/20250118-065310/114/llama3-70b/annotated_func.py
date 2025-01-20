#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9, and k is a non-negative integer such that 0 ≤ k ≤ 8.
def func():
    n, k = map(int, input().split())

x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: `n` is the smallest multiple of \(10^k\) that is greater than or equal to the initial value of `n`, `k` is the integer value read from input, `x` is \(10^k\) where `k` is the integer value read from input.
    print(n)
#Overall this is what the function does:The function reads two integers `n` and `k` from the user input, where `n` is a positive integer (1 ≤ n ≤ 10^9) and `k` is a non-negative integer (0 ≤ k ≤ 8). It then calculates the smallest multiple of \(10^k\) that is greater than or equal to `n`. The function prints this calculated value and does not return any value. After the function executes, `n` is the smallest multiple of \(10^k\) that is greater than or equal to the initial value of `n`, and `k` and `x` retain their values as read from the input and computed, respectively.

