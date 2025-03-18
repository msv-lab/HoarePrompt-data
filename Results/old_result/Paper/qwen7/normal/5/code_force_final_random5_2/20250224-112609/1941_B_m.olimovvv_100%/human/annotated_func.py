#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a is a list of n integers where 0 ≤ a_j ≤ 10^9 for each element a_j in the array. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        for i in range(0, a - 2):
            if b[i] < 0:
                print('NO')
                break
            b[i + 1] -= b[i] * 2
            b[i + 2] -= b[i]
            b[i] -= b[i]
        else:
            if b[-1] != 0 or b[-2] != 0:
                print('NO')
            else:
                print('YES')
        
    #State: Output State: `a` is less than 3, `b` is a list of integers where all elements are zero, and the final output printed is 'YES'.
    #
    #Explanation: After the loop has executed all its iterations, `a` will be less than 3 because each iteration decrements `a` by 1. All elements in `b` that were accessed and modified will have been processed according to the loop's logic. Since the loop processes all elements and does not encounter a negative value in `b` (which would cause an early break), and given that the operations continue until the end of the list, all elements in `b` will be reduced to 0. As a result, the conditions `if b[-1] != 0 or b[-2] != 0:` will not be met, and the final output will be 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) integers. For each test case, it checks if any element in the array is negative or if the operations defined in the loop leave any non-zero elements in the array. If any condition is violated, it prints 'NO'. Otherwise, it prints 'YES'. The function implicitly uses input from standard input and outputs to standard output.

