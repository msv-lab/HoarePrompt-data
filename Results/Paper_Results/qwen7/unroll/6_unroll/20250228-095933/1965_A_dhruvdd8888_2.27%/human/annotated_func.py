#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for each pile i. The sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice'
    #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `N` is an input integer such that 1 ≤ N ≤ 2⋅10^5, and `nums` is a list of the unique elements from the input sorted in ascending order. The length of `nums` is greater than 1
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob'
    #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `N` is an input integer such that 1 ≤ N ≤ 2⋅10^5, and `nums` is a list of unique elements from the input sorted in ascending order with a length greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: Output State: `cd` is the length of the longest consecutive sequence of numbers starting from the second element of the list `nums`, `t` remains a positive integer such that 1 ≤ t ≤ 10^4, `N` remains an input integer such that 1 ≤ N ≤ 2⋅10^5, `nums` is a list with an additional element 0 inserted at the beginning, and the rest of the list remains unchanged.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    else :
        return print('Alice')
        #The program prints 'Alice'
#Overall this is what the function does:The function processes a list of integers and determines whether to print 'Alice' or 'Bob'. Depending on the conditions, it may also return None. If the length of the longest consecutive sequence of numbers starting from the second element of the list `nums` is odd, the program prints 'Bob' and returns None. If the length of the longest consecutive sequence is even, the program prints 'Alice'.

