#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following t lines contains a string s (1 ≤ |s| ≤ 10^6) consisting of lowercase Latin characters. The sum of the lengths of all strings s over all test cases does not exceed 10^6.
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
        
    #State: The output state consists of `t` lines of results, each corresponding to a test case. For each test case, the output is either 'NO' if it's not possible to split the string into two non-empty parts such that one part is a prefix and the other is a suffix of the original string and they are different, or 'YES' followed by the number of splits (1 or 2) and the resulting split string(s) if such a split is possible. The state of the input variable `t` and the strings `s` remain unchanged, and no other variables are affected beyond their use within the loop iterations.
#Overall this is what the function does:The function processes multiple test cases, where each test case is a string of lowercase Latin characters. For each string, it determines if the string can be split into two non-empty parts such that one part is a prefix and the other is a suffix of the original string and they are different. If such a split is possible, it outputs 'YES' followed by the number of splits (1 or 2) and the resulting split string(s). If no such split is possible, it outputs 'NO'. The input strings remain unchanged.

