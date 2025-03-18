#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^3) representing the number of test cases. For each test case, there are two lines: the first line contains an integer n (2 ≤ n ≤ 50) representing the length of the array, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 99) representing the elements of the array.
def func():
    n = int(input())
    for _ in range(n):
        m = int(input())
        
        arr = [int(i) for i in input().split()]
        
        ans = True
        
        for i in range(m - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                nums = [int(i) for i in str(arr[i - 1])] + [arr[i]]
                if nums != sorted(nums):
                    ans = False
                    break
                arr[i - 1] = nums[0]
        
        print(['NO', 'YES'][ans])
        
    #State: a series of 'YES' or 'NO' outputs for each test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an array of integers. For each test case, it checks if the array can be rearranged by merging adjacent elements such that the digits of the merged elements are in non-decreasing order. It outputs 'YES' if such a rearrangement is possible for the array, otherwise 'NO'.

