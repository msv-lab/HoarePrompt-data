#State of the program right berfore the function call: numbers is a list of integers or floating-point numbers.
def func_1(numbers):
    product = 1
    for num in numbers:
        product *= num
        
    #State of the program after the  for loop has been executed: `numbers` is a list of integers or floating-point numbers, `product` is the product of all elements in `numbers`, and `num` is the last element in the list if the loop executes at least once. If the loop does not execute, `product` is 1.
    return product / len(numbers)
    #`The program returns product divided by the length of the list 'numbers'`
#Overall this is what the function does:The function accepts a list `numbers` of integers or floating-point numbers and returns the product of all elements in the list divided by the length of the list.

