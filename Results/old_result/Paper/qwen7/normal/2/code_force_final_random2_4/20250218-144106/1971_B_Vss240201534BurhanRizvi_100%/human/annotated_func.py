#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 1000, and `s` is the input string received from the input mechanism. After all iterations of the loop, `s2` will be determined based on the following rules:
    #- If the length of `s` is 1, `s2` remains `s`.
    #- If `s` consists of all the same characters and has a length greater than 1, `s2` is the string `s` rotated by one character to the left.
    #- Otherwise, `s2` is a random permutation of the string `s`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` and a string `s`. For each test case, it checks the properties of the string `s`. If `s` has a single character, it prints 'No'. If `s` consists of identical characters and has more than one character, it rotates `s` one character to the left and prints 'Yes' followed by the modified string. In all other cases, it generates a random permutation of `s`, prints 'Yes', and then prints the permuted string. The function does not return any value but prints the results for each test case.

