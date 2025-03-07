#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: For each test case, the output will be the sum of the maximum value from all elements except the last one in the list `a` and the last element itself. The variable `t` remains unchanged as it represents the number of test cases.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list of `n` integers. It then calculates and prints the sum of the maximum value from all elements except the last one in the list and the last element itself.

