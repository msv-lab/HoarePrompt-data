#State of the program right berfore the function call: The input is a string s consisting of lowercase Latin letters and characters [, ], :, and |, with a length between 1 and 500000 (inclusive).
def func():
    s = input()
    n = len(s)
    ind = -1
    for i in range(n):
        if s[i] == '[':
            ind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and characters [, ], :, and |, with a length between 1 and 500000 (inclusive), `n` is an integer between 1 and 500000 (inclusive), `ind` is either -1 (if `s` does not contain the character '[') or the index of the first '[' character in `s` (if `s` contains the character '['), and `i` is `n-1` (since the loop iterates over the range `n`)
    bind = -1
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            bind = i
            break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and characters [, ], :, and |, with a length between 1 and 500000 (inclusive), `n` is an integer between 1 and 500000 (inclusive), `ind` is either -1 or the index of the first '[' character in `s`, `i` is -1, and `bind` is either the index of the first ']' character from the end of `s` or -1.
    if (ind == -1 or bind == -1 or ind >= bind) :
        print(-1)
    else :
        start_colon = -1
        for i in range(ind + 1, bind):
            if s[i] == ':':
                start_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and characters [, ], :, and |, with a length between 1 and 500000 (inclusive), `n` is an integer between 1 and 500000 (inclusive), `ind` is the index of the first '[' character in `s` and not -1, `bind` is the index of the first ']' character from the end of `s` and not -1, `i` is `bind - 1`, and `start_colon` is the index of the first ':' character in `s` between `ind + 1` and `bind - 1`, or -1 if no ':' character is found in the range.
        end_colon = -1
        for i in range(bind - 1, ind, -1):
            if s[i] == ':':
                end_colon = i
                break
            
        #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and characters [, ], :, and |, with a length between 1 and 500000 (inclusive), `n` is an integer between 1 and 500000 (inclusive), `ind` is the index of the first '[' character in `s`, `bind` is the index of the first ']' character from the end of `s`, `i` is `ind`, `start_colon` is the index of the first ':' character in `s` between `ind + 1` and `bind - 1` or -1 if no ':' character is found in the range, and `end_colon` is the index of the last ':' character in `s` between `bind - 1` and `ind` (inclusive) or -1 if no ':' character is found in this range.
        if (start_colon == -1 or end_colon == -1 or start_colon >= end_colon) :
            print(-1)
        else :
            pipe_count = 0
            for i in range(start_colon + 1, end_colon):
                if s[i] == '|':
                    pipe_count += 1
                
            #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and characters [, ], :, and |, with a length between 1 and 500000 (inclusive), `n` is an integer between 1 and 500000 (inclusive), `ind` is the index of the first '[' character in `s`, `bind` is the index of the first ']' character from the end of `s`, `start_colon` is the index of the first ':' character in `s` between `ind + 1` and `bind - 1`, `end_colon` is the index of the last ':' character in `s` between `bind - 1` and `ind` (inclusive), `i` is `end_colon - 1` if the loop executes, otherwise `i` remains as its initial value, and `pipe_count` is the total number of '|' characters in the substring of `s` from `start_colon + 1` to `end_colon - 1`.
            result = 4 + pipe_count
            print(result)
        #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase Latin letters and characters [, ], :, and |, with a length between 1 and 500000 (inclusive), `n` is an integer between 1 and 500000 (inclusive), `ind` is the index of the first '[' character in `s`, `bind` is the index of the first ']' character from the end of `s`. If `start_colon == -1`, `end_colon == -1`, or `start_colon >= end_colon`, then -1 has been printed. Otherwise, `start_colon` is the index of the first ':' character in `s` between `ind + 1` and `bind - 1`, `end_colon` is the index of the last ':' character in `s` between `bind - 1` and `ind` (inclusive), `i` is `end_colon - 1` if the loop executes, otherwise `i` remains as its initial value, `pipe_count` is the total number of '|' characters in the substring of `s` from `start_colon + 1` to `end_colon - 1`, `result` is `4 + pipe_count`, and the value of `result` has been printed.
    #State of the program after the if-else block has been executed: `s` is a string consisting of lowercase Latin letters and characters [, ], :, and |, with a length between 1 and 500000 (inclusive), `n` is an integer between 1 and 500000 (inclusive), if `ind` is -1 or `bind` is -1 or `ind` is greater than or equal to `bind`, then the value -1 has been printed. Otherwise, `ind` is the index of the first '[' character in `s`, `bind` is the index of the first ']' character from the end of `s`, and if `start_colon` is -1 or `end_colon` is -1 or `start_colon` is greater than or equal to `end_colon`, then -1 has been printed. If `start_colon` and `end_colon` are valid, then `start_colon` is the index of the first ':' character in `s` between `ind + 1` and `bind - 1`, `end_colon` is the index of the last ':' character in `s` between `bind - 1` and `ind` (inclusive), `i` is either -1 or `end_colon - 1` depending on the loop execution, `pipe_count` is the total number of '|' characters in the substring of `s` from `start_colon + 1` to `end_colon - 1`, and `result` is `4 + pipe_count`, with the value of `result` having been printed.
#Overall this is what the function does:The function accepts a string `s` and returns the count of '|' characters between the first and last ':' characters within a pair of '[' and ']' characters, plus 4, if such a structure exists in the string; otherwise, it returns -1.

