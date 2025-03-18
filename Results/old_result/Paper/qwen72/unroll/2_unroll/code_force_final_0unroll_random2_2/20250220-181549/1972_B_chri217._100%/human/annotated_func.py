#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and each (n, s) in cases is a tuple where n is an integer such that 1 <= n <= 100 and s is a string of length n containing only "U" and "D".
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: Output State: `t` remains the same as the initial input integer value, `cases` is a list containing `t` tuples, where each tuple consists of an integer `n` and a string `s` read from the input.
    return cases
    #The program returns the list `cases` which contains `t` tuples, where each tuple consists of an integer `n` and a string `s` read from the input.
#Overall this is what the function does:The function reads from standard input a series of test cases, each consisting of an integer `n` and a string `s` of length `n` containing only "U" and "D". It returns a list of `t` tuples, where `t` is the number of test cases provided, and each tuple contains the integer `n` and the corresponding string `s`. The state of the program after the function concludes is that the integer `t` and the list `cases` are as read from the input, with `cases` being the returned value.

#State of the program right berfore the function call: case is a list where case[1] is a string of length n (1 ≤ n ≤ 100) consisting of 'U' and 'D' characters, representing the state of the coins.
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the number of 'U' characters in `case[1]` is even, otherwise it returns 'NO'
#Overall this is what the function does:The function `func_2` accepts a list `case` where `case[1]` is a string consisting of 'U' and 'D' characters. It returns 'YES' if the number of 'U' characters in `case[1]` is even, and 'NO' if the number of 'U' characters is odd. The function does not modify the input list `case`.

