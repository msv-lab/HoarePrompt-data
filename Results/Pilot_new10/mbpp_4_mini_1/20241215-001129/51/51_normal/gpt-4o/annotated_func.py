#State of the program right berfore the function call: numbers is a list of numbers (integers or floats) and is non-empty.
def func_1(numbers):
    product = 1
    for num in numbers:
        product *= num
        
    #State of the program after the  for loop has been executed: `product` is the product of all numbers in the list `numbers`, and `numbers` is a non-empty list of numbers.
    result = product / len(numbers)
    return result
    #The program returns the result which is equal to the product of all numbers in the list 'numbers' divided by the length of 'numbers'
#Overall this is what the function does:The function accepts a non-empty list of numbers (either integers or floats) and calculates the product of all the numbers in the list. It then divides this product by the length of the list and returns the resulting value.

