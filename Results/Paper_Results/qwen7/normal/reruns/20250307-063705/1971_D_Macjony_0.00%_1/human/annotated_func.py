#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with a length between 1 and 500, inclusive.
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        count = 1
        
        flag = False
        
        j = 0
        
        while j < len(s) - 1:
            if s[j] != s[j + 1]:
                count += 1
                if s[j] == '0' and s[j + 1] == '1':
                    flag = True
                    j += 1
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: Output State: `t` is a positive integer between 1 and 500, `s` is an updated input string with a length equal to the total number of iterations plus one, `count` is the total number of times the condition `s[j] != s[j + 1]` was met across all iterations, which is equal to `len(s) - 1`, `flag` is True because the loop executed at least once with the condition `s[j] == '0' and s[j + 1] == '1'` being true in at least one iteration, `i` is 0, `j` is `len(s) - 1`, and the condition `flag` is True.
    #
    #This means that after all iterations of the loop have finished, `t` will still be the initial value since it's not modified within the loop. The string `s` will have a length equal to the total number of iterations plus one because each iteration processes one character of the string. The variable `count` accumulates the number of transitions from '0' to '1' or vice versa across all iterations. The variable `flag` remains True as long as there is at least one instance where `s[j]` is '0' and `s[j + 1]` is '1' during any iteration.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads a positive integer `t` and a binary string `s`. It then counts the number of times the string `s` transitions from '0' to '1' or '1' to '0'. If there is at least one transition from '0' to '1', it subtracts one from the count. Finally, it prints the count for each test case.

