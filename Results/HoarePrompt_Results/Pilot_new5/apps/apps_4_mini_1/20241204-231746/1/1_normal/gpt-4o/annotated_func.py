#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters and the characters [, ], :, and |, with a length between 1 and 500,000.
def func():
    s = input()
    n = len(s)
    ind = -1
    for i in range(n):
        if s[i] == '[':
            ind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and the characters [, ], :, and |, with a length equal to `len(s)`; `n` is the length of `s`; `ind` is the index of the first occurrence of '[' in `s`, or -1 if '[' does not exist in `s`; `i` is equal to `n` if no '[' is found, indicating that the loop has checked all characters in `s`.
    bind = -1
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            bind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and the characters [, ], :, and |; `n` is greater than 0; `i` is -1 if no ']' is found; `bind` is the index of the last occurrence of ']' in `s`, or -1 if ']' does not exist.
    if (ind == -1 or bind == -1 or ind >= bind) :
        print(-1)
    else :
        start_colon = -1
        for i in range(ind + 1, bind):
            if s[i] == ':':
                start_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and the characters [, ], :, and |; `n` is greater than 0; `i` is equal to `bind`; `bind` is not -1; `ind` is less than `bind`; `start_colon` is the index of the first colon character found in the substring from `ind + 1` to `bind`, or -1 if no colon was found in that range.
        end_colon = -1
        for i in range(bind - 1, ind, -1):
            if s[i] == ':':
                end_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and the characters [, ], :, and |; `n` is greater than 0; `i` is between `ind + 1` and `bind - 1`; `bind` is not -1; `ind` is less than `bind`; `end_colon` is the index of the last colon character found in the substring from `ind + 1` to `bind - 1`, or -1 if no colon was found in that range.
        if (start_colon == -1 or end_colon == -1 or start_colon >= end_colon) :
            print(-1)
        else :
            pipe_count = 0
            for i in range(start_colon + 1, end_colon):
                if s[i] == '|':
                    pipe_count += 1
                
            #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and the characters [, ], :, and |; `n` is greater than 0; `i` is updated to `end_colon - 1`; `pipe_count` is the total number of '|' characters found in the substring of `s` from `start_colon + 1` to `end_colon - 1`; the conditions for `bind`, `ind`, `end_colon`, and `start_colon` remain valid. If no '|' characters are found, `pipe_count` remains 0.
            result = 4 + pipe_count
            print(result)
        #State of the program after the if-else block has been executed: *`s` is a string of lowercase Latin letters and the characters [, ], :, and |; `n` is greater than 0; `i` is between `ind + 1` and `bind - 1`; `bind` is not -1; `ind` is less than `bind`; if `start_colon` is -1, `end_colon` is -1, or `start_colon` is greater than or equal to `end_colon`, then -1 is printed. Otherwise, `i` is updated to `end_colon - 1`, `pipe_count` is the total number of '|' characters found in the substring of `s` from `start_colon + 1` to `end_colon - 1`, and `result`, which is equal to `4 + pipe_count`, has been printed.
    #State of the program after the if-else block has been executed: *`s` is a string of lowercase Latin letters and the characters [, ], :, and |; `n` is greater than 0; `i` is -1 if no ']' is found; `bind` is the index of the last occurrence of ']' in `s`, or -1 if ']' does not exist. If `ind` is -1 or `bind` is -1 or `ind` is greater than or equal to `bind`, the output is -1. Otherwise, with `i` between `ind + 1` and `bind - 1`, if `start_colon` is -1, `end_colon` is -1, or `start_colon` is greater than or equal to `end_colon`, -1 is printed. Otherwise, `i` is updated to `end_colon - 1`, the total number of '|' characters in the substring from `start_colon + 1` to `end_colon - 1` is counted as `pipe_count`, and `result`, equal to `4 + pipe_count`, is printed.
#Overall this is what the function does:The function accepts a string `s` that consists of lowercase Latin letters and the characters [, ], :, and |. It attempts to find the first occurrence of '[' and the last occurrence of ']' in the string. If these characters are not found or are in the wrong order, it returns -1. If valid, it then looks for the first ':' after the '[' and the last ':' before the ']', counting the number of '|' characters between these two colons. The function finally returns the count of '|' plus 4. If there are no colons or pipes in the relevant sections, it also returns -1.

