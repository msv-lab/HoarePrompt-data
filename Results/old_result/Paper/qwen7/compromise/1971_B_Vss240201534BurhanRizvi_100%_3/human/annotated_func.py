#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: Output State: The output state will consist of multiple lines, each representing the output of one test case. For each test case, if the input string `s` has a length greater than 1 and contains more than one unique character, it will print 'Yes' followed by a permutation of the string `s`. If the string `s` has a length of 1 or contains only one unique character, it will print 'No'. The exact permutations printed for each valid string `s` will vary due to the random sampling in the code.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a string `s`. For each test case, it checks if the string `s` has a length greater than 1 and contains more than one unique character. If so, it prints 'Yes' followed by a randomly permuted version of the string `s`. If the string `s` has a length of 1 or contains only one unique character, it prints 'No'. The function does not return any value but outputs the results for each test case.

