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
        
        if len(set(a[0])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: All test cases have been processed, and for each test case, the final state of the variables is as follows:
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of size n × m filled with 'W' (white) and 'B' (black) characters. For each test case, it checks if the first row is identical to the last row or if the first and last characters of each row are the same. If either condition is met, it prints 'NO'. Otherwise, it prints 'YES'. After processing all test cases, the function does not return any value but prints 'YES' or 'NO' for each test case based on the conditions checked.

