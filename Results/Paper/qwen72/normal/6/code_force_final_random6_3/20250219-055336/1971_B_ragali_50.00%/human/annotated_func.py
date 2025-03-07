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
        
    #State: After all iterations, `t` is the initial user input, `i` has completed all iterations from 0 to `t-1`, and for each string `s` input during the loop, `a` is a set containing all unique characters from `s`. If `len(a) > 1`, the program has printed 'YES' and either a rotated version of `s` (second half concatenated with the first half), the reversed version of `s`, or a modified version of `s` (second half concatenated with the first half again) based on the conditions checked. If `len(a) <= 1`, the program has printed 'NO' for each such string.
#Overall this is what the function does:The function reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads a string `s` from user input. If the string `s` contains more than one unique character, it prints 'YES' followed by a modified version of `s`: either a rotated version (second half concatenated with the first half), a reversed version, or a modified version (second half concatenated with the first half again), depending on the conditions checked. If the string `s` contains only one unique character, it prints 'NO'. After processing all `t` test cases, the function ends.

