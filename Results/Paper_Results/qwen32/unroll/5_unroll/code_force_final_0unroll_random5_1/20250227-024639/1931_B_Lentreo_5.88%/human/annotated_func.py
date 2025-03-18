#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i ≤ 10^9. The sum of a_i for each test case is divisible by n. The sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: The output will be a series of 'YES' or 'NO' printed for each test case, depending on whether the condition `curr == 0` is satisfied for each test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it checks if a specific condition is met (related to the sum of the elements in the list relative to the last element) and prints 'YES' if the condition is satisfied, otherwise 'NO'.

