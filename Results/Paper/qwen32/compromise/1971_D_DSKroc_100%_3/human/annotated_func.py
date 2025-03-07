#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a string consisting of characters '0' and '1' with length 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        flag = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) != int(s[i + 1]):
                count += 1
            if int(s[i]) < int(s[i + 1]):
                flag = 1
        
        if flag == 0:
            print(count + 1)
        else:
            print(count)
        
    #State: The program will have printed the number of transitions between different characters in each string `s` provided by the user, incremented by 1 if there are no transitions where a character is less than the next character, for a total of `t` iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string `s` consisting of '0's and '1's. It then calculates and prints the number of transitions between different characters in the string `s`. If there are no transitions where a '0' is followed by a '1', it increments the count by 1. This process is repeated for all `t` test cases.

