#State of the program right berfore the function call: numbers is a list of integers.
def func_1(numbers):
    product = 1
    for num in numbers:
        product *= num
        
    #State of the program after the  for loop has been executed: `product` is the product of all integers in `numbers`, `numbers` is an empty list.
    result = product / len(numbers)
    return result
    #The program returns None since `result` is not defined and no value is explicitly returned or calculated
#Overall this is what the function does:The function accepts a list of integers `numbers` and returns None.

