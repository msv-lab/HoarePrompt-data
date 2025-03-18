#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 100. Each test case consists of two lines: the first line contains an integer n (1 ≤ n ≤ 100) representing the number of coins, and the second line contains a string s of length n consisting of "U" and "D" representing the orientation of the coins (facing up or down).
def func_1():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: `cases` is a list containing `t` tuples, where each tuple consists of an integer `n` and a string `s`. Each tuple represents a pair of an input integer and the next line of input from stdin with leading and trailing whitespace removed, for a total of `t` such pairs.
    return cases
    #The program returns a list containing `t` tuples, where each tuple consists of an integer `n` and a string `s`. Each tuple represents a pair of an input integer and the next line of input from stdin with leading and trailing whitespace removed, for a total of `t` such pairs.
#Overall this is what the function does:The function reads `t` pairs of inputs from standard input, where each pair consists of an integer `n` and a string `s`. It processes these inputs, removing any leading or trailing whitespace from the string `s`, and stores them as tuples. Finally, it returns a list containing `t` such tuples.

#State of the program right berfore the function call: case is a list where the first element is an integer n (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string s of length n containing only "U" and "D", where "U" represents a coin facing up and "D" represents a coin facing down.
def func_2(case):
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #'YES' if the count of 'U' in the string s is even, otherwise 'NO'
#Overall this is what the function does:The function accepts a list `case` where the first element is an integer `n` (1 ≤ n ≤ 100) representing the number of coins, and the second element is a string `s` of length `n` containing only "U" and "D". It counts the number of "U" characters in the string `s`. If the count of "U" is even, it returns 'YES'; otherwise, it returns 'NO'.

