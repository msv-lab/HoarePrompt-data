#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), and the second input line is a string of length n consisting of characters 'D' and 'R' representing the fractions of the employees.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 200,000), `fractions` is a string of length `n`, `depublicans` is the count of 'D' characters in `fractions`, `remocrats` is the count of characters in `fractions` that are not 'D'.
    if (depublicans > remocrats) :
        print('D')
    else :
        print('R')
    #State of the program after the if-else block has been executed: *`n` is a positive integer (1 ≤ n ≤ 200,000), `fractions` is a string of length `n`, if the count of 'D' characters (`depublicans`) is greater than the count of characters that are not 'D' (`remocrats`), then 'D' has been printed. Otherwise, the count of 'D' characters is less than or equal to the count of characters that are not 'D'.
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 200,000) and a string `fractions` of length `n` consisting of characters 'D' and 'R'. It counts the occurrences of 'D' and 'R' in the string and prints 'D' if there are more 'D's than 'R's; otherwise, it prints 'R'. The function does not handle cases where `n` is 0 or where the input does not strictly consist of 'D' and 'R' characters, which could lead to incorrect behavior.

