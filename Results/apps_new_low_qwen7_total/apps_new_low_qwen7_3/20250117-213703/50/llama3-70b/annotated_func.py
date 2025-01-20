#State of the program right berfore the function call: k is an integer such that 1 <= k <= 10^12.
def func():
    k = int(input())

n = 1
    while True:
        s = str(n)
        
        if len(s) >= k:
            print(s[k - 1])
            break
        
        k -= len(s)
        
        n += 1
        
    #State of the program after the loop has been executed: k is an integer such that \(1 \leq k \leq 10^{12}\), n is the smallest integer such that \(len(str(n)) \geq k\), and s is the string representation of n.
#Overall this is what the function does:The function reads an integer `k` from the user, where \(1 \leq k \leq 10^{12}\). It then finds the smallest integer `n` such that the length of its string representation (`len(str(n))`) is greater than or equal to `k`. The function prints the `k`-th character (0-indexed) of the string representation of `n` and returns nothing. If `k` exceeds the length of the string representation of `n`, `k` is adjusted by subtracting the length of the current string representation of `n` and continues the search for the next integer `n` until the condition is met.

