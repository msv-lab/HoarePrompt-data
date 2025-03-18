#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the second line contains n non-negative integers a_1, a_2, ..., a_n such that the sum of a_i is divisible by n.
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
        
    #State: Output State: The output state consists of 'YES' or 'NO' printed for each of the t test cases. For each test case, 'YES' is printed if the cumulative sum of non-zero differences between consecutive numbers in the list is zero, otherwise 'NO' is printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` indicating the number of cases, followed by an integer `n` and a list of `n` non-negative integers. It calculates the cumulative sum of the differences between consecutive non-zero numbers in the list. If this cumulative sum is zero, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

