#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, s is a string consisting of lowercase Latin characters with a length such that 1 <= |s| <= 10^6. The sum of the lengths of all strings s across all test cases does not exceed 10^6.
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
        
    #State: For each test case, the program will output 'YES' or 'NO' based on the conditions specified in the loop. If 'YES' is output, it will also specify the number of operations (1 or 2) and the resulting string(s). The variables `t`, `string`, `s`, `n`, `done`, `x`, `count`, and `count2` will be in their final states after processing all test cases, but their exact values are not specified as they are local to each iteration. The global state outside the loop remains unchanged.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a string of lowercase Latin characters. For each string, it determines if it is possible to make the string non-palindromic by removing at most two characters. If it is possible, the function outputs 'YES' followed by the number of characters removed (either 1 or 2) and the resulting string(s). If it is not possible, the function outputs 'NO'.

