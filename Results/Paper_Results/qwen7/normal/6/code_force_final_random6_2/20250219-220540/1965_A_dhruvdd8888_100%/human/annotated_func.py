#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each pile, where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: Output State: `ls` is the sum of all elements in `nums`, `nums` is a sorted list of integers including '0', `i` is the length of `nums`.
    #
    #Explanation: After the loop completes all its iterations, `ls` will accumulate the value of each element in `nums`. Since the loop runs for each index from 0 to len(nums)-1, `ls` will be the sum of all elements in `nums`. The value of `i` will be equal to the length of `nums` because the loop increments `i` until it reaches the length of `nums`. The list `nums` remains sorted and includes '0' as per the initial condition and no changes within the loop affect its sorted order or inclusion of '0'.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: Output State: `cw` is `True`, `ls` is the sum of all elements in `nums`, `nums` is a sorted list of integers including '0', `i` is 0, `nw` is `True`.
    #
    #Explanation: The loop runs from `len(nums) - 2` down to `1`. After each iteration, `i` decreases by 1. Since the loop continues until `i` is 0 (inclusive), it will run exactly `len(nums) - 1` times if `nums` has more than one element. Given that the loop has executed three times, `i` is now `len(nums) - 4`. The loop will continue to decrement `i` until it reaches 0. At that point, `cw` will be set to `True` on the last iteration because the condition `nums[i] == 1` will no longer be checked (as `i` is 0, which is less than the start of the range). Therefore, `cw` remains `True`, `i` becomes 0, and the other variables (`ls`, `nums`, and `nw`) remain unchanged as they are not affected by the loop.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: Postcondition: `cw` is `True`, `ls` is the sum of all elements in `nums`, `nums` is a sorted list of integers including '0', `i` is 0, `nw` is `True`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `n` and a list of `n` integers representing the number of stones in each pile. It sorts the list of integers, subtracts a cumulative sum from each element, and then iterates through the list to determine a boolean value `cw`. Based on the final value of `cw`, it prints either "Alice" or "Bob". The function does not return any value but prints the result directly.

