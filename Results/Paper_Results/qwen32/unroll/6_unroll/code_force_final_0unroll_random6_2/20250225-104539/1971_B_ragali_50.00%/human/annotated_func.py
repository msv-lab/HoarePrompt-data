#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: `t` is an integer between 1 and 1000, and `s` is a string of length at most 10 consisting of lowercase English letters, representing the last string processed.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a string `s` of length at most 10. For each string, it checks if the string contains more than one unique character. If it does, it prints 'YES' and then prints a modified version of the string, which could be a rotated version of the string or its reverse, depending on specific conditions. If the string contains only one unique character, it prints 'NO'.

