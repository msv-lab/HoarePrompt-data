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
        
    #State: All input strings have been processed, and the final state of the variables is as follows: `t` is the original input integer, `i` ranges from `0` to `t-1`, `string` is the input string for each iteration, `s` is the list representation of `string`, `n` is the length of `s`, `done` is `True` if a valid condition was met for the string, otherwise it remains `False`, `x` is the first character of `s`, `count` and `count2` are integers that track specific conditions during the loop, and `j` is the last index checked in the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer `t` and a string `s`. For each test case, it checks if the string `s` meets certain conditions and prints one of three possible outputs: "YES" followed by the number of operations needed to transform the string into a palindrome, or "NO" if no transformation can achieve the required condition. After processing all test cases, the function does not return any value but prints the results for each test case.

