#State of the program right berfore the function call: a and b are integers, 1 ≤ a ≤ b ≤ 10, and represent the initial weights of Limak and Bob respectively.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `a` is `3^years * initial_a`, `b` is `2^years * initial_b`, `years` is the number of iterations needed for `a` to exceed `b`, starting from their initial values
    print(years)
#Overall this is what the function does:The function accepts two integer inputs representing initial weights, iteratively triples the first weight and doubles the second until the first exceeds the second, and prints the number of iterations required, handling any integer inputs but not validating or handling non-integer inputs.

