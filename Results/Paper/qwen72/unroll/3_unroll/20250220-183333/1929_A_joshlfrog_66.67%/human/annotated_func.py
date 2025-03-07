#State of the program right berfore the function call: The function should accept two parameters: t (1 ≤ t ≤ 500), the number of test cases, and a list of lists, where each inner list contains n integers (2 ≤ n ≤ 100) with each integer a_i (1 ≤ a_i ≤ 10^9).
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
        
    #State: The function will print the difference between the maximum and minimum values of each list in the input. The variables `x` and `y` will be reset to 0 and 100000000 respectively for each iteration of the outer loop. After all iterations, the function will have printed `t` lines, each containing the difference for the corresponding list.
#Overall this is what the function does:The function `func` reads an integer `t` (1 ≤ t ≤ 500) from the input, representing the number of test cases. For each test case, it reads an integer `l` (2 ≤ l ≤ 100) indicating the length of the list, followed by a list of `l` integers (1 ≤ a_i ≤ 10^9). The function then calculates and prints the difference between the maximum and minimum values in each list. After processing all test cases, the function will have printed `t` lines, each containing the difference for the corresponding list. The function does not return any value.

