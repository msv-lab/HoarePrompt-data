#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters and the characters [, ], :, and |, with a length between 1 and 500000 inclusive.
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
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of lowercase Latin letters and characters [, ], :, and |; `n` is the length of `s`; `f` is True if at least one `[` has been found, otherwise it is False; `ind` is the index of the first `:` found after a `[` if such a combination exists, otherwise it remains -1.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of lowercase Latin letters and characters [, ], :, and |; `n` is the length of `s`; `f` is True if at least one ']' has been encountered in `s` while scanning from the end; `bind` is the index of the last ':' found after the first ']', or -1 if no such ':' exists; `ind` remains -1 if no ':' is found after a '['.
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
                
            #State of the program after the  for loop has been executed: `s` is an input string consisting of lowercase Latin letters and characters [, ], :, and |; `n` is the length of `s`; `f` is True; `bind` is greater than `ind`; `ind` is not -1; `ans` is 4 plus the number of '|' characters found between `ind + 1` and `bind - 1`.
            print(ans)
        #State of the program after the if-else block has been executed: *`s` is an input string consisting of lowercase Latin letters and characters [, ], :, and |; `n` is the length of `s`; `f` is True if at least one ']' has been encountered in `s` while scanning from the end; `bind` is the index of the last ':' found after the first ']', or -1 if no such ':' exists; `ind` is not -1, meaning at least one ':' is found after the last '['; and `bind` is not -1, indicating that at least one ':' has been found after the first ']'. If `ind` is greater than or equal to `bind`, then -1 has been printed. Otherwise, `f` is True, `bind` is greater than `ind`, `ind` is not -1, `ans` is 4 plus the number of '|' characters found between `ind + 1` and `bind - 1`, and the value of `ans` is printed.
    #State of the program after the if-else block has been executed: *`s` is an input string consisting of lowercase Latin letters and characters [, ], :, and |; `n` is the length of `s`; `f` is True if at least one ']' has been encountered in `s` while scanning from the end; `bind` is the index of the last ':' found after the first ']', or -1 if no such ':' exists; `ind` remains -1 if no ':' is found after a '['. If either `ind` is -1 or `bind` is -1, then -1 is printed. Otherwise, if `ind` is greater than or equal to `bind`, then -1 is printed. If `ind` is less than `bind`, then `f` is True, `bind` is greater than `ind`, `ind` is not -1, `ans` is 4 plus the number of '|' characters found between `ind + 1` and `bind - 1`, and the value of `ans` is printed.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters and the characters [, ], :, and |. It searches for the first `:` after a `[` and the last `:` before a `]`. If either `:` is not found, or if the first `:` is not before the last `:`, it prints -1. If the conditions are met, it counts the number of `|` characters between the first `:` and the last `:` (exclusive) and adds 4 to this count before printing the result. If there are no `|` characters, it will print 4.

