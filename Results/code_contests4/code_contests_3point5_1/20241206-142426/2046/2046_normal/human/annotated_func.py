#State of the program right berfore the function call: t is a positive integer. For each test case, n is a positive integer and the string contains only '.' and '*' characters.**
def func():
    le = sys.__stdin__.read().split('\n')[::-1]
    af = []
    for zorg in range(int(le.pop())):
        n = int(le.pop())
        
        l = le.pop()
        
        l = [k for k in range(n) if l[k] == '*']
        
        l = [(b - a) for a, b in enumerate(l)]
        
        if l:
            med = l[len(l) // 2]
            af.append(sum(abs(k - med) for k in l))
        else:
            af.append(0)
        
    #State of the program after the  for loop has been executed: `af` is a list containing the sum of absolute differences for each iteration, `n` is an integer, `l` is a list with absolute differences and indices, `le` is empty
    print('\n'.join(map(str, af)))
#Overall this is what the function does:The function `func` reads input from the standard input, processes each test case to calculate the sum of absolute differences between positions of '*' characters in a string, and prints the result for each test case. It assumes a positive integer `t` representing the number of test cases. For each test case, a positive integer `n` denotes the length of the string, which contains only '.' and '*' characters. The function does not explicitly return a value but outputs the calculated sum for each test case.

