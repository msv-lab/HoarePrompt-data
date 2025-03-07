#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' and 'B', with at least one 'B' present in s.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; for each test case, `n` is an integer such that 1 <= n <= 10, and `s` is a string of length `n` consisting of characters 'W' and 'B', with at least one 'B' present in `s`; `inpstr` is assigned the value of `input()`; `ind1` is the index of the first occurrence of 'B' in `inpstr`; `ind2` is 0; `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; for each test case, `n` is an integer such that 1 <= n <= 10, and `s` is a string of length `n` consisting of characters 'W' and 'B', with at least one 'B' present in `s`; `inpstr` is assigned the value of `input()`; `ind1` is the index of the first occurrence of 'B' in `inpstr`; `ind2` is the index of the first occurrence of 'B' from the end of `inpstr`; `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: Output:
#Overall this is what the function does:The function reads a string `s` consisting of characters 'W' and 'B', with at least one 'B' present, and outputs the minimum number of swaps needed to bring all 'B's together in the string.

