#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: For each test case, the program will print 'YES' if the string `s` contains more than one unique character. If it does, it will then print a modified version of the string based on the conditions provided. If the string contains only one unique character, it will print 'NO'. The variable `t` will remain unchanged, and `s` will hold the last input string processed by the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` of length at most 10 consisting of lowercase English letters. It prints 'YES' if the string contains more than one unique character; otherwise, it prints 'NO'. If the string contains more than one unique character, it also prints a modified version of the string based on specific conditions.

