#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a consists of n integers where 0 ≤ a_j ≤ 10^9; the sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a consists of n integers where 0 ≤ a_j ≤ 10^9; the sum of the values of n over all test cases does not exceed 2 \cdot 10^5; after executing the loop, for each test case, if the first element of the array a is odd and the second element is not equal to the first element plus 2, or if the last element of the array a is odd and the second last element is not equal to the last element plus 2, the output will be 'NO', otherwise 'YES'.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and an array `a` of `n` integers. It checks if the first element of `a` is odd and the second element is not equal to the first element plus 2, or if the last element of `a` is odd and the second last element is not equal to the last element plus 2. If either condition is true, it prints 'NO'. Otherwise, it prints 'YES'. After processing all test cases, the function does not return any value but prints 'YES' or 'NO' for each test case based on the conditions checked.

