#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an even integer such that 2 ≤ n ≤ 2·10^5; the sum of n over all test cases does not exceed 2·10^5; the second and third lines of each test case are strings of length n consisting of characters '<' and/or '>' representing the arrows in the first and second rows of the grid, respectively.
def func():
    for i in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        if b[-2] != '>':
            print('NO')
        elif n == 1:
            print('YES')
        else:
            no_path = True
            for k in range(0, n, 2):
                if b[k] != '>':
                    no_path = False
            if not no_path:
                no_path = True
                for k in range(1, n - 1, 2):
                    print(k)
                    if a[k] != '>':
                        no_path = False
            if no_path:
                print('YES')
            else:
                print('NO')
        
    #State: The loop iterates through each test case, and for each test case, it prints 'YES' if the conditions for the arrows are met, otherwise it prints 'NO'. The variables `t`, `n`, `a`, and `b` are updated according to the input for each test case, but their values are not retained between iterations. After all iterations, the loop completes and the program ends.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an even integer `n` and two strings `a` and `b` of length `n` consisting of characters '<' and/or '>'. For each test case, it prints 'YES' if the following conditions are met: the second-to-last character of `b` is '>', and there is no path from the first row to the second row of a grid represented by `a` and `b` that avoids all '>' characters. If these conditions are not met, it prints 'NO'. The function does not return any values; it only prints the results for each test case. The variables `t`, `n`, `a`, and `b` are updated for each test case, but their values are not retained between iterations. After processing all test cases, the function completes and the program ends.

