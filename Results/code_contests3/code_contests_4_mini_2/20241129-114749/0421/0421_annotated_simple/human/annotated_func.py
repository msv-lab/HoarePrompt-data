#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 10), which is the size of the array, followed by n space-separated integers ai (1 ≤ ai ≤ 100), representing the elements of the array.
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
        
    #State of the program after the loop has been executed: `n` is an input string representing a valid integer, `flag` is False if any adjacent elements in `nums` had an absolute difference of 2 or more during the iterations, otherwise `flag` is True, and `nums` is an empty map object after all maximum values have been removed.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 10) and a list of `n` integers (each between 1 and 100). It checks if the absolute difference between any two adjacent elements in the list is less than 2. If such a difference is found, it sets a flag to False. It continues checking until all maximum values are removed from the list. Finally, it prints 'YES' if the flag remains True (indicating all adjacent differences were within the limit) and 'NO' if the flag was set to False. The code may not handle cases where there are fewer than 2 elements in the list correctly, as the loop may not execute as intended.

