#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, s is a string of length between 1 and 500 consisting only of the characters '0' and '1'.
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
        
    #State: The output state consists of `t` number of lines, each representing the count of transitions between '0' and '1' in the respective input string `s`. If the string is non-decreasing (i.e., no '1' is preceded by a '0'), the count is incremented by 1. Variables `t`, `s`, `count`, and `flag` do not retain their values after the loop; `t` remains the initial integer input, and `s` is the last input string processed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string `s` consisting of '0's and '1's. It then calculates and prints the number of transitions between '0' and '1' in the string `s`. If the string is non-decreasing (i.e., no '1' is preceded by a '0'), it increments the count by 1. The function outputs `t` lines, each corresponding to the result of one test case.

