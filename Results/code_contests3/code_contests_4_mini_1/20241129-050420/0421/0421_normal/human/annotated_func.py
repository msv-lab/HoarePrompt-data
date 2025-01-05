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
        
    #State of the program after the loop has been executed: `n` is a non-empty input string; `flag` is False if any adjacent integers in `nums` had an absolute difference of 2 or more during any iteration; otherwise, `flag` is True; `nums` is empty if the loop executed completely until all elements were removed, or it contains integers that all had adjacent differences of less than 2 before the maximum was repeatedly removed. In the end, `i` is not relevant as the loop has finished executing.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 10) that indicates the number of elements in an array, followed by `n` space-separated integers (1 ≤ ai ≤ 100). It checks if all adjacent integers in the array have an absolute difference of less than 2. If any adjacent integers do have a difference of 2 or more, it prints 'NO'; otherwise, it prints 'YES'. The function modifies the list by repeatedly removing the maximum element until all elements are processed or the condition is violated.

