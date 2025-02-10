#State of the program right berfore the function call: userString is a string of length 5 consisting of letters 'A' and 'B'.
def func_1(userString):
    list(userString)
    countA = 0
    countB = 0
    for letter in userString:
        if letter == 'A':
            countA += 1
        elif letter == 'B':
            countB += 1
        else:
            continue
        
    #State: After the loop executes all the iterations, `userString` remains a string of length 5 consisting of letters 'A' and 'B'. The variable `countA` will be the total number of 'A's in `userString`, and the variable `countB` will be the total number of 'B's in `userString`.
    if (countA > countB) :
        print('A')
        #This is printed: A
    else :
        if (countB > countA) :
            print('B')
            #This is printed: B
        else :
            pass
        #State: *`userString` remains a string of length 5 consisting of letters 'A' and 'B'. The variable `countA` is the total number of 'A's in `userString`, and the variable `countB` is the total number of 'B's in `userString`. Additionally, `countA` is less than or equal to `countB`. If `countB` is greater than `countA`, no changes occur. If `countB` is equal to `countA`, no changes occur.
    #State: *`userString` remains a string of length 5 consisting of letters 'A' and 'B'. The variable `countA` is the total number of 'A's in `userString`, and the variable `countB` is the total number of 'B's in `userString`. If `countA` is greater than `countB`, no changes occur. If `countA` is less than or equal to `countB`, no changes occur.
#Overall this is what the function does:The function `func_1` takes a string `userString` of length 5 consisting only of the characters 'A' and 'B'. It counts the occurrences of 'A' and 'B' in the string. If there are more 'A's than 'B's, it prints 'A'. If there are more 'B's than 'A's, it prints 'B'. If the counts of 'A' and 'B' are equal, it does nothing. The function does not modify `userString` and does not return any value.

