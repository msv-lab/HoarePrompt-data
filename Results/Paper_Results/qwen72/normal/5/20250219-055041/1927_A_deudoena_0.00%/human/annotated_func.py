#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' or 'B', with at least one 'B' character.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 10, `s` is a string of length n consisting of characters 'W' or 'B', with at least one 'B' character, `inpstr` is a string, `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is 0, `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 10, `s` is a string of length n consisting of characters 'W' or 'B', with at least one 'B' character, `inpstr` is a string, `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is the index of the last occurrence of 'B' in `inpstr` if 'B' is found, otherwise `ind2` remains 0, `outind` is 0, `i` is the index of the last character in `inpstr` if 'B' is not found, otherwise it is the index of the last occurrence of 'B' in `inpstr`.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) - ind2 - ind1 (where ind1 is the index of the first 'B' in inpstr, ind2 is the index of the last 'B' in inpstr if 'B' is found, otherwise ind2 is 0, and len(inpstr) is the length of the string inpstr)
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads a string `inpstr` from user input, which is expected to contain characters 'W' or 'B' and at least one 'B' character. After processing, it prints the difference between the length of the string and the sum of the indices of the first and last occurrences of 'B' in the string. If 'B' is not found in the string, the function will print the length of the string minus the index of the first occurrence of 'B'.

