#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each of the t test cases, there is a string of length 5 consisting solely of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: t lines, each containing either 'A' or 'B', based on the counts of 'A' and 'B' in each of the t test cases.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string of length 5 consisting of 'A' and 'B'. It then prints 'A' if there are more 'A's in the string, otherwise it prints 'B'. The final state of the program is that it outputs `t` lines, each containing either 'A' or 'B', based on the counts of 'A' and 'B' in each test case's string.

