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
        
    #State: Output State: The loop has executed all its iterations, with the following characteristics:
    #
    #- `i` is 0, as the loop decremented `i` from `m - 1` to 0.
    #- `m` remains unchanged, as it is not modified within the loop.
    #- `arr` is updated such that for every pair of consecutive elements where the second element is less than the first, the first element has been updated to match the smallest value in the sequence formed by concatenating and sorting the digits of the two elements.
    #- `ans` is either `True` or `False` depending on whether the loop's condition was met throughout all iterations. If `ans` is `True`, it means that for every pair of consecutive elements where the second element is less than the first, the first element has been successfully updated to match the smallest value in the sequence formed by concatenating and sorting the digits of the two elements. If `ans` is `False`, it means that at some point during the loop's execution, the condition `arr[i] < arr[i - 1]` was found to be true, and `ans` was set to `False`, breaking the loop.
    #
    #The final state of `arr` and `ans` will reflect the outcome of the loop's execution based on the input provided.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer \( n \) and then \( n \) integers. It checks if the sequence of integers can be adjusted so that for every pair of consecutive elements where the second element is smaller than the first, the first element can be updated to match the smallest possible value formed by concatenating and sorting the digits of both elements. If such adjustments can be made for all pairs, the function prints "YES"; otherwise, it prints "NO".

