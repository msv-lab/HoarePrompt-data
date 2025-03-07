#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 10) representing the length of the strip, followed by a string s of length n consisting of characters 'W' or 'B', where 'W' denotes a white cell and 'B' denotes a black cell. It is guaranteed that at least one cell in each test case is black.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `inpstr` is a string containing the integer `t`, `i` is `len(inpstr) - 1`, `j` is the last character of `inpstr`, `ind1` is 0, `ind2` is 0, `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: `inpstr` is a string containing the integer `t`, `i` is `len(inpstr) - 1`, `j` is the last character of `inpstr`, `ind1` is 0, `ind2` is 0, `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: the length of the string representation of the integer `t`
#Overall this is what the function does:The function reads an input string representing multiple test cases. For each test case, it calculates and prints the length of the strip minus the sum of the positions of the first and last black cells ('B') in the strip.

