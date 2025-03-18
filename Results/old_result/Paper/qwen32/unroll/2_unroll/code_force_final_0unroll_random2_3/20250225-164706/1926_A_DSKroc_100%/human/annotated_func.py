#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each of the t test cases, there is a string of length 5 consisting of only the characters 'A' and 'B'.
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
        
        if ac > bc:
            print('A')
        else:
            print('B')
        
    #State: For each of the `t` test cases, the output will be either 'A' or 'B' depending on whether the count of 'A's or 'B's is greater in the respective string. If counts are equal, it will output 'B'. The variable `t` and the strings provided as input remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case consists of a string of length 5 containing only 'A' and 'B'. For each test case, it outputs 'A' if the string contains more 'A's than 'B's, otherwise it outputs 'B'. The input values `t` and the strings remain unchanged.

