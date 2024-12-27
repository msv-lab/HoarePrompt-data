#State of the program right berfore the function call: a and b are integers such that 1 <= a <= b <= 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `years` is the number of iterations required for `a` to exceed `b` given their initial values, with `a` being `3^years * a_init` and `b` being `2^years * b_init` just before the last iteration where `a` exceeds `b`.
    print(years)
#Overall this is what the function does:The function reads two integers `a` and `b` from the user, where initially 1 <= `a` <= `b` <= 10, and calculates the number of years required for `a` to exceed `b` when `a` is multiplied by 3 and `b` is multiplied by 2 in each year. It then prints the number of years. The function does not accept any parameters and does not return a value. The state of the program after execution is that `a` and `b` have been updated to their final values after the loop, but these values are not returned or used further, and the number of years is printed to the console. The function does not handle cases where the user input is not within the specified range or is not an integer, as it assumes the input will always be valid.

