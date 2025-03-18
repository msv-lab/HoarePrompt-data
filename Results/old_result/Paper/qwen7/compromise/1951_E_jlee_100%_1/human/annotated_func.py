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
        
    #State: The loop has executed all iterations, and the final state of the variables is as follows: `i` is equal to `t`, `done` is `False`, `count` is either 0 or 1, `count2` is 1 if `count` was less than `count2` during the last iteration, otherwise `count2` remains unchanged, `j` is equal to `n - 1`, `n` is the length of the list `s`, and `x` is the first character of the string `s`.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `t` and a string `s`. For each test case, it checks if the string can be split into two parts such that the first part is the reverse of the second part, or if the string can be made into a palindrome by removing at most one character. If such a condition is met, it prints "YES" along with the number of operations needed and the modified string; otherwise, it prints "NO". After processing all test cases, the function ensures that all possible conditions have been checked and outputs the final results accordingly.

