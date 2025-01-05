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
        
    #State of the program after the loop has been executed: `n` is a non-empty string representing an integer; `flag` is False if there exists at least one pair of consecutive integers in `nums` with an absolute difference of 2 or more; otherwise, `flag` remains True; `nums` is empty after all maximum integers have been removed.
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function accepts an integer `n` and an array of `n` integers. It checks for the presence of at least one pair of consecutive integers in the array with an absolute difference of 2 or more. If such a pair exists, it prints 'NO'; otherwise, it prints 'YES'. The function modifies the array by repeatedly removing the maximum integer until the array is empty, potentially leading to situations where the check for consecutive integers is not fully comprehensive or accurate, especially if the input array contains multiple elements with the same value.

