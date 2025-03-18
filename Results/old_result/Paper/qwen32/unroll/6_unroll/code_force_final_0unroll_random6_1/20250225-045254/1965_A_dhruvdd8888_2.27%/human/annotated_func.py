#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program returns None and prints 'Alice'
    #State: `N` is assigned the value of the first integer input; `nums` is a sorted list of integers derived from the split first line input, and the length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    #State: `N` is assigned the value of the first integer input; `nums` is a sorted list of integers derived from the split first line input, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: N is the first integer input; nums is a sorted list of integers derived from the split first line input, with 0 inserted at the beginning; cd is the count of consecutive elements in nums that differ by 1, starting from the beginning of the list.
    if (cd & 1) :
        return print('Bob')
        #The program returns None after printing 'Bob'
    else :
        return print('Alice')
        #The program returns Alice
#Overall this is what the function does:The function processes multiple test cases where each test case consists of an integer `n` representing the number of piles and a list of `n` integers representing the number of stones in each pile. It determines the outcome based on the input and prints either 'Alice' or 'Bob'. The function returns `None` after printing the result.

