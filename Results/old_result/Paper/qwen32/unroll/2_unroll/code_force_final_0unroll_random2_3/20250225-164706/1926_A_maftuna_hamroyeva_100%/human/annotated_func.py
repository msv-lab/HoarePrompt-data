#State of the program right berfore the function call: t is an integer such that 1 <= t <= 32, and for each of the t test cases, there is a string of length 5 consisting only of the characters 'A' and 'B'. All t strings are distinct.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        l = 0
        
        h = 0
        
        for j in a:
            if j == 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        else:
            print('B')
        
    #State: a sequence of 'A's and 'B's, one for each test case, indicating the majority character in each string.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case is a distinct string of length 5 consisting only of the characters 'A' and 'B'. For each test case, it determines the majority character ('A' or 'B') in the string and prints that character. If the counts of 'A' and 'B' are equal, it prints 'B'.

