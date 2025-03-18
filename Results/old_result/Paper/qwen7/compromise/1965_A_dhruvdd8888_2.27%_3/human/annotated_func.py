#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each pile, where 1 ≤ a_i ≤ 10^9, and the sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice'
    #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `N` is an input integer, `nums` is a list of integers sorted in ascending order, and the length of `nums` is not equal to 1
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob'
    #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `N` is an input integer, `nums` is a list of integers sorted in ascending order, and the length of `nums` is greater than 2
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: Output State: `cd` is the number of consecutive pairs of 1 in the list `nums`, starting from the first element up to the second last element. `t` remains a positive integer such that 1 ≤ t ≤ 10^4, `N` remains the input integer, and `nums` remains a list of integers sorted in ascending order with an additional 0 inserted at the beginning, and the length of `nums` is now greater than 3.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    else :
        return print('Alice')
        #The program prints 'Alice'
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `N` and a list of integers `nums`. It then checks the length of `nums` and performs specific operations based on its length. If the length of `nums` is 1, it prints 'Alice'. If the length is 2, it prints 'Bob'. If the length is greater than 2, it inserts a 0 at the beginning of `nums`, counts the number of consecutive pairs of 1s, and based on whether this count is odd or even, it prints either 'Alice' or 'Bob'. In all cases, the function does not return any value other than printing 'Alice' or 'Bob'.

