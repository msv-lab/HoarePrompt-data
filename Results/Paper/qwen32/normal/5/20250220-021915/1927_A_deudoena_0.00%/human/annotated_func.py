#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' or 'B', with at least one 'B' in the string.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `ind1` is the index of the first 'B' in `inpstr`, `ind2` is 0, `outind` is 0, `n` is the length of `s`, `s` is the original string, `t` is the length of `inpstr`.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: `ind1` is the index of the first 'B' in `inpstr`, `ind2` is the index of the first 'B' from the end of `inpstr` if a 'B' is found, otherwise `ind2` is 0, `outind` is 0, `n` is the length of `s`, `s` is the original string, `t` is the length of `inpstr`.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) + 1 if no 'B' is found in inpstr, otherwise the number of characters between the first 'B' from the start and the first 'B' from the end, inclusive (where ind1 is the index of the first 'B' from the start and ind2 is the index of the first 'B' from the end)
#Overall this is what the function does:The function reads a string `inpstr` consisting of characters 'W' and 'B', with at least one 'B'. It calculates and prints the number of characters between the first 'B' from the start and the first 'B' from the end of the string, inclusive. If no 'B' is found (which is not possible as per the problem statement), it would print `len(inpstr) + 1`.

