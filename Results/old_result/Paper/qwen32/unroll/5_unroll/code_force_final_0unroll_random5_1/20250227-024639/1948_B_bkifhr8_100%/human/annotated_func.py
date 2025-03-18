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
        
    #State: t is an integer such that 1 <= t <= 10^3; n is the integer value provided by the input; a is a list of n integers where each integer a_i satisfies 0 <= a_i <= 99. The output for each test case is printed as either "YES" or "NO" based on the condition inside the loop.
#Overall this is what the function does:The function reads multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then checks if the list can be modified by repeatedly replacing a pair of adjacent elements with a new list formed by concatenating the digits of the larger element followed by the smaller element, such that the resulting list is sorted in non-decreasing order. If this condition can be met, it prints "YES"; otherwise, it prints "NO".

