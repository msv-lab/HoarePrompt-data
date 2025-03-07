#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 500, and n * m ≤ 3 * 10^5; each test case consists of n lines, each containing m characters 'W' (for white) and 'B' (for black), representing the initial colors of the grid.
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
        
    #State: Output State: After the loop executes all the iterations, `n` is a non-negative integer, `i` is equal to `n`, `a` is a list of length `n` containing all the inputs in the order they were provided, `first_row` is a string formed by taking the first character of each string in `a`, and `last_row` is a string formed by taking the last character of each string in `a`. The loop processes all the test cases provided as input, and based on the conditions checked within the loop, it prints either 'YES' or 'NO' for each test case. If any test case meets the conditions to print 'NO', the loop will print 'NO' for that specific test case. Otherwise, for all other test cases, it will print 'YES'. The final state of `a`, `first_row`, and `last_row` will reflect the last processed test case's data, and the loop will terminate once all test cases have been processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid represented by `n` rows and `m` columns of 'W' (white) and 'B' (black) characters. For each test case, it checks if the first and last rows, as well as the first and last characters of each row, are uniform but different from each other. If any test case fails this condition, it prints 'NO' for that case; otherwise, it prints 'YES'. After processing all test cases, the function outputs the results for each case.

