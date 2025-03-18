#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' and 'B', with at least one 'B' present in s.
def func():
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: - `ind1` will be the index of the first 'B' in `inpstr`.
    #- `ind2` remains 0.
    #- `outind` remains 0.
    #- `i` and `j` will be the last checked index and character, but they are not relevant to the final output state as the loop breaks immediately upon finding 'B'.
    #
    #Output State:
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: `ind1` is the index of the first 'B' in `inpstr`, `ind2` is the index of the first 'B' from the end of `inpstr`, and `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: number of characters between the first 'B' from the start and the first 'B' from the end, excluding these two 'B's (where ind1 is the index of the first 'B' from the start and ind2 is the index of the first 'B' from the end)
#Overall this is what the function does:The function reads a string `s` consisting of characters 'W' and 'B', finds the first 'B' from the start and the first 'B' from the end, and prints the number of characters between these two 'B's, excluding the 'B's themselves.

