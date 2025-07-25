#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters and the characters [, ], : and |, with a length between 1 and 500,000.
def func():
    s = input()
    n = len(s)
    ind = -1
    for i in range(n):
        if s[i] == '[':
            ind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and specific characters, `n` is the length of `s` which is greater than or equal to 0, `ind` is the index of the first occurrence of '[' in `s` if it exists, or remains -1 if '[' is not present in `s`.
    bind = -1
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            bind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and specific characters, `n` is greater than or equal to 0, `ind` is the index of the first occurrence of '[' in `s`, `bind` is the index of the last occurrence of ']' if it exists, otherwise it remains -1, `i` is the last index checked, which will be -1 if the loop does not execute.
    if (ind == -1 or bind == -1 or ind >= bind) :
        print(-1)
    else :
        start_colon = -1
        for i in range(ind + 1, bind):
            if s[i] == ':':
                start_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and specific characters; `n` is greater than or equal to 0; `ind` is the index of the first occurrence of '[' in `s`; `bind` is the index of the last occurrence of ']' in `s' which is greater than `ind + 1`; `i` is `bind`, and `start_colon` is the index of the first occurrence of ':' after `ind` and before `bind` if such a colon exists, otherwise `start_colon` will remain -1.
        end_colon = -1
        for i in range(bind - 1, ind, -1):
            if s[i] == ':':
                end_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and specific characters, `n` is greater than or equal to 0, `ind` is the index of the first occurrence of '[' in `s`, `bind` is the index of the last occurrence of ']' in `s' which is greater than `ind + 1`, `end_colon` is the index of the first occurrence of ':' after `ind` and before `bind`, which can be -1 if no colon exists; `i` will be less than or equal to `ind` but greater than or equal to `bind - 1` after all iterations. If `end_colon` is updated, it is set to the index of the colon, otherwise it remains -1. The loop will execute at least once only if there is at least one character ':' between `ind` and `bind`.
        if (start_colon == -1 or end_colon == -1 or start_colon >= end_colon) :
            print(-1)
        else :
            pipe_count = 0
            for i in range(start_colon + 1, end_colon):
                if s[i] == '|':
                    pipe_count += 1
                
            #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and specific characters, `n` is greater than or equal to 0, `ind` is the index of the first occurrence of '[', `bind` is the index of the last occurrence of ']' which is greater than `ind + 1`, `end_colon` is the index of the first occurrence of ':' after `ind` and before `bind`, `start_colon` is the index of the first occurrence of ':' before `end_colon`, `start_colon` is less than `end_colon`, and `pipe_count` is the count of '|' characters found in the substring between `start_colon` and `end_colon` (exclusive).
            result = 4 + pipe_count
            print(result)
        #State of the program after the if-else block has been executed: *`s` is a string of lowercase Latin letters and specific characters, `n` is greater than or equal to 0, `ind` is the index of the first occurrence of '[', `bind` is the index of the last occurrence of ']', and `end_colon` is the index of the first occurrence of ':' after `ind` and before `bind`. If either `start_colon` or `end_colon` is -1, or if `start_colon` is greater than or equal to `end_colon`, then -1 has been printed. Otherwise, `start_colon` is the index of the first occurrence of ':' before `end_colon`, `start_colon` is less than `end_colon`, `pipe_count` is the count of '|' characters found in the substring between `start_colon` and `end_colon` (exclusive), `result` is equal to `4 + pipe_count`, and the value of `result` has been printed.
    #State of the program after the if-else block has been executed: *`s` is a string of lowercase Latin letters and specific characters, `n` is greater than or equal to 0, `ind` is the index of the first occurrence of '[', `bind` is the index of the last occurrence of ']', `i` is the last index checked, which will be -1 if the loop does not execute. If `ind` is -1, `bind` is -1, and `i` is -1, then -1 has been printed. Otherwise, if `start_colon` or `end_colon` is -1, or if `start_colon` is greater than or equal to `end_colon`, then -1 has been printed. If `start_colon` is valid and less than `end_colon`, `pipe_count` is the count of '|' characters found in the substring between `start_colon` and `end_colon` (exclusive), `result` is equal to `4 + pipe_count`, and the value of `result` has been printed.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters along with the characters `[`, `]`, `:`, and `|`. It searches for the first occurrence of `[` and the last occurrence of `]` in the string. If either bracket is missing, or if the order is invalid (i.e., `[` appears after `]`), it prints `-1`. It then looks for the first `:` after the `[` and the last `:` before the `]`. If these colons are not found, or if the order is invalid, it again prints `-1`. If valid colons are found, it counts the number of `|` characters between these two colons and prints the result as `4 + pipe_count`. If no valid structure is found, it will print `-1`. The function does not handle unexpected characters and relies on the structure of `s` being specifically in line with its expectations.

