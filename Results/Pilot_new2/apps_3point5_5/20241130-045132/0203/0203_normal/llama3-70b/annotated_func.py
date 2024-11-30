#State of the program right berfore the function call: n is a positive integer representing the number of employees, and the list of characters contains only 'D' and 'R' representing depublicans and remocrats respectively.**
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
        
    #State of the program after the  for loop has been executed: n is a positive integer representing the number of employees, fractions contains the input string of fractions representing the political affiliations of the employees. depublicans contains the count of employees with political affiliation as 'D' and remocrats contains the count of employees with political affiliation as 'R'.
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *n is a positive integer representing the number of employees, fractions contains the input string of fractions representing the political affiliations of the employees, depublicans contains the count of employees with political affiliation as 'D', and remocrats contains the count of employees with political affiliation as 'R'. If the count of depublicans is higher than the count of remocrats, 'D' is printed to the console. Otherwise, 'R' is printed.
#Overall this is what the function does:The function accepts user input for the number of employees and their political affiliations ('D' for depublicans and 'R' for remocrats). It then calculates the count of each political affiliation and prints 'D' if there are more depublicans than remocrats, and 'R' otherwise. The function does not have any return value.

