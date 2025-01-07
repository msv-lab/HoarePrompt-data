#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters and characters [, ], :, and |, with a length between 1 and 500000.
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
        
    #State of the program after the  for loop has been executed: `s` is the input string, `n` is the length of `s`, `ind` is the index of the first `:` after the first `[` in the string, and `f` is True. If no such pair is found, `ind` remains `-1` and `f` remains False.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is the input string, `n` is the length of `s`, `ind` is the index of the first `:` after the first `[` in the string, `f` is `False`, and `bind` is `-1`. After the loop executes, if the loop did not find a `':'` following a `']'`, `f` remains `False` and `bind` remains `-1`. If the loop finds a `':'` following a `']'`, `f` becomes `True` and `bind` is set to the index of the `':'`.
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
                
            #State of the program after the  for loop has been executed: `s` is the input string, `n` is the length of `s`, `ind` is the index of the first `:` after the first `[` in the string, `bind` is greater than `ind + 1`, `f` is `False`, and `ans` is the number of `'|'` characters found in the substring of `s` from index `ind + 1` to `bind - 1`.
            print(ans)
        #State of the program after the if-else block has been executed: *`s` is the input string, `n` is the length of `s`, `ind` is the index of the first `:` after the first `[` in the string, `f` is `False`, and `bind` is `-1`. If `ind >= bind`, the console displays `-1`. Otherwise, `bind` is greater than `ind + 1`, `f` remains `False`, and `ans` is the number of `'|'` characters found in the substring of `s` from index `ind + 1` to `bind - 1`, which is printed.
    #State of the program after the if-else block has been executed: `s` is the input string, `n` is the length of `s`, `ind` is the index of the first `:` after the first `[` in the string, `f` is `False`, and `bind` is `-1`. If `ind == -1` or `bind == -1`, then the condition is met and no further actions are taken. Otherwise, if `ind >= bind`, the console displays `-1`. Otherwise, `bind` is greater than `ind + 1`, `f` remains `False`, and `ans` is the number of `'|'` characters found in the substring of `s` from index `ind + 1` to `bind - 1`, which is printed.
#Overall this is what the function does:The function processes a string `s` consisting of lowercase Latin letters and characters `[`, `,`, `:`, and `|`, with a length between 1 and 500000. It searches for the first occurrence of `[` and the first occurrence of `:` immediately following it. Similarly, it searches for the last occurrence of `]` and the first occurrence of `:` immediately preceding it. If either pair is not found, it prints `-1`. If the substring between the first `:` after `[` and the first `:` before `]` is empty or invalid, it also prints `-1`. Otherwise, it counts the number of `|` characters in that substring and prints the count.

