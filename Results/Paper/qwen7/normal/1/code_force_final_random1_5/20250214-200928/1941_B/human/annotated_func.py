#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a consists of n integers where 0 ≤ a_j ≤ 10^9 for each element a_j in the array. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `a` is an input integer, `b` is a list of integers obtained from the final input string split on spaces and converted to integers, and the number of iterations left is `0`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer n and an array a of n integers. It checks if the first two elements of the array have a difference of 2 and are both odd, or if the last two elements have a difference of 2 and are both odd. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value but prints 'YES' or 'NO' for each test case.

