#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10^6; and the corresponding string is of length n, consisting of the characters '.' (empty space) and '*' (sheep). The sum of all n across test cases does not exceed 10^6.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that 1 ≤ `t` ≤ 10^4; `le` is a list with at most `t` less 1 elements; `af` contains the sums of absolute differences from the middle indices of the lists created from the 'n' elements of `le`, or 0 if no '*' was found; `zorg` is equal to the number of iterations executed, which equals the value of the last popped element from `le`.
    print('\n'.join(map(str, af)))
#Overall this is what the function does:The function processes multiple test cases where each test case consists of an integer `n` and a string of length `n` containing characters '.' (representing empty space) and '*' (representing sheep). For each test case, it calculates the sum of the absolute differences from the median position of the indices of the '*' characters in the string. If no '*' characters are present in the string, it records a sum of 0. After processing all test cases, it prints the results.

