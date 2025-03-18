#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) where a_i is the number of stones in the i-th pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program returns Alice
    #State: `N` is an input integer, `t` is an integer (1 ≤ t ≤ 10^4), `n` is an integer (1 ≤ n ≤ 2·10^5) for each test case, `a_1, a_2, ..., a_n` are integers (1 ≤ a_i ≤ 10^9) for each test case, `nums` is a list of integers sorted in ascending order, and the length of `nums` is greater than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program returns 'Bob'
    #State: `N` is an input integer, `t` is an integer (1 ≤ t ≤ 10^4), `n` is an integer (1 ≤ n ≤ 2·10^5) for each test case, `a_1, a_2, ..., a_n` are integers (1 ≤ a_i ≤ 10^9) for each test case, `nums` is a list of integers sorted in ascending order, and the length of `nums` is greater than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: `cd` is the number of consecutive elements in `nums` starting from the second element that have a difference of 1.
    if (cd & 1) :
        return print('Bob')
        #The program returns None and prints 'Bob'
    else :
        return print('Alice')
        #The program returns None and prints 'Alice'
#Overall this is what the function does:The function reads input values representing the number of test cases, the number of piles for each test case, and the number of stones in each pile. It determines the winner of a game based on these inputs and either prints 'Alice' or 'Bob'. The function does not return any value explicitly, but it prints the name of the winner.

