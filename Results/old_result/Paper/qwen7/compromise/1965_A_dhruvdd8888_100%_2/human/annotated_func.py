#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9. It is also guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: Output State: `ls` is the sum of all elements in `nums`, `t` remains a positive integer such that 1 ≤ t ≤ 10^4, `N` remains an input integer such that 1 ≤ N ≤ 2⋅10^5, `nums` is a list of integers sorted in descending order where each element is initially from the original list minus `ls`. '0' is added to the set `nums`.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: Output State: `cw` is False, `ls` is the sum of all elements in `nums`, `t` remains a positive integer such that 1 ≤ t ≤ 10^4, `N` remains an input integer such that 1 ≤ N ≤ 2⋅10^5, `nums` is a list of integers sorted in descending order where each element is initially from the original list minus `ls`, and `nw` is set to False.
    #
    #Explanation: The loop iterates over `nums` from the second last element to the first element. If `nums[i]` equals 1, `cw` is toggled based on the value of `nw`. Otherwise, `cw` is set to `True`. Since `nw` starts as `True` and `cw` is only toggled when `nums[i]` is 1, and given that `nums` is sorted in descending order (meaning it will contain 1s at the end if present), `cw` will eventually become `False` if there is at least one 1 in `nums`. If there are no 1s in `nums`, `cw` will remain `True` until the last iteration where it gets toggled to `False` due to `nw` being `True`.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: `cw` is False, `ls` is the sum of all elements in `nums`, `t` remains a positive integer such that 1 ≤ t ≤ 10^4, `N` remains an input integer such that 1 ≤ N ≤ 2⋅10^5, `nums` is a list of integers sorted in descending order where each element is initially from the original list minus `ls`, and `nw` remains True.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` (1 ≤ t ≤ 10^4), a positive integer `n` (1 ≤ n ≤ 2⋅10^5), and a list of integers `a` (length `n`, 1 ≤ a_i ≤ 10^9) representing the initial number of stones in each of the `n` piles. It sorts the list of integers in descending order, subtracts a running total (`ls`) from each element, and then determines whether a certain condition (`cw`) is met. Based on the final state of `cw`, it prints either "Alice" or "Bob".

