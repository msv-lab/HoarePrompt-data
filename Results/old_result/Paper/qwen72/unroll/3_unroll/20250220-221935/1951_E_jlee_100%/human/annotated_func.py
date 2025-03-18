#State of the program right berfore the function call: The function `func` is expected to take no input parameters, but based on the problem description, it should be modified to take an integer `t` and a list of strings `s_list` where `t` represents the number of test cases (1 ≤ t ≤ 10^4) and each string `s` in `s_list` consists of lowercase Latin characters (1 ≤ |s| ≤ 10^6). The sum of the lengths of all strings in `s_list` does not exceed 10^6.
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
        
    #State: The function `func` will have processed all `t` test cases, and for each test case, it will have printed either 'NO' if the string does not meet the conditions, or 'YES' followed by the number of parts (1 or 2) and the parts of the string if it does meet the conditions. The variables `t` and `s_list` will remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. It takes no input parameters but reads from standard input. The first input is an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it reads a string `s` (1 ≤ |s| ≤ 10^6) consisting of lowercase Latin characters. The function checks if the string can be split into one or two non-empty parts such that the first and last characters of the string are different. If the string meets the conditions, it prints 'YES' followed by the number of parts (1 or 2) and the parts of the string. If the string does not meet the conditions, it prints 'NO'. The function processes all `t` test cases and does not modify any external variables.

