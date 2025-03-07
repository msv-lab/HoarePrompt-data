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
        
    #State: For each of the `t` test cases, the output will be either 'A' or 'B', depending on which character ('A' or 'B') appears more frequently in the respective 5-character string. If 'A' appears more times, 'A' is printed; otherwise, 'B' is printed. The value of `t` and the distinct 5-character strings remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a 5-character string consisting only of 'A' and 'B'. It then outputs 'A' if 'A' appears more frequently in the string, otherwise it outputs 'B'. The values of `t` and the input strings remain unchanged after the function executes.

