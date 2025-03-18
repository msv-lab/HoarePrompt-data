#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, s is a string consisting of lowercase Latin characters with length 1 <= |s| <= 10^6. The sum of lengths of all strings s over all test cases does not exceed 10^6.
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
        
    #State: `t` is the number of test cases; `s` is the list of characters from the last test case's string; `n` is the length of the last test case's string; `x` is the first character of the last test case's string; `done` is `False` if the loop did not break early in the last test case, otherwise `True`; `count` and `count2` are the final values after processing the last test case's string.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a string of lowercase Latin characters. For each string, it determines whether it is possible to split the string into one or two non-empty parts such that the parts are distinct and prints 'YES' along with the split(s) if possible, otherwise it prints 'NO'.

