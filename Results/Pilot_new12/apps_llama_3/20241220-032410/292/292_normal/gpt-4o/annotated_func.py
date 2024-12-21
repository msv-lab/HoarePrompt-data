#State of the program right berfore the function call: a and b are integers such that 1 <= a <= b <= 10, representing the weights of Limak and Bob respectively.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is `3^years` times the original value of `a`, `b` is `2^years` times the original value of `b`, and `years` records the number of iterations until `a` exceeded `b`.
    print(years)
#Overall this is what the function does:The function calculates and prints the number of years it takes for Limak's weight to exceed Bob's weight, given their initial weights, which are input by the user. It assumes that Limak's weight triples and Bob's weight doubles every year. The function does not accept any parameters and does not return any value. After execution, the program's state is that the number of years until Limak's weight exceeds Bob's weight is printed to the console, and the original input values of `a` and `b` are modified to their final values after the loop, although these final values are not used or returned by the function. Note that the function does not handle any potential errors that may occur during the input process.

