#State of the program right berfore the function call: nums is a list of integers.
def func_1(nums):
    even = next((num for num in nums if num % 2 == 0), None)

odd = next((num for num in nums if num % 2 != 0), None)
    return even * odd
    #The program returns the product of the first even number and the first odd number in the list `nums`, or `None` if either an even or odd number does not exist.
#Overall this is what the function does:The function `func_1` accepts a list of integers `nums` and returns the product of the first even number and the first odd number found in the list. If either an even or an odd number does not exist in the list, the function returns `None`. If the list is empty, the function also returns `None` since no numbers are present to determine even or odd.

