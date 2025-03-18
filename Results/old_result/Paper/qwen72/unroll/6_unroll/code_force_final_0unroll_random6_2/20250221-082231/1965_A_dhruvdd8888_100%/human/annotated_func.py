#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains n (1 ≤ n ≤ 2·10^5) integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: `t` remains the number of test cases (1 ≤ t ≤ 10^4), `N` remains the input integer, `nums` is a list of integers where each element is 0, and `ls` is the sum of the initial elements in `nums`. The list of lists containing the initial number of stones in each pile remains unchanged.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: `t` remains the number of test cases (1 ≤ t ≤ 10^4), `N` remains the input integer, `nums` is a list of integers where each element is 0, `ls` is the sum of the initial elements in `nums`, `nw` is True, `cw` is True.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: *`t` remains the number of test cases (1 ≤ t ≤ 10^4), `N` remains the input integer, `nums` is a list of integers where each element is 0, `ls` is the sum of the initial elements in `nums`, `nw` is True, and `cw` retains its initial value (True or False).
#Overall this is what the function does:The function `func_1` reads an integer `N` from the input, which represents the number of stones. It then reads a list of integers from the input, processes it, and determines the winner of a game between Alice and Bob. The game is based on the initial number of stones in the piles, and the function prints either "Alice" or "Bob" as the winner. After the function concludes, `t` remains the number of test cases, `N` remains the input integer, `nums` is a list of integers where each element is 0, and `ls` is the sum of the initial elements in `nums`. The list of lists containing the initial number of stones in each pile remains unchanged.

