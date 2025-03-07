#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; and the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9 for each pile. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice'
    #State: Postcondition: `nums` is a sorted list of integers converted from the original set, and the length of `nums` is not equal to 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' to the console
    #State: Postcondition: `nums` is a sorted list of integers converted from the original set, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: Output State: The loop will continue to execute as long as the condition `nums[i + 1] - nums[i] == 1` holds true for consecutive elements in the list `nums`. After all iterations of the loop, the variable `cd` will hold the count of consecutive pairs of elements in `nums` that differ by exactly 1.
    #
    #If there are no such pairs throughout the entire list, `cd` will remain 0. If there are one or more pairs of consecutive elements that differ by exactly 1, `cd` will be incremented for each such pair until the condition is no longer met, at which point the loop will break.
    #
    #The final value of `i` will be the index just beyond the last pair of consecutive elements that differ by exactly 1, or it will be equal to `len(nums) - 2` if such pairs exist throughout the list.
    #
    #In summary, the output state after the loop executes all its iterations will be:
    #- `cd`: The count of consecutive pairs of elements in `nums` that differ by exactly 1.
    #- `i`: The index just beyond the last pair of consecutive elements that differ by exactly 1, or `len(nums) - 2` if such pairs exist throughout the list.
    #- `nums`: Unchanged from the initial state.
    #- `cd`: Updated based on the conditions within the loop.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    else :
        return print('Alice')
        #The program prints 'Alice'
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a set of integers from the input, sorts them, and then checks for consecutive pairs of elements that differ by exactly 1. Based on the count of such pairs (`cd`), it prints either 'Alice' or 'Bob' to the console. If `cd` is odd, it prints 'Bob' and returns `None`; otherwise, it prints 'Alice'.

