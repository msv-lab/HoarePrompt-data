#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is now equal to `n-1`. For the loop to have completed all its iterations without returning 'YES', it must be true that for every index `i` from `0` to `n-1`, either `a[i] == c[i]` or `b[i] == c[i]` holds. If any index `i` from `0` to `n-1` satisfies both `a[i] != c[i]` and `b[i] != c[i]`, the function would have returned 'YES' before completing all iterations. Therefore, the function does not return 'YES' after all iterations, and the final state is that the loop has completed without interruption, with `i` set to `n-1`.
    #
    #In simpler terms: After running the loop through all its iterations, the value of `i` will be `n-1`. The function did not return 'YES' during these iterations, meaning for each index `i` from `0` to `n-1`, at least one of the conditions `a[i] == c[i]` or `b[i] == c[i]` is true.
    return 'NO'
    #The program returns 'NO', with i being equal to n-1 and the loop having completed all its iterations without finding any index where both a[i] != c[i] and b[i] != c[i] hold.
#Overall this is what the function does:The function accepts three parameters: an integer \( n \) (where \( 1 \leq n \leq 20 \)), and two strings \( a \) and \( b \), each consisting of exactly \( n \) lowercase Latin letters. It also accepts a third string \( c \) of the same length. The function checks if there exists any index \( i \) from \( 0 \) to \( n-1 \) where both \( a[i] \neq c[i] \) and \( b[i] \neq c[i] \) are true. If such an index is found, the function returns 'YES'. If no such index exists, the function returns 'NO', with the loop having completed all its iterations and the variable \( i \) set to \( n-1 \).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings of exactly n lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: `results` is a list containing the return values of `func_1(n, a, b, c)` for each iteration of the loop, with `c` being the input string stripped of leading and trailing whitespace, `n` being the integer input stripped of leading and trailing whitespace, `a` being the input string stripped of leading and trailing whitespace, and `b` being the input string stripped of leading and trailing whitespace for each iteration. `t` is an integer between 1 and 1000 inclusive, representing the total number of iterations the loop will execute.
    for result in results:
        print(result)
        
    #State: Output State: `results` is a list containing the return values of `func_1(n, a, b, c)` for each of the 1000 iterations of the loop, `t` is 1000, `c` is the input string stripped of leading and trailing whitespace, `n` is the integer input stripped of leading and trailing whitespace, `a` is the input string stripped of leading and trailing whitespace, and `b` is the input string stripped of leading and trailing whitespace for each iteration, `result` is the last (1000th) element in the `results` list.
    #
    #In this final state, the `results` list will contain the return values from calling `func_1(n, a, b, c)` exactly 1000 times, with `t` set to 1000 indicating that the loop has completed all its iterations. The values of `c`, `n`, `a`, and `b` remain unchanged as they were in the initial state, since these values do not change within the loop. The `result` variable will hold the value returned by `func_1(n, a, b, c)` during the last iteration of the loop.
#Overall this is what the function does:The function processes up to 1000 test cases. For each test case, it reads an integer `t` (1 ≤ t ≤ 1000), an integer `n` (1 ≤ n ≤ 20), and three strings `a`, `b`, and `c` (each of length `n`). It then calls `func_1(n, a, b, c)` for each test case and stores the return values in a list. Finally, it prints the return values of `func_1` for all test cases.

