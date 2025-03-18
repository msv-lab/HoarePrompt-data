#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: After the loop executes all iterations, the value of `t` remains unchanged as it is not modified within the loop. The value of `s` will be the last input string provided by the user, stripped of any leading or trailing spaces. The set `a` will contain the unique characters of the last input string `s`.
#Overall this is what the function does:The function reads an integer `t` from user input, where `1 <= t <= 1000`, and then for each of the `t` iterations, it reads a string `s` of length at most 10 consisting of lowercase English letters. For each string `s`, it checks if the string contains more than one unique character. If it does, it prints 'YES' followed by a modified version of the string `s` (either by rotating it or reversing it, depending on the conditions). If the string contains only one unique character, it prints 'NO'. After all iterations, the value of `t` remains unchanged, and the last input string `s` and its unique characters are stored in the variables `s` and `a`, respectively.

