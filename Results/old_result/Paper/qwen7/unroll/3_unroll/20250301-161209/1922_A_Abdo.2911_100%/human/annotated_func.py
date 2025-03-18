#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20. a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        possible = False
        
        for i in range(n):
            if a[i] == b[i]:
                if c[i] != a[i]:
                    possible = True
                    break
            elif c[i] == a[i] or c[i] == b[i]:
                continue
            else:
                possible = True
                break
        
        if possible:
            print('YES')
        else:
            print('NO')
        
    #State: The output state will consist of 'YES' or 'NO' printed for each iteration of the loop based on the conditions specified in the loop body. If for any iteration 'possible' is set to True, 'YES' is printed; otherwise, 'NO' is printed. The final state will be determined by the last printed output after all iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it checks if it's possible to transform string `a` into string `b` using string `c` as an intermediate step. For each test case, it prints 'YES' if the transformation is possible according to specific conditions, otherwise it prints 'NO'. After processing all test cases, the function concludes with the final output state consisting of 'YES' or 'NO' for each case.

