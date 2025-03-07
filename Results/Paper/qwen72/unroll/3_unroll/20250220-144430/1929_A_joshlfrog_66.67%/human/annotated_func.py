#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 500) representing the number of test cases, and a list of lists, where each inner list contains n (2 ≤ n ≤ 100) integers (1 ≤ a_i ≤ 10^9) representing the elements of the array a for each test case.
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
        
    #State: The loop will print the difference between the maximum and minimum elements of each array `nums` for each test case. After all iterations, the variables `t`, `l`, `nums`, `x`, and `y` will retain their final values from the last iteration, but the specific values of `x` and `y` will depend on the last array `nums` processed.
#Overall this is what the function does:The function reads an integer `t` (1 ≤ t ≤ 500) representing the number of test cases. For each test case, it reads an integer `l` (2 ≤ l ≤ 100) representing the length of the array, followed by `l` integers (1 ≤ a_i ≤ 10^9) from the input. It then calculates and prints the difference between the maximum and minimum elements of the array for each test case. After processing all test cases, the function does not return any value, but the variables `t`, `l`, `nums`, `x`, and `y` will retain their final values from the last test case processed.

