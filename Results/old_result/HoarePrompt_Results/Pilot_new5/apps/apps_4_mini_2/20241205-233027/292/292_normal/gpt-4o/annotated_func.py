#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, where a is Limak's weight and b is Bob's weight.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `b` is between its original value and 40 (considering it was capped at 20), and `years` is the total number of iterations the loop executed, which will be at least 1.
    print(years)
#Overall this is what the function does:The function accepts two integers, `a` (Limak's weight) and `b` (Bob's weight), both constrained by 1 ≤ a ≤ b ≤ 10. It calculates the number of years required for Limak's weight to surpass Bob's weight, where Limak's weight triples each year and Bob's weight doubles. The function returns the total number of years it takes for this to happen.

