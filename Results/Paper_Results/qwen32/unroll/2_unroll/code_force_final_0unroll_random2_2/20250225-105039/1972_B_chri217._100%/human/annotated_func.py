#State of the program right berfore the function call: n is a positive integer representing the number of coins (1 <= n <= 100), and s is a string of length n consisting only of the characters "U" and "D".
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: `n` is a positive integer representing the number of coins (1 <= n <= 100) from the last iteration, `s` is a string of length n consisting only of the characters "U" and "D" from the last iteration, `t` is the integer read from the standard input, `cases` is a list of tuples where each tuple contains the `n` and `s` values read in each iteration.
    return cases
    #The program returns a list of tuples where each tuple contains the `n` and `s` values read in each iteration. Each `n` is a positive integer representing the number of coins (1 <= n <= 100) and each `s` is a string of length `n` consisting only of the characters "U" and "D".
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a string `s`. The integer `n` represents the number of coins (1 <= n <= 100), and the string `s` is of length `n` and contains only the characters "U" and "D". The function returns a list of tuples, with each tuple containing the `n` and `s` values from each test case.

#State of the program right berfore the function call: case is a tuple or list where the first element is an integer n (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string of length n containing only "U" and "D" representing the state of each coin (facing up or facing down).
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the count of 'U' characters in the string `case[1]` is even, otherwise 'NO'
#Overall this is what the function does:The function accepts a parameter `case`, which is a tuple or list consisting of an integer `n` (1 ≤ n ≤ 100) and a string of length `n` containing only "U" and "D". It returns 'YES' if the number of "U" characters in the string is even, and 'NO' if the number of "U" characters is odd.

