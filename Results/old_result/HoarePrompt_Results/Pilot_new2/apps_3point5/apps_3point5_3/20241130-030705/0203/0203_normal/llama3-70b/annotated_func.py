#State of the program right berfore the function call: n is a positive integer representing the number of employees. The input characters represent the fractions of the employees, where 'D' stands for depublicans and 'R' stands for remocrats.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `fractions` is a string with at least one fraction, `republicans` is the count of 'D' fractions, `remocrats` is the count of non-'D' fractions. If all fractions are 'D', `republicans` will be equal to the total number of fractions. If all fractions are not 'D', `remocrats` will be equal to the total number of fractions.
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `fractions` is a string with at least one fraction, `republicans` is the count of 'D' fractions, `remocrats` is the count of non-'D' fractions. If all fractions are 'D', `republicans` will be equal to the total number of fractions. If all fractions are not 'D', `remocrats` will be equal to the total number of fractions. If republicans > remocrats, the code snippet prints 'D' but does not affect any variables. If (republicans <= remocrats), the program variables remain unchanged and the code prints 'R'.
#Overall this is what the function does:Functionality: The function does not accept any parameters. It reads an integer `n` representing the number of employees and a string `fractions` representing the political affiliations of the employees as 'D' for depublicans and 'R' for remocrats. It then counts the number of depublicans and remocrats in the fractions. After that, it determines which political party has the majority based on the counts. If depublicans outnumber remocrats, it prints 'D'. If remocrats outnumber depublicans or if the counts are equal, it prints 'R'. This function does not handle the case where the counts are equal and does not print 'tie' as mentioned in the annotations.

