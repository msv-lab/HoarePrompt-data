#State of the program right berfore the function call: n is a positive integer representing the size of the array, and ai is a list of n positive integers each ranging from 1 to 100.**
def func():
    n = input()
    flag = True
    nums = map(int, raw_input().split())
    while flag and nums:
        for i in xrange(len(nums) - 1):
            if abs(nums[i] - nums[i + 1]) >= 2:
                flag = False
                break
        
        nums.remove(max(nums))
        
    #State of the program after the loop has been executed: `n` is a string representing the size of the array, `ai` is a list of `n` positive integers each ranging from 1 to 100 except for the maximum value which has been removed, `flag` is True if all elements in `nums` are within a difference of 1, and flag is False if there is an absolute difference of 2 or more between any two elements in `nums`, `nums` is an empty list, `i` is updated to `-1`
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` reads an integer `n` as the size of an array and a list of `n` positive integers. It then iterates through the list to check if the absolute difference between any two consecutive elements is less than 2. If this condition holds for all elements, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. However, the annotation mentions the removal of the maximum value from the list, which is missing in the code implementation.

