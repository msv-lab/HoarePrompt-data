#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4) representing the number of test cases, n is a positive integer (1 ≤ n ≤ 2·10^5) representing the number of piles in the game, and piles is a list of n positive integers (1 ≤ a_i ≤ 10^9) where each a_i represents the initial number of stones in the i-th pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `n` is a positive integer (1 ≤ n ≤ 2·10^5), `piles` is a list of n positive integers (1 ≤ a_i ≤ 10^9), `N` is an input integer, `nums` is a sorted list of integers where each element is 0, `ls` is the sum of all elements in the original `nums` list.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `n` is a positive integer (1 ≤ n ≤ 2·10^5), `piles` is a list of n positive integers (1 ≤ a_i ≤ 10^9), `N` is an input integer, `nums` is a sorted list of integers where each element is 0, `ls` is the sum of all elements in the original `nums` list, `nw` is True, `cw` is True.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: *`t` is a positive integer (1 ≤ t ≤ 10^4), `n` is a positive integer (1 ≤ n ≤ 2·10^5), `piles` is a list of n positive integers (1 ≤ a_i ≤ 10^9), `N` is an input integer, `nums` is a sorted list of integers where each element is 0, `ls` is the sum of all elements in the original `nums` list, `nw` is True, and `cw` is True if the initial value of `cw` was True. Otherwise, `cw` is False.
#Overall this is what the function does:The function `func_1` reads an integer `N` from the input, which represents the number of unique piles of stones. It then reads a list of integers from the input, converts it to a set to remove duplicates, adds `0` to the set, and sorts the resulting set into a list `nums`. The function modifies `nums` such that each element is reduced by a cumulative sum `ls` of the previous elements, effectively setting each element to 0. It then determines the winner of a game based on the modified `nums` list and prints either "Alice" or "Bob" as the winner. The function does not return any value and does not modify the original `t`, `n`, or `piles` variables. After the function concludes, `N` is an input integer, `nums` is a sorted list of integers where each element is 0, `ls` is the sum of all elements in the original `nums` list, and `cw` and `nw` are boolean variables indicating the game's outcome.

