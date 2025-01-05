#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^4.
def func():
    x = int(input())
    i = 0
    k = 1
    c = 0
    while x - (i + k) >= 0:
        i = i + k
        
        x = x - i
        
        c = c + 1
        
        k = k + 1
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10^4, `i` is the last value reached before termination, `k` is the value of `k` incremented once after the last successful iteration, `c` is the total count of iterations, and `x` is the remaining value that is less than `i + k`.
    print(c)
#Overall this is what the function does:The function accepts no parameters and prompts the user to input an integer `x` (where 1 ≤ x ≤ 10^4). It then calculates how many times it can successively subtract increasing integers (1, 2, 3, ...) from `x` until `x` becomes less than the next integer to subtract. The final count of successful subtractions is printed.

