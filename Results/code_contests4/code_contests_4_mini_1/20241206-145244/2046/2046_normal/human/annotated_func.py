#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 10^6 and the level string is of length n consisting only of the characters '.' and '*'. The sum of n over all test cases does not exceed 10^6.
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
        
    #State of the program after the  for loop has been executed: `le` is a list with at least one element remaining after all iterations; `af` is a list containing the sums of absolute differences for each processed line based on the median of the transformed list `l`, and its length corresponds to the last element popped from `le`. If no '*' characters were found in any `l`, `af` will contain only zeros for those iterations.
    print('\n'.join(map(str, af)))
#Overall this is what the function does:The function processes multiple test cases where each test case consists of a level string made of characters '.' and '*'. For each level string, it identifies the positions of '*' characters, calculates the absolute differences of these positions from their median, and sums these differences. If no '*' characters are found in a level string, the function appends 0 for that test case. Finally, it prints the sum of absolute differences for each test case. The function processes up to 10,000 test cases with the combined length of the level strings not exceeding 1,000,000 characters.

