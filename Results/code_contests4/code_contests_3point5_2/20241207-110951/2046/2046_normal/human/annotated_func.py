#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n (1 ≤ n ≤ 10^6) and a string of length n containing '.' and '*'.**
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
        
    #State of the program after the  for loop has been executed: If the loop executes, `af` contains [0]. If the loop does not execute, `af` remains an empty list.
    print('\n'.join(map(str, af)))
#Overall this is what the function does:The function `func` reads input from the standard input, processes each test case consisting of an integer `n` and a string of length `n` containing '*' and '.', calculates the distance between consecutive '*' characters, finds the median distance, and computes the sum of absolute differences between each distance and the median. The function then prints the resulting sums for each test case. The function does not explicitly return a value.

