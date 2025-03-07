#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B'.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: Output State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is 0, `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: Output State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is the index of the last occurrence of 'B' in `inpstr` from the end, `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) - ind2 - ind1
#Overall this is what the function does:The function processes an input string `s` containing characters 'W' and 'B', where at least one character is 'B'. It finds the index of the first occurrence of 'B' (`ind1`) and the index of the last occurrence of 'B' from the end (`ind2`). Finally, it prints and returns the length of the string minus these two indices (`len(inpstr) - ind2 - ind1`).

