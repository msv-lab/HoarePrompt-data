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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `N` is the input integer representing `t`, `n` is an integer such that 1 ≤ n ≤ 2·10^5, `nums` is a list of differences between consecutive elements starting from the original first element, and `ls` is the sum of all elements in the original `nums` list.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `N` is the input integer representing `t`, `n` is an integer such that 1 ≤ n ≤ 2·10^5, `nums` is a list of differences between consecutive elements starting from the original first element, `ls` is the sum of all elements in the original `nums` list, `nw` is `False` if `nums[1]` is 1, otherwise `nw` is `True`, and `cw` is `False` if `nums[1]` is 1, otherwise `cw` is `True`.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `N` is the input integer representing `t`, `n` is an integer such that 1 ≤ n ≤ 2·10^5, `nums` is a list of differences between consecutive elements starting from the original first element, `ls` is the sum of all elements in the original `nums` list, `nw` is `False` if `nums[1]` is 1, otherwise `nw` is `True`, and `cw` is `False` if `nums[1]` is 1, otherwise `cw` is `True`. If `cw` is `True`, then `nums[1]` is not 1. If `cw` is `False`, then `nums[1]` is 1.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It processes these inputs to determine and print either "Alice" or "Bob" based on the specific conditions derived from the list of integers.

