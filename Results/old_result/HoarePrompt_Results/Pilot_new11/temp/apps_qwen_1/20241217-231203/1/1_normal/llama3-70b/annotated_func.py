#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, characters [, ], :, and |, with a length between 1 and 500000 inclusive.
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
        
    #State of the program after the  for loop has been executed: `n` is the length of the input string `s`, `f` is a boolean indicating whether a '[' character was found and `ind` is the index of the first ':' character that occurs after the first '[' character if such a '[' exists, otherwise `ind` is -1.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `n` is the length of the input string `s`, `f` is `True`, `ind` is the index of the first `':'` character after the first `['` if such a `['` exists; otherwise, `ind` is `-1`. If `s[i]` is `']'` for any `i`, then `bind` is `-1`; otherwise, `bind` is the last index `i` where `s[i]` is `':'` and `f` is `True`.
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
                
            #State of the program after the  for loop has been executed: `ind` is the index of the first `':'` character after the first `['` if such a `['` exists; otherwise, `ind` is `-1`, `bind` is the last index `i` where `s[i]` is `':'` and `f` is `True`, `ans` is `4` plus the number of `|` characters in the substring `s[ind+1:bind]`.
            print(ans)
        #State of the program after the if-else block has been executed: *`n` is the length of the input string `s`, `f` is `True`, `ind` is the index of the first `':'` character after the first `['` if such a `['` exists; otherwise, `ind` is `-1`, and `bind` is the last index `i` where `s[i]` is `':'` and `f` is `True`. If `ind` is greater than or equal to `bind`, the console prints `-1`. Otherwise, `ans` is `4` plus the number of `|` characters in the substring `s[ind+1:bind]`, and `ans` is printed.
    #State of the program after the if-else block has been executed: *`n` is the length of the input string `s`, `f` is `True`, `ind` is the index of the first `':'` character after the first `['` if such a `['` exists; otherwise, `ind` is `-1`, and `bind` is the last index `i` where `s[i]` is `':'` and `f` is `True`. If `(ind == -1 or bind == -1)`, the function does nothing. If `ind` is greater than or equal to `bind`, the console prints `-1`. Otherwise, `ans` is `4` plus the number of `|` characters in the substring `s[ind+1:bind]`, and `ans` is printed.
#Overall this is what the function does:The function processes a string `s` consisting of lowercase Latin letters, characters `[`, `]`, `:`, and `|`, with a length between 1 and 500000 inclusive. It searches for the first occurrence of `['` and the last occurrence of `']'` that follow it, and if such occurrences are found, it calculates the number of `|` characters in the substring between them (excluding the delimiters). If no valid pair of `['` and `']'` is found, or if the substring between them is empty or starts with `]`, the function prints `-1`. Otherwise, it prints the count of `|` characters plus 4. The function does not modify the input string `s`.

