#State of the program right berfore the function call: The function should take a single parameter, `s`, which is a string of length at most 10 consisting of lowercase English letters. Additionally, the function should handle multiple test cases, where the number of test cases, `t`, is an integer such that 1 ≤ t ≤ 1000.
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
        
    #State: The variable `s` will be the last string input by the user, and `a` will be a set containing the unique characters of the last input string `s`. The loop will print 'YES' if the last input string `s` contains more than one unique character, and it will print a modified version of `s` based on the conditions specified. If the last input string `s` contains only one unique character, it will print 'NO'. The variable `t` will remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. It first reads an integer `t` from the input, representing the number of test cases, where 1 ≤ t ≤ 1000. For each test case, it reads a string `s` of at most 10 lowercase English letters. The function checks if the string `s` contains more than one unique character. If it does, the function prints 'YES' and then prints a modified version of `s` based on specific conditions: it either prints the second half of `s` concatenated with the first half, the reverse of `s`, or a combination of the second half and the first character repeated. If the string `s` contains only one unique character, the function prints 'NO'. After processing all test cases, the function does not return any value, but the final state includes the last input string `s` and a set `a` containing the unique characters of `s`. The variable `t` remains unchanged.

