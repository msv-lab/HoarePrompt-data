#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters and the characters [, ], :, and |, with a length between 1 and 500,000.
def func():
    s = input()
    n = len(s)
    ind = -1
    f = False
    for i in range(n):
        if s[i] == '[':
            f = True
        elif s[i] == ':':
            if f:
                ind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and the characters [, ], :, and |, of length `n` (where `n` is greater than 0). If there exists at least one '[' before the first occurrence of ':', then `ind` will be the index of the first occurrence of ':' after the first '['; if no such ':' exists after the first '[', then `ind` remains -1. If there are no '[' characters in the string, then `ind` will remain -1 regardless of the presence of ':' in `s`. `f` will be True if at least one '[' was found; otherwise, `f` will be False.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and characters [, ], :, and |; `bind` is the index of the last ':' that appears after the last ']' in the string `s`, or -1 if such a ':' does not exist; `f` is True if at least one ']' was found in `s`, otherwise False; `n` is the length of the string `s`.
    if (ind == -1 or bind == -1) :
        print(-1)
    else :
        if (ind >= bind) :
            print(-1)
        else :
            ans = 4
            for i in range(ind + 1, bind):
                if s[i] == '|':
                    ans += 1
                
            #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and characters [, ], :, and |; `bind` is greater than `ind + 1`, `ind` is a valid index in the string, `f` is True, `n` is the length of the string `s`, and `ans` is 4 plus the count of '|' found between indices `ind + 1` and `bind`.
            print(ans)
        #State of the program after the if-else block has been executed: *`s` is a string of lowercase Latin letters and characters [, ], :, and |; if `ind` is greater than or equal to `bind`, `print` outputs -1. Otherwise, `bind` is greater than `ind + 1`, `ind` is a valid index in the string, `f` is True, `n` is the length of the string `s`, and `ans` is calculated as 4 plus the count of '|' found between indices `ind + 1` and `bind`.
    #State of the program after the if-else block has been executed: *`s` is a string of lowercase Latin letters and characters [, ], :, and |; if either `ind` or `bind` is -1, the output of the print statement is -1. Otherwise, if `ind` is greater than or equal to `bind`, `print` outputs -1. If `bind` is greater than `ind + 1`, `ind` is a valid index in the string, `f` is True, `n` is the length of the string `s`, and `ans` is calculated as 4 plus the count of '|' found between indices `ind + 1` and `bind.
#Overall this is what the function does:The function reads a string `s` containing lowercase letters and the characters `[`, `]`, `:`, and `|`. It identifies the first occurrence of `:` after the first `[`, and the last occurrence of `:` before the last `]`. If either `:` does not exist in the expected positions, or if the first `:` is not before the last `:`, the function outputs -1. If valid indices are found, it counts the occurrences of `|` between these indices and returns that count plus 4. The function does not accept any parameters.

