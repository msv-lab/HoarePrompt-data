#State of the program right berfore the function call: numbers is a list of numbers (integers or floats) and is not empty.
def func_1(numbers):
    product = 1
    for num in numbers:
        product *= num
        
    #State of the program after the  for loop has been executed: `product` is equal to the product of all numbers in the list `numbers`, `numbers` is a list of numbers that is not empty.
    result = product / len(numbers)
    return result
    #The program returns the result which is equal to the product of all numbers in the list 'numbers' divided by the length of 'numbers', where 'numbers' is a non-empty list.
#Overall this is what the function does:The function accepts a non-empty list of numbers (either integers or floats) and returns the product of all the numbers in the list divided by the length of the list. If any number in the list is zero, the product will be zero, and the result will consequently be zero regardless of the length. The function does not handle cases where the list might contain non-numeric types, which could lead to a TypeError during multiplication.

