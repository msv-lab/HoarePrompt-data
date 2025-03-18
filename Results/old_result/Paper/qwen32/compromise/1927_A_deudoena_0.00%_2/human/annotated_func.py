#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 10) representing the length of the strip, followed by a string s of length n consisting of characters 'W' and 'B', where 'W' denotes a white cell and 'B' denotes a black cell. It is guaranteed that at least one cell in the strip is black.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `inpstr` is a string containing the first line of the input, which is the integer `t` representing the number of test cases; `ind1` is the index of the first 'B' in `inpstr` or 0 if 'B' is not present; `ind2` is 0; `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: `inpstr` is a string containing the first line of the input, which is the integer `t` representing the number of test cases; `ind1` is the index of the first 'B' in `inpstr` or 0 if 'B' is not present; `ind2` is the index of the last 'B' in `inpstr` from the end or 0 if 'B' is not present; `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: length of `inpstr` (where `inpstr` is the string representation of the integer `t`)
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting of 'W' and 'B'. It then calculates and prints the length of the string `s` minus the sum of the index of the first 'B' from the start and the index of the last 'B' from the end. However, the provided annotations and comments do not accurately describe the intended functionality, as the function seems to be incorrectly processing the input and does not handle multiple test cases as described.

