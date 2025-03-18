#State of the program right berfore the function call: t is an integer such that 1 <= t <= 32, and for each of the t test cases, there is a string of length 5 consisting only of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: After executing the loop, for each of the `t` test cases, the program will have printed either 'A' or 'B' depending on whether the count of 'A's (`ac`) in the string is greater than the count of 'B's (`bc`). The variable `t` remains unchanged, and all `t` strings are still distinct as per the initial state.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a distinct string of length 5 consisting only of the characters 'A' and 'B'. It then prints 'A' if the string contains more 'A's than 'B's, otherwise it prints 'B'.

