#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and s is a binary string of length 1 ≤ |s| ≤ 500 consisting of characters '0' and '1'.
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
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: `t` is an input integer such that 1 ≤ t ≤ 500, `i` is `t`, `s` is a new input binary string of length 1 ≤ |s| ≤ 500 consisting of characters '0' and '1', `j` is `len(s) - 1`. For each iteration, if `flag` is True, indicating there is at least one occurrence of '0' followed immediately by '1' in `s`, then `count` is the number of adjacent character pairs in `s` that are different minus 1. Otherwise, `count` remains the number of adjacent character pairs in `s` that are different, and `flag` remains False. After all iterations, the loop has processed `t` binary strings, and for each string, the number of transitions between '0' and '1' (plus 1 if no '0' to '1' transition exists) has been printed.
#Overall this is what the function does:The function reads an integer `t` (1 ≤ t ≤ 500) indicating the number of test cases, and for each test case, it reads a binary string `s` (1 ≤ |s| ≤ 500). It then calculates the number of transitions between '0' and '1' in the string `s`. If there is at least one '0' followed immediately by '1', the count is reduced by 1. The function prints the calculated count for each test case. After processing all `t` test cases, the function completes its execution without returning any value.

