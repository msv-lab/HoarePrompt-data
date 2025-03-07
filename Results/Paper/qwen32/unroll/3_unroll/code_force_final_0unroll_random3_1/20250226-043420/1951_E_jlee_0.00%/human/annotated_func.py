#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following t lines contains a string s consisting of lowercase Latin characters (1 ≤ |s| ≤ 10^6). The sum of the lengths of all strings s over all test cases does not exceed 10^6.
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
        
    #State: The output state consists of `t` lines of results, each corresponding to one of the `t` test cases. For each test case, the output is either 'NO' or 'YES' followed by additional information if 'YES'. The 'NO' output indicates that it's not possible to split the string into two non-empty parts such that the first character of the first part is not equal to the last character of the second part, and the string cannot be split into two parts with a character that appears only once in the middle. The 'YES' output is followed by the number of splits needed (either 1 or 2) and the split strings if applicable. The state of the variables `t`, `s`, `n`, `done`, `x`, `count`, and `count2` are not preserved between iterations and are reset for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string of lowercase Latin characters. For each string, it determines whether it can be split into two non-empty parts such that the first character of the first part is not equal to the last character of the second part, or if it can be split into two parts with a character that appears only once in the middle. It outputs 'YES' followed by the number of splits needed and the split strings if possible, or 'NO' if such a split is not possible.

