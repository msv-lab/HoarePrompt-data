#State of the program right berfore the function call: n is a positive integer. ai is a list of integers where each integer is between 1 and 100 (inclusive).**
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
        
    #State of the program after the loop has been executed: n` is a positive integer, `ai` is a list of integers between 1 and 100, `flag` is False if there exists an absolute difference between consecutive elements in `nums` that is greater than or equal to 2, `flag` is True otherwise, `nums` is an empty list, `i` is 0
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` takes user input for a positive integer `n` and a list `ai` of integers. It then iterates through the list checking if the absolute difference between consecutive elements is greater than or equal to 2. If such a difference is found, the function sets `flag` to False; otherwise, it remains True. Finally, the function prints 'YES' if `flag` is True, indicating all differences are less than 2, and 'NO' if `flag` is False.

