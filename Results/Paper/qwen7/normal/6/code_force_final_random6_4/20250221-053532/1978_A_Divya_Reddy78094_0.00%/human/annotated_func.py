#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: Output State: `t` must be equal to 3, `n` is an input integer, `nums` is a list of integers sorted in descending order.
    #
    #This means after the loop has executed all its iterations, `t` will be set to 3, indicating that the loop ran exactly 3 times. For each iteration, `n` is an integer input, and `nums` is a list of integers that gets updated and sorted in descending order based on the input provided during that iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) (1 ≤ \( t \) ≤ 500) and a list of \( n \) integers (2 ≤ \( n \) ≤ 100), where each integer \( a_i \) (1 ≤ \( a_i \) ≤ 10^9). For each test case, it sorts the list of integers in descending order and prints the sum of the first two elements. After processing all test cases, it outputs the results for each case.

