#State of the program right berfore the function call: The function `func_1` takes no arguments. The input is provided via standard input and consists of multiple test cases. Each test case starts with an integer `t` (1 ≤ t ≤ 10^4), the number of test cases. For each test case, the first line contains an integer `n` (1 ≤ n ≤ 2·10^5), the number of piles. The second line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ 10^9), representing the initial number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: `N` is unchanged, `nums` is a list where each element is the difference between consecutive elements in the original sorted list, and `ls` is the last element of the original sorted list.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: N is unchanged, nums is a list where each element is the difference between consecutive elements in the original sorted list, ls is the last element of the original sorted list, nw is True, cw is True.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: N is unchanged, nums is a list where each element is the difference between consecutive elements in the original sorted list, ls is the last element of the original sorted list, nw is True, and cw is either True or False depending on the initial value of cw. If the initial value of cw was True, it remains True; otherwise, it is set to False.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of the number of piles and the number of stones in each pile. It processes each test case to determine the winner of a game (either Alice or Bob) based on the differences between the sorted number of stones in the piles, and prints the winner for each test case.

