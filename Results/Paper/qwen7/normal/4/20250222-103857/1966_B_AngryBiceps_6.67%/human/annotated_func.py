#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, both positive integers such that 1 ≤ n, m ≤ 500, and a grid of size n × m filled with characters 'W' and 'B'. The sum of n·m over all test cases does not exceed 3·10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = []
        
        first_row = ''
        
        last_row = ''
        
        for i in range(n):
            a.append(input())
            first_row += a[-1][0]
            last_row += a[-1][-1]
        
        if len(set(a[0])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is the total number of iterations the loop executed, `i` is equal to `n - 1`, `m` retains the value it had after the first input, `a` is a list containing `n` elements (each element being an input provided during the loop's iterations), `first_row` is the concatenation of the first character of each element in list `a`, `last_row` is a string consisting of the last character of the second element in list `a` repeated `n-1` times, followed by the last character of the last element in list `a`. The conditions specified in the if part hold if either the first string in the list `a` consists of the same character repeated and is different from the last string in the list `a`, or the first string in the list `a` does not consist of a single character repeated and is not equal to the last string. Otherwise, the conditions specified in the else part hold.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of size n x m where each cell contains either 'W' or 'B'. It reads the grid and checks specific conditions related to the first and last rows of the grid. If the first row consists of the same character repeated and is different from the last row, or if the first row does not consist of a single character repeated and is not equal to the last row, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value but prints the result for each test case.

