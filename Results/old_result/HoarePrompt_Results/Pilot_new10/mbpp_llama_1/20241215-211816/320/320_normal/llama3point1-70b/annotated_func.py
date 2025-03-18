#State of the program right berfore the function call: nums is a list of integers with at least two distinct elements.
def func_1(nums):
    unique_nums = list(set(nums))
    if (len(unique_nums) < 2) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `nums` is a list of integers with at least two distinct elements, `unique_nums` is a list of unique integers from `nums`, with length less than or equal to the length of `nums`, and the length of `unique_nums` is more than or equal to 2
    return sorted(unique_nums)[1]
    #The program returns the second smallest unique integer from the list `nums`.
#Overall this is what the function does:The function accepts a list of integers and returns None if the list has less than two distinct elements, or the second smallest unique integer from the list otherwise

