#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where 'W' represents a white cell and 'B' represents a black cell, and it is guaranteed that at least one cell in s is black.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: Output State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `t` is an integer such that 1 ≤ t ≤ 10^4, `inpstr` is the input string which is a string of length n consisting of characters 'W' and 'B', `ind2` is 0, `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: Output State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `t` is an integer such that 1 ≤ t ≤ 10^4, `inpstr` is the input string which is a string of length n consisting of characters 'W' and 'B', `ind2` is the index of the last occurrence of 'B' in `inpstr`, `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: n - ind2 - ind1
#Overall this is what the function does:The function processes an input string `inpstr` containing characters 'W' and 'B', identifying the indices of the first and last occurrences of 'B'. It then calculates and prints the length of the string minus these two indices, effectively returning the length of the substring between the first and last 'B' (if they exist). If no 'B' is found, the output will be the length of the string.

