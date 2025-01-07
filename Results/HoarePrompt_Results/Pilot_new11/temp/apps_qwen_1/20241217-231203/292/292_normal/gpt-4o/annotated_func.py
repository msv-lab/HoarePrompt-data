#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a ≤ b ≤ 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is a power of 3 up to \(3^4\) (i.e., 27); `b` is a power of 2 up to \(2^4\) (i.e., 16); `years` is the number of iterations the loop executed.
    print(years)
#Overall this is what the function does:The function reads two positive integers `a` and `b` (where \(1 \leq a \leq b \leq 10\)) from the standard input. It then enters a loop where `a` is multiplied by 3 and `b` is multiplied by 2 in each iteration until `a` exceeds `b`. The function counts the number of iterations required for this condition and prints the count. If `a` and `b` are such that `a` becomes greater than `b` immediately without entering the loop, the count will be 0. The final state of the program after the function concludes is that it outputs the number of years (iterations) taken for `a` to become greater than `b`. If `a` is already greater than `b` when the function starts, the output will be 0.

