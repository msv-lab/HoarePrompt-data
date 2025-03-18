#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where 'W' represents a white cell and 'B' represents a black cell, with at least one 'B' in the string.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: ind1 is the index of the first 'B' in the string inpstr, ind2 is 0, inpstr is a string of length n consisting of characters 'W' and 'B' that must contain at least one 'B', outind is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: ind1 is the index of the first 'B' in the string inpstr, ind2 is the index of the last 'B' in inpstr, inpstr is a string of length n consisting of characters 'W' and 'B' that must contain at least one 'B', outind is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: n - ind2 - ind1
#Overall this is what the function does:The function processes an input string `inpstr` that consists of characters 'W' and 'B', and contains at least one 'B'. It finds the index of the first 'B' (ind1) and the index of the last 'B' (ind2) in the string. After determining these indices, it prints the length of the string minus the sum of these two indices (len(inpstr) - ind1 - ind2). The function does not return any value but prints the calculated result.

