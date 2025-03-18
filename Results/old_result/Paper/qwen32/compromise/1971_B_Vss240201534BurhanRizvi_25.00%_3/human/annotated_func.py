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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, the output is either "No" if the string s is the same as its random permutation s2, or "Yes" followed by the permuted string s2. The value of t remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string `s` of lowercase English letters. It then checks if a random permutation of the string `s` is different from `s` itself. If they are different, it outputs "Yes" followed by the permuted string; otherwise, it outputs "No". The value of `t` remains unchanged throughout the execution.

