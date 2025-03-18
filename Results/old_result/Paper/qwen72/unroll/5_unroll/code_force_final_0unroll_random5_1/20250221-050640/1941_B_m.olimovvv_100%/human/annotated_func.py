#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_j <= 10^9 for each j from 1 to n. The sum of the values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it processes the list `b` such that after the inner loop completes, the elements at indices `a-1` and `a-2` of `b` are checked. If both `b[a-1]` and `b[a-2]` are zero, 'YES' is printed; otherwise, 'NO' is printed. The values of `t`, `n`, and the list `a` remain unchanged.
#Overall this is what the function does:The function `func` reads input from the user, processes multiple test cases, and prints 'YES' or 'NO' for each test case. It expects the user to provide an integer `t` indicating the number of test cases, followed by `t` pairs of inputs: an integer `a` and a list `b` of `a` integers. For each test case, the function modifies the list `b` and checks if the last two elements of `b` are zero after processing. If both are zero, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any values and does not modify the input variables `t`, `n`, or `a`.

