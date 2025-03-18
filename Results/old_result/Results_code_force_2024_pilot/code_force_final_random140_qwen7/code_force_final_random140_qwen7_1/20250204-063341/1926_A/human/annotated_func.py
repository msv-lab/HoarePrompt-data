#State of the program right berfore the function call: userString is a string of length 5 consisting of the characters 'A' and 'B'.
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
        
    #State: After the loop executes all the iterations, `userString` is a string of length 5 consisting of the characters 'A' and 'B'. `countA` is the total number of 'A's in `userString`, and `countB` is the total number of 'B's in `userString`.
    if (countA > countB) :
        print('A')
        #This is printed: A
    else :
        if (countB > countA) :
            print('B')
            #This is printed: B
        else :
            pass
        #State: Postcondition: `userString` is a string of length 5 consisting of the characters 'A' and 'B', `countA` is the total number of 'A's in `userString`, and `countB` is the total number of 'B's in `userString`. After executing the if-else block, the number of 'B's (`countB`) is greater than or equal to the number of 'A's (`countA`).
    #State: Postcondition: `userString` is a string of length 5 consisting of the characters 'A' and 'B', `countA` is the total number of 'A's in `userString`, and `countB` is the total number of 'B's in `userString`. After executing the if-else block, either `countA` is greater than `countB` or `countB` is greater than or equal to `countA`.
#Overall this is what the function does:The function `func_1` accepts a string `userString` of length 5 consisting of the characters 'A' and 'B'. It counts the occurrences of 'A' and 'B' in the string. Based on the count, it prints 'A' if there are more 'A's, 'B' if there are more 'B's, and does nothing if the counts are equal. The function does not return anything; instead, it prints the result directly.

