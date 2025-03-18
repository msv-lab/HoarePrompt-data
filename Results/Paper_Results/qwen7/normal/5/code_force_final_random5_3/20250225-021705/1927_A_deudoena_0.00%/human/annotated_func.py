#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character in s is 'B'.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: All iterations of the loop have been executed. `ind1` is the index of the first occurrence of 'B' in `inpstr`, or it remains 0 if no 'B' is found. The value of `i` is equal to the length of `inpstr` if the loop completes without finding a 'B'. The other variables (`j`, `t`, `n`, `s`, `ind2`, `inpstr`, `outind`) remain in their initial or unchanged states.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: `i` is 3, `ind2` is 1.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) - 1 - ind1 (where len(inpstr) is the length of the string inpstr and ind1 is undefined)
#Overall this is what the function does:The function processes a string `inpstr` containing characters 'W' and 'B', and calculates and prints the difference between the length of the string and the sum of the indices of the first and last occurrences of 'B' in the string. If no 'B' is found, `ind1` remains 0. The function does not return any value but prints the calculated result.

