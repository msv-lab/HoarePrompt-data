#State of the program right berfore the function call: The function should take an integer t and a list of strings s as inputs, where 1 ≤ t ≤ 10^4 and each string s consists of lowercase Latin characters with 1 ≤ |s| ≤ 10^6. The sum of |s| over all test cases does not exceed 10^6.
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
        
    #State: The loop has finished executing all `t` iterations, and the values of `t` and `s` remain unchanged. The loop processes each string in `s` and prints 'YES' or 'NO' based on the conditions specified, and may also print additional information if 'YES' is printed. The internal variables `string`, `n`, `done`, `x`, `count`, and `count2` are reset or modified during each iteration but do not persist outside the loop.
#Overall this is what the function does:The function `func` takes an integer `t` and processes `t` strings, each provided as input. For each string, it checks if the string can be split into two non-empty substrings such that the first and last characters of the string are different, or if the string has a specific pattern where it can be split into two substrings that meet certain conditions. If the string meets these conditions, the function prints 'YES' followed by the number of substrings (1 or 2) and the substrings themselves. If the string does not meet these conditions, the function prints 'NO'. After processing all `t` strings, the function concludes without returning any value, and the values of `t` and the input strings remain unchanged.

