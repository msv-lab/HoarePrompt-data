#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' and 'B', with at least one 'B'.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is 0, `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: Output State: `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is the index of the last occurrence of 'B' in `inpstr` when counting from the end, `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: - The print statement will output the result of the expression `len(inpstr) - ind2 - ind1`.
    #
    #Output:
#Overall this is what the function does:The function `func` reads a string `inpstr` from the user input. It then finds the index of the first occurrence of 'B' in `inpstr` (from the beginning) and the index of the last occurrence of 'B' in `inpstr` (from the end). The function prints the difference between the length of `inpstr` and the sum of these two indices. The function does not return any value.

