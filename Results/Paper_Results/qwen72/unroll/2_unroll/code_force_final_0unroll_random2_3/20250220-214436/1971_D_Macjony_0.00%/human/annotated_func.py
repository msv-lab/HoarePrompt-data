#State of the program right berfore the function call: The function should take a single argument, a binary string `s` (1 ≤ |s| ≤ 500), where |s| denotes the length of the string `s`. The string `s` consists only of characters '0' and '1'.
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
        
    #State: The loop will print the value of `count` for each iteration, which is the number of transitions between '0' and '1' in the input string `s`, adjusted by the `flag` variable. The `flag` variable is used to reduce the `count` by 1 if a specific transition ('0' to '1') is found. The variables `i`, `s`, `count`, `flag`, and `j` will be updated during each iteration, but the input integer `t` will remain unchanged. After all iterations, the final value of `t` will be the same as the initial value, and the final value of `s` will be the last input string provided.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of binary strings to process. For each of the `t` binary strings `s` (where 1 ≤ |s| ≤ 500 and `s` consists only of '0' and '1'), it calculates the number of transitions between '0' and '1' in the string, adjusting the count by subtracting 1 if a specific transition ('0' to '1') is found. The function then prints the adjusted count for each string. After processing all `t` strings, the final value of `t` remains unchanged, and the last value of `s` is the last input string provided. The function does not return any value.

