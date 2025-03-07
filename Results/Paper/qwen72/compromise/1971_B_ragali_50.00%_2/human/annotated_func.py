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
        
    #State: After all iterations of the loop, `t` is reduced to 0, and the loop has processed `t` strings `s` of length at most 10 consisting of lowercase English letters, each stripped of leading and trailing spaces. For each string `s` processed, a set `a` containing all unique characters from `s` was created. If the length of `a` was greater than 1, the program printed 'YES' and then printed either the string formed by concatenating the second half of `s` with the first half, the reversed string of `s`, or the string formed by concatenating the second half of `s` with the first half again, depending on which condition was met. If the length of `a` was 1 or less, the program printed 'NO' for that string. The variable `i` has taken on the values of all characters in each string `s` during the loop, and the variable `a` has been reset for each new string `s`.
#Overall this is what the function does:The function reads an integer `t` from user input, where `1 <= t <= 1000`. It then processes `t` strings, each of length at most 10 and consisting of lowercase English letters, also read from user input. For each string `s`, it checks if the string contains more than one unique character. If so, it prints 'YES' and then prints a modified version of the string: either the string formed by concatenating the second half with the first half, the reversed string, or the string formed by concatenating the second half with the first half again, depending on which condition is met first. If the string contains one or fewer unique characters, it prints 'NO'. After processing all `t` strings, the function concludes.

