#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, characters [, ], :, and |, with a length between 1 and 500000.
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
        
    #State of the program after the  for loop has been executed: `s` is the string input by the user, `n` is the length of `s`, `f` is True if any '[' is found in the string, `ind` is the index of the first ':' following a '[', otherwise `ind` is -1.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string, `n` is the length of `s`, `f` is `True` if a `':'` follows a `['`, otherwise `f` is `False`, `ind` is the index of the first `':'` following a `['`, otherwise `ind` is `-1`, `bind` is the index of the `':'` if a match is found, otherwise `bind` is `-1`.
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
                
            #State of the program after the  for loop has been executed: `s` is a non-empty string, `n` is the length of `s`, `f` is `True` if a `':'` follows a `['`, otherwise `f` is `False`, `ind` is a valid index within `s` if the loop executed at least once, `bind` is a valid index within `s` such that `bind > ind + 1` if the loop executed at least once, `i` is `bind + 1` if the loop executed at least once, `ans` is the number of `|` characters encountered between `ind + 1` and `bind - 1` if the loop executed at least once, and if the loop does not execute, `ans` remains `4`, `ind` is `-1`, and `bind` is `-1`.
            print(ans)
        #State of the program after the if-else block has been executed: `s` is a non-empty string, `n` is the length of `s`, `f` is `True` if a `':'` follows a `['`, otherwise `f` is `False`, `ind` is the index of the first `':'` following a `['`, otherwise `ind` is `-1`, `bind` is the index of the `':'` if a match is found, otherwise `bind` is `-1`, and `ans` is the number of `|` characters encountered between `ind + 1` and `bind - 1` if the loop executed at least once, otherwise `ans` is `4`, `ind` is `-1`, and `bind` is `-1`.
    #State of the program after the if-else block has been executed: *`s` is a non-empty string, `n` is the length of `s`, `f` is `True` if a `':'` follows a `['`, otherwise `f` is `False`, `ind` is the index of the first `':'` following a `['`, otherwise `ind` is `-1`, `bind` is the index of the `':'` if a match is found, otherwise `bind` is `-1`. If `ind == -1` or `bind == -1`, the console prints `-1`. Otherwise, `ans` is the number of `|` characters encountered between `ind + 1` and `bind - 1` if the loop executed at least once, otherwise `ans` is `4`, `ind` is `-1`, and `bind` is `-1`.
#Overall this is what the function does:The function processes a string `s` consisting of lowercase Latin letters, characters `[`, `]`, `:`, and `|`. It finds the first `:` following a `[` and the last `:` preceding a `]`. If either of these `:` is not found, it prints `-1`. Otherwise, it counts the number of `|` characters between the indices of the found `:` and prints the count. If no matching `:` is found, it defaults to printing `4`.

