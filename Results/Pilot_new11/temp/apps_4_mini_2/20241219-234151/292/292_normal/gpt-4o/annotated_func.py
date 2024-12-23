#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ b ≤ 10, where a is Limak's weight and b is Bob's weight.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is greater than `b`, `years` is the number of times the loop executed until `a` exceeded `b` (which could be 3 or even 4 if `a` was close to `b` initially),  `b` is greater than or equal to its initial value and still positive.
    print(years)
#Overall this is what the function does:The function accepts two integers, `a` and `b`, representing Limak's weight and Bob's weight, respectively, with a condition that 1 ≤ a ≤ b ≤ 10. It repeatedly increases Limak's weight (`a`) by multiplying it by 3 and Bob's weight (`b`) by multiplying it by 2 until Limak's weight becomes greater than Bob's weight. The function counts the number of years (iterations) it takes for Limak's weight to exceed Bob's weight. At the end of execution, it returns the count of years via a print statement. Notably, initial checks ensure a proper range for `a` and `b`, and the function does not handle cases where inputs are out of range or equal, falling strictly in the range defined. If the inputs do not adhere to the imposed conditions, the function's behavior is undefined. The output is the number of years it took for Limak to outweigh Bob as calculated by the loop.

