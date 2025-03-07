#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: The output state consists of `t` lines, each containing the sum of the maximum value in the first `n-1` elements and the last element of the list for each respective test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates the sum of the maximum value from the first `n-1` integers and the last integer in the list, then outputs this sum.

