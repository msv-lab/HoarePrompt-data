#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= b <= 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is 3 raised to the power of `years`, `b` is 2 raised to the power of `years` multiplied by the original value of `b` (which is between 1 and 5), `years` is the number of iterations the loop executed
    print(years)
#Overall this is what the function does:The function accepts two positive integers `a` and `b` such that \(1 \leq a \leq b \leq 10\). It repeatedly multiplies `a` by 3 and `b` by 2, incrementing a counter `years` each time, until `a` exceeds `b`. Finally, it prints the number of iterations `years` performed.

