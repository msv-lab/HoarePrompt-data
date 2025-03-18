#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, both positive integers such that 1 ≤ n, m ≤ 500, and a grid of size n × m filled with 'W' (white) and 'B' (black) characters. The sum of n·m over all test cases does not exceed 3·10^5.
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
        
    #State: Postcondition: `i` is equal to `n-1`, `n` is a valid integer, `a` is a list containing `n` elements, each being the input received during the corresponding iteration of the loop. The variable `first_row` is a string consisting of the first character of each string in the list `a`. The variable `last_row` is a string consisting of the last character of each string in `a`. After all iterations, the conditions for printing 'NO' or 'YES' have been fully evaluated for all test cases. If any test case fails the conditions to print 'NO', it will print 'NO'. Otherwise, for all test cases that pass the conditions to print 'YES', it will print 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of size n × m filled with 'W' (white) and 'B' (black) characters. For each test case, it checks if the first and last rows of the grid are uniform (all 'W' or all 'B') and distinct from each other. If any test case fails this condition, it prints 'NO'. Otherwise, it prints 'YES' for all passing test cases.

