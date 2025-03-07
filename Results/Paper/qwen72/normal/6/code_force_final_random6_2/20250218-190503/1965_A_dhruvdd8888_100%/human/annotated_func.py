#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The length of test_cases is t (1 ≤ t ≤ 10^4), and the sum of n over all test cases does not exceed 2·10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: After the loop executes all iterations, `test_cases` remains a list of tuples, where each tuple contains an integer `n` (1 ≤ n ≤ 2·10^5) and a list of `n` integers (1 ≤ a_i ≤ 10^9). The length of `test_cases` is `t` (1 ≤ t ≤ 10^4), and the sum of `n` over all test cases does not exceed 2·10^5. `N` is an input integer. `nums` is a sorted list of integers with all elements modified such that each element `nums[i]` is now `nums[i] - (nums[0] + nums[1] - nums[0] + ... + nums[i-1] - (nums[i-2] + ... + nums[0]))`. `ls` is the sum of all elements in the modified `nums` list. `i` is equal to the length of `nums` - 1.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: `test_cases` remains a list of tuples, where each tuple contains an integer `n` (1 ≤ n ≤ 2·10^5) and a list of `n` integers (1 ≤ a_i ≤ 10^9). The length of `test_cases` is `t` (1 ≤ t ≤ 10^4), and the sum of `n` over all test cases does not exceed 2·10^5. `N` is an input integer. `nums` is a sorted list of integers with at least 2 elements, and all elements modified such that each element `nums[i]` is now `nums[i] - (nums[0] + nums[1] - nums[0] + ... + nums[i-1] - (nums[i-2] + ... + nums[0]))`. `ls` is the sum of all elements in the modified `nums` list. `i` is equal to 0. `nw` is `True` or `False` depending on the value of `nums[1]`. `cw` is `True` or `False` depending on the value of `nums[1]`.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: *`test_cases` remains a list of tuples, where each tuple contains an integer `n` (1 ≤ n ≤ 2·10^5) and a list of `n` integers (1 ≤ a_i ≤ 10^9). The length of `test_cases` is `t` (1 ≤ t ≤ 10^4), and the sum of `n` over all test cases does not exceed 2·10^5. `N` is an input integer. `nums` is a sorted list of integers with at least 2 elements, and all elements modified such that each element `nums[i]` is now `nums[i] - (nums[0] + nums[1] - nums[0] + ... + nums[i-1] - (nums[i-2] + ... + nums[0]))`. `ls` is the sum of all elements in the modified `nums` list. `i` is equal to 0. `nw` is `True` or `False` depending on the value of `nums[1]`. If `cw` is `True`, then `cw` remains `True`. If `cw` is `False`, then `cw` remains `False`.
#Overall this is what the function does:The function `func_1` reads an integer `N` from the input, which represents the number of elements in a set. It then reads a line of space-separated integers, converts them to a set, adds '0' to the set, and sorts the resulting set into a list `nums`. The function modifies the elements of `nums` such that each element is reduced by the cumulative sum of the previous elements. It then determines a winner between 'Alice' and 'Bob' based on the modified list `nums` and prints the winner. The function does not return any value. The state of `test_cases` remains unchanged.

