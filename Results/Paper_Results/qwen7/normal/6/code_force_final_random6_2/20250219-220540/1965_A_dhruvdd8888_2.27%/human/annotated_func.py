#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a (length n) represents the initial number of stones in each pile, with each a_i satisfying 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice'
    #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `N` is an input integer, `nums` is a list of integers sorted in ascending order, and the length of `nums` is not equal to 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob'
    #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `N` is an input integer, `nums` is a list of integers sorted in ascending order, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `cd` is a non-negative integer, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `N` is an input integer, `nums` is a list of integers sorted in ascending order with an additional 0 at the beginning, and the length of `nums` is at least 3.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob'
    else :
        return print('Alice')
        #The program prints 'Alice'
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `N` and a set of space-separated integers representing the number of stones in each pile. It then sorts these integers and checks specific conditions to determine whether to print 'Alice' or 'Bob'. If the sorted list has only one element, it prints 'Alice'. If the list has exactly two elements, it prints 'Bob'. Otherwise, it inserts a zero at the beginning of the list, counts the number of consecutive pairs with a difference of 1, and based on whether this count is odd or even, it prints either 'Alice' or 'Bob'.

