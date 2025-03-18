#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    return abs(a * b) // gcd(a, b)
    #The program returns the result of `abs(a * b) // gcd(a, b)` where `a` and `b` are integers, and `gcd(a, b)` is the greatest common divisor of `a` and `b`.
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`. It returns the result of the expression `abs(a * b) // gcd(a, b)`, where `gcd(a, b)` is the greatest common divisor of `a` and `b`.

#State of the program right berfore the function call: numbers is a list of integers, where each integer is a multiplier (2 <= numbers[i] <= 20) representing the multiplier for the amount of coins if the corresponding outcome turns out to be winning.
def func_2(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = func_1(result, num)
        
    #State: result is the product of all integers in the list numbers.
    return result
    #The program returns the product of all integers in the list 'numbers'.
#Overall this is what the function does:The function accepts a parameter `numbers`, which is a list of integers where each integer is a multiplier between 2 and 20. It returns the product of all integers in the list `numbers`.

