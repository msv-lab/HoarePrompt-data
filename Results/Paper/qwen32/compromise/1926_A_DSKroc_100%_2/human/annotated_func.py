#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each of the t test cases, there is a string of length 5 consisting solely of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: After processing all `t` test cases, the output consists of `t` lines where each line is either 'A' or 'B', depending on whether the number of 'A's in the corresponding string is greater than the number of 'B's.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, followed by `t` distinct strings of length 5 consisting solely of the characters 'A' and 'B'. For each string, it determines whether the number of 'A's is greater than the number of 'B's and prints 'A' if true, otherwise it prints 'B'. After processing all test cases, the output consists of `t` lines, each indicating the result ('A' or 'B') for the corresponding test case.

