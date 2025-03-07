#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each case, n is an integer such that 1 <= n <= 100, and s is a string of length n containing only "U" and "D".
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: t is an integer read from the standard input and stripped of any leading or trailing whitespace, and for each case, n is an integer such that 1 <= n <= 100, and s is a string of length n containing only "U" and "D". `cases` is a list containing t tuples, where each tuple consists of an integer n and a string s.
    return cases
    #The program returns the list `cases` which contains `t` tuples. Each tuple in the list consists of an integer `n` and a string `s`, where `n` is an integer such that 1 <= n <= 100, and `s` is a string of length `n` containing only "U" and "D".
#Overall this is what the function does:The function reads from the standard input to collect `t` test cases, where `t` is an integer between 1 and 100. For each test case, it reads an integer `n` (1 <= n <= 100) and a string `s` of length `n` containing only the characters "U" and "D". The function returns a list of `t` tuples, where each tuple contains the integer `n` and the string `s`.

#State of the program right berfore the function call: case is a list where case[0] is an integer n (1 ≤ n ≤ 100) representing the number of coins, and case[1] is a string s of length n containing only "U" and "D" representing the state of each coin.
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the number of "U" characters in the string `s` is even, otherwise it returns 'NO'.
#Overall this is what the function does:The function `func_2` accepts a list `case` where the first element is an integer `n` (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string `s` of length `n` containing only "U" and "D". It returns 'YES' if the number of "U" characters in `s` is even, and 'NO' if the number of "U" characters is odd. The function does not modify the input list `case`.

