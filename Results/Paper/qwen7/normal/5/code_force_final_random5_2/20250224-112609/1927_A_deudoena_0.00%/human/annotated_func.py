#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where 'W' represents a white cell and 'B' represents a black cell, and it is guaranteed that at least one cell is black.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: The loop has executed fully, and `ind1` is set to the index of the first occurrence of 'B' in `inpstr`, or remains 0 if 'B' does not appear in `inpstr`. The value of `i` is equal to the length of `inpstr`, `j` is the last character of `inpstr`, and `outind` remains 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: The loop has executed fully, and `ind2` is the index of the first occurrence of 'B' from the end of `inpstr`. If 'B' does not appear in `inpstr`, `ind2` remains 0. The value of `i` is `len(inpstr)`, `j` is the last character of `inpstr`, and `outind` remains 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) - ind2
#Overall this is what the function does:The function processes a single string `inpstr` containing only 'W' and 'B' characters. It finds the indices of the first and last occurrences of 'B' in the string. If 'B' is not found, both indices are considered 0. The function then prints the length of the string minus the sum of these two indices.

