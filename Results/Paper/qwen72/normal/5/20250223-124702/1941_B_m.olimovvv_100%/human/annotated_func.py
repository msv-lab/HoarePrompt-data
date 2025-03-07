#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each element a_j is an integer such that 0 <= a_j <= 10^9.
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
        
    #State: The loop iterates `t` times. For each iteration, it reads an integer `a` and a list `b` of `a` integers. After processing the list `b` according to the loop logic, if any element `b[i]` is negative or if the last two elements of `b` are not zero, it prints 'NO'. Otherwise, it prints 'YES'. The values of `t`, `n`, and `a` remain unchanged, and the list `a` (if it was part of the initial state) is not modified by the loop.
#Overall this is what the function does:The function `func` reads `t` test cases from the input. For each test case, it reads an integer `a` and a list `b` of `a` integers. It processes the list `b` by modifying its elements according to a specific logic. If any element in `b` becomes negative during the processing or if the last two elements of `b` are not zero after the processing, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value and does not modify the initial state of `t`, `n`, or `a` (if they were part of the initial state).

