#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; the first line of each test case contains a string of length n consisting of characters '<' and/or '>'; the second line of each test case contains a string of length n consisting of characters '<' and/or '>'.
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
        
    #State: Output State: All test cases have been processed, and for each test case, one of the following outputs has been printed: 'YES' or 'NO'. The variables `i`, `n`, `a`, and `b` have been updated according to the loop's logic, but their final values are not specified as they depend on the input for each test case. The variable `no_path` has been determined based on the conditions inside the loop and affects the final output.
    #
    #In natural language, this means that after all iterations of the loop have completed, the program has processed all given test cases and printed 'YES' or 'NO' for each one based on the conditions specified in the loop. The values of `i`, `n`, `a`, `b`, and `no_path` reflect the outcome of processing each test case, but without specific inputs, we cannot determine their exact final values.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer \( t \) (1 ≤ \( t \) ≤ 10^4) and an integer \( n \) (2 ≤ \( n \) ≤ 2⋅10^5, \( n \) is even). For each test case, it reads two strings of length \( n \), each consisting only of '<' and/or '>'. Based on the conditions specified in the code, it prints either 'YES' or 'NO' for each test case. After processing all test cases, the function ensures that the correct output ('YES' or 'NO') is printed for each one.

