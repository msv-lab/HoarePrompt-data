#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200000. The input characters are either 'D' or 'R'.**
def func():
    n = int(input())
    fractions = input()
    depublicans = 0
    remocrats = 0
    for fraction in fractions:
        if fraction == 'D':
            depublicans += 1
        else:
            remocrats += 1
        
    #State of the program after the  for loop has been executed: n is an input integer such that 1 ≤ n ≤ 200000, fractions is a non-empty string. depublicans is the count of 'D' fractions in the string, remocrats is the count of non-'D' fractions in the string
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *n is an input integer such that 1 ≤ n ≤ 200000, fractions is a non-empty string. The count of 'D' fractions in the string is depublicans and the count of non-'D' fractions is remocrats. If depublicans > remocrats, the program prints 'D'. If depublicans is less than or equal to remocrats, the program prints 'R'.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `fractions` composed of characters 'D' or 'R'. It then counts the occurrences of 'D' and 'R' characters in the string. If the count of 'D' is greater than the count of 'R', it prints 'D'. Otherwise, it prints 'R'. The function processes the input character sequence based on the specified constraints. However, the function lacks explicit return values and handles input processing and comparison logic only.

