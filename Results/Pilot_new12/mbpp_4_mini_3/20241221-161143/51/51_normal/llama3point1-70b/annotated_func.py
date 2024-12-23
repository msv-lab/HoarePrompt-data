#State of the program right berfore the function call: numbers is a list of numbers (integers or floats) and the list is not empty.
def func_1(numbers):
    product = 1
    for num in numbers:
        product *= num
        
    #State of the program after the  for loop has been executed: `product` is equal to the product of all numbers in the list `numbers`, `numbers` is a list of numbers that has at least one element, `num` is the last number in the list.
    return product / len(numbers)
    #The program returns the value of product divided by the length of the list 'numbers', where product is the product of all numbers in the list and len(numbers) is the number of elements in 'numbers'.
#Overall this is what the function does:The function accepts a non-empty list of numerical values (integers or floats) and computes the product of all elements in the list. It then returns the result divided by the number of elements in the list. Since the input list is non-empty, the division by the length of the list will not lead to a division by zero error. However, there is no handling for cases where the list contains zeros, which would result in the product being zero. The function finalizes by providing an average product per element, offering insight into the scale of the product relative to the count of elements in the list.

