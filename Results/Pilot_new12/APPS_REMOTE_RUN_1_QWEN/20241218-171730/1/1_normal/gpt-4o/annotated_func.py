#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters and the characters '[', ']', ':', and '|'. The length of s is between 1 and 500000, inclusive.
def func():
    s = input()
    n = len(s)
    ind = -1
    for i in range(n):
        if s[i] == '[':
            ind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of lowercase Latin letters and the characters `[`, `]`, `:`, and `|`, `n` is the length of `s`, and `ind` is the index of the first `[` in the string `s`. If there is no `[` in the string `s`, `ind` remains -1 and unchanged.
    bind = -1
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            bind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of lowercase Latin letters and the characters `[`, `]`, `:`, and `|`, `n` is the length of `s`, `ind` can be any integer value (or -1 if there is no `[`), `bind` is the index of the last `]` character in the string `s` or -1 if there is no `]` in the string.
    if (ind == -1 or bind == -1 or ind >= bind) :
        print(-1)
    else :
        start_colon = -1
        for i in range(ind + 1, bind):
            if s[i] == ':':
                start_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is an input string consisting of lowercase Latin letters and the characters `[`, `]`, `:`, and `|`, `n` is the length of `s`, `ind` is not -1, `bind` is not -1, `ind` is less than `bind`, `ind + 1` is a valid index, `bind` is the last index of the string, `start_colon` is equal to the index of the first `:` found in the substring from `ind + 1` to `bind`, or remains `-1` if no `:` is found.
        end_colon = -1
        for i in range(bind - 1, ind, -1):
            if s[i] == ':':
                end_colon = i
                break
            
        #State of the program after the  for loop has been executed: `ind` is not -1, `bind` is not -1, `ind` is less than `bind`, `start_colon` remains unchanged, `end_colon` is equal to the index of the last `:` found in the substring from `ind + 1` to `bind` (or remains `-1` if no `:` is found), `i` is `-1` if the loop does not execute, otherwise `i` is `ind + 1` if no `:` is found or `end_colon` if `s[i]` equals `':'
        if (start_colon == -1 or end_colon == -1 or start_colon >= end_colon) :
            print(-1)
        else :
            pipe_count = 0
            for i in range(start_colon + 1, end_colon):
                if s[i] == '|':
                    pipe_count += 1
                
            #State of the program after the  for loop has been executed: Output State:
            result = 4 + pipe_count
            print(result)
        #State of the program after the if-else block has been executed: *`ind` is not -1, `bind` is not -1, `ind` is less than `bind`, `start_colon` remains unchanged, `end_colon` is equal to the index of the last `:` found in the substring from `ind + 1` to `bind` (or remains `-1` if no `:` is found), `i` is `-1` if the loop does not execute, otherwise `i` is `ind + 1` if no `:` is found or `end_colon` if `s[i]` equals `':'`, and either `start_colon` is `-1` or `end_colon` is `-1` or `start_colon` is greater than or equal to `end_colon`, and `result` is `4 + pipe_count`, `pipe_count` is its original value, and the value of `result` is printed.
    #State of the program after the if-else block has been executed: *`s` is an input string consisting of lowercase Latin letters and the characters `[`, `]`, `:`, and `|`, `n` is the length of `s`, `ind` is an integer value, `bind` is the index of the last `]` character in the string `s` or -1 if there is no `]` in the string. If `ind == -1` or `bind == -1` or `ind >= bind`, -1 is printed to the console. Otherwise, `ind` is not -1, `bind` is not -1, `ind` is less than `bind`, `start_colon` remains unchanged, `end_colon` is equal to the index of the last `:` found in the substring from `ind + 1` to `bind` (or remains `-1` if no `:` is found), `i` is `-1` if the loop does not execute, otherwise `i` is `ind + 1` if no `:` is found or `end_colon` if `s[i]` equals `':'`, and either `start_colon` is `-1` or `end_colon` is `-1` or `start_colon` is greater than or equal to `end_colon`, and `result` is `4 + pipe_count`, `pipe_count` is its original value, and the value of `result` is printed.
#Overall this is what the function does:The function processes a string `s` consisting of lowercase Latin letters and the characters `[`, `]`, `:`, and `|`. It aims to find the first occurrence of `[` and the last occurrence of `]` within the string. Then, it searches for the first and last occurrences of `:` within the substring between these two brackets. If any of these characters do not exist in the specified order or positions, the function prints `-1`. Otherwise, it counts the number of `|` characters between the first and last `:` found within the bracketed substring and adds 4 to this count, then prints the result.

