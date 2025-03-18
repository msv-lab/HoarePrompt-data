#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, n is a positive integer such that 1 <= n <= 100 for each test case, and s is a string of length n containing only "U" and "D" for each test case.
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: `t` is 0, `n` is a new positive integer read from input (1 <= n <= 100), `s` is a new string of length `n` containing only "U" and "D" as read from the input, `cases` is a list containing `t` tuples, each representing a pair of `(n, s)` as read from the input during each iteration.
    return cases
    #The program returns a list named `cases` which contains `t` tuples. Each tuple consists of a positive integer `n` (where 1 <= n <= 100) and a string `s` of length `n` containing only "U" and "D".
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a string `s` of length `n` containing only "U" and "D". It returns a list of tuples, each containing the integer `n` and the corresponding string `s` for each test case.

#State of the program right berfore the function call: case is a tuple where case[0] is an integer n (1 ≤ n ≤ 100) representing the number of coins, and case[1] is a string of length n containing only "U" and "D", representing that each coin is facing up or facing down.
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the count of 'U' in `case[1]` is odd, otherwise it returns 'NO'.
#Overall this is what the function does:The function takes a tuple `case` as input, where the first element is an integer `n` representing the number of coins, and the second element is a string of length `n` consisting of "U" and "D". It returns 'YES' if the number of "U" characters in the string is odd, and 'NO' otherwise.

