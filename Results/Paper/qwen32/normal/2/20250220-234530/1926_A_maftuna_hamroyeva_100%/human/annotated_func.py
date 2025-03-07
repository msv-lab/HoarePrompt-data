#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each of the t test cases, there is a string of length 5 consisting only of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: t is an integer between 1 and 32, inclusive; i is t-1 (indicating the last iteration); a is the last input string; l is the number of 'A's in the last input string; h is the number of characters in the last input string that are not 'A'. If l is greater than h, then 'A' is printed; otherwise, 'B' is printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case consists of a distinct string of length 5 containing only 'A' and 'B'. For each test case, it counts the occurrences of 'A' and 'B', and prints 'A' if there are more 'A's than 'B's, otherwise it prints 'B'.

