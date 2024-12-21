#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= b <= 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is less than or equal to 6 \* 3 \* 3 \* ... (times `years`), `b` is less than or equal to 16, 32, 48, 64, or 80 (depending on the value of `years`), and `years` is the number of iterations the loop executed.
    print(years)
#Overall this is what the function does:The function accepts two parameters `a` and `b`, both positive integers such that \(1 \leq a \leq b \leq 10\). It then enters a loop where `a` is tripled and `b` is doubled in each iteration until `a` exceeds `b`. The function counts the number of iterations performed and prints the result. After the function concludes, `a` is greater than `b`, `years` contains the number of iterations performed, and `b` is at most 80 (since the maximum value for `b` starts at 10 and doubles up to five times).

