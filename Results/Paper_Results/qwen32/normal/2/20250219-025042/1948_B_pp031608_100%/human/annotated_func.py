#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 99.
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
        
    #State: The final output state consists of `n` lines, each containing either 'YES' or 'NO', corresponding to the result of each test case. The variables `t`, `n`, and `a` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it determines if the list can be modified by replacing each pair of adjacent elements (from right to left) with a new element formed by concatenating the digits of the larger element followed by the smaller element, such that the resulting list is sorted in non-decreasing order. It outputs 'YES' if such modifications can result in a sorted list, otherwise 'NO'.

