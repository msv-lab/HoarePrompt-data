#State of the program right berfore the function call: n is a positive integer representing the size of the array, and ai is a list of integers where each element is between 1 and 100.**
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
        
    #State of the program after the loop has been executed: `n` is a positive integer, `ai` is a list of integers, `flag` is False if there exists at least one pair of consecutive elements in `nums` with an absolute difference of 2 or more, `nums` is a non-empty map object with a length of at least 1 after removing the maximum element from it, and `i` is len(nums) - 2
    print['NO', 'YES'][flag]
#Overall this is what the function does:The function `func` takes input for the size of an array (n) and the elements of the array (ai). It then iterates through the array elements, checking if the absolute difference between any two consecutive elements is at least 2. If such a pair is found, the function sets the flag to False and exits the loop. After that, it removes the maximum element from the array. Finally, it prints either 'NO' if the flag is False or 'YES' if the flag is True. The function works with implicit parameters, an array of integers, and its purpose is to determine if there are consecutive elements with an absolute difference of at least 2 in the array.

