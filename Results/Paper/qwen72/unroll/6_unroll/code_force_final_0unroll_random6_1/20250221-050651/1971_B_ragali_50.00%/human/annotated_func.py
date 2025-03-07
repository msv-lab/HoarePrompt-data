#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and each string s in the test cases is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: The loop has finished executing all iterations. The variable `t` is unchanged as it controls the number of iterations. Each string `s` from the input has been processed, and for each `s` where the set `a` (containing unique characters of `s`) has more than one unique character, the output is 'YES' followed by a modified version of `s`. If `s` has only one unique character, the output is 'NO'. The set `a` is reset for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 1000`, and then processes `t` strings, each of length at most 10 consisting of lowercase English letters. For each string `s`, if `s` contains more than one unique character, it prints 'YES' followed by a modified version of `s` (either the second half concatenated with the first half, the reverse of `s`, or a combination of the second half and the first character of the first half, depending on which modification is different from the original `s`). If `s` contains only one unique character, it prints 'NO'. After processing all `t` strings, the function concludes. The function does not return any value.

