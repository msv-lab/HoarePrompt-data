#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    return abs(a * b) // gcd(a, b)
    #The program returns the integer value of the absolute product of a and b divided by their greatest common divisor (gcd)
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`, and returns the integer value of the absolute product of `a` and `b` divided by their greatest common divisor (gcd).

#State of the program right berfore the function call: numbers is a list of integers, where each integer is a multiplier \( k_i \) for the amount of coins if the corresponding outcome turns out to be winning.
def func_2(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = func_1(result, num)
        
    #State: result is the product of all elements in the `numbers` list.
    return result
    #The program returns the product of all elements in the `numbers` list.
#Overall this is what the function does:The function accepts a list of integers named `numbers` and returns the product of all elements in the list.

