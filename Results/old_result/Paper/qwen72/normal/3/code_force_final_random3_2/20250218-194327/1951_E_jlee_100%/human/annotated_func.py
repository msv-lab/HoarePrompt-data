#State of the program right berfore the function call: The function should take an integer t and a list of strings s as inputs, where 1 ≤ t ≤ 10^4 and each string s consists of lowercase Latin characters with 1 ≤ |s| ≤ 10^6. The sum of |s| over all test cases does not exceed 10^6.
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
        
    #State: `t` is greater than or equal to the initial value of `t`, `i` is `t-1`, `s` is a list of characters from the last input string `string`, `string` is the last input string, `n` is the length of the list `s`, `x` is the first character of the list `s`, `j` is `n-1`, `count` is the index of the first character in `s` that is not equal to `x` (or 0 if all characters are equal to `x`), `count2` is the number of characters in `s` that are equal to `x` after the first character that is not equal to `x` (or 0 if `count` is 0), and `done` is False if none of the conditions for a 'YES' output were met in the last iteration.
#Overall this is what the function does:The function `func` reads an integer `t` and a list of `t` strings from the user. For each string, it checks if the string can be split into two non-empty substrings such that the first and last characters of the string are different. If such a split is possible, it prints 'YES' followed by the number of splits (1 or 2) and the substrings. If no such split is possible, it prints 'NO'. After processing all `t` strings, the function terminates.

