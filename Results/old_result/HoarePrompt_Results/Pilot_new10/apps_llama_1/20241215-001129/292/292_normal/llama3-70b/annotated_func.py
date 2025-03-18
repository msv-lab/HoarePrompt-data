#State of the program right berfore the function call: a and b are integers such that 1 <= a <= b <= 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `years` is the number of iterations for `a` to exceed `b` with their respective multiplications, `a` is the initial `a` multiplied by \(3^{years}\), `b` is the initial `b` multiplied by \(2^{years}\), unless initially `a` > `b`, in which case `years` is 0, and `a` and `b` retain their initial values.
    print(years)
#Overall this is what the function does:The function accepts two integer parameters, multiplies the first by 3 and the second by 2 in each iteration until the first exceeds the second, and prints the number of iterations required for this condition to be met, working with any integer inputs regardless of their initial values or ranges.

