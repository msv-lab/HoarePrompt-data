#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and there are n integers a_1, a_2, ..., a_n where 0 ≤ a_i ≤ 10^9. The sum of a_i for each test case is divisible by n, and the sum of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().strip().split()))
        
        last = nums[-1]
        
        curr = 0
        
        for i in nums:
            if i != 0:
                curr += i - last
        
        if curr == 0:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: The output state consists of 'YES' or 'NO' printed for each test case, depending on whether the cumulative sum of non-zero numbers in the list equals zero after processing all elements in the list. For each test case, it checks if the sum of differences between each element (except the last one) and the last element is zero; if it is, it prints 'YES', otherwise 'NO'.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` indicating the number of cases, followed by `n` integers. It then calculates the cumulative sum of the differences between each non-zero element (excluding the last one) and the last element in the list. If this cumulative sum equals zero, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints 'YES' or 'NO' for each test case based on the specified condition.

