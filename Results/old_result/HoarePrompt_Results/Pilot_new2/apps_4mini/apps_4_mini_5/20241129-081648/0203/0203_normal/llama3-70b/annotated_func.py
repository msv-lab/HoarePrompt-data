#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000, and the second input line is a string of length n consisting of characters 'D' and 'R', where 'D' represents an employee from the depublicans fraction and 'R' represents an employee from the remocrats fraction.
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
        
    #State of the program after the  for loop has been executed: `depublicans` is the count of 'D' characters in `fractions`, `remocrats` is the count of 'R' characters in `fractions`, `fractions` is a string of length `n` consisting of characters 'D' and 'R', and `n` is an integer such that 1 ≤ `n` ≤ 200,000.
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *`depublicans` is the count of 'D' characters in `fractions`, `remocrats` is the count of 'R' characters in `fractions`, and `fractions` is a string of length `n` consisting of characters 'D' and 'R'. If `depublicans` is greater than `remocrats`, then 'D' is printed. Otherwise, if `depublicans` is less than or equal to `remocrats`, 'R' is printed.
#Overall this is what the function does:The function accepts an integer `n` and a string `fractions` of length `n` consisting of characters 'D' and 'R'. It counts the occurrences of 'D' and 'R' in the string. The function prints 'D' if there are more 'D' characters than 'R' characters; otherwise, it prints 'R'. If `n` is outside the specified range (1 ≤ n ≤ 200,000) or if the string contains characters other than 'D' and 'R', the function does not handle these cases, which could lead to incorrect results or runtime errors.

