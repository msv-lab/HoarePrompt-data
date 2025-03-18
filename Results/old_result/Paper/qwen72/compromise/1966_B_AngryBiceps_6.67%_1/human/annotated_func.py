#State of the program right berfore the function call: The function `func` is expected to read input from stdin and process multiple test cases. Each test case includes an n x m grid represented as a list of strings, where each string consists of characters 'W' and 'B' indicating the colors of the grid's squares. The values of n and m are integers such that 1 ≤ n, m ≤ 500, and the total number of test cases t is an integer such that 1 ≤ t ≤ 10^4. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop has processed all test cases, and for each test case, it has printed 'NO' if the first row or the first column contains only one unique color and that color is different from the last row or the last column, respectively. Otherwise, it has printed 'YES'. The variables `n`, `m`, `a`, `first_row`, and `last_row` are reset for each test case, and their final values after the loop are undefined as they are overwritten in each iteration.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case consists of an n x m grid represented as a list of strings with characters 'W' and 'B'. For each test case, the function checks if the first row or the first column contains only one unique color and that color is different from the last row or the last column, respectively. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function processes all test cases and prints the results, one per test case. The final state of the program after the function concludes is that all test cases have been processed and the appropriate 'YES' or 'NO' result has been printed for each. The internal variables used for processing are reset for each test case and are undefined after the function completes.

