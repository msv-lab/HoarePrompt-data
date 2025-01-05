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
        
    #State of the program after the loop has been executed: `n` is a non-empty string representing a valid number, `flag` is False if any absolute difference between consecutive elements in `nums` is at least 2, otherwise `flag` is True; `nums` is an empty array after all maximum values have been removed, `i` is equal to -1 since the loop has completed.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` followed by `n` space-separated integers from input. It checks if the absolute difference between any two consecutive elements in the list is less than 2. If it finds such a difference, it continues removing the maximum element from the list until it is empty or finds an invalid difference. The function prints 'YES' if all differences are valid and 'NO' if it finds an invalid difference. However, it does not handle cases where the input may not be a valid integer or where `n` is outside the specified bounds (1 to 10).

