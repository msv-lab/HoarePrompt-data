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
        
    #State: Output State: The value of `t` is an integer between 1 and 10^4. For each input string `string` of length `n`, the program checks various conditions to determine if the string can be split into two parts such that each part is a palindrome or if the entire string is a palindrome with one character differing from the others. Based on these conditions, the program prints either 'YES' or 'NO' along with additional details if applicable. After processing all `t` strings, the final state of `t` remains unchanged, but the printed outputs (either 'YES' or 'NO' with possible additional details) reflect the results of each string's evaluation.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of a string `s` of lowercase Latin characters. For each string, it checks if the string can be split into two palindromic parts or if the entire string is a palindrome with at most one character differing from the others. If such a condition is met, it prints 'YES' along with additional details; otherwise, it prints 'NO'. The function does not return any value but produces output based on the conditions checked for each string.

