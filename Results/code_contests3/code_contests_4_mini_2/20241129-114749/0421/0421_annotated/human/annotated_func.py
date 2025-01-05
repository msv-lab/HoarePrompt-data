#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10) representing the size of the array, followed by n space-separated integers ai (1 ≤ ai ≤ 100) which are the elements of the array.
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
        
    #State of the program after the loop has been executed: `n` is a valid string that converts into a non-empty list of integers, `flag` is False if there was any pair of consecutive integers in `nums` with an absolute difference of 2 or more, otherwise `flag` is True; `nums` is an empty list as all elements have been removed through the iterations of the loop.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 10) followed by `n` space-separated integers (1 ≤ ai ≤ 100) representing elements of an array. It checks if every pair of consecutive integers in the array has an absolute difference of less than 2. If any such pair is found, it sets a flag to False. The function continues removing the maximum element from the list until it is empty. Finally, it prints 'YES' if the flag remains True (indicating all pairs met the condition) or 'NO' if at least one pair did not meet the condition. Note: The removal of elements and the check for the flag is done in a way that could lead to unexpected behavior if `nums` is empty or if there are other edge cases in the input handling.

