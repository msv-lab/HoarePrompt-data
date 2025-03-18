#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The length of test_cases is t (1 ≤ t ≤ 10^4), and the sum of all n values across all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: `test_cases` is a list of tuples, `N` is an input integer, `nums` is a sorted list of integers that includes the integer 0, `ls` is now the sum of all elements in `nums` before the loop, and each element in `nums` is now 0.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: `test_cases` is a list of tuples, `N` is an input integer, `nums` is a sorted list of integers that includes the integer 0 and has at least 3 elements, each element in `nums` is now 0, `ls` is the sum of all elements in `nums` before the loop, `i` is 1, `nw` is the same as the last value of `cw`. If `nums[1]` is 1, `cw` is False. Otherwise, `cw` is True and `nums[1]` is not equal to 1.
    if cw :
        print('Alice')
        #This is printed: Output:
    else :
        print('Bob')
        #This is printed: Bob
    #State: *`test_cases` is a list of tuples, `N` is an input integer, `nums` is a sorted list of integers that includes the integer 0 and has at least 3 elements, each element in `nums` is now 0, `ls` is the sum of all elements in `nums` before the loop, `i` is 1, and `nw` is the same as the last value of `cw`. If `cw` is True, `nums[1]` is not equal to 1. If `cw` is False, `nums[1]` is 1.
#Overall this is what the function does:The function reads an integer `N` from the input, representing the number of elements, and then reads a list of `N` integers from the input. It processes these integers to determine the winner of a game (Alice or Bob) based on the final state of the list after a series of operations. The function does not modify the `test_cases` list or return any value; instead, it prints the name of the winner ('Alice' or 'Bob') based on the game's outcome. The game's outcome is determined by the final state of the list, where if the second smallest number in the list is 1, Bob wins; otherwise, Alice wins.

