#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200000) representing the number of employees, and a string of length n consisting of characters 'D' and 'R' where 'D' represents depublicans and 'R' represents remocrats.
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
        
    #State of the program after the  for loop has been executed: `depublicans` is the count of 'D' in `fractions`, `remocrats` is the count of 'R' in `fractions`, `fractions` is a non-empty string of 'D' and 'R'.
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *`depublicans` is the count of 'D' in `fractions`, `remocrats` is the count of 'R' in `fractions`, and `fractions` is a non-empty string of 'D' and 'R'. If `depublicans` is greater than `remocrats`, then the condition holds true, otherwise, `depublicans` is less than or equal to `remocrats`.
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 200000) and a string `fractions` of length `n` consisting of characters 'D' (depublicans) and 'R' (remocrats). It counts the occurrences of 'D' and 'R' in the string and prints 'D' if depublicans outnumber remocrats; otherwise, it prints 'R'. Note that if both counts are equal, it will still print 'R', which may not be clearly stated in the annotations.

