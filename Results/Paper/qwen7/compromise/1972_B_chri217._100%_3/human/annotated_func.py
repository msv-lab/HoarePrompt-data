#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 100. For each test case, n is an integer representing the number of coins, where 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D", where "U" represents a coin facing up and "D" represents a coin facing down.
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: Output State: `cases` is a list containing `t` tuples, where each tuple consists of an integer `n` followed by a string `s`. The values of `n` and `s` are read from standard input for each iteration of the loop.
    return cases
    #The program returns a list called 'cases' containing tuples. Each tuple consists of an integer 'n' followed by a string 's', where these values were read from standard input during the iterations of the loop.
#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer `n` representing the number of coins and a string `s` of length `n` containing only "U" and "D". It then constructs a list of tuples, where each tuple contains the values of `n` and `s` for each test case, and returns this list.

#State of the program right berfore the function call: case is a list where the first element is an integer n (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string of length n containing only "U" and "D", representing the initial state of each coin (facing up or down).
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #'YES' if the count of 'U' in the second element of `case` is even, otherwise 'NO'
#Overall this is what the function does:The function accepts a list `case` where the first element is an integer indicating the number of coins, and the second element is a string representing the initial state of each coin (either "U" for up or "D" for down). It counts the number of coins facing up ("U") and returns 'YES' if this count is even, otherwise it returns 'NO'.

