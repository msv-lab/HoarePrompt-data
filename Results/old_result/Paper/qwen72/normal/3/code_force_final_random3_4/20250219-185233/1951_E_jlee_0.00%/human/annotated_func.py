#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of strings s where each string consists of lowercase Latin characters (1 ≤ |s| ≤ 10^6) and the sum of |s| over all test cases does not exceed 10^6.
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
        
    #State: `t` is an input integer between 1 and 10^4, `i` is `t - 1`, `string` is the last input string, `s` is a list of characters from the last `string`, `n` is the length of the last `s`, `x` is the first character of the last `s`, `j` is `(n + 1) // 2 - 1`, `count` is the index of the first character in the last `s` that is not equal to `x` (or 0 if all characters are equal to `x`), `done` is False, and `count2` is the count of characters in the last `s` that are equal to `x` after the first mismatch (or 0 if no such characters exist). If `done` is False, the program continues with these variable states.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads a string and determines if it can be split into two non-empty substrings such that the first and last characters of the original string are not the same. If such a split is possible, it prints 'YES' followed by the number of parts (1 or 2) and the substrings. If not, it prints 'NO'. The function does not return any value; it only prints the results. After processing all test cases, the function concludes, and the program state is undefined as the function does not modify any global variables or return any values.

