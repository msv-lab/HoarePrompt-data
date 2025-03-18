#State of the program right berfore the function call: The function `func` is expected to take an input, but the function definition provided does not include any parameters. Based on the problem description, the function should take a single string `s` as input, where `s` is a binary string (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: The loop will print the number of positions in each binary string `s` where a '1' is immediately followed by a '0', plus one, for each of the `t` iterations. The variable `t` will be unchanged, and the variable `s` will retain the value of the last input string provided.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of binary strings to process. For each of the `t` binary strings `s` read from the input, the function prints the number of positions where a '1' is immediately followed by a '0', plus one. The function does not return any value. After the function concludes, the variable `t` remains unchanged, and the variable `s` retains the value of the last binary string processed.

