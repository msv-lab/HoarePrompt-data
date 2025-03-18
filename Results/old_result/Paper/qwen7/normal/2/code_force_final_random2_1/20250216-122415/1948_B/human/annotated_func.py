#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^3. Each test case consists of two lines: the first line contains a single integer n such that 2 <= n <= 50, and the second line contains n integers a_1, a_2, ..., a_n such that 0 <= a_i <= 99.
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
        
    #State: After all iterations of the loop, `m` will be 0, `i` will be -1, `arr` will be a list as it was initially, and `ans` will be `False`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( n \) followed by \( n \) integers. For each test case, it checks if the last digit of each number (except the first one) is less than or equal to the last digit of the previous number. If the digits form a non-decreasing sequence when reversed, it sets a flag `ans` to `True`; otherwise, it sets `ans` to `False`. Finally, it prints "YES" if `ans` is `True`, indicating the sequence meets the condition, or "NO" if `ans` is `False`.

