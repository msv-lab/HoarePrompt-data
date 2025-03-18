#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. Each test case consists of two lines: the first line contains an integer n such that 2 ≤ n ≤ 50, and the second line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i ≤ 99.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^3, n is an input integer such that 2 ≤ n ≤ 50, each iteration of the loop processes input values for `m` and `arr`, and after all iterations, the final value of `ans` is printed as either 'NO' or 'YES'. The final state of `t` and `n` remains unchanged from their initial values, while `m` and `arr` are updated based on the input during each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) (where \( 2 \leq n \leq 50 \)) followed by \( n \) integers \( a_1, a_2, \ldots, a_n \) (each between 0 and 99). For each test case, it checks if the sequence can be made non-decreasing by swapping adjacent elements at most once. If such a swap is possible, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function outputs the results for each case.

