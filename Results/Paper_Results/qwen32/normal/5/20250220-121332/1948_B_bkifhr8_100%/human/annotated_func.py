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
        
    #State: `t` is an integer such that 1 <= t <= 10^3, `n` is 0, `a` is a list of the original `n` integers where each integer `a_i` satisfies 0 <= `a_i` <= 99.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks a list of integers to determine if it can be rearranged such that each integer is greater than or equal to the previous one by potentially concatenating digits of the previous integer with the current one. It outputs "YES" if such a rearrangement is possible for the list, otherwise "NO".

