#State of the program right berfore the function call: The function `func` is expected to take a binary string `s` as input, where `s` consists only of characters '0' and '1', and its length is between 1 and 500 inclusive. The function should be called within a loop that processes multiple test cases, where the number of test cases `t` is an integer such that 1 ≤ t ≤ 500.
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
        
    #State: The loop will execute `t` times, and for each iteration, it will read a binary string `s` from the input, process it to count the number of transitions between '0' and '1' (excluding the transition from '0' to '1' if it occurs), and print the count. The variables `i`, `s`, `count`, `flag`, and `j` will be reset for each iteration, so their final values after the loop will be the values from the last iteration. Specifically, `i` will be `t-1`, `s` will be the last input binary string, `count` will be the count of transitions for the last input string, `flag` will be `True` if the last input string contained a transition from '0' to '1', and `j` will be the length of the last input string minus 1.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads a binary string `s` and processes it to count the number of transitions between '0' and '1', excluding the transition from '0' to '1' if it occurs. The function prints the count for each test case. After processing all test cases, the final state of the program includes the variables `i`, `s`, `count`, `flag`, and `j` holding the values from the last test case. Specifically, `i` will be `t-1`, `s` will be the last input binary string, `count` will be the count of transitions for the last input string, `flag` will be `True` if the last input string contained a transition from '0' to '1', and `j` will be the length of the last input string minus 1. The function does not return any value.

