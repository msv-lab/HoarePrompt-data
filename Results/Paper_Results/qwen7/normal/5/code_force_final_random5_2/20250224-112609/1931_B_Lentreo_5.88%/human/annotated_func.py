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
        
    #State: After all iterations, `curr` will be the sum of all non-zero elements in `nums` from the first input, adjusted by subtracting the last element of the original `nums` for each non-zero element, unless `curr` becomes zero in any iteration, in which case it remains zero. The value of `t` will be reduced by the length of `nums` for each iteration, and `last` will be the last element of the original `nums` list.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) (indicating the number of subsequent test cases) and a list of \( n \) non-negative integers whose sum is divisible by \( n \). For each test case, it calculates the sum of the non-zero elements in the list, adjusted by subtracting the last element of the list for each non-zero element. If this adjusted sum equals zero, it prints 'YES', indicating the sum is divisible by \( n \); otherwise, it prints 'NO'.

