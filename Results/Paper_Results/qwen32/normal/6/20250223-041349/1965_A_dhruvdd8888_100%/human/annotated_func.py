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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `N` is an input integer, `nums` is a list where each element is the difference between the original element and the cumulative sum of all previous elements, and `ls` is the sum of all elements in the original `nums`.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `N` is an input integer, `nums` is a list, `ls` is the sum of all elements in the original `nums`, `nw` is `False` if `nums[1]` is equal to 1, otherwise `nw` is `True`, and `cw` is `False` if `nums[1]` is equal to 1, otherwise `cw` is `True`.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `N` is an input integer, `nums` is a list, `ls` is the sum of all elements in the original `nums`, `nw` is `False` if `nums[1]` is equal to 1, otherwise `nw` is `True`, and `cw` is `True` if `nums[1]` is not equal to 1, otherwise `cw` is `False`.
#Overall this is what the function does:The function reads an integer `N` and a list of `N` integers, processes the list to compute differences based on cumulative sums, and then determines whether to print 'Alice' or 'Bob' based on the processed list.

