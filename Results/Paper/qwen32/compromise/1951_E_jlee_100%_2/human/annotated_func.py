#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, s is a string of lowercase Latin characters with length 1 <= |s| <= 10^6. The sum of |s| over all test cases does not exceed 10^6.
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
        
    #State: The loop has completed all `t` iterations, and the variables `t`, `i`, `s`, `string`, `n`, `done`, `count`, and `count2` reflect the final state of the last test case processed. Specifically, `i` is equal to `t`, `done` is `False` if no non-palindromic splits were found in the last test case, and `count` and `count2` reflect the final state of the character checks for the last test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` of lowercase Latin characters and determines if the string can be split into one or two non-empty substrings such that the concatenation of these substrings is not a palindrome. It prints 'YES' followed by the number of splits (1 or 2) and the resulting substrings if such a split is possible; otherwise, it prints 'NO'.

