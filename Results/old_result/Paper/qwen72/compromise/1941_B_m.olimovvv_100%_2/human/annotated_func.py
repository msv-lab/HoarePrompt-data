#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_j satisfies 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, if the loop completes all iterations without encountering a negative value in `b` and the last two elements of `b` are both 0, it prints 'YES'. Otherwise, it prints 'NO'. The values of `t` and `n` remain unchanged, and the list `a` is modified as per the operations inside the loop.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `a` and a list `b` of `a` integers. It then iterates through the list `b` and modifies its elements according to specific operations. If at any point an element in `b` becomes negative, or if the last two elements of `b` are not both zero after the loop, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value and does not modify the input parameters `t` and `n`. The list `b` is modified during the process but is not retained after the function concludes.

