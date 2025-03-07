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
        
    #State: Output State: The output state will consist of multiple lines, each line containing 'Yes' followed by a string s2. The value of s2 is either a randomly shuffled version of the input string s, or a cyclically shifted version of s (s[1:] + s[0]) if the shuffled version is the same as the original string s. The number of such lines will be equal to the number of test cases provided as input. Each test case is defined by a string s of length at most 10, and the output for each test case adheres to the conditions specified in the loop body.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (number of test cases) and a string `s` (of length at most 10 consisting of lowercase English letters). For each test case, it checks if `s` contains only one unique character or is a single character. If these conditions are met, it prints 'No'. Otherwise, it generates a new string `s2` by either randomly shuffling the characters of `s` or performing a cyclic shift if the shuffle results in the original string. It then prints 'Yes' followed by `s2`. The function outputs this information for each test case.

