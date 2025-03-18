#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each pile, where 1 ≤ a_i ≤ 10^9, and the sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: Output State: `nums` is a list of integers where each element has been decremented by the cumulative sum of all previous elements in `nums`; `ls` is the sum of all elements in the original `nums`.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: Output State: `cw` is False, `nums` is a list of integers where each element has been decremented by the cumulative sum of all previous elements in `nums`, `ls` is the sum of all elements in the original `nums`.
    #
    #Explanation: The loop iterates from the second last element to the second element of the `nums` list. For each element, if it equals 1, `cw` is toggled; otherwise, `cw` remains True. Since the loop starts from the end and moves towards the beginning, and given that the value of `cw` at the start of the loop is True, it will be toggled for every 1 found in the `nums` list. If there is an odd number of 1s, `cw` will end up being False; if even, it would be True. However, since we do not know the exact number of 1s in the list, we can only definitively say that `cw` will be False if there was at least one 1 and the total number of 1s was odd. The `nums` and `ls` values remain as per the initial state because the loop does not modify these variables.
    if cw :
        print('Alice')
        #This is printed: nothing
    else :
        print('Bob')
        #This is printed: Bob
    #State: Postcondition: `cw` is False, `nums` is a list of integers where each element has been decremented by the cumulative sum of all previous elements in `nums`, and `ls` is the sum of all elements in the original `nums`. This holds true regardless of whether the if condition `(cw)` is true or false, as the else part ensures `cw` remains False and the lists `nums` and `ls` retain their initial states.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer n and a list of n integers representing the number of stones in each pile. It calculates the cumulative sum of stones in each pile, decrements each pile's stone count by this cumulative sum, and then checks the parity of the number of piles with exactly one stone remaining. Based on this check, it prints either 'Alice' or 'Bob'. Regardless of the outcome, the final state of the program includes a boolean variable `cw` set to False, a list `nums` with decremented stone counts, and an integer `ls` representing the sum of the original stone counts.

