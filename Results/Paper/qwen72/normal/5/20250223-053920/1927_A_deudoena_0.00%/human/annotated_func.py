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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 10, `s` is a string of length n consisting of characters 'W' or 'B', with at least one 'B' character, `inpstr` is the input string provided by the user, `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is 0, `outind` is 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: Output State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 10, `s` is a string of length n consisting of characters 'W' or 'B', with at least one 'B' character, `inpstr` is the input string provided by the user, `ind1` is the index of the first occurrence of 'B' in `inpstr`, `ind2` is the index of the last occurrence of 'B' in `inpstr` (counting from the end of the string), `outind` is 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: 1
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an input string from the user, which is expected to be a string of length `n` (1 <= n <= 10) consisting of characters 'W' or 'B', with at least one 'B' character. The function calculates the difference between the length of the input string and the sum of the indices of the first and last occurrences of 'B' in the string (with the last occurrence index counted from the end of the string). It then prints this calculated value. After the function concludes, the input string and the calculated value are no longer accessible outside the function.

