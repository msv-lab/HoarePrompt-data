#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000) representing the number of employees, and a string of length n consisting only of the characters 'D' and 'R', where 'D' indicates an employee belongs to the depublicans fraction and 'R' indicates an employee belongs to the remocrats fraction.
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
        
    #State of the program after the  for loop has been executed: `depublicans` is the count of 'D' in `fractions`, `remocrats` is the count of 'R' in `fractions`, and `depublicans` + `remocrats` equals `n`.
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *`depublicans` is the count of 'D' in `fractions`, `remocrats` is the count of 'R' in `fractions`, and `depublicans` + `remocrats` equals `n`. If `depublicans` is greater than `remocrats`, 'D' is printed. Otherwise, if `remocrats` is greater than or equal to `depublicans`, 'R' is printed.
#Overall this is what the function does:The function accepts an implicit positive integer `n` (1 ≤ n ≤ 200,000) representing the number of employees and a string `fractions` of length `n` consisting only of the characters 'D' and 'R'. It counts the occurrences of 'D' and 'R' in `fractions`, and prints 'D' if there are more 'D's than 'R's; otherwise, it prints 'R'. There are no return values and the function relies on user input for both `n` and `fractions`.

