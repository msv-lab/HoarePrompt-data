#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: `t` is an integer such that 1 <= `t` <= 500, `n` is the integer provided by the user input, and `nums` is a list of `n` integers provided by the user input. The loop has executed `t` times, and for each execution, it prints the sum of the maximum value from the first `n-1` elements of `nums` and the last element of `nums`.
#Overall this is what the function does:The function processes `t` test cases, where each test case includes an integer `n` and a list of `n` integers. For each test case, it outputs the sum of the maximum value from the first `n-1` integers in the list and the last integer in the list.

