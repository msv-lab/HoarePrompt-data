#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, where a is the weight of Limak and b is the weight of Bob.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is `3^years * a_initial`, `b` is `2^years * b_initial`, `years` is the number of iterations before `a` became greater than `b`, and `1 ≤ a_initial ≤ b_initial ≤ 10` still valid.
    print(years)
#Overall this is what the function does:The function accepts no parameters and reads two integers, `a` and `b`, from input, representing the weights of Limak and Bob, respectively, where `1 ≤ a ≤ b ≤ 10`. It then calculates the number of years required for Limak's weight (tripled each year) to exceed Bob's weight (doubled each year) and prints this number of years. The function assumes valid input according to the specified constraints, and does not handle any cases where the input may be invalid.

