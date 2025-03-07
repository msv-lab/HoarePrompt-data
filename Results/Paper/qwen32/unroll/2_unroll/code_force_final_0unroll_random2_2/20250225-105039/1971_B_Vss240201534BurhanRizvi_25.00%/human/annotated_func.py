#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, either "Yes" followed by a shuffled version of the input string s (if s was not equal to the shuffled string s2) or "No" (if s was equal to the shuffled string s2) is printed. The values of s and s2 are not preserved after the loop.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a string `s` of lowercase English letters. For each string `s`, it checks if a shuffled version of `s` is different from `s` itself. If they differ, it prints "Yes" followed by the shuffled string; otherwise, it prints "No". The function does not return any value but outputs the results directly.

