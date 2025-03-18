#State of the program right berfore the function call: The function should take two integers n and m (1 ≤ n, m ≤ 500) and a list of n strings, each of length m, consisting of characters 'W' and 'B' representing the colors of the grid. The function should also handle multiple test cases, indicated by an integer t (1 ≤ t ≤ 10^4) at the beginning of the input. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop iterates through each test case, reads the grid dimensions and the grid itself, and checks specific conditions to determine if the grid is valid. For each test case, it prints 'NO' if the first or last row is entirely one color and different from each other, or if the first and last columns are entirely one color and different from each other. Otherwise, it prints 'YES'. The variables `n`, `m`, `a`, `first_row`, and `last_row` are reset for each test case, and the loop continues until all test cases are processed.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `m` (1 ≤ n, m ≤ 500) and a list of `n` strings, each of length `m`, containing characters 'W' and 'B'. For each test case, it reads the grid dimensions and the grid itself, then checks if the first or last row is entirely one color and different from each other, or if the first and last columns are entirely one color and different from each other. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function continues processing until all test cases are handled.

