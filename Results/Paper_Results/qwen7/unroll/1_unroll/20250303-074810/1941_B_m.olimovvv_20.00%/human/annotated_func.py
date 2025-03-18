#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers such that 0 ≤ a_j ≤ 10^9 for each element a_j in the list. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: The output state consists of a series of 'YES' and 'NO' printed for each test case based on the conditions specified in the loop. For each test case, if the first element of the list `b` is odd and the second element is not equal to the first element plus 2, or if the last element of the list `b` is odd and the second-to-last element is not equal to the last element plus 2, then 'NO' is printed. Otherwise, 'YES' is printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `a` and a list `b`. It checks if the first element of `b` is odd and the second element is not equal to the first element plus 2, or if the last element of `b` is odd and the second-to-last element is not equal to the last element plus 2. If either condition is met, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value but prints 'YES' or 'NO' for each test case based on the specified conditions.

