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
        
    #State: The final output state after the loop executes all iterations is as follows: `s` is the original input string, `i` is the last character of `s`, `a` is a set containing all unique characters from the string `s`, and `isreverse` is the reversed version of `s` if the length of `a` is greater than 1. If the length of `a` is 1, `isreverse` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a string `s`. For each test case, it checks if the string `s` contains more than one unique character. If so, it rearranges the string into two halves and prints either the second half followed by the first half, the reversed string, or the original string based on certain conditions. If the string contains only one unique character, it simply prints 'NO'. After processing all test cases, the function does not return any value but prints the results for each test case.

