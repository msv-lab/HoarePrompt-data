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
        
    #State: t is 0, and s is the last string processed by the loop (not retained after the loop).
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a string `s` of lowercase English letters. It then processes each string to determine if it can be rearranged to form a different string. If the string can be rearranged, it prints 'Yes' followed by one possible rearrangement; otherwise, it prints 'No'.

