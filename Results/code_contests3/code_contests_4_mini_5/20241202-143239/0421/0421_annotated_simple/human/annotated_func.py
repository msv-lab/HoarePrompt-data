#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10) representing the size of the array, followed by n space-separated integers ai (1 ≤ ai ≤ 100) representing the elements of the array.
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
        
    #State of the program after the loop has been executed: `n` is an input string representing an integer greater than 0; `flag` is False if any pair of consecutive elements in `nums` has an absolute difference of 2 or more, otherwise `flag` is True; `nums` is empty if all elements were removed; `i` is less than 0 since the loop has finished executing.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 10) representing the size of an array, followed by `n` space-separated integers `ai` (1 ≤ ai ≤ 100). It checks if all consecutive elements in the array have an absolute difference of less than 2. If any such pair is found, the function returns 'NO'; otherwise, it returns 'YES' after removing the maximum element from the array iteratively until it's empty or the condition fails. Note that the function may not handle certain edge cases correctly, such as when `n` is less than 1 or when the input format is incorrect.

