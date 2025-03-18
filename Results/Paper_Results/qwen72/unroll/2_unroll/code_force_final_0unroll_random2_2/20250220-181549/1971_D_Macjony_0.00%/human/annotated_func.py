#State of the program right berfore the function call: The function should take a single parameter, `s`, which is a binary string (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'.
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
        
    #State: The loop will print the value of `count` after each iteration, which represents the number of alternating character sequences in the binary string `s` minus one if a '01' pattern is found. The variable `s` will be updated to the input string provided during each iteration, and `t` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads a binary string `s` (1 ≤ |s| ≤ 500) from the input. It then calculates and prints the number of alternating character sequences in the string `s`, subtracting one if a '01' pattern is found. The function does not return any value; it only prints the result for each test case. The variable `s` is updated for each test case, and `t` remains unchanged throughout the function's execution.

