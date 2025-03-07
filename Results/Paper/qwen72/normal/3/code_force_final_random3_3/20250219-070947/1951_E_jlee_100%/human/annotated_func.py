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
        
    #State: `i` is `t-1`, `string` is the last input string, `s` is a list of characters from the last input string, `n` is the length of the last input string, `x` is the first character of the last input string, `count` and `count2` are updated as per the loop logic, and `done` is `True` or `False` depending on the conditions within the loop.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases, and then for each of the `t` test cases, it reads a string `string` from the input. The function checks if the string can be split into two non-empty substrings such that the first and last characters of the string are different. If such a split is possible, it prints 'YES' followed by the number of splits (either 1 or 2) and the resulting substrings. If no such split is possible, it prints 'NO'. The function does not return any value; it only prints the results to the console. After processing all test cases, the function concludes, and the final state of the program is that all input strings have been processed and the corresponding results have been printed.

