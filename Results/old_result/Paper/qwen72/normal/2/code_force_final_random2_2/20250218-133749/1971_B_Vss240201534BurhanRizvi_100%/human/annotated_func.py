#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: After all iterations of the loop, `t` is an integer such that 1 <= t <= 1000, and `s` is a string of length at most 10 consisting of lowercase English letters. For each iteration, if the length of `s` is 1 or if all characters in `s` are the same, the program outputs 'No'. Otherwise, it outputs 'Yes' followed by a shuffled version of `s` (or a shifted version if the shuffled version matches the original `s`). The loop runs `t` times, and for each input string `s`, the conditions and outputs described above are applied.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 <= t <= 1000. For each test case, it reads a string `s` of up to 10 lowercase English letters. If the string `s` has a length of 1 or all characters in `s` are the same, the function prints 'No'. Otherwise, it prints 'Yes' followed by a shuffled version of `s`. If the shuffled version matches the original string, it prints a shifted version of `s` (the last character moved to the front). The function processes `t` test cases and prints the results for each.

