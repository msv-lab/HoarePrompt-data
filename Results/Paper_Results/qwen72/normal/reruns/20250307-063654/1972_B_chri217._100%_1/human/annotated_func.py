#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, and each (n, s) in cases is a tuple where n is a positive integer such that 1 <= n <= 100, and s is a string of length n containing only "U" and "D".
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: `t` must be greater than or equal to the number of iterations, `_` is `t-1`, `cases` is a list containing `t` tuples, each tuple `(n, s)` where `n` is an input integer and `s` is a string read from the standard input and stripped of leading and trailing whitespace.
    return cases
    #The program returns the list `cases` which contains `t` tuples, where each tuple consists of an integer `n` and a string `s` that has been stripped of leading and trailing whitespace.
#Overall this is what the function does:The function reads a positive integer `t` from the standard input, where `1 <= t <= 100`. It then reads `t` pairs of inputs, each consisting of a positive integer `n` (where `1 <= n <= 100`) and a string `s` of length `n` containing only "U" and "D". The function returns a list `cases` containing `t` tuples, where each tuple consists of the integer `n` and the string `s` stripped of leading and trailing whitespace.

#State of the program right berfore the function call: case is a list where the first element is an integer n (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string s of length n containing only "U" and "D" representing the state of each coin (facing up or facing down).
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the number of "U" characters in the string `s` is even, otherwise it returns 'NO'.
#Overall this is what the function does:The function `func_2` accepts a list `case` where the first element is an integer `n` (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string `s` of length `n` containing only "U" and "D" characters. It returns 'YES' if the number of "U" characters in `s` is even, and 'NO' if the number of "U" characters is odd. The function does not modify the input list `case`.

