#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), n is a positive integer (1 ≤ n ≤ 2·10^5) representing the number of piles, and piles is a list of n positive integers (1 ≤ a_i ≤ 10^9) where each a_i represents the initial number of stones in the i-th pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: t remains a positive integer (1 ≤ t ≤ 10^4), n remains a positive integer (1 ≤ n ≤ 2·10^5) representing the number of piles, piles remains a list of n positive integers (1 ≤ a_i ≤ 10^9), N remains an input integer, nums is a list of integers where each element is 0, ls is the sum of the original elements in nums.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: t remains a positive integer (1 ≤ t ≤ 10^4), n remains a positive integer (1 ≤ n ≤ 2·10^5) representing the number of piles, piles remains a list of n positive integers (1 ≤ a_i ≤ 10^9), N remains an input integer, nums remains a list of integers where each element is 0, ls is the sum of the original elements in nums, nw is the same as the value of cw after the last iteration, cw is the same as the value of nw after the last iteration.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: t remains a positive integer (1 ≤ t ≤ 10^4), n remains a positive integer (1 ≤ n ≤ 2·10^5) representing the number of piles, piles remains a list of n positive integers (1 ≤ a_i ≤ 10^9), N remains an input integer, nums remains a list of integers where each element is 0, ls is the sum of the original elements in nums, nw is the same as the value of cw after the last iteration, and cw is the same as the value of nw after the last iteration. If cw is non-zero, the current value of cw is non-zero. If cw is zero, cw is False.
#Overall this is what the function does:The function `func_1` does not accept any parameters directly but reads input from the user. It processes a list of integers (representing piles of stones) and determines the winner of a game between two players, Alice and Bob, based on the final state of the piles. The function modifies the list of integers such that each element is reduced by a cumulative sum of previously processed elements, and then it iterates through the modified list to decide the winner. If the game state leads to a win for Alice, it prints "Alice"; otherwise, it prints "Bob". The function does not return any value. After the function concludes, the original input variables `t`, `n`, and `piles` remain unchanged, while the list `nums` is transformed into a list of zeros, and the variables `ls`, `nw`, and `cw` hold the final state of the game.

