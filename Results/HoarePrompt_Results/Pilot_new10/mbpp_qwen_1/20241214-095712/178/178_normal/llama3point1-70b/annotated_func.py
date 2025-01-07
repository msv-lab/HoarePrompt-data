#State of the program right berfore the function call: numbers is a list of float or integer numbers.
def func_1(numbers):
    rounded_numbers = [round(num) for num in numbers]
    total_sum = sum(rounded_numbers)
    return total_sum * len(numbers)
    #The program returns total_sum multiplied by the length of list 'numbers'
#Overall this is what the function does:The function accepts a list of numbers and returns the sum of the rounded values of the elements in the list, multiplied by the length of the list.

