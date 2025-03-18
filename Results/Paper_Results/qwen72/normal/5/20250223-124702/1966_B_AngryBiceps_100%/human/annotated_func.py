#State of the program right berfore the function call: The function should accept multiple test cases. Each test case includes two integers n and m (1 ≤ n, m ≤ 500) representing the dimensions of the grid, and a list of n strings, each of length m, containing characters 'W' and 'B' representing the initial colors of the grid. The total number of test cases t is an integer (1 ≤ t ≤ 10^4) and the sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
        if len(set(a[0])) == 1 and len(set(a[-1])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and len(set(last_row)
            ) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: The loop processes each test case and prints 'YES' or 'NO' based on the conditions specified. After all iterations, the variables `n`, `m`, `a`, `first_row`, and `last_row` are reset for each new test case, and the loop continues to the next test case until all test cases are processed. The initial state of the function remains unchanged, and the function is ready to accept new test cases.
#Overall this is what the function does:The function `func` accepts multiple test cases, each consisting of a grid represented by two integers `n` and `m` (1 ≤ n, m ≤ 500) and a list of `n` strings, each of length `m`, containing characters 'W' and 'B'. For each test case, the function checks if the first row and the last row of the grid are either entirely one color and different from each other, or if the first column and the last column of the grid are entirely one color and different from each other. If either condition is met, the function prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function ends, and the program state is reset for each new test case, with no lasting changes to the initial state.

