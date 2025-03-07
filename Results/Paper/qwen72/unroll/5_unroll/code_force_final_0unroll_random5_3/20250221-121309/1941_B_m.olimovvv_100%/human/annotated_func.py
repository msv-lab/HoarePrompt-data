#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_j is such that 0 <= a_j <= 10^9.
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
        
    #State: The loop will iterate `t` times. For each iteration, if the list `b` can be modified such that the last two elements are 0 by the given operations and all elements in `b` are non-negative during the process, the output will be 'YES'. Otherwise, the output will be 'NO'. The values of `t` and `n` will remain unchanged, and the list `a` will be re-assigned to a new list of `n` integers in each iteration, but its final state after the loop is undefined as it is overwritten in each iteration.
#Overall this is what the function does:The function `func` does not accept any parameters directly. It reads input from the user multiple times, where the first input is an integer `t` (1 <= t <= 10^4) indicating the number of test cases. For each test case, it reads an integer `a` (3 <= a <= 2 * 10^5) and a list `b` of `a` integers (0 <= b_j <= 10^9). The function then attempts to modify the list `b` such that the last two elements become 0 by performing a series of operations on the elements of `b`. If it can achieve this without any element in `b` becoming negative during the process, it prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value. The values of `t` and `n` remain unchanged, and the list `a` is re-assigned in each iteration but its final state is undefined.

