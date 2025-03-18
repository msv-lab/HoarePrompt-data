#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, there is an integer n (2 ≤ n ≤ 100) representing the length of the array, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array. The number of test cases t satisfies 1 ≤ t ≤ 500.
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
        
    #State: `t` is an integer such that 1 ≤ `t` ≤ 500, `l` is the integer value provided by the user input, `nums` is the list of integers obtained from the new input, `x` is the maximum value in `nums`, `y` is the minimum value in `nums`, and `e` is equal to `t`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an array of integers. For each array, it calculates the difference between the maximum and minimum values and prints this difference.

