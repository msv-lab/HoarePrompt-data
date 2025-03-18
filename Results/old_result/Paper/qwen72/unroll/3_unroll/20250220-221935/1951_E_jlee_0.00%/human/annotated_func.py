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
        
    #State: The loop has finished executing for all `t` test cases. The variables `t` and `s` remain unchanged. The loop has processed each string in the list `s` and printed the appropriate output for each string based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` accepts no parameters and reads input from the user. It processes `t` test cases, where `t` is an integer (1 ≤ t ≤ 10^4). For each test case, it reads a string `s` consisting of lowercase Latin characters (1 ≤ |s| ≤ 10^6). The function checks if the string can be split into two non-empty substrings such that the first and last characters of the string are different, or if the string contains at least two different characters. If either condition is met, it prints 'YES' followed by the number of splits (1 or 2) and the resulting substrings. If neither condition is met, it prints 'NO'. After processing all test cases, the function terminates, and the variables `t` and `s` remain unchanged.

