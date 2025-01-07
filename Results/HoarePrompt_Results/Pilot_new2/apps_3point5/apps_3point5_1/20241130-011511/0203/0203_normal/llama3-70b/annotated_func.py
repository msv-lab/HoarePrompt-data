#State of the program right berfore the function call: n is a positive integer representing the number of employees. The input characters are either 'D' or 'R'.**
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
        
    #State of the program after the  for loop has been executed: n is a positive integer representing the number of employees; fractions is a non-empty list of characters 'D' or 'R'; depublicans is the number of 'D's in the list fractions, remocrats is the number of 'R's in the list fractions
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *n is a positive integer representing the number of employees; fractions is a non-empty list of characters 'D' or 'R'; depublicans is the number of 'D's in the list fractions; remocrats is the number of 'R's in the list fractions. If depublicans is greater than remocrats, 'D' is printed on the screen. Otherwise, 'R' is printed on the screen.
#Overall this is what the function does:The function `func` reads a positive integer `n` representing the number of employees and a string of characters 'D' or 'R'. It then counts the occurrences of 'D' and 'R' in the input string, compares them, and prints 'D' if the count of 'D' is greater than 'R', otherwise it prints 'R'. The function does not explicitly return a value.

