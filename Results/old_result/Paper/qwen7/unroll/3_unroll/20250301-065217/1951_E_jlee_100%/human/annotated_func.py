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
        
    #State: Output State: The value of `t` is reduced to 0, and no changes are made to the input integer `t`. For each iteration of the loop, based on the conditions provided in the loop body, either 'YES' or 'NO' is printed along with some additional information, and the loop continues to the next iteration until `t` reaches 0. The final state of `t` is 0, and the output consists of the printed results from each iteration.
#Overall this is what the function does:The function processes a series of test cases where each test case includes an integer `t` and a string `s`. For each test case, it checks specific conditions related to the string `s` and prints either 'YES' or 'NO' along with additional information if applicable. After processing all test cases, the function ensures that the counter `t` is reduced to 0, and the output consists of the printed results for each test case.

