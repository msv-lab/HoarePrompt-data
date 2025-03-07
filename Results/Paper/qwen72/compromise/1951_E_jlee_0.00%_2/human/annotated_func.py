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
        
    #State: `t` is 0, `i` is `t` (initially provided `t`), `string` is the last input string processed, `s` is a list of characters from the last `string`, `n` is the length of the last `s`, `done` is True or False, `x` is the first character of the last `s`, `count` is a non-negative integer, `count2` is a non-negative integer.
#Overall this is what the function does:The function `func` processes a series of test cases, each containing a string of lowercase Latin characters. For each test case, it determines whether the string can be split into two non-empty substrings such that the first and last characters of the original string are different in at least one of the substrings. If such a split is possible, it prints 'YES' followed by the number of splits (1 or 2) and the substrings. If no such split is possible, it prints 'NO'. After processing all test cases, the function does not return any value, but the state of the program includes the number of test cases `t` being 0, the last processed string, and various internal variables used during the processing.

