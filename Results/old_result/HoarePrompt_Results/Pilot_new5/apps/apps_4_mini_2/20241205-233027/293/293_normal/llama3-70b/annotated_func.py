#State of the program right berfore the function call: h is a positive integer such that 1 ≤ h ≤ 50, and n is an integer such that 1 ≤ n ≤ 2^h.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `n` is 1, `ans` is the sum computed from the iterations based on the initial value of `n`, `h` is a positive integer such that 1 ≤ `h` ≤ 50.
    print(ans)
#Overall this is what the function does:The function accepts two integers `h` (1 ≤ h ≤ 50) and `n` (1 ≤ n ≤ 2^h). It computes a sum based on the iterative halving of `n`, where it adds different values to `ans` depending on whether `n` is even or odd, and continues this process until `n` equals 1. Finally, it outputs the computed sum `ans`.

