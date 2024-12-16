#State of the program right berfore the function call: The input string s consists of lowercase Latin letters and characters [, ], :, and |, and its length is between 1 and 500000 inclusive.
def func():
    s = input()
    n = len(s)
    ind = -1
    for i in range(n):
        if s[i] == '[':
            ind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is a string input by the user, `n` is the length of `s`, `ind` is either equal to `-1` (if no character `[` is found in `s`) or equal to the index of the first occurrence of `[` in `s`.
    bind = -1
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            bind = i
            break
        
    #State of the program after the  for loop has been executed: `total` is 0, `i` is `-1`, `n` is the original length of `s`, `ind` is the index of the first occurrence of `[` in `s` (or `-1` if `[` is not present), `bind` is the index of the last occurrence of `]` in `s` (or `-1` if no `]` is present).
    if (ind == -1 or bind == -1 or ind >= bind) :
        print(-1)
    else :
        start_colon = -1
        for i in range(ind + 1, bind):
            if s[i] == ':':
                start_colon = i
                break
            
        #State of the program after the  for loop has been executed: `total` is 0, `i` is `bind` (if `start_colon` is set), `ind` is a non-negative integer (original value), `bind` is a non-negative integer (original value), `start_colon` is either `ind + 1` (if a colon is found) or `-1` (if no colon is found).
        end_colon = -1
        for i in range(bind - 1, ind, -1):
            if s[i] == ':':
                end_colon = i
                break
            
        #State of the program after the  for loop has been executed: `total` is 0, `i` is `-1`, `ind` is a non-negative integer and must be less than `bind`, `start_colon` is `ind + 1`, `end_colon` is the index of the last colon found during the loop execution or `-1` if no colon is found.
        if (start_colon == -1 or end_colon == -1 or start_colon >= end_colon) :
            print(-1)
        else :
            pipe_count = 0
            for i in range(start_colon + 1, end_colon):
                if s[i] == '|':
                    pipe_count += 1
                
            #State of the program after the  for loop has been executed: `total` is 0, `i` is `end_colon`, `ind` is a non-negative integer, `start_colon` is `ind + 1`, `end_colon` is a valid index greater than `start_colon`, and `pipe_count` is the number of `'|'` characters in the substring `s[start_colon + 1:end_colon]`
            result = 4 + pipe_count
            print(result)
        #State of the program after the if-else block has been executed: *`total` is 0, `i` is -1, `ind` is a non-negative integer and must be less than `bind`. If `start_colon` is -1, `end_colon` is -1, or `start_colon` is greater than or equal to `end_colon`, the console prints `-1`. Otherwise, `i` is `end_colon`, `start_colon` is `ind + 1`, `end_colon` is a valid index greater than `start_colon`, and `result` is `4 + pipe_count`, where `pipe_count` is the number of `'|'` characters in the substring `s[start_colon + 1:end_colon]` (result is printed).
    #State of the program after the if-else block has been executed: `total` is 0, `i` is -1, `n` is the original length of `s`, `ind` is the index of the first occurrence of `[` in `s` (or -1 if `[` is not present), `bind` is the index of the last occurrence of `]` in `s` (or -1 if no `]` is present). If `[` and `]` do not exist or `ind` is greater than or equal to `bind`, then -1 is printed to the console. Otherwise, `i` is set to `end_colon`, `start_colon` is set to `ind + 1`, `end_colon` is a valid index greater than `start_colon`, and the result, which is `4 + pipe_count`, is printed, where `pipe_count` is the number of `'|'` characters in the substring `s[start_colon + 1:end_colon]`.
#Overall this is what the function does:The function processes an input string `s` consisting of lowercase Latin letters and characters `[`, `]`, `:`, and `|`. It finds the indices of the first `[` and last `]`, and then looks for the first `:` within the substring defined by these indices. If a `:` is found, it then searches for the last `:` within the same substring. If both `:` are found and their positions are correct, it counts the number of `|` characters between them and calculates the result as `4 + pipe_count`. If any of the necessary characters are missing or the indices are incorrect, it prints `-1`.

