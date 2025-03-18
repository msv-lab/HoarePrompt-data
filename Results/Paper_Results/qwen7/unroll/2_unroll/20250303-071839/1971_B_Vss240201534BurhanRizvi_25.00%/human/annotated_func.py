#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: Output State: The output state will consist of multiple lines, where for each test case, either 'Yes' followed by a randomly permuted version of the input string `s`, or 'No' will be printed. The number of lines will be equal to the number of test cases provided as input. Each line either confirms that the string was not a palindrome (by printing 'Yes' and a random permutation) or denies it (by printing 'No').
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` and a string `s`. For each test case, it generates a random permutation of the string `s` and checks if the original string is different from the permutation. If they are different, it prints 'Yes' followed by the random permutation; otherwise, it prints 'No'. The function does not return any value but prints the results for each test case.

