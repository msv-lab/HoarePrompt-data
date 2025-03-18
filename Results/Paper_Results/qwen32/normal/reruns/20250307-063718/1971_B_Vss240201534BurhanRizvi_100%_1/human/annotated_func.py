#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: The loop has processed all `t` test cases, printing 'No' or 'Yes' and the corresponding modified string `s2` for each case. The variable `t` remains unchanged, and `s` holds the value of the last string processed.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a string `s`. For each string, it determines if the string can be rearranged to form a different string. If the string cannot be rearranged (i.e., it is either a single character or all characters are the same), it outputs 'No'. Otherwise, it outputs 'Yes' and provides a rearranged version of the string. The function does not modify the original string `s` but uses it to generate and print the output for each test case.

