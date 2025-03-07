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
        
    #State: After all iterations of the loop, `t` is an integer between 1 and 1000, `i` is the last character of the string `s` if the length of the set `a` is greater than 1. Otherwise, `i` is the third element of the set `s`. `s` is an empty string, `a` is a set containing all unique characters from the original string `s`, and if the length of set `a` is greater than 1, `newstr` is a string identical to `s`; otherwise, the length of `a` is 1.
#Overall this is what the function does:The function processes a series of test cases, each defined by a positive integer `t` (1 ≤ t ≤ 1000) followed by a string `s` consisting of lowercase English letters with a maximum length of 10. For each test case, it checks if the string `s` can be split into two halves such that reversing one half and concatenating it with the other half results in a different string, or if reversing the entire string results in a different string. If neither condition is met, it prints 'NO'. Otherwise, it prints the modified string according to the conditions checked.

