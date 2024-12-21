#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, where a is Limak's weight and b is Bob's weight.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `b` is equal to `2^(years) * original_value_of_b`, `a` is equal to `3^(years) * original_value_of_a`, and `years` is the total iterations executed.
    print(years)
#Overall this is what the function does:The function accepts two integers, a and b, which represent the weights of Limak and Bob, respectively, with the constraint that 1 ≤ a ≤ b ≤ 10. It simulates a growth cycle where Limak's weight triples and Bob's weight doubles in each iteration of a loop, continuing until Limak's weight exceeds Bob's weight. The function counts the number of iterations (years) it takes for Limak's weight to surpass Bob's weight. After the function concludes, it outputs the total count of years required for Limak to become heavier than Bob. In cases where Limak starts with the same weight as Bob, the loop will execute at least once. The function does not handle any input validation for weights outside the specified range or non-integer inputs.

