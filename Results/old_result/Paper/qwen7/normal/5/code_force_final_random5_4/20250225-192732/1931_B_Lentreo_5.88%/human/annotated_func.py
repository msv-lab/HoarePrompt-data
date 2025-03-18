#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the second line contains n non-negative integers a_1, a_2, ..., a_n such that the sum of a_i is divisible by n. Additionally, the sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: After all iterations, `curr` is the sum of all non-zero elements in the concatenated list of `nums` from all iterations, each subtracted by its respective `last` value from the end of the corresponding `nums` list. If `curr` equals 0, the function prints 'YES'. Otherwise, it prints 'NO'.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( t \) and then \( t \) lists of \( n \) non-negative integers. It calculates the sum of all non-zero elements in these lists, each subtracted by its respective last element from the end of the list. If this sum equals zero, it prints 'YES'; otherwise, it prints 'NO'.

