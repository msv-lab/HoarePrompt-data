#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3. For each test case, n is an integer such that 2 <= n <= 50, and a is a list of n integers where each integer a_i satisfies 0 <= a_i <= 99.
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
        
    #State: t is an integer such that 1 <= t <= 10^3; n is the integer read from input, where 2 <= n <= 50; a is a list of n integers where each integer a_i satisfies 0 <= a_i <= 99. The loop has printed 'YES' or 'NO' for each of the n iterations.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it checks if the list can be modified by a specific rule such that all elements are in non-decreasing order. It prints 'YES' if the list can be modified accordingly, otherwise 'NO'.

