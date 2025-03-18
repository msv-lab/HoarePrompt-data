#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of the characters 'A' and 'B'.
def func():
    t = int(input())
    for q in range(t):
        ac = 0
        
        bc = 0
        
        s = input()
        
        for i in s:
            if i == 'A':
                ac += 1
            else:
                bc += 1
        
    #State: Output State: `t` is an integer between 1 and 32, `ac` is the total number of 'A's across all strings `s` entered, `bc` is the total number of characters that are not 'A' across all strings `s` entered.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: 'B'
    #State: Postcondition: `t` is an integer between 1 and 32, `ac` is the total number of 'A's across all strings `s` entered, `bc` is the total number of characters that are not 'A' across all strings `s` entered. If the number of 'A's (`ac`) is greater than the number of non-'A' characters (`bc`), then the condition remains as is. Otherwise, `ac` is less than or equal to `bc`.
#Overall this is what the function does:The function processes up to 32 input strings, each of length 5 containing only 'A' and 'B'. It counts the total number of 'A's and 'B's across all strings. Based on whether the count of 'A's is greater than the count of 'B's, it prints 'A' or 'B'. The function does not return any value but prints the result directly.

