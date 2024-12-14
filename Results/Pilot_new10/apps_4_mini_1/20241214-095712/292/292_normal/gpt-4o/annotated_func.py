#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is at least 27, `b` is at most less than `a`, and `years` is at least 3
    print(years)
#Overall this is what the function does:The function accepts two integers `a` and `b` (both between 1 and 10, with `a` ≤ `b`) and calculates the number of years it takes for `a` (tripled each year) to exceed `b` (doubled each year). It prints the total number of years required for this condition to be met.

