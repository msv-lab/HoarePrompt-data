#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string such that 1 ≤ |s| ≤ 500.
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
        
    #State: Output State: The value of `t` remains unchanged, and for each string `s` provided by the user, if the string is non-decreasing, the output is `count + 1`, otherwise, it is `count`. The variable `count` and `flag` are reset for each iteration of the outer loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` and a binary string `s`. For each string `s`, it counts the number of positions where consecutive characters differ. If the string is non-decreasing, it adds one to this count before printing it; otherwise, it prints the count as is. After processing all test cases, the function outputs the results and resets the count and flag variables for each new string.

