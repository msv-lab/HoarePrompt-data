#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, representing the weights of Limak and Bob respectively, with Limak's weight being less than or equal to Bob's weight.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `years` is the number of iterations it took for `a` to exceed `b`.
    print(years)
#Overall this is what the function does:The function accepts two integers `a` and `b`, representing the weights of Limak and Bob, respectively. It calculates the number of years it takes for Limak's weight (which increases by a factor of 3 each year) to exceed Bob's weight (which increases by a factor of 2 each year). The function prints the number of years required for this condition to be met. The function does not handle any input validation and assumes that the input will always satisfy the constraints 1 ≤ a ≤ b ≤ 10.

