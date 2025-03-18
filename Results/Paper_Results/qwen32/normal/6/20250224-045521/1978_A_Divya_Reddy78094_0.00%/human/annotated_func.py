#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500; for each test case, n is an integer such that 2 <= n <= 100, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: `t` is 0; no more test cases are left to process; the state of `n` and `nums` from the last iteration is not relevant as the loop has terminated.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then outputs the sum of the two largest integers in the list.

