#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: t is an integer such that 1 <= t <= 1000.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a string `s` of lowercase English letters with a length of at most 10. For each string, it determines if the string can be rearranged to form a different string and prints 'Yes' along with the rearranged string if possible. If the string cannot be rearranged to form a different string, it prints 'No'.

