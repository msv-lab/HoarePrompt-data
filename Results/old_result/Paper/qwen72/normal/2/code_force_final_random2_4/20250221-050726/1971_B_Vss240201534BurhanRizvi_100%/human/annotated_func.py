#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: After all iterations of the loop, `t` is an integer where 1 ≤ t ≤ 1000, and for each iteration, `s` was a string of length at most 10 consisting of lowercase English letters. For each `s` input during the loop: If the length of `s` was 1, the program did nothing. If the length of `s` was greater than 1 and all characters in `s` were the same, the program did nothing. Otherwise, `s2` was a shuffled version of `s`. If `s` was equal to `s2`, then `s2` was the string formed by moving the first character of `s` to the end. The loop executed `t` times, and the final state of `s` and `s2` for each iteration depends on the specific input provided.
#Overall this is what the function does:The function processes a series of inputs where `t` is an integer (1 ≤ t ≤ 1000) indicating the number of test cases, and for each test case, `s` is a string of length at most 10 consisting of lowercase English letters. For each `s`, if the string has a length of 1 or all characters are the same, the function prints 'No'. Otherwise, it generates a shuffled version of `s` (`s2`). If the shuffled version is identical to `s`, it modifies `s2` by moving the first character to the end. The function then prints 'Yes' followed by the modified or shuffled string `s2`. The function does not return any value.

