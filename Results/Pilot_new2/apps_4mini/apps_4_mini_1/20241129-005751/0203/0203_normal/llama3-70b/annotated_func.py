#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), and the second input line is a string of length n consisting of characters 'D' and 'R', where 'D' represents an employee from the depublicans faction and 'R' represents an employee from the remocrats faction.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 200,000), `fractions` is a non-empty string, `depublicans` is the count of 'D' characters in `fractions`, `remocrats` is the count of characters in `fractions` that are not 'D', and the length of `fractions` is equal to `n`.
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *`n` is a positive integer (1 ≤ n ≤ 200,000), `fractions` is a non-empty string, `depublicans` is the count of 'D' characters in `fractions`, `remocrats` is the count of characters in `fractions` that are not 'D', and the length of `fractions` is equal to `n`. If `depublicans` is greater than `remocrats`, then 'D' has been printed; otherwise, 'D' has not been printed.
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 200,000) and a string `fractions` of length `n` consisting of characters 'D' and 'R'. It counts the occurrences of 'D' and 'R' in the string, and prints 'D' if there are more 'D' characters than 'R' characters; otherwise, it prints 'R'. The function does not return any value; it solely prints the result based on the counts.

