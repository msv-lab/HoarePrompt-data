#State of the program right berfore the function call: The function should accept a single parameter, `s`, which is a binary string (a string consisting of characters '0' and '1') with a length of 1 to 500 characters.
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
        
    #State: After all iterations of the loop, `s` will be the last input binary string provided, with a length of 2 to 500 characters. The variable `t` will be the same as the initial input value, indicating the total number of iterations. The loop index `i` will be equal to `t - 1`, indicating that the loop has completed its final iteration. The variable `j` will be equal to `len(s) - 1`, reflecting the last position checked in the string `s`. The variable `count` will represent the number of transitions between '0' and '1' in the string `s`, adjusted by decrementing by 1 if there was at least one transition from '0' to '1' (`flag` is True). If there were no such transitions, `count` will remain unchanged and `flag` will be False.
#Overall this is what the function does:The function reads an integer `t` from the input, which specifies the number of binary strings to process. For each of the `t` binary strings provided as input, the function calculates and prints the number of transitions between '0' and '1' in the string, adjusting the count by subtracting 1 if there is at least one transition from '0' to '1'. After processing all `t` strings, the function completes without returning any value. The final state includes the last processed binary string `s` and the original value of `t`, with the loop index `i` set to `t - 1` and the position index `j` set to `len(s) - 1`.

