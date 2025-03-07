#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, s is a string consisting of characters '0' and '1' with length 1 <= |s| <= 500.
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
        
    #State: a sequence of t printed values, each representing the count of transitions between different characters plus one if the string is non-increasing.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a binary string `s` and prints the number of transitions between different characters in the string. If the string is non-increasing, it adds one to the count of transitions.

