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
        
    #State: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4; i is t-1; string is the last input string; s is a list of characters from the last input string; n is the length of s; x is s[0]; j is n; count is the number of characters not equal to x before the first occurrence of a different character; count2 is the number of characters not equal to x after the first occurrence of a different character; done is False or True based on the last iteration; and the condition not done is true if done is False, otherwise no further action is taken.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a string of lowercase Latin characters. For each string, it determines whether it is possible to split the string into two non-empty parts such that the resulting parts are not palindromes and prints 'YES' along with the split positions if possible, otherwise prints 'NO'.

