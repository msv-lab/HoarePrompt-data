#State of the program right berfore the function call: The function should take a single parameter, `s`, which is a binary string (a string consisting of characters '0' and '1') with a length of 1 to 500 characters.
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
        
    #State: After the loop has completed all its iterations, `s` remains the final input string provided during the last iteration, `t` is the original input integer, `i` is equal to `t` (indicating the loop has run `t` times), `j` is `len(s) - 1` (indicating the last position checked in the string `s`), and `count` is the total number of transitions between different characters in the string `s` across all iterations. If `flag` is True, it indicates there was at least one instance where `s[j]` is '0' and `s[j + 1]` is '1' during the loop, and `count` is decremented by 1. Otherwise, `flag` remains False, and `count` is unchanged.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, followed by `t` binary strings (each consisting of '0's and '1's). For each binary string, it calculates the number of transitions between different characters ('0' to '1' or '1' to '0'). If there is at least one transition from '0' to '1', the count is decremented by 1. The function prints the adjusted count for each binary string. After processing all test cases, the function ends, leaving the input variables `t` and the final binary string `s` in their respective states, and the loop counters `i` and `j` reflecting the completion of the loops.

