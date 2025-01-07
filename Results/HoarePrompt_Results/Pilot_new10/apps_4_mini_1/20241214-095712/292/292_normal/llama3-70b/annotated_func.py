#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, representing the weights of Limak and Bob respectively, with Limak's weight being less than or equal to Bob's weight.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `years` is 3, `b` is between 8 and 80, `a` is between 27 and 270.
    print(years)
#Overall this is what the function does:The function accepts two integers `a` and `b`, representing the weights of Limak and Bob, respectively, where 1 ≤ a ≤ b ≤ 10. It calculates the number of years it takes for Limak's weight, which triples each year, to exceed Bob's weight, which doubles each year, and prints this number of years. The function does not return a value but directly prints the result.

