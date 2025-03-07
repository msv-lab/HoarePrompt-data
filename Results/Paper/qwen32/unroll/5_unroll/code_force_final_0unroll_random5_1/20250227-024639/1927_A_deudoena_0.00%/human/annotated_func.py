#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' or 'B', with at least one 'B' in s.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 10; `s` is a string of length `n` consisting of characters 'W' or 'B', with at least one 'B' in `s`; `inpstr` is assigned the value of the input string; `ind1` is the index of the first 'B' in `s`; `ind2` is 0; `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: t is an integer such that 1 <= t <= 10^4; n is an integer such that 1 <= n <= 10; s is a string of length n consisting of characters 'W' or 'B', with at least one 'B' in s; inpstr is assigned the value of the input string; ind1 is the index of the first 'B' in s; ind2 is the index of the last 'B' in s from the end of the string; outind is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: 
#Overall this is what the function does:The function reads a string consisting of characters 'W' and 'B', finds the index of the first 'B' and the last 'B' in the string, and prints the length of the string minus the sum of these two indices.

