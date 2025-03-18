#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and each string s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: After the loop executes all iterations, `t` is 0, `i` is the last character of the last processed string `s`, `s` is the input string with leading and trailing spaces removed and must not be empty, `a` is a set containing all unique characters from the last processed string `s`. If `len(a) > 1`, then `newstr` is the string formed by concatenating the second half of `s` (from the middle to the end) with the first half of `s` (from the start to the middle), and `isreverse` is the reversed string of `s`. If `len(a) == 1`, then `newstr` and `isreverse` remain as defined in the last iteration.
#Overall this is what the function does:The function reads an integer `t` from user input, representing the number of test cases, and for each test case, it reads a string `s`. It checks if the string `s` contains more than one unique character. If so, it prints 'YES' and then prints a modified version of `s` that is either the second half concatenated with the first half, the reversed string, or a combination of both, ensuring the output is different from the original string `s`. If the string `s` contains only one unique character, it prints 'NO'. After processing all `t` test cases, the function concludes.

