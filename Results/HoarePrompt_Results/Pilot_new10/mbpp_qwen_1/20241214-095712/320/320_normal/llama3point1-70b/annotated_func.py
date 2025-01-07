#State of the program right berfore the function call: nums is a list of integers with at least two distinct elements.
def func_1(nums):
    unique_nums = list(set(nums))
    if (len(unique_nums) < 2) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `nums` is a list of integers with at least two distinct elements; `unique_nums` is a list of the unique elements from `nums`, maintaining their original order. The length of `unique_nums` is greater than or equal to 2
    return sorted(unique_nums)[1]
    #The program returns the second smallest element from the list 'unique_nums'
#Overall this is what the function does:The function `func_1` accepts a list `nums` of integers with at least two distinct elements. It first removes duplicates and sorts the unique elements. If there are fewer than two unique elements, it returns `None`. Otherwise, it returns the second smallest element from the sorted list of unique elements.

