#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program returns Alice
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is an integer read from input; `nums` is a list of integers, sorted in ascending order, that were originally represented as strings in the input set, and the length of `nums` is not equal to 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program returns None after printing 'Bob'
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is an integer read from input; `nums` is a list of integers, sorted in ascending order, that were originally represented as strings in the input set, and the length of `nums` is not equal to 1. Additionally, the length of `nums` is not equal to 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is an integer read from input; `nums` is a list of integers, sorted in ascending order starting from 0, and the length of `nums` is not equal to 1 or 2; `cd` is the count of consecutive pairs of integers in `nums` starting from the beginning that have a difference of 1.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    else :
        return print('Alice')
        #The program returns 'Alice'
#Overall this is what the function does:The function reads an integer `N` and a list of integers from the input, processes the list to determine the number of unique integers and their consecutive differences, and then prints and returns either 'Alice' or 'Bob' based on specific conditions.

