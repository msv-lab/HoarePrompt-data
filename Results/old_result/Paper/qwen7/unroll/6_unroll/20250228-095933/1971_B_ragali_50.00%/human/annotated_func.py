#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
def func():
    t = int(input().strip(' '))
    for i in range(t):
        s = input().strip(' ')
        
        a = set()
        
        for i in s:
            a.add(i)
        
        if len(a) > 1:
            print('YES')
            newstr = s[len(s) // 2:] + s[:len(s) // 2]
            isreverse = s[::-1]
            if newstr != s:
                print(s[len(s) // 2:] + s[:len(s) // 2])
            elif isreverse != s:
                print(isreverse)
            else:
                print(s[len(s) // 2:] + s[0:len(s) // 2])
        else:
            print('NO')
        
    #State: Output State: The output consists of 'YES' or 'NO' for each iteration based on whether the string `s` has more than one unique character. If 'YES', it prints a modified version of the string `s` where the second half is concatenated with the first half, or the reverse of the string, or the original string depending on the conditions met. If 'NO', it simply prints 'NO'. The output will contain exactly `t` lines, each line representing the output of one iteration of the loop.
#Overall this is what the function does:The function processes `t` test cases, where `t` is a positive integer between 1 and 1000. For each test case, it reads a string `s` consisting of lowercase English letters with a maximum length of 10. It checks if the string has more than one unique character. If true, it prints 'YES' followed by a modified version of the string `s` (either by swapping halves or reversing the string). If false, it prints 'NO'. The function outputs exactly `t` lines, each corresponding to the result of one test case.

