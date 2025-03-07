#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n is an integer such that 1 ≤ n ≤ 100, and s is a string of length n consisting of only "U" and "D".
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: Output State: `cases` is a list containing `t` tuples. Each tuple contains an integer `n` (where 1 ≤ n ≤ 100) and a string `s` of length `n` consisting of only "U" and "D".
    return cases
    #The program returns a list named 'cases' containing 't' tuples. Each tuple contains an integer 'n' (where 1 ≤ n ≤ 100) and a string 's' of length 'n' consisting of only "U" and "D".
#Overall this is what the function does:The function reads multiple test cases from standard input. Each test case consists of an integer \( n \) (where 1 ≤ \( n \) ≤ 100) and a string \( s \) of length \( n \) made up of characters "U" and "D". It then constructs a list of tuples, where each tuple contains the integer \( n \) and the string \( s \) from each test case. Finally, it returns this list of tuples.

#State of the program right berfore the function call: case is a list of length 2, where the first element is an integer n (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string s of length n containing only "U" and "D", representing the initial state of the coins (facing up or down).
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #'YES' if the count of 'U' in the string `case[1]` is odd, otherwise 'NO'
#Overall this is what the function does:The function accepts a list `case` containing two elements: an integer `n` (1 ≤ n ≤ 100) and a string `s` of length `n` consisting of "U" and "D". It counts the number of "U" characters in the string `s`. If the count of "U" is odd, it returns 'YES'; otherwise, it returns 'NO'.

