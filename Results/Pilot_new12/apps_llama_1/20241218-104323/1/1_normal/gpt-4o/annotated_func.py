#State of the program right berfore the function call: The input is a string s consisting of lowercase Latin letters and the characters [, ], :, |, with a length between 1 and 500000 (inclusive).
def func():
    s = input()
    n = len(s)
    ind = -1
    for i in range(n):
        if s[i] == '[':
            ind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and the characters [, ], :, |, with a length between 1 and 500000 (inclusive), `n` is an integer equal to the length of `s`, `ind` is either -1 if no '[' character is found in `s`, or the index of the first '[' character in `s` if it exists.
    bind = -1
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            bind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and the characters [, ], :, |, with a length between 1 and 500000 (inclusive), `n` is an integer equal to the length of `s`, `ind` is either -1 or the index of the first '[' character in the original string `s`, `bind` is either -1 or the index of the last ']' character in `s`.
    if (ind == -1 or bind == -1 or ind >= bind) :
        print(-1)
    else :
        start_colon = -1
        for i in range(ind + 1, bind):
            if s[i] == ':':
                start_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and the characters [, ], :, |, with a length between 1 and 500000 (inclusive), `n` is an integer equal to the length of `s`, `ind` is the index of the first '[' character in the original string `s`, `bind` is the index of the last ']' character in `s`, `ind` is not equal to -1, `bind` is not equal to -1, `ind` is less than `bind`, and `start_colon` is either -1 if no colon is found in `s[ind + 1:bind]`, or the index of the first colon found in `s[ind + 1:bind]`.
        end_colon = -1
        for i in range(bind - 1, ind, -1):
            if s[i] == ':':
                end_colon = i
                break
            
        #State of the program after the  for loop has been executed: 
        if (start_colon == -1 or end_colon == -1 or start_colon >= end_colon) :
            print(-1)
        else :
            pipe_count = 0
            for i in range(start_colon + 1, end_colon):
                if s[i] == '|':
                    pipe_count += 1
                
            #State of the program after the  for loop has been executed: `start_colon` and `end_colon` are integers, neither `start_colon` nor `end_colon` is -1, `start_colon` is less than `end_colon`, `i` equals `end_colon - 1`, and `pipe_count` equals the number of '|' characters in string `s` from index `start_colon + 1` to `end_colon - 1`. If `start_colon` is not less than `end_colon - 1`, then the loop does not execute, and `pipe_count` remains 0.
            result = 4 + pipe_count
            print(result)
        #State of the program after the if-else block has been executed: *`start_colon` and `end_colon` have values. If at least one of the conditions is true: `start_colon` equals -1, `end_colon` equals -1, or `start_colon` is greater than or equal to `end_colon`, then the value -1 is returned. Otherwise, `start_colon` and `end_colon` are integers, neither `start_colon` nor `end_colon` is -1, `start_colon` is less than `end_colon`, and the value of `result`, which equals 4 plus the number of '|' characters in string `s` from index `start_colon + 1` to `end_colon - 1`, is printed.
    #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase Latin letters and the characters [, ], :, |, with a length between 1 and 500000 (inclusive), `n` is an integer equal to the length of `s`, `ind` is either -1 or the index of the first '[' character in the original string `s`, `bind` is either -1 or the index of the last ']' character in `s`. If `ind` equals -1, `bind` equals -1, or `ind` is greater than or equal to `bind`, then the value -1 is printed and returned. Otherwise, `start_colon` and `end_colon` have values. If at least one of the conditions is true: `start_colon` equals -1, `end_colon` equals -1, or `start_colon` is greater than or equal to `end_colon`, then the value -1 is returned. If none of the above conditions are true, `start_colon` and `end_colon` are integers, neither `start_colon` nor `end_colon` is -1, `start_colon` is less than `end_colon`, and the value of `result`, which equals 4 plus the number of '|' characters in string `s` from index `start_colon + 1` to `end_colon - 1`, is printed.
#Overall this is what the function does:The function reads a string `s` as input and performs pattern matching to extract specific characters. It searches for the first occurrence of '[' and the last occurrence of ']' in the string, as well as the first and last occurrences of ':' within the substring defined by '[' and ']'. If any of these characters are not found or are out of order, it prints -1. Otherwise, it counts the number of '|' characters between the first and last ':' characters and adds 4 to this count, printing the result. The function effectively validates the input string's format and calculates a value based on its contents, specifically: 
- It requires the input string to contain '[' and ']' characters with '[' appearing before ']'. 
- It requires at least two ':' characters within the substring defined by '[' and ']', with the first ':' appearing before the second ':'.
- If the input string does not meet these requirements, it outputs -1, indicating an invalid format.
- If the input string is valid, it outputs a value which is 4 plus the number of '|' characters between the first and last ':' characters.
- The function handles edge cases such as missing or out-of-order characters by printing -1.

