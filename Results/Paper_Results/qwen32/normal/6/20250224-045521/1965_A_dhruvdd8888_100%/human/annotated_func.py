#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: - `t` remains the same.
    #- `n` remains the same.
    #- `a_1, a_2, ..., a_n` remain the same.
    #- `N` remains the same.
    #- `nums` is transformed such that each `nums[i]` is the original `nums[i]` minus the cumulative sum of all previous elements.
    #- `ls` is the sum of all elements in the original `nums` list.
    #- `i` will be `len(nums) - 1` (the last index of `nums`).
    #
    #### Final Output State:
    #Output State:
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: t, n, a_1, a_2, ..., a_n, N, ls, i is 1, nums remains the same, nw is True if nums[1] is not 1, otherwise False, cw is True if nums[1] is not 1, otherwise False.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: t, n, a_1, a_2, ..., a_n, N, ls, i are unchanged, nums remains the same, nw is True if nums[1] is not 1, otherwise False, and cw reflects whether nums[1] is not 1 (True if nums[1] is not 1, otherwise False).
#Overall this is what the function does:The function reads input for multiple test cases, each consisting of an integer `n` and a list of `n` integers. It processes these integers to determine the outcome of a game between Alice and Bob, printing 'Alice' or 'Bob' based on the processed list. The function does not modify the input values `t`, `n`, or the list of integers; it only outputs the result of each test case.

