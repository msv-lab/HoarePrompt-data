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
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and the characters [, ], :, and | with a length `n` that is greater than 0; if `s` contains at least one '[', `f` is True, and `ind` is the index of the first ':' after the last '[' (or remains -1 if no ':' follows); otherwise, if there is no '[', `f` is False, and `ind` is -1.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and the characters [, ], :, and | with a length `n` greater than 0; `f` is True if there is at least one ']' before a ':'; `bind` is the index of the last ':' after the last ']', or remains -1 if ']' never encountered or ':' exists before ']'; `ind` remains -1.
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
                
            #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters and the characters [, ], :, and | with a length `n` greater than 0; `f` is True; `bind` is the index of the last ':' after the last ']', which is greater than `ind`; `ind` is a valid index (not -1) and is less than `bind`, which can go up to `bind - 1`; `ans` is the initial value of 4 plus the count of '|' characters found in `s[ind + 1:bind]`.
            print(ans)
        #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase Latin letters and the characters [, ], :, and | with a length `n` greater than 0. If `ind` is greater than or equal to `bind`, then -1 has been printed. Otherwise, `f` is True, `bind` is the index of the last ':' after the last ']', which is greater than `ind`, `ind` is less than `bind`, `ans` is initialized to 4 plus the count of '|' characters found in the substring `s[ind + 1:bind]`, and `ans` is printed.
    #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase Latin letters and the characters [, ], :, and | with a length `n` greater than 0; `f` is True if there is at least one ']' before a ':'; `bind` is the index of the last ':' after the last ']', or remains -1 if ']' never encountered or ':' exists before ']'; `ind` remains -1; if either `ind` is -1 or `bind` is -1, the function continues without performing further actions. Otherwise, if `ind` is greater than or equal to `bind`, -1 is printed. If `ind` is less than `bind`, `f` is True, `bind` is correctly set to the index of the last ':' after the last ']', `ind` is less than `bind`, `ans` is initialized to 4 plus the count of '|' characters found in the substring `s[ind + 1:bind]`, and `ans` is printed.
#Overall this is what the function does:The function reads a string `s` of lowercase Latin letters along with the characters `[`, `]`, `:`, and `|` from input, and analyzes its structure to check for specific patterns. It determines the positions of the first `:` after the last `[`, and the last `:` before the first `]`. If either of these characters is absent in the expected order, it prints `-1`. If the first `:` appears after the last `[`, it counts the occurrences of `|` between these two characters, adds 4 to that count, and prints the result. If there are no valid `:` characters in the required positions, or if the positions are invalid (first `:` not after last `[`), the function will print `-1`. This function essentially checks for the proper structure between brackets and colons, and performs an arithmetic operation based on the occurrences of the `|` character.

