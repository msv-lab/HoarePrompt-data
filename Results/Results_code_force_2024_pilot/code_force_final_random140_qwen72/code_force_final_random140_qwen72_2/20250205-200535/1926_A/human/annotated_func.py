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
        
    #State: `userString` is a string of length 5 consisting of letters 'A' and 'B', `list(userString)` is a list of 5 elements, each element being one of the letters from `userString`, `countA` is the number of 'A's in `userString`, and `countB` is the number of 'B's in `userString`.
    if (countA > countB) :
        print('A')
        #This is printed: A
    else :
        if (countB > countA) :
            print('B')
            #This is printed: B
        else :
            pass
        #State: *`userString` is a string of length 5 consisting of letters 'A' and 'B', `list(userString)` is a list of 5 elements, each element being one of the letters from `userString`, `countA` is the number of 'A's in `userString`, and `countB` is the number of 'B's in `userString`. Additionally, `countA` is less than or equal to `countB`. If `countB` is greater than `countA`, the condition `countB > countA` holds true. If `countB` is equal to `countA`, the condition `countB == countA` holds true.
    #State: *`userString` is a string of length 5 consisting of letters 'A' and 'B', `list(userString)` is a list of 5 elements, each element being one of the letters from `userString`, `countA` is the number of 'A's in `userString`, and `countB` is the number of 'B's in `userString`. If `countA` is greater than `countB`, the condition `countA > countB` holds true. If `countA` is less than or equal to `countB`, the condition `countA <= countB` holds true. Specifically, if `countB` is greater than `countA`, the condition `countB > countA` holds true. If `countB` is equal to `countA`, the condition `countB == countA` holds true.
#Overall this is what the function does:The function `func_1` takes a string `userString` of length 5, which consists only of the characters 'A' and 'B'. It counts the occurrences of 'A' and 'B' in `userString`. If there are more 'A's than 'B's, it prints 'A'. If there are more 'B's than 'A's, it prints 'B'. If the counts of 'A' and 'B' are equal, it does nothing. The function does not return any value. After the function completes, `userString` remains unchanged, and the counts of 'A' and 'B' are stored in `countA` and `countB` respectively.

