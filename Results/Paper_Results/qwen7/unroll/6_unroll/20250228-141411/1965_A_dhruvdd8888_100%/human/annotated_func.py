#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for each pile i. Additionally, the sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `N` is an input integer such that 1 ≤ N ≤ 2⋅10^5, `nums` is a list of integers sorted in ascending order where each element has been decremented by the cumulative sum of previous elements in the list, and `ls` is the sum of all elements in the modified `nums` list.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: Output State: `nw` is False, `cw` is False, `t` is a positive integer such that 1 ≤ t ≤ 10^4, `N` is an input integer such that 1 ≤ N ≤ 2⋅10^5, `nums` is a list of integers sorted in ascending order where each element has been decremented by the cumulative sum of previous elements in the list, and `ls` is the sum of all elements in the modified `nums` list.
    #
    #Explanation: The loop iterates from the second last element to the first element of the `nums` list. If `nums[i]` is equal to 1, `cw` toggles the value of `nw`. Otherwise, `cw` is set to `True`. Since the loop starts from the second last element and moves towards the first, and given that `nw` is initially `True`, it will toggle to `False` on encountering the first `1` in the list (if any), and then remain `False` for the rest of the iterations. `cw` will follow the same pattern but will start with the value of `nw` after the first iteration. Therefore, both `nw` and `cw` will end up being `False` after all iterations, assuming there is at least one `1` in the list; otherwise, they would still be `True`. However, without specific values in `nums`, we can only definitively say they will be `False` if there is at least one `1` in the list.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: `nw` and `cw` are both False, `t` is a positive integer such that 1 ≤ t ≤ 10^4, `N` is an input integer such that 1 ≤ N ≤ 2⋅10^5, `nums` is a list of integers sorted in ascending order where each element has been decremented by the cumulative sum of previous elements in the list, and `ls` is the sum of all elements in the modified `nums` list.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (1 ≤ t ≤ 10^4), an integer `N` (1 ≤ N ≤ 2⋅10^5), and a list of `N` integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ 10^9). It sorts the list of integers in ascending order and modifies each element by subtracting the cumulative sum of all previous elements. After processing, it checks the modified list to determine if there is at least one `1` present. Based on this check, it prints either "Alice" or "Bob". The function does not return any value but prints the result directly.

