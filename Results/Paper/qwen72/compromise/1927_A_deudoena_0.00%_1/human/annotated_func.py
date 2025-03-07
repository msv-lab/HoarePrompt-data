#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples where each tuple contains an integer n (1 ≤ n ≤ 10) and a string s of length n consisting of 'W' and 'B', with at least one 'B'.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `ind2` is 0, `ind1` is the index of the first occurrence of 'B' in `inpstr`, `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: Output State: `ind2` is the index of the last occurrence of 'B' in `inpstr` (counting from the end, starting from 0), `ind1` is the index of the first occurrence of 'B' in `inpstr`, `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) - ind2 - ind1 (where len(inpstr) is the length of the string inpstr, ind1 is the index of the first 'B' in inpstr, and ind2 is the index of the last 'B' in inpstr)
#Overall this is what the function does:The function `func` reads a string `inpstr` from the user input, finds the index of the first occurrence of 'B' (`ind1`) and the index of the last occurrence of 'B' (`ind2`), and prints the difference between the length of the string and the sum of these indices (`len(inpstr) - ind2 - ind1`). The function does not return any value and does not modify any external state.

