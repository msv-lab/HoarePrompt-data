#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, both positive integers such that 1 ≤ n, m ≤ 500, and the grid is represented as an n × m matrix where each element is either 'W' or 'B'. The sum of n·m over all test cases does not exceed 3·10^5.
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
        
    #State: Postcondition: `a` is a list containing all the inputs provided by the user, with each input as a separate element. `first_row` is a string consisting of the first character of each input string in `a`. `last_row` is a string consisting of the last character of each input string in `a`. The variable `i` is equal to `-1`, indicating that the loop has completed all its iterations. `n` is the final length of the list `a`, which is determined by the number of test cases provided.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an n × m grid where each cell contains either 'W' or 'B'. It constructs a list of these grids, along with strings representing the first and last characters of each row. The function then checks if the first row of any grid is uniform and different from the last row of that grid, or if the first character of each row is uniform and different from the last character of each row. If either condition is met, the function prints 'NO'; otherwise, it prints 'YES'.

