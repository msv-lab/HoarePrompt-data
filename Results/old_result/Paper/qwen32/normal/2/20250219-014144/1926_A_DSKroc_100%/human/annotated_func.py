#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each of the t test cases, there is a string of length 5 consisting only of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: For each of the `t` test cases, the program will output either 'A' or 'B' based on whether the count of 'A's (`ac`) in the string `s` is greater than the count of 'B's (`bc`). After all `t` iterations, the program will have processed all input strings and printed the corresponding result ('A' or 'B') for each one.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, then for each test case, it reads a string of length 5 consisting of 'A' and 'B' characters. It compares the counts of 'A' and 'B' in each string and prints 'A' if there are more 'A's, otherwise it prints 'B'. This process is repeated for all `t` test cases.

