#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, s is a string consisting of lowercase Latin characters with a length such that 1 <= |s| <= 10^6. The sum of the lengths of all strings s over all test cases does not exceed 10^6.
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
        
        for j in range(n):
            if s[j] != s[n - 1 - j]:
                print('YES')
                print(1)
                print(string)
                done = True
                break
            if s[j] != x and count < 1:
                count = j
                continue
            if count > 0:
                if s[j] != x:
                    if count2 < count:
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
        
    #State: All `t` test cases have been processed, and the corresponding outputs (either 'YES' or 'NO' along with the required indices and substrings if applicable) have been printed for each test case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of a string `s` of lowercase Latin characters. For each string, it determines if it is possible to split the string into two non-empty parts such that the two parts are not identical and the concatenation of these parts in any order results in the original string. If such a split is possible, it prints "YES" followed by the number of splits (1 or 2) and the resulting substrings. If no such split is possible, it prints "NO".

