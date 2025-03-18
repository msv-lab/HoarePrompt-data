#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of strings s where each string consists of lowercase Latin characters (1 ≤ |s| ≤ 10^6). The sum of the lengths of all strings across all test cases does not exceed 10^6.
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
        
    #State: The loop will have processed all `t` test cases, and for each test case, it will have printed either 'YES' or 'NO' followed by additional information if 'YES'. The variables `i`, `string`, `s`, `n`, `done`, `x`, `count`, and `count2` will have their final values after the last test case has been processed. The list `s` will contain the characters of the last processed string, and `n` will be the length of that string. The variable `done` will be `True` if the last test case was processed and a 'YES' condition was met, otherwise it will be `False`. The variables `x`, `count`, and `count2` will hold the last values they were set to during the processing of the last test case.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer (1 ≤ t ≤ 10^4). For each test case, it takes a string `string` consisting of lowercase Latin characters (1 ≤ |string| ≤ 10^6). The function checks if the string can be split into two non-empty substrings such that the first and last characters of the original string are different, or if the string can be split into two non-empty substrings where the first and last characters are the same but the string is not a palindrome. If either condition is met, it prints 'YES' followed by the number of splits (1 or 2) and the resulting substrings. If neither condition is met, it prints 'NO'. After processing all test cases, the function has printed the results for each test case, and the variables `i`, `string`, `s`, `n`, `done`, `x`, `count`, and `count2` will hold their final values from the last test case processed.

