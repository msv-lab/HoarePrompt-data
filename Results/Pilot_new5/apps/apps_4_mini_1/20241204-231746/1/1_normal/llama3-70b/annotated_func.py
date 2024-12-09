#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters and the characters [, ], :, and |, with a length between 1 and 500,000 inclusive.
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
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of lowercase Latin letters and the characters [, ], :, and |, with a length of at least 1; `n` is the length of `s`; `f` is True if at least one '[' was encountered before the first ':'; `ind` is the index of the first ':' encountered after the first '[' if such a ':' exists, otherwise `ind` remains -1; 'i' is `n` after all iterations.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of lowercase Latin letters and the characters [, ], :, and |, with a length of at least 1; `n` is greater than 0; `i` is -1; `bind` is the index of the last ':' found after the last ']', or -1 if such a ':' does not exist; `f` is True if the character ']' was encountered, otherwise False.
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
                
            #State of the program after the  for loop has been executed: `s` is a valid input string, `n` is greater than 0, `i` is `bind`, `bind` is greater than `ind`, `f` is True or False, `ind` is valid and less than `bind`, `ans` is equal to the number of '|' characters found in the substring `s[ind + 1:bind]`.
            print(ans)
        #State of the program after the if-else block has been executed: *`s` is an input string consisting of lowercase Latin letters and the characters [, ], :, and |, with a length of at least 1; `n` is greater than 0; if `ind` is greater than or equal to `bind`, -1 is printed. Otherwise, since `bind` is greater than `ind`, `ans` is equal to the number of '|' characters found in the substring `s[ind + 1:bind]` and `ans` is printed.
    #State of the program after the if-else block has been executed: *`s` is an input string consisting of lowercase Latin letters and the characters [, ], :, and |, with a length of at least 1; `n` is greater than 0; if `ind` is -1 or `bind` is -1, -1 is printed. Otherwise, if `ind` is greater than or equal to `bind`, -1 is printed; if `bind` is greater than `ind`, `ans` is equal to the number of '|' characters found in the substring `s[ind + 1:bind]` and `ans` is printed.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters and the characters [, ], :, and |, with a length between 1 and 500,000. It searches for the first occurrence of a ':' that follows at least one '[' and the last occurrence of a ':' that precedes at least one ']'. If either ':' can't be found or if the first ':' is not before the last ':', it prints -1. Otherwise, it counts the number of '|' characters between these two ':' characters and prints that count plus 4.

