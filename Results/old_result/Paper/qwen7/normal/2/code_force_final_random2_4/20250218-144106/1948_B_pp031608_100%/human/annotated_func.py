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
        
    #State: Output State: The array `arr` is now a non-decreasing sequence where no two consecutive elements violate the order based on the described condition. The variable `i` is 0, `m` is 0, `nums` is not relevant, and `ans` is `False` if any changes were made during the process, otherwise `ans` is `True`.
    #
    #Explanation: After the loop completes all its iterations, the array `arr` will be transformed into a non-decreasing sequence where no two consecutive elements violate the order based on the described condition. The variable `i` will be 0, indicating that the loop has completed its iterations. The variable `m` will be 0 since it is decremented in the loop header and will reach 0 after all elements are processed. The variable `nums` will not be relevant as it is only used within the loop. The variable `ans` will be `False` if any replacements were made during the loop's execution, indicating that the array was not in a state where no two consecutive elements were in the correct order after all possible replacements. If no replacements were made, `ans` will remain `True`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n` followed by `n` integers. For each test case, it checks if the sequence of integers can be transformed into a non-decreasing sequence by ensuring no two consecutive elements violate a specific order condition. If any changes are needed, it makes the necessary adjustments. After processing all test cases, it outputs "YES" if the sequence can be transformed as required, otherwise "NO".

