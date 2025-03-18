#State of the program right berfore the function call: The function should take a single argument, `s`, which is a string of length at most 10 consisting of lowercase English letters. Additionally, the function should be called within a loop that processes `t` test cases, where `t` is a positive integer such that 1 <= t <= 1000.
def func():
    for _ in range(int(input())):
        s = input()
        
        if len(s) == 1:
            print('No')
        elif len(set(s)) == 1 and len(s) > 1:
            print('No')
        else:
            s2 = ''.join(random.sample(s, len(s)))
            if s == s2:
                s2 = s[1:] + s[0]
            print('Yes')
            print(s2)
        
    #State: Output State: The loop processes `t` test cases, where for each test case, if the string `s` has a length of 1 or all characters in `s` are the same, it prints 'No'. Otherwise, it prints 'Yes' followed by a shuffled version of `s` that is different from the original `s`. The variable `s` is re-assigned in each iteration based on the input provided, and the loop runs `t` times. After all iterations, the variable `t` remains unchanged, and `s` will be the last input string processed in the loop.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is a positive integer (1 <= t <= 1000). For each test case, it reads a string `s` of length at most 10 consisting of lowercase English letters. If the string `s` has a length of 1 or all characters in `s` are the same, it prints 'No'. Otherwise, it prints 'Yes' followed by a shuffled version of `s` that is different from the original `s`. The variable `s` is re-assigned in each iteration based on the input provided, and the loop runs `t` times. After all iterations, the variable `t` remains unchanged, and `s` will be the last input string processed in the loop.

