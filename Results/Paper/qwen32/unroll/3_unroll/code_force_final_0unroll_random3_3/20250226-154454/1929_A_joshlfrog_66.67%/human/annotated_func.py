#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 100) representing the length of the array. This is followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) which are the elements of the array. The number of test cases t (1 ≤ t ≤ 500) is given at the beginning of the input.
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
        
    #State: t test cases have been processed, and for each test case, the difference between the maximum and minimum numbers in the list has been printed. The variables `l`, `nums`, `x`, and `y` no longer hold any specific values as they are reinitialized in each iteration of the outer loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an array of integers. For each test case, it calculates and prints the difference between the maximum and minimum values in the array.

