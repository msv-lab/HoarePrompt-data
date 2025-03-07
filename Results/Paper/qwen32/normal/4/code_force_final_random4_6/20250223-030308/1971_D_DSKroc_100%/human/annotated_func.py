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
        
    #State: `t` remains unchanged as it is the number of test cases and is not modified by the loop. `s` is the input string for the current iteration, `count` is the number of transitions between '0' and '1' in the string `s` for the current iteration, `flag` indicates whether there is at least one occurrence of '0' followed by '1' in the string `s` for the current iteration (0 if no such pair exists, 1 if at least one exists). `q` will be equal to `t` after the loop completes, as it increments with each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string `s` consisting only of the characters '0' and '1'. It then calculates and prints the number of transitions between '0' and '1' in the string `s`, adding 1 to the count if there are no occurrences of '0' followed by '1'.

