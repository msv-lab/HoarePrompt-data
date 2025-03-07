#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, representing the number of test cases.
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: Output State: `t` is the integer value read from the standard input, and 1 <= t <= 100; `cases` is a list containing `t` tuples, where each tuple consists of an integer `n` and a string `s`, both read from the standard input.
    return cases
    #The program returns a list `cases` containing `t` tuples, where each tuple consists of an integer `n` and a string `s`, and `t` is an integer between 1 and 100. Each `n` is an integer, and each `s` is a string, both read from the standard input.
#Overall this is what the function does:The function reads a number of test cases `t` from the standard input, where `t` is an integer between 1 and 100. For each test case, it reads an integer `n` and a string `s` from the standard input. The function returns a list of `t` tuples, where each tuple contains an integer `n` and a string `s`.

#State of the program right berfore the function call: case is a list where case[0] is an integer representing the number of coins (1 ≤ case[0] ≤ 100), and case[1] is a string of length case[0] containing only 'U' and 'D', representing the state of each coin (facing up or facing down).
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the number of 'U' characters in `case[1]` is even, otherwise it returns 'NO'.
#Overall this is what the function does:The function `func_2` accepts a parameter `case`, which is a list where the first element is an integer representing the number of coins (1 ≤ case[0] ≤ 100), and the second element is a string of length case[0] containing only 'U' and 'D', representing the state of each coin (facing up or facing down). The function returns 'YES' if the number of 'U' characters in the string is even, otherwise it returns 'NO'. The function does not modify the input `case` and only evaluates the state of the coins.

