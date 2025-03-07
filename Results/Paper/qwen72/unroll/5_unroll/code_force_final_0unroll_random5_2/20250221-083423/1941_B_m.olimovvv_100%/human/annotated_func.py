#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each element a_j satisfies 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The variable `t` is decremented by the number of iterations that the outer loop has executed. The variable `n` remains unchanged. The list `a` is modified such that all elements from the first to the third last are set to 0, and the last two elements are checked to determine if they are both 0. If they are both 0, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input. Each test case consists of an integer `a` and a list `b` of `a` integers. For each test case, the function modifies the list `b` such that each element from the first to the third last is set to 0, and the last two elements are checked. If both the last two elements are 0, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value.

