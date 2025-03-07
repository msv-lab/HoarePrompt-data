#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples test_cases, where each tuple contains an integer n (1 ≤ n ≤ 10) and a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `ind1` is the index of the first 'B' character in `inpstr`, `ind2` is 0, `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: `ind1` is the index of the first 'B' character in `inpstr`, `ind2` is the index of the last 'B' character in `inpstr` when counting from the end, `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: - Since the exact value of `inpstr` is not provided, we can't compute the exact numerical value of `len(inpstr) - ind2 - ind1`. However, based on the given information, the print statement will output the result of this calculation.
    #
    #Output:
#Overall this is what the function does:The function `func` reads a string `inpstr` from user input. It then finds the index of the first 'B' character (`ind1`) and the index of the last 'B' character (`ind2`) in the string. The function prints the difference between the length of the string and the sum of these two indices (`len(inpstr) - ind2 - ind1`). The function does not return any value; it only prints the calculated result.

