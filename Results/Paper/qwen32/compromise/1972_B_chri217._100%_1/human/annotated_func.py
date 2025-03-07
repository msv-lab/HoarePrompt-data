#State of the program right berfore the function call: n is a positive integer representing the number of coins, and s is a string of length n consisting only of the characters "U" and "D".
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: `n` is the number of coins from the last test case, `s` is the string "U" and "D" from the last test case, `t` is the integer read from the standard input, `cases` is a list of tuples where each tuple contains the number of coins and the corresponding string for each test case.
    return cases
    #The program returns `cases`, which is a list of tuples where each tuple contains the number of coins and the corresponding string for each test case.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a positive integer `n` and a string `s` of length `n` containing only "U" and "D". It returns a list of tuples, with each tuple containing the integer `n` and the string `s` for each test case.

#State of the program right berfore the function call: case is a tuple where the first element is an integer n (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string of length n containing only "U" and "D".
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the count of 'U' characters in the string `case[1]` is odd, otherwise it returns 'NO'.
#Overall this is what the function does:The function accepts a tuple `case` where the first element is an integer `n` (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string of length `n` containing only "U" and "D". It returns 'YES' if the count of 'U' characters in the string is odd; otherwise, it returns 'NO'.

