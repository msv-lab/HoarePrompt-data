#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following t lines contains a string s consisting of lowercase Latin characters (1 ≤ |s| ≤ 10^6). The sum of the lengths of all strings s over all test cases does not exceed 10^6.
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
        
    #State: The output state consists of a series of responses for each test case. For each string `s`, the program determines if it's possible to split the string into two parts such that the first part is not equal to the second part, or if the string is already unique or symmetrical in a specific way. The responses are printed line by line, indicating whether it's possible ('YES') or not ('NO') to make such a split, and if possible, the number of splits and the resulting parts of the string. The state of the variables `t`, `string`, `s`, `n`, `done`, `x`, `count`, and `count2` will vary based on each test case but will not persist beyond the current iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a string of lowercase Latin characters. For each string, it determines if it's possible to split the string into two parts such that the first part is not equal to the second part. If such a split is possible, it outputs 'YES', the number of splits (either 1 or 2), and the resulting parts of the string. If no such split is possible, it outputs 'NO'.

