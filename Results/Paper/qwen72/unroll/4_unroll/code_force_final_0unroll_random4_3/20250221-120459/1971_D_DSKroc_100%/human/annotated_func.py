#State of the program right berfore the function call: The function should take a single argument, a binary string `s` (1 ≤ |s| ≤ 500), where |s| denotes the length of the string `s`. The string `s` consists only of characters '0' and '1'.
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
        
    #State: The loop will execute `t` times, and for each iteration, it will read a binary string `s` from the input. After processing `s`, it will print the number of transitions between different bits in `s` (i.e., '0' to '1' or '1' to '0'). If there are no transitions from '0' to '1', it will print the number of transitions plus one. The variables `s`, `count`, and `flag` will be reset for each iteration, so their final values will be the result of the last iteration. The variable `t` will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each of the `t` test cases, it reads a binary string `s` from the input. It then calculates the number of transitions between different bits in `s` (i.e., '0' to '1' or '1' to '0'). If there are no transitions from '0' to '1', it prints the number of transitions plus one; otherwise, it prints the number of transitions. The function does not return any value, but it prints the result for each test case. The variable `t` remains unchanged after the function concludes.

