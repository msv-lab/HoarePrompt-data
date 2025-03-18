#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    return abs(a * b) // gcd(a, b)
    #The program returns the value of `abs(a * b) // gcd(a, b)`
#Overall this is what the function does:The function accepts two integer parameters, `a` and `b`, and returns the value of the absolute product of `a` and `b` divided by their greatest common divisor (GCD).

#State of the program right berfore the function call: numbers is a list of integers, where each integer is a multiplier (2 ≤ numbers[i] ≤ 20) for the amount of coins if the corresponding outcome turns out to be winning.
def func_2(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = func_1(result, num)
        
    #State: `result` is the value returned by `func_1(func_1(...func_1(numbers[0], numbers[1]), numbers[2]), ..., numbers[len(numbers) - 1])`
    return result
    #The program returns the value of `result`, which is the output of the nested function calls `func_1(func_1(...func_1(numbers[0], numbers[1]), numbers[2]), ..., numbers[len(numbers) - 1])`.
#Overall this is what the function does:The function `func_2` accepts a list of integers, each representing a multiplier between 2 and 20. It processes these integers through a series of nested calls to another function `func_1`, and returns the final result of these operations.

