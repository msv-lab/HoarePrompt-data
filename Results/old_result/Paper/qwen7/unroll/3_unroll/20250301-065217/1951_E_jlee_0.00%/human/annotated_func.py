#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, s is a string consisting of lowercase Latin characters such that 1 ≤ |s| ≤ 10^6. Additionally, the sum of |s| over all test cases does not exceed 10^6.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 10^4, and `s` is a string consisting of lowercase Latin characters such that 1 ≤ |`s`| ≤ 10^6. The loop processes each string `s` according to its conditions, and based on the given logic, it determines whether the string meets certain criteria and prints either 'YES' or 'NO' along with additional information if applicable. After all iterations, the variable `t` will be decremented to 0, and the variable `done` will be set to `True` for each iteration where the condition is met. The strings `s` will be processed according to the rules defined within the loop, and the output will reflect whether each string satisfies the specified conditions or not.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (number of test cases) and a string `s` (lowercase Latin characters). For each test case, it checks specific conditions on the string `s` and prints either 'YES' or 'NO' along with additional information if the conditions are met. The function does not return any value but outputs the results for each test case. After processing all test cases, the variable `t` is decremented to 0, and `done` is set to `True` for each test case where the conditions are satisfied.

