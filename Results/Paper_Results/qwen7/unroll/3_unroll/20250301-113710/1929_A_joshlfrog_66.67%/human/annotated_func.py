#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    t = int(input())
    for e in range(t):
        l = int(input())
        
        nums = [int(x) for x in input().split()]
        
        x = 0
        
        y = 100000000
        
        for i in range(l):
            if nums[i] > x:
                x = nums[i]
            if nums[i] < y:
                y = nums[i]
        
        print(x - y)
        
    #State: Output State: t is an integer between 1 and 500 (inclusive), l is an integer, nums is a list of integers, x is an integer initialized to 100000000, y is an integer initialized to 100000000, and the loop has executed t times. After each iteration of the outer loop, x and y are updated based on the values in the list nums, and then x - y is printed. The other variables remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` (number of sub-cases), an integer `n` (number of integers), and a list of `n` integers. It then finds the maximum and minimum values in the list and prints their difference. The function does not return any value but prints the result for each test case.

