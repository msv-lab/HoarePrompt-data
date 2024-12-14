#State of the program right berfore the function call: nums is a list of integers, and the list contains at least two distinct integers.
def func_1(nums):
    unique_nums = sorted(set(nums))
    return unique_nums[1] if len(unique_nums) > 1 else None
    #`The program returns the second element of the list 'unique_nums' if it has more than one element, otherwise returns None`
#Overall this is what the function does:The function `func_1` accepts a list `nums` of integers (with at least two distinct integers) and returns the second element of the sorted unique elements of `nums`. If there is only one unique element or no unique elements, it returns `None`.

