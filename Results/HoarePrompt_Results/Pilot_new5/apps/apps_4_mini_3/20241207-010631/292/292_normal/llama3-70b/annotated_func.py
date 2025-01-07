#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, representing the weights of Limak and Bob respectively, with Limak's weight being less than or equal to Bob's weight.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `years` is the number of iterations it took for `a` to exceed `b`, where `a` is equal to `orig_a * 3^years` and `b` is equal to `orig_b * 2^years`, with the original value of `a` (orig_a) being less than or equal to `orig_b / 3`.
    print(years)
#Overall this is what the function does:The function accepts two integers `a` and `b`, representing the weights of Limak and Bob, respectively, where 1 ≤ a ≤ b ≤ 10. It calculates and outputs the number of years it takes for Limak's weight (growing threefold each year) to exceed Bob's weight (growing twofold each year). The function does not return any value; it simply prints the number of years.

