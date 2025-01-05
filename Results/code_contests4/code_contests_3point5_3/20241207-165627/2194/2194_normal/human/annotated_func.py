#State of the program right berfore the function call: n is a positive integer between 1 and 10^18 without leading zeroes.**
def func():
    s = str(input())
    if (int(s) % 25 == 0) :
        print(0)
    else :
        zero = s.count('0')
        five = s.count('5')
        two = s.count('2')
        seven = s.count('7')
        fin = 10 ** 18
        if (zero >= 2) :
            t = list(s)
            n = len(t)
            ans = 0
            cnt = 0
            for i in xrange(n - 1, -1, -1):
                if t[i] == '0':
                    if cnt == 0:
                        ans += n - 1 - i
                        cnt += 1
                    elif cnt == 1:
                        ans += n - 2 - i
                        cnt += 1
                        break
                
            #State of the program after the  for loop has been executed: n is the length of list t, s is a string input, zero, five, two, seven are the counts of '0', '5', '2', '7' characters in string s respectively, fin is 10^18, t is a list containing characters of string s, ans is either equal to the sum of n - 1 - i and n - 2 - i where i ranges from n - 1 to 0, or it remains 0 if the conditions in the loop are not satisfied, and cnt is either 1 or 0 based on the conditions met during each iteration.
            fin = min(fin, ans)
        #State of the program after the if block has been executed: *n is a positive integer between 1 and 10^18 without leading zeroes, s is a string input, zero, five, two, seven are the counts of '0', '5', '2', '7' characters in string s respectively, fin is 10^18. If zero >= 2, the list t contains characters of string s, ans is either the sum of n - 1 - i and n - 2 - i where i ranges from n - 1 to 0, or it remains 0, and cnt is either 1 or 0 based on the conditions met during each iteration.
        if (two >= 1 and five >= 1) :
            t = list(s)
            n = len(t)
            ans = 0
            for i in xrange(n - 1, -1, -1):
                if t[i] == '5':
                    break
                
            #State of the program after the  for loop has been executed: n is the length of list t, ans is 0, n is greater than 0. If '5' is not found in the list t, ans remains 0 after the loop execution. If '5' is found in the list t, the loop breaks when encountering '5' and ans remains 0.
            for j in xrange(i, n - 1):
                ans += 1
                
                temp = t[j + 1]
                
                t[j + 1] = t[j]
                
                t[j] = temp
                
            #State of the program after the  for loop has been executed: n is the length of list t, ans is increased by (n-1), '5' is not found in list t, i is a valid index and is equal to n-1, n is greater than i+1, temp is assigned the value of t[j]
            for i in xrange(n - 2, -1, -1):
                if t[i] == '2':
                    break
                
            #State of the program after the  for loop has been executed: n is the length of list t, ans is increased by n, '5' is not found in list t, i is equal to -1, n is greater than n-1, temp is assigned the value of t[j] for the loop to execute the last time. If t[i] == '2', then the loop breaks out of the most internal loop or if statement.
            for j in xrange(i, n - 2):
                ans += 1
                
                temp = t[j + 1]
                
                t[j + 1] = t[j]
                
                t[j] = temp
                
            #State of the program after the  for loop has been executed: `n` is the length of list `t`, `ans` is increased by `n * (n - 1) / 2`, '5' is not found in list `t`, `i` is equal to `n - 2`, `n` is greater than or equal to n-2, `temp` is assigned the value of `t[j]` for the loop to execute the last time
            if (t[0] == '0') :
                if (n == 3) :
                    ans = 10 ** 15
                else :
                    for i in xrange(n - 3):
                        if t[i] != '0':
                            break
                        
                        ans += 1
                        
                    #State of the program after the  for loop has been executed: `n` is greater than or equal to 3, `i` is equal to `n - 3`, `ans` is increased by `n * (n - 1) / 2 + (n - 3)`, '5' is not found in list `t`, `temp` is assigned the value of `t[j]` for the loop to execute the last time, the first element of list `t` is '0'
                #State of the program after the if-else block has been executed: *`n` is the length of list `t`, `ans` is increased by `n * (n - 1) / 2`, '5' is not found in list `t`, `i` is equal to `n - 2`, `n` is greater than or equal to `n-2`, `temp` is assigned the value of `t[j]` for the loop to execute the last time, and the first element of list `t` is '0'. If `n` is equal to 3, `ans` is assigned the value 10. Otherwise, if `n` is greater than or equal to 3, `i` is equal to `n - 3`, `ans` is increased by `n * (n - 1) / 2 + (n - 3)`.
            #State of the program after the if block has been executed: *`n` is the length of list `t`, `ans` is increased by `n * (n - 1) / 2`, '5' is not found in list `t`, `i` is equal to `n - 2`, `n` is greater than or equal to n-2, `temp` is assigned the value of `t[j]` for the loop to execute the last time, and the first element of list `t` is '0'. If `n` is equal to 3, `ans` is assigned the value 10. Otherwise, if `n` is greater than or equal to 3, `i` is equal to `n - 3`, `ans` is increased by `n * (n - 1) / 2 + (n - 3)`.
            fin = min(fin, ans)
        #State of the program after the if block has been executed: *n is a positive integer between 1 and 10^18 without leading zeroes. s is a string input where zero, five, two, seven are the counts of '0', '5', '2', '7' characters in string s respectively. fin is 10^18. If zero >= 2, the list t contains characters of string s, ans is either the sum of n - 1 - i and n - 2 - i where i ranges from n - 1 to 0, or it remains 0, and cnt is either 1 or 0 based on the conditions met during each iteration. If two >= 1 and five >= 1, n is the length of list t, ans is increased by n * (n - 1) / 2, '5' is not found in list t, i is equal to n - 2, n is greater than or equal to n-2, temp is assigned the value of t[j] for the loop to execute the last time, the first element of list t is '0', if n is equal to 3, ans is assigned the value 10, otherwise, if n is greater than or equal to 3, i is equal to n - 3, ans is increased by n * (n - 1) / 2 + (n - 3), fin is assigned the minimum value between fin and ans.
        if (seven >= 1 and five >= 1) :
            t = list(s)
            n = len(t)
            ans = 0
            for i in xrange(n - 1, -1, -1):
                if t[i] == '5':
                    break
                
            #State of the program after the  for loop has been executed: Output State: *n is the length of list t, ans is 0, n is greater than 0, i is equal to the first index of '5' in list t (if '5' exists in the list), t is a non-empty list. If '5' is found in list t, the loop breaks at that index. If '5' is not found in list t, then i is -1.
            for j in xrange(i, n - 1):
                ans += 1
                
                temp = t[j + 1]
                
                t[j + 1] = t[j]
                
                t[j] = temp
                
            #State of the program after the  for loop has been executed: n is the length of list t, ans is equal to n - i - 1, n is greater than 0, i is equal to the first index of '5' in list t (if '5' exists in the list) or -1, t is a non-empty list. If '5' is found in the list, the loop will break at that index. If '5' is not found, the loop will continue until j reaches n - 2.
            for i in xrange(n - 2, -1, -1):
                if t[i] == '7':
                    break
                
            #State of the program after the  for loop has been executed: n is the length of list t, ans is equal to 1, n is greater than 0, i is equal to the first index of '7' in list t (if '7' exists in the list) or -1, t is a non-empty list. If '7' is found in the list, the loop will break at that index. If '7' is not found, the loop will continue until i reaches -1.
            for j in xrange(i, n - 2):
                ans += 1
                
                temp = t[j + 1]
                
                t[j + 1] = t[j]
                
                t[j] = temp
                
            #State of the program after the  for loop has been executed: Output State: n is the length of list t, ans is equal to n - i + 1, n is greater than 0, i is the index of the first occurrence of '7' in list t (if '7' exists) or -1, t is a non-empty list. If '7' is not found in the list, the values in the list t will be shifted accordingly.
            if (t[0] == '0') :
                if (n == 3) :
                    ans = 10 ** 15
                else :
                    for i in xrange(n - 3):
                        if t[i] != '0':
                            break
                        
                        ans += 1
                        
                    #State of the program after the  for loop has been executed: n is the length of list t, ans is equal to n - i + 4, n is greater than 3, i is the new index of the first occurrence of '7' in list t (if '7' exists) or -1, t is a non-empty list with the first element being '0' and i is less than n - 3. If '7' is not found in the list, the values in the list t will be shifted accordingly.
                #State of the program after the if-else block has been executed: *Output State: n is the length of list t, ans is equal to n - i + k, n is greater than 0, i is the index of the first occurrence of '7' in list t (if '7' exists) or -1, t is a non-empty list. The first element of list t is '0'. If '7' is not found in the list, the values in the list t will be shifted accordingly. If n equals 3, ans is 10^15. If n is greater than 3, ans is equal to n - i + 4. If i is less than n - 3, then i is the new index of the first occurrence of '7' in list t (if '7' exists) or -1.
            #State of the program after the if block has been executed: *Output State: n is the length of list t, ans is equal to n - i + k, n is greater than 0, i is the index of the first occurrence of '7' in list t (if '7' exists) or -1, t is a non-empty list. If the first element of list t is '0', then if n equals 3, ans is 10^15. If n is greater than 3, ans is equal to n - i + 4. If i is less than n - 3, then i is the new index of the first occurrence of '7' in list t (if '7' exists) or -1.
            fin = min(fin, ans)
        #State of the program after the if block has been executed: *n is a positive integer between 1 and 10^18 without leading zeroes. s is a string input where zero, five, two, seven are the counts of '0', '5', '2', '7' characters in string s respectively. If seven >= 1 and five >= 1, n is the length of list t, ans is equal to n - i + k, i is the index of the first occurrence of '7' in list t (if '7' exists) or -1. If the first element of list t is '0', then if n equals 3, ans is 10^15. If n is greater than 3, ans is equal to n - i + 4. If i is less than n - 3, then i is the new index of the first occurrence of '7' in list t (if '7' exists) or -1. The variable `fin` is updated to the minimum value between its current value and `ans`.
        if (zero >= 1 and five >= 1) :
            t = list(s)
            n = len(t)
            ans = 0
            for i in xrange(n - 1, -1, -1):
                if t[i] == '0':
                    break
                
            #State of the program after the  for loop has been executed: `ans` is 0, `n` is a positive integer between 1 and 10^18 without leading zeroes, `s` is a string, zero >= 1, five >= 1, two, seven are the counts of '0', '5', '2', '7' characters in string s respectively, i is an integer, `t` is a list of characters from string `s`, `fin` is updated to the minimum value between its current value and `ans`. The loop does not execute, so all variables remain in their initial state.
            for j in xrange(i, n - 1):
                ans += 1
                
                temp = t[j + 1]
                
                t[j + 1] = t[j]
                
                t[j] = temp
                
            #State of the program after the  for loop has been executed: `ans` is increased by `n - i - 1`, `n` is a positive integer between 1 and 10^18 without leading zeroes, `s` is a string, zero >= 1, five >= 1, two, seven are the counts of '0', '5', '2', '7' characters in string s respectively, `i` is greater than or equal to `n - 1, `t` is a list of characters from string `s`, `fin` is updated to the minimum value between its current value and `ans`, `temp` is assigned the value of `t[n - 1]`
            for i in xrange(n - 2, -1, -1):
                if t[i] == '5':
                    break
                
            #State of the program after the  for loop has been executed: `ans` is 1, `n` is a positive integer between 2 and 10^18, `s` is a string, `zero` >= 1, `five` >= 1, `two`, `seven` are the counts of '0', '5', '2', '7' characters in string `s` respectively, `i` is 0, `t` is a list of characters from string `s`, `fin` is updated to the minimum value between its current value and `ans`, `temp` is assigned the value of `t[n - 1] and `t[i]` is not equal to '5'.
            for j in xrange(i, n - 2):
                ans += 1
                
                temp = t[j + 1]
                
                t[j + 1] = t[j]
                
                t[j] = temp
                
            #State of the program after the  for loop has been executed: `ans` will be increased by `n - 2` times, `n` will remain a positive integer between 2 and 10^18, `s` will be a non-empty string, `zero` will remain greater than or equal to 1, `five` will remain greater than or equal to 1, `two` and `seven` will be the counts of '0' and '5', '2', '7' characters in string `s` respectively, `i` will be `n - 2`, `t` will be a non-empty list of characters from string `s`, `fin` will be updated to the minimum value between its current value and `ans`, `temp` will be assigned the value of `t[n - 2]`, `t[n - 2]` will be equal to `temp`.
            if (t[0] == '0') :
                if (n == 3) :
                    ans = 10 ** 15
                else :
                    for i in xrange(n - 3):
                        if t[i] != '0':
                            break
                        
                        ans += 1
                        
                    #State of the program after the  for loop has been executed: `ans` will be increased by `n - 2` times, `n` will remain a positive integer between 2 and 10^18, `s` will be a non-empty string, `zero` will remain greater than or equal to 1, `five` will remain greater than or equal to 1, `two` and `seven` will be the counts of '0', '5', '2', '7' characters in string `s` respectively, `i` will be 0, `t` will be a list of characters from string `s` starting with '0', `fin` will be updated to the minimum value between its current value and `ans`, `temp` will be assigned the last character of `t`, `t[n - 2]` will be equal to `temp`, the loop will not execute as `n` is not equal to 3
                #State of the program after the if-else block has been executed: *`ans` will be increased by 10^15 times if `n` equals 3, otherwise `ans` will be increased by `n - 2` times. `n` will remain a positive integer between 2 and 10^18, `s` will be a non-empty string, `zero` will remain greater than or equal to 1, `five` will remain greater than or equal to 1, `two` and `seven` will be the counts of '0', '5', '2', '7' characters in string `s` respectively, `i` will be `n - 2` if `n` equals 3, otherwise `i` will be 0, `t` will be a list of characters from string `s`, with the first element being '0' if `n` equals 3, otherwise `t` will start with '0'. `fin` will be updated to the minimum value between its current value and `ans`. `temp` will be assigned the value of `t[n - 2]` in both cases, and `t[n - 2]` will be equal to `temp`.
            #State of the program after the if block has been executed: *`ans` is increased by 10^15 times if `n` equals 3, otherwise `ans` is increased by `n - 2` times. `n` remains a positive integer between 2 and 10^18, `s` is a non-empty string, `zero` remains greater than or equal to 1, `five` remains greater than or equal to 1, `two` and `seven` are the counts of '0', '5', '2', '7' characters in string `s` respectively. `i` is `n - 2` if `n` equals 3, otherwise `i` is 0. `t` is a list of characters from string `s`, with the first element being '0' if `n` equals 3, otherwise `t` starts with '0'. `fin` is updated to the minimum value between its current value and `ans`. `temp` is assigned the value of `t[n - 2]` in both cases, and `t[n - 2]` is equal to `temp` after the execution of the if else block.
            fin = min(fin, ans)
        #State of the program after the if block has been executed: *`n` is a positive integer between 1 and 10^18 without leading zeroes. `s` is a non-empty string where zero, five, two, seven are the counts of '0', '5', '2', '7' characters in string `s` respectively. If both zero and five are greater than or equal to 1, `ans` is increased by 10^15 times if `n` equals 3, otherwise `ans` is increased by `n - 2` times. The variable `fin` is updated to the minimum value between its current value and `ans`.
        if (fin > 10 ** 10) :
            print(-1)
        else :
            print(fin)
        #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 10^18 without leading zeroes. `s` is a non-empty string where zero, five, two, seven are the counts of '0', '5', '2', '7' characters in string `s` respectively. If both zero and five are greater than or equal to 1, `ans` is increased by 10^15 times if `n` equals 3, otherwise `ans` is increased by `n - 2` times. The variable `fin` is updated to the minimum value between its current value and `ans`. If `fin` is greater than 10^10, then `fin` retains its current value. If `fin` is not greater than 10^10, then `fin` retains its current value.
    #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 10^18 without leading zeroes. If the integer value of `s` is divisible by 25, then the program executes the if part. Otherwise, the program executes the else part where `n` is a positive integer between 1 and 10^18 without leading zeroes. `s` is a non-empty string with counts of '0', '5', '2', '7' characters in string `s` denoted by zero, five, two, seven respectively. If zero and five are both greater than or equal to 1, `ans` is increased by 10^15 times if `n` equals 3, otherwise `ans` is increased by `n - 2` times. The variable `fin` is updated to the minimum value between its current value and `ans`. If `fin` is greater than 10^10, then `fin` retains its current value. If `fin` is not greater than 10^10, then `fin` retains its current value.
#Overall this is what the function does:The function `func` reads a string input and performs various calculations based on the occurrences of '0', '5', '2', '7' characters in the string. It then updates and prints the minimum value calculated. The function is intended to handle cases where certain characters are present multiple times in the input string and adjust the calculations accordingly to find the minimum value. The code includes multiple loops to iterate through the string and perform specific operations based on the characters found. The final output is either the calculated minimum value or -1 if it exceeds 10^10. The function does not accept any parameters explicitly, and the user is expected to provide a string input.

