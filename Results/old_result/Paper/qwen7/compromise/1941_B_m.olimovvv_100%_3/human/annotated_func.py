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
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\), `a` is an integer such that \(a \geq 3\), and `b` is a list of integers where each element is equal to the integer input split by spaces, and after all iterations, `b[-1]` and `b[-2]` are both 0.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t`, an integer `n`, and a list `a` of `n` integers. It then iterates through the list `a` and modifies its elements based on specific conditions. If any condition is violated during the iteration, it prints 'NO' and breaks. After processing all elements, if the last two elements of the list are both zero, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

