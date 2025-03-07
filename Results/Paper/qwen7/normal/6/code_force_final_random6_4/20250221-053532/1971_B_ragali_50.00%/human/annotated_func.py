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
        
    #State: After all iterations of the loop have finished, `t` will be 0, `i` will be the last character of the original string `s` after all iterations, `s` will be an empty string, `a` will be a set containing all unique characters from the original string `s` for each iteration, and `newstr` will be either the string formed by concatenating the second half of `s.strip()` with the first half of `s.strip()` if the length of `a` is greater than 1, or it will be the original string `s.strip()` if `newstr` is equal to `s.strip()`, or it will be an empty string if the length of `a` is less than or equal to 1.
#Overall this is what the function does:The function processes a series of test cases where each test case consists of a positive integer `t` (1 ≤ t ≤ 1000) followed by a string `s` of lowercase English letters with a maximum length of 10. For each test case, it checks if the string `s` contains more than one unique character. If so, it rearranges `s` by moving the second half to the front and prints the result. If the rearranged string is not a palindrome, it prints the rearranged string; otherwise, it prints the reverse of the original string. If the string `s` contains one or zero unique characters, it prints 'NO'. The function ultimately outputs information about each test case based on the conditions described.

