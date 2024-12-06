#State of the program right berfore the function call: s is a string consisting of characters from the set {lowercase Latin letters, [, ], :, |}, with a length between 1 and 500000.
def func():
    s = input()
    n = len(s)
    ind = -1
    for i in range(n):
        if s[i] == '[':
            ind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is an input string, `n` is the length of `s` (a positive integer between 1 and 500000), `ind` is the index of the first occurrence of '[' if it exists, otherwise `ind` is -1, `i` is the last index checked (either `ind` if '[' was found or `n - 1` if not found).
    bind = -1
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            bind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is an input string, `n` is a positive integer between 1 and 500000, `ind` is -1 or a valid index, `i` is -1, and `bind` is the index of the last occurrence of ']' or -1 if ']' is not present in `s`.
    if (ind == -1 or bind == -1 or ind >= bind) :
        print(-1)
    else :
        start_colon = -1
        for i in range(ind + 1, bind):
            if s[i] == ':':
                start_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is an input string, `n` is a positive integer between 1 and 500000, `ind` is a valid index, `i` is `bind`, `bind` is the index of the last occurrence of ']' or -1 if ']' is not present in `s`, `ind` is not equal to -1, `bind` is not equal to -1, `ind` is less than `bind`, and `start_colon` is set to the index of the first occurrence of ':' after `ind` within the bounds defined by `bind`, or remains -1 if no ':' is found in that range.
        end_colon = -1
        for i in range(bind - 1, ind, -1):
            if s[i] == ':':
                end_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is an input string, `n` is a positive integer between 1 and 500000, `ind` is a valid index, `bind` is at least `ind + 2`, `end_colon` is either the index of the first colon (`:`) found in the range from `bind - 1` down to `ind + 1`, or remains -1 if no colon is found, `i` is `ind + 1` (after the loop completes the last decrement).
        if (start_colon == -1 or end_colon == -1 or start_colon >= end_colon) :
            print(-1)
        else :
            pipe_count = 0
            for i in range(start_colon + 1, end_colon):
                if s[i] == '|':
                    pipe_count += 1
                
            #State of the program after the  for loop has been executed: `s` is an input string, `n` is a positive integer between 1 and 500000, `ind` is a valid index, `bind` is at least `ind + 2`, `end_colon` is at least `start_colon + 2`, `pipe_count` is the number of '|' characters found between `start_colon + 1` and `end_colon - 1`, and `i` is equal to `end_colon`. If the loop does not execute, then `pipe_count` remains 0.
            result = 4 + pipe_count
            print(result)
        #State of the program after the if-else block has been executed: *`s` is an input string, `n` is a positive integer between 1 and 500000, `ind` is a valid index, `bind` is at least `ind + 2`, and if `start_colon == -1` or `end_colon == -1` or `start_colon >= end_colon`, the output is -1. Otherwise, `end_colon` is at least `start_colon + 2`, `pipe_count` is 0, `i` is equal to `end_colon`, `result` is 4, and the value 4 has been printed.
    #State of the program after the if-else block has been executed: *`s` is an input string, `n` is a positive integer between 1 and 500000, `ind` is -1 or a valid index, and `bind` is the index of the last occurrence of ']' or -1 if ']' is not present in `s`. If `ind` is -1, `bind` is -1, or `ind` is greater than or equal to `bind`, -1 has been printed. Otherwise, if `ind` is a valid index and `bind` is at least `ind + 2`, then if `start_colon` is -1, `end_colon` is -1, or `start_colon` is greater than or equal to `end_colon`, the output is -1; otherwise, `end_colon` is at least `start_colon + 2`, `pipe_count` is 0, `i` is equal to `end_colon`, `result` is 4, and the value 4 has been printed.
#Overall this is what the function does:The function accepts a string `s` composed of lowercase Latin letters and specific characters ('[', ']', ':', '|'). It searches for the first occurrence of '[' and the last occurrence of ']', along with colons (':') between these brackets. If the conditions are met, it counts the number of pipes ('|') between the first colon after '[' and the last colon before ']', and returns this count plus 4. If any of the required characters are not found or the indices are not in the correct order, it returns -1.

