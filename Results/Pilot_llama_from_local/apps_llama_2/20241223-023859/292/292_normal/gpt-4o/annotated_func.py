#State of the program right berfore the function call: a and b are integers such that 1 <= a <= b <= 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `years` is the number of iterations until `3^years * a_orig > 2^years * b_orig`, `a` is `3^years * a_orig`, and `b` is `2^years * b_orig`, where `a_orig` and `b_orig` are the original values of `a` and `b`, respectively. If `a_orig > b_orig`, then `years` is 0, and `a` and `b` retain their original values.
    print(years)
#Overall this is what the function does:The function calculates the number of years it takes for the population of a species to surpass the population of another species, given their initial populations and growth rates. It takes two integer inputs from the user, representing the initial populations of the two species, and returns the number of years until the population of the first species exceeds the population of the second species. The function assumes the first species grows at a rate of 3 times its current population per year, and the second species grows at a rate of 2 times its current population per year. The function handles cases where the initial population of the first species is greater than the initial population of the second species, returning 0 years in such cases. The function also handles cases where the initial populations are equal, correctly calculating the number of years until the first species surpasses the second. Note that the function does not handle cases where the user input is not valid (i.e., not integers or out of the specified range), and it does not provide any error handling or input validation.

