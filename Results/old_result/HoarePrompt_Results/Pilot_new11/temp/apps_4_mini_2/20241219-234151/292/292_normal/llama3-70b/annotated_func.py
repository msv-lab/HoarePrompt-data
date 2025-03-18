#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, where a is Limak's initial weight and b is Bob's initial weight.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, specifically `a` is at least `3^years * original a`, `b` is at most `2^years * original b`, `years` is the total number of iterations executed.
    print(years)
#Overall this is what the function does:The function reads two integers, a and b, which represent Limak's and Bob's initial weights, respectively, where 1 ≤ a ≤ b ≤ 10. It then enters a loop, multiplying Limak's weight by 3 and Bob's weight by 2 in each iteration until Limak's weight exceeds Bob's weight. The function counts the number of iterations, `years`, until this condition is met. Finally, it prints the total number of years it took for Limak's weight to exceed Bob's weight. The function's output reflects the number of iterations needed, which should account for the growth rates of both weights. The function does not handle cases where invalid input (e.g., non-integers) is provided or where the initial weights do not conform to the specified constraints.

