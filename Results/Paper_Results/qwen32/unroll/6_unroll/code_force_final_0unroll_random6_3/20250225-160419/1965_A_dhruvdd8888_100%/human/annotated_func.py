#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: `nums` is a list of 1s with the same length as the initial `nums`, and `ls` is the sum of the original `nums` list.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: `nums` is a list of 1s with the same length as the initial `nums`, `ls` is the sum of the original `nums` list, `nw` is `True`, `cw` is `False`.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: `nums` is a list of 1s with the same length as the initial `nums`, `ls` is the sum of the original `nums` list, `nw` is `True`, and `cw` is `False`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of piles and the number of stones in each pile. It processes each test case to determine the winner of a game (either Alice or Bob) based on the given conditions and prints the result for each test case.

