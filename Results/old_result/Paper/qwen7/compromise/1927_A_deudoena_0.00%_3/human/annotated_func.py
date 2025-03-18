#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B'.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: Output State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is 0, `inpstr` is the string input by the user, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 10, `s` is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B', `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: Output State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is the index of the last occurrence of 'B' in `inpstr`, `inpstr` is the string input by the user, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 10, `s` is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B', `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) - ind2 - ind1 (the number of characters between the first and last 'B' in inpstr, excluding the 'B' characters themselves)
#Overall this is what the function does:The function processes a string `inpstr` containing characters 'W' and 'B', where at least one character is 'B'. It finds the indices of the first and last occurrences of 'B' in the string. After determining these indices (`ind1` and `ind2`), it calculates and prints the number of characters between the first and last 'B' (excluding the 'B' characters themselves). The function does not return any value but modifies and prints the result based on the input string.

