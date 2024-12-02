#State of the program right berfore the function call: n is a positive integer representing the number of employees. The input characters represent the fractions of employees, where 'D' represents depublicans and 'R' represents remocrats.**
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
        
    #State of the program after the  for loop has been executed: n is a positive integer representing the number of employees; fractions is a string that contains at least one fraction. depublicans contains the count of 'D' fractions in the string, remocrats contains the count of fractions that are not 'D'.
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *n is a positive integer representing the number of employees; fractions is a string that contains at least one fraction. depublicans contains the count of 'D' fractions in the string, remocrats contains the count of fractions that are not 'D'. If depublicans is greater than remocrats, the code prints 'D'. If depublicans is less than or equal to remocrats, the code prints 'R'.
#Overall this is what the function does:The function `func` takes input from the user: a positive integer `n` representing the number of employees and a string of characters representing fractions of employees (where 'D' represents depublicans and 'R' represents remocrats). It then calculates the count of 'D' and 'R' fractions. After that, it determines the majority political party among the employees based on the counts. If the count of 'D' fractions is greater than the count of 'R' fractions, it prints 'D'; otherwise, it prints 'R'.

