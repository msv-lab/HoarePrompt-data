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
        
    #State: Prints 'YES' or 'NO' for each of the n test cases, with t and a unchanged.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it checks if the list can be rearranged in a specific way to ensure that each number is not less than the previous one when digits are considered. It prints 'YES' if the list can be rearranged as per the condition, otherwise 'NO'. The input values `t` and the lists remain unchanged after the function execution.

