#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for each pile i, and the sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: Output State: `i` is equal to the length of `nums`; `ls` is the sum of all elements in the original `nums` list; each element in `nums` has been reduced by its corresponding cumulative `ls` value starting from the first iteration.
    #
    #In simpler terms, after the loop completes all its iterations, the index `i` will be equal to the total number of elements in the `nums` list. The variable `ls` will hold the sum of all the original values in the `nums` list. Each element in the `nums` list will have been decreased by the cumulative value of `ls` as it was updated in each iteration of the loop.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: Output State: `cw` is a boolean flag, `nw` equals `cw`, `i` is `0`.
    #
    #Explanation: The loop runs from `len(nums) - 2` down to `1`. After the loop completes, `i` will be decremented to `0`. Since the loop condition is `i in range(len(nums) - 2, 0, -1)`, once `i` reaches `0`, the loop stops. At this point, `cw` and `nw` will retain their last values determined by the loop's final iteration, and `i` will be `0`.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: Postcondition: `cw` is a boolean flag, `nw` equals `cw`, and `i` is `0`, regardless of whether `cw` is `True` or `False` in the if condition.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `n` and a list of `n` integers. It first sorts the list and adjusts its elements based on a cumulative sum. Then, it iterates through the modified list to determine a boolean flag `cw`. Based on the final value of `cw`, it prints either "Alice" or "Bob". The function does not return any value but modifies and processes the input data as described.

