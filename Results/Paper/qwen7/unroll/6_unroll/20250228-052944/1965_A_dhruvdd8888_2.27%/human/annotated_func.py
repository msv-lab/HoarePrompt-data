#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each pile, where 1 ≤ a_i ≤ 10^9, and the sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None
    #State: `nums` is a sorted list of integers converted from the original set of strings, and the length of `nums` is not equal to 1
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' to the console
    #State: Postcondition: `nums` is a sorted list of integers converted from the original set of strings, and the length of `nums` is not equal to 2
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: Output State: `cd` is the number of consecutive pairs of 1 in the list `nums`, starting from the second element. The length of `nums` remains unchanged.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    else :
        return print('Alice')
        #The program prints 'Alice'
#Overall this is what the function does:The function processes a series of test cases, each consisting of a list of integers representing the number of stones in piles. Based on specific conditions related to the differences between consecutive numbers in the list, it determines whether to print 'Alice' or 'Bob'. If the count of consecutive pairs of 1s starting from the second element is odd, it prints 'Bob'; otherwise, it prints 'Alice'. The function does not return any value.

