#State of the program right berfore the function call: The function `func` is expected to read input from stdin and output to stdout. The input consists of multiple test cases, where the first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with two integers n and m (1 ≤ n, m ≤ 500) representing the dimensions of the grid, followed by n lines each containing m characters 'W' or 'B' representing the initial colors of the grid. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop reads the input for each test case, processes the grid, and prints 'YES' or 'NO' for each test case based on the conditions specified. After all iterations, the variables `n`, `m`, `a`, `first_row`, and `last_row` will have their final values corresponding to the last test case processed. The variable `t` will be unchanged as it is only used to determine the number of iterations.
#Overall this is what the function does:The function `func` reads input from stdin, processes multiple test cases, and prints 'YES' or 'NO' to stdout for each test case. Each test case consists of a grid of dimensions `n` x `m` with cells colored 'W' or 'B'. The function checks if the first row and the first column of the grid are uniform in color and if they are different from the last row and the last column, respectively. If these conditions are met, 'NO' is printed; otherwise, 'YES' is printed. After processing all test cases, the function has no return value, and the variables `n`, `m`, `a`, `first_row`, and `last_row` will hold the values corresponding to the last test case processed.

