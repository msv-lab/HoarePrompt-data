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
        
    #State: countA is between 0 and 5, countB is between 0 and 5, and their sum is 5.
    if (countA > countB) :
        print('A')
        #This is printed: 'A'
    else :
        if (countB > countA) :
            print('B')
            #This is printed: B
        else :
            pass
        #State: countA is between 0 and 5, countB is between 0 and 5, and their sum is 5. Regardless of whether countB is greater than countA or not, the conditions hold true.
    #State: `countA` is between 0 and 5, `countB` is between 0 and 5, and their sum is 5. Regardless of whether `countA` is greater than `countB` or not, the conditions hold true.
#Overall this is what the function does:The function accepts a string `userString` of length 5 consisting of the characters 'A' and 'B'. It counts the occurrences of 'A' and 'B' in the string. Based on the counts, it prints either 'A' or 'B' and returns nothing. If the string contains any characters other than 'A' and 'B', it prints nothing and returns nothing. The final state of the program ensures that `countA` and `countB` are both between 0 and 5, and their sum is always 5.

