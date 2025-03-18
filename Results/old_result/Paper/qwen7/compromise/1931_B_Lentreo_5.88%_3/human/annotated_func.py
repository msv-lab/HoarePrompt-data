#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the second line contains n non-negative integers a_1, a_2, \dots, a_n such that the sum of a_i is divisible by n. Additionally, the sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: After all iterations, `curr` will be the sum of all non-zero elements in the final `nums` list minus the last element of the final `nums` list. If `curr` equals 0, it remains 0. Otherwise, `curr` is the sum of all non-zero elements in the final `nums` list minus the last element of the final `nums` list.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( t \) indicating the number of cases, then for each case, it reads an integer \( n \) and a list of \( n \) non-negative integers. It calculates the sum of all non-zero elements in the list, subtracting the last element of the list, and checks if this value is zero. If it is zero, it prints 'YES', otherwise it prints 'NO'. The function does not return any value but prints the result for each test case.

