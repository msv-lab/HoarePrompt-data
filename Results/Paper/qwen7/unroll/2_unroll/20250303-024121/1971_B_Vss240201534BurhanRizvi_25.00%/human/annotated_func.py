#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: For each test case, the output will either print 'Yes' followed by a randomly permuted version of the input string, or 'No' if the string does not change after permutation. The number of test cases and their respective outputs depend on the input provided during the loop's execution.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` and a string `s`. For each test case, it generates a random permutation of the string `s` and checks if the original string is different from the permutation. If they are different, it prints 'Yes' followed by the permuted string; otherwise, it prints 'No'. The function does not return any value but prints the results for each test case.

