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
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 10^3\), `n` must be greater than 2, `m` is 0, `arr` is a list of integers entered by the user, `ans` remains False, `i` is -1.
    #
    #Explanation: After the loop completes all its iterations, `i` will eventually reach -1 because the loop starts from `m-1` and decrements `i` by 1 in each iteration until it reaches 0. If the loop completes all iterations without finding any pair of elements in `arr` that violate the condition `arr[i] < arr[i - 1]`, then `ans` will still be False. The value of `m` will be 0 since the loop processes each element in `arr` exactly once. The variable `i` will be -1 after the loop completes, indicating that the loop has finished processing all elements.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n` (2 ≤ n ≤ 50) followed by `n` integers (0 ≤ a_i ≤ 99). For each test case, it checks if the sequence of integers can be rearranged such that for every pair of consecutive elements, the first element is not less than the second element. If such a rearrangement is possible, it prints "YES"; otherwise, it prints "NO". The function does not return any value but prints the result for each test case.

