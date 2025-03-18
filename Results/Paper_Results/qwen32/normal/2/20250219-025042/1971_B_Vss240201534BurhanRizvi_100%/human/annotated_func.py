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
        
    #State: A series of "No" or "Yes" followed by modified strings `s2` for each test case, depending on the conditions specified.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a string `s`. For each string, it determines if the string can be rearranged to form a different string. If the string cannot be rearranged (either because it has only one character or all characters are the same), it outputs "No". Otherwise, it outputs "Yes" and provides a rearranged version of the string.

