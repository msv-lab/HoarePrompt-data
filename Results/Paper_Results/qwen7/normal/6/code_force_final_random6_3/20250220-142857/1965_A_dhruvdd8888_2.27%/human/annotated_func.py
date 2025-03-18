#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; and the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9 for each i. The sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice'
    #State: `nums` is a list of integers sorted in ascending order, and the length of `nums` is not equal to 1
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    #State: `nums` is a list of integers sorted in ascending order, and the length of `nums` is greater than 2
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `cd` is either 1 or 0, `i` is the index where the condition `nums[i + 1] - nums[i] != 1` is first met, or `i` is equal to `len(nums) - 3` if the condition is never broken.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob'
    else :
        return print('Alice')
        #The program prints 'Alice'
#Overall this is what the function does:The function processes a series of test cases. For each case, it reads a set of integers representing the number of stones in each pile, sorts them, and then determines whether to print 'Alice' or 'Bob' based on specific conditions. If the count of consecutive integers starting from the second element is odd, it prints 'Bob'; otherwise, it prints 'Alice'. The function does not return any value but prints 'Alice' or 'Bob' for each test case.

