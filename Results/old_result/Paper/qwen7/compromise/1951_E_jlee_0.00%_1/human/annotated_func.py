#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, s is a string consisting of lowercase Latin characters with 1 ≤ |s| ≤ 10^6.
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
        
    #State: All input strings have been processed, `i` equals `t`, `string` is the last input string, `s` is a list of characters from the last input string, `n` is the length of `s`, `done` is `True` or `False` based on the conditions met, `count` is 0, `count2` is 0, `j` is the last value in the range `(n + 1) // 2` for the last iteration.
#Overall this is what the function does:The function processes up to 10,000 test cases, where each test case consists of a string `s` of lowercase Latin characters. For each string, it checks if the string can be split into two parts such that the first part is the reverse of the second part, or if the string can be made into such a form by removing at most one character. If such a transformation is possible, it prints "YES" along with the number of operations (either 1 or 2) and the modified string; otherwise, it prints "NO". After processing all test cases, the function does not return any value but prints the results for each test case.

