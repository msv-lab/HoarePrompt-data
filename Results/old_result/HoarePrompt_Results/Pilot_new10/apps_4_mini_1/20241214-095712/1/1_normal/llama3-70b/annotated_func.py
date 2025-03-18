#State of the program right berfore the function call: s is a string of length between 1 and 500,000, consisting of lowercase Latin letters and the characters [, ], :, and |.
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
        
    #State of the program after the  for loop has been executed: `s` is a string of length between 1 and 500,000; `n` is the length of `s`; `ind` is the index of the first occurrence of ':' following the first '[' in `s` or remains -1 if ':' was not found after any '['; `f` is True if at least one '[' was encountered in `s`, otherwise False; `i` is `n`, indicating the end of the string traversal.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is a string of length between 1 and 500,000; `n` is the length of `s`; `ind` is the index of the first occurrence of ':' following the first '[' in `s` or remains -1 if ':' was not found after any '['; `f` is True if at least one ']' was found in the string; `bind` is the index of the first ':' found after the last ']' if such ':' exists and `-1` otherwise.
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
                
            #State of the program after the  for loop has been executed: `s` is a string of length between 1 and 500,000, `n` is the length of `s`, `ind` is the index of the first occurrence of ':' following the first '[', `f` is True if at least one ']' was found in the string, `bind` is the index of the first ':' found after the last ']', `ans` is equal to 4 plus the number of '|' characters found in the substring `s[ind + 1:bind]` if the loop executes; if the loop does not execute, `ans` remains 4.
            print(ans)
        #State of the program after the if-else block has been executed: *`s` is a string of length between 1 and 500,000; `n` is the length of `s`; `ind` is the index of the first occurrence of ':' following the first '[' in `s` and is not -1; `f` is True if at least one ']' was found in the string; `bind` is the index of the first ':' found after the last ']' and is not -1 if such ':' exists. If `ind` is greater than or equal to `bind`, the printed value is -1. Otherwise, `ans` is equal to 4 plus the number of '|' characters found in the substring `s[ind + 1:bind]` if the loop executes, and remains 4 if the loop does not execute; the value of `ans` has been printed.
    #State of the program after the if-else block has been executed: *`s` is a string of length between 1 and 500,000; `n` is the length of `s`; if either `ind` is -1 or `bind` is -1, it indicates that no ':' was found after the first '[' or no ':' was found after the last ']', and thus the relevant conditions for `f` and `bind` hold. If `ind` is not -1, and `bind` is not -1, it indicates that both ':' occurrences exist, and if `ind` is greater than or equal to `bind`, the printed value is -1; otherwise, `ans` is calculated as 4 plus the number of '|' characters found in the substring `s[ind + 1:bind]`, or remains 4 if the loop does not execute, with the final value of `ans` printed.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters and the characters [, ], :, and | (length between 1 and 500,000). It searches for the first occurrence of ':' after the first '[' and the first occurrence of ':' before the last ']', returning -1 if either ':' is not found, or if the first ':' occurs at or after the last ':' in the defined substring. If both ':' characters are found appropriately, it counts the number of '|' characters between these indices, adds 4 to this count, and prints the result. If there are no '|' characters in this range, it prints 4.

