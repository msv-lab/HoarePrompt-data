#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a consists of n integers where 0 ≤ a_j ≤ 10^9 for each element a_j; the sum of all n values across all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: The loop will continue to run for all test cases provided by the user until all test cases are processed. For each test case, if the condition `b[0] % 2 == 1 and b[1] != b[0] + 2` or `b[-1] % 2 == 1 and b[-2] != b[-1] + 2` is met, the output will be 'NO'. Otherwise, the output will be 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t`, an integer `n`, and an array `a` of `n` integers. For each test case, it checks if the first element of the array `a` is odd and the second element is not two more than the first, or if the last element of the array `a` is odd and the second-to-last element is not two less than the last. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value but prints the result for each test case.

