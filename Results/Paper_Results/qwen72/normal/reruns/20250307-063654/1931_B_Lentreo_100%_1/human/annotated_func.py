#State of the program right berfore the function call: nums is a list of integers where the length of nums is n (1 ≤ n ≤ 2 · 10^5), and each element a_i in nums is an integer (0 ≤ a_i ≤ 10^9). The sum of all elements in nums is divisible by n.
def func_1(nums):
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns 'NO'
    #State: `nums` is a list of integers where the length of `nums` is `n` (1 ≤ n ≤ 2 · 10^5), and each element `a_i` in `nums` is an integer (0 ≤ a_i ≤ 10^9). The sum of all elements in `nums` is divisible by `n`. `n` is now equal to the length of `nums`. `total` is the sum of all elements in `nums`. Additionally, `total % n` is equal to 0.
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: `nums` is a list of integers with length `n` (1 ≤ n ≤ 2 · 10^5), each element `a_i` in `nums` is an integer (0 ≤ a_i ≤ 10^9), and the sum of all elements in `nums` is divisible by `n`. `n` is equal to the length of `nums` and is greater than 0. `total` is the sum of all elements in `nums`, and `mean` is the integer value of `total // n`. `total % n` is equal to 0. `curr` is now the sum of all elements in `nums` minus `n * mean`, and `i` is `n - 1`. If `curr` is less than 0 at any point during the loop, the program returns 'NO'. Otherwise, `curr` is 0.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a list of integers `nums` and checks if it is possible to make all elements in the list equal by performing a series of operations where each element can be increased or decreased by 1. The function returns 'NO' if at any point during the process, the current cumulative difference from the mean becomes negative, indicating that it is not possible to achieve the goal. If the function completes the iteration without encountering a negative cumulative difference, it returns 'YES', indicating that it is possible to make all elements equal.

