#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, and the sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: Output State: `ls` is the sum of all elements in the list `nums`, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `N` is an input integer, `n` is a positive integer such that \(1 \leq n \leq 2 \cdot 10^5\), `a_1, a_2, ..., a_n` is a list of \(n\) integers where \(1 \leq a_i \leq 10^9\), `nums` is a sorted list of integers, `i` is equal to the length of `nums`, and `nums[i]` is not accessed since `i` equals the length of `nums`.
    #
    #In natural language, after the loop has executed all its iterations, the variable `ls` will hold the sum of all elements in the list `nums`. The variable `t` remains unchanged as it was initially defined. The other variables (`N`, `n`, `a_1, a_2, ..., a_n`, and `nums`) also remain in their initial or updated states according to the operations performed within the loop. The variable `i` will be equal to the length of `nums` after the last iteration, and since the loop increments `i` until it reaches the length of `nums`, `nums[i]` would be out of bounds and not accessed.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: `cw` is either `not nw` or `True`; `ls` remains the sum of all elements in the list `nums`; `t` is a positive integer such that \(1 \leq t \leq 10^4\); `N` is an input integer; `n` is a positive integer such that \(1 \leq n \leq 2 \cdot 10^5\); `a_1, a_2, ..., a_n` is a list of \(n\) integers where \(1 \leq a_i \leq 10^9\); `nums` is a sorted list of integers; `i` is 0; `nw` is equal to `cw`.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: 'Bob'
    #State: `cw` is either `not nw` or `True`, `ls` remains the sum of all elements in the list `nums`, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `N` is an input integer, `n` is a positive integer such that \(1 \leq n \leq 2 \cdot 10^5\), `a_1, a_2, ..., a_n` is a list of \(n\) integers where \(1 \leq a_i \leq 10^9\), `nums` is a sorted list of integers, `i` is 0, and `nw` is equal to `cw`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` (1 ≤ t ≤ 10^4), a positive integer `n` (1 ≤ n ≤ 2⋅10^5), and a list of `n` integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ 10^9). For each test case, it first sorts the list and adjusts the values to compute the cumulative sum `ls`. Then, it iterates through the sorted list to determine whether `cw` is `not nw` or `True`. Based on the final value of `cw`, it prints either "Alice" or "Bob". The function does not return any value but prints the result for each test case.

