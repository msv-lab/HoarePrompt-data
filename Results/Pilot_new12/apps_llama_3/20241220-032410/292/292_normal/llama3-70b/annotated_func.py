#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, representing Limak's and Bob's initial weights respectively.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is `3^years` times the original value of `a`, `b` is `2^years` times the original value of `b`, `years` is the number of iterations until `a` exceeds `b`, unless `a` is initially greater than `b`, in which case `years` is 0 and `a` and `b` retain their original values.
    print(years)
#Overall this is what the function does:The function calculates and prints the number of years it takes for Limak's weight to exceed Bob's weight, assuming Limak's weight triples and Bob's weight doubles every year, given their initial weights as input. The function accepts two integers, a and b, representing Limak's and Bob's initial weights, respectively, and returns the number of years until Limak's weight exceeds Bob's weight. If Limak's weight is initially greater than or equal to Bob's weight, the function prints 0, indicating that no years are needed for Limak's weight to exceed Bob's weight. The function does not explicitly return any value but prints the result, implying that the return value is the number of years, which can be considered as the primary output of the function. The function does not handle cases where the input values are not integers or are outside the specified range (1 ≤ a ≤ b ≤ 10), potentially leading to undefined behavior or incorrect results in such scenarios.

