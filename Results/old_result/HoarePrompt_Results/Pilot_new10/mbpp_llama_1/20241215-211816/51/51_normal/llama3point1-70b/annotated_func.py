#State of the program right berfore the function call: numbers is a list of numbers (either integers or floats), and the list is not empty.
def func_1(numbers):
    product = 1
    for num in numbers:
        product *= num
        
    #State of the program after the  for loop has been executed: `numbers` is a list of numbers, `product` is the product of all numbers in the `numbers` list, `num` is the last number in the `numbers` list.
    return product / len(numbers)
    #The program returns the average of all numbers in the list, which is calculated as the product of all numbers divided by the total count of numbers
#Overall this is what the function does:The function accepts a non-empty list of numbers, calculates the product of all numbers in the list, and returns the result divided by the count of numbers, which is not equivalent to the average of the numbers in the list

