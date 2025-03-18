#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an even integer where 2 ≤ n ≤ 2·10^5, representing the number of columns in the grid. The sum of n over all test cases does not exceed 2·10^5. Each test case includes two strings of length n, consisting only of the characters '<' and '>', representing the arrows in the first and second rows of the grid, respectively.
def func():
    for j in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('NO')
                break
        else:
            print('YES')
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `j` is `t-1`, `n` is an input integer greater than 0, `a` is an input string, `b` is an input string, and `i` is the largest odd integer less than `n`. The loop has completed all iterations without breaking, so the final output is 'YES' for each test case that did not encounter the break condition.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves an even integer `n` and two strings of length `n` containing only the characters '<' and '>'. The function checks if the arrows in the two strings can form a valid grid configuration by ensuring no two adjacent arrows point towards each other. If any such pair is found, the function outputs 'NO' for that test case; otherwise, it outputs 'YES'. The function does not return any values but prints the result for each test case. After processing all test cases, the function completes its execution.

