#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, and each (n, s) in cases is a tuple where n is a positive integer such that 1 <= n <= 100, and s is a string of length n containing only 'U' and 'D'.
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: `t` is an integer read from input, 1 <= t <= 100, `cases` is a list containing `t` tuples, each tuple is `(n, s)`, where `n` is an integer read from the corresponding line of input, and `s` is a string read from the corresponding line of input and stripped of leading and trailing whitespace. `_` is `t-1`.
    return cases
    #The program returns a list named `cases` containing `t` tuples, where `t` is an integer between 1 and 100. Each tuple in the list is of the form `(n, s)`, where `n` is an integer read from the corresponding line of input, and `s` is a string read from the corresponding line of input and stripped of leading and trailing whitespace.
#Overall this is what the function does:The function `func_1` reads input from the standard input. It first reads an integer `t` (where 1 <= t <= 100), indicating the number of test cases. For each test case, it reads another integer `n` (where 1 <= n <= 100) and a string `s` of length `n` containing only the characters 'U' and 'D'. The function returns a list named `cases` containing `t` tuples, where each tuple is of the form `(n, s)`. The string `s` is stripped of leading and trailing whitespace.

#State of the program right berfore the function call: case is a list where case[0] is an integer representing the number of coins (1 ≤ case[0] ≤ 100), and case[1] is a string of length case[0] containing only 'U' and 'D', representing the state of each coin (up or down).
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the number of 'U' characters in the string case[1] is even, otherwise it returns 'NO'.
#Overall this is what the function does:The function `func_2` takes a list `case` as input, where `case[0]` is an integer representing the number of coins, and `case[1]` is a string of the same length containing only 'U' and 'D'. The function returns 'YES' if the number of 'U' characters in the string `case[1]` is even, and 'NO' if the number of 'U' characters is odd. The state of the input `case` remains unchanged after the function call.

