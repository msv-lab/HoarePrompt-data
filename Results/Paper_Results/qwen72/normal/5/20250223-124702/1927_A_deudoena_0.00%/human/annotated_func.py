#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples, each containing an integer n (1 ≤ n ≤ 10) and a string s of length n consisting of 'W' and 'B', where 'W' denotes a white cell and 'B' denotes a black cell, and it is guaranteed that at least one cell in each strip is black.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is 0, `outind` is 0, and `t` remains unchanged.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: Output State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is the index of the last occurrence of 'B' in `inpstr` when counted from the end, `outind` is 0, and `t` remains unchanged.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) - ind2 - ind1 (where `ind1` is the index of the first 'B' in `inpstr`, `ind2` is the index of the last 'B' in `inpstr`, and `len(inpstr)` is the length of the string `inpstr`)
#Overall this is what the function does:The function `func` reads a string `inpstr` from the user input, finds the index of the first occurrence of 'B' (`ind1`) and the index of the last occurrence of 'B' (`ind2`) in the string, and then prints the length of the substring between these two indices, inclusive. The function does not return any value. The parameters `t` and the list of tuples mentioned in the comments are not used in the function.

