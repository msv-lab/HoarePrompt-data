#State of the program right berfore the function call: The function should take an integer t and a list of strings s as inputs, where 1 ≤ t ≤ 10^4 and each string s consists of lowercase Latin characters with 1 ≤ |s| ≤ 10^6. The sum of the lengths of all strings s across all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        string = input()
        
        s = list(string)
        
        n = len(s)
        
        done = False
        
        if n == 1:
            print('NO')
            continue
        
        x = s[0]
        
        if x != s[-1]:
            print('YES')
            print(1)
            print(string)
            continue
        
        if s.count(x) == n:
            print('NO')
            continue
        elif s.count(x) == n - 1:
            if n % 2 == 1 and s[(n - 1) // 2] != x:
                print('NO')
            else:
                print('YES')
                print(1)
                print(string)
            continue
        
        count = 0
        
        count2 = 0
        
        for j in range((n + 1) // 2):
            if s[j] != s[n - 1 - j]:
                print('YES')
                print(1)
                print(string)
                done = True
                break
            if s[j] != x and count < 1:
                count = j
            if count > 0:
                if s[j] != x:
                    if count2 > 0 and count2 < count:
                        print('YES')
                        print(2)
                        print(string[:j], string[j:])
                        done = True
                        break
                    elif count2 == count:
                        if count > 1:
                            print('YES')
                            print(2)
                            print(string[:j - 1], string[j - 1:])
                            done = True
                            break
                        else:
                            count2 = 0
                            continue
                    elif count2 > count:
                        print('YES')
                        print(2)
                        print(string[:j], string[j:])
                        done = True
                        break
                else:
                    count2 += 1
        
        if not done:
            print('NO')
        
    #State: `t` is an input integer between 1 and 10^4, inclusive, `i` is `t - 1`, `s` is a list of characters from the last input string `string`, `string` is the last input string consisting of lowercase Latin characters, `n` is the length of the list `s`, `x` is the first character of the list `s`, `j` is `(n + 1) // 2 - 1`, `count` is the index of the first character in `s` that is not equal to `x`, or 0 if all characters are equal to `x`, `count2` is the number of times `s[j]` is equal to `x` after `count` is set, or 0 if `count` is 0, and `done` is a boolean. If `done` is False, the program maintains the initial state of all variables.
#Overall this is what the function does:The function `func` reads an integer `t` and a list of `t` strings from the input. For each string, it checks if the string can be split into two non-empty substrings such that the first and last characters of the string are different. If such a split is possible, it prints 'YES' followed by the number of substrings (1 or 2) and the substrings themselves. If the string cannot be split in this manner, it prints 'NO'. After processing all `t` strings, the function concludes, and the final state of the program includes the input variables `t` and `string` as they were last read, and the internal variables `s`, `n`, `x`, `j`, `count`, `count2`, and `done` as they were last modified during the processing of the last string.

