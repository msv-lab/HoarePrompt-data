#State of the program right berfore the function call: The input is a string s consisting of lowercase Latin letters and characters [, ], :, |, and its length is between 1 and 500000 (inclusive).
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
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and characters [, ], :, |, with a length between 1 and 500000 (inclusive), `n` is an integer equal to the length of `s`, `i` is the last index checked in `s`, `f` is True if an '[' was encountered before the loop ended, otherwise False, and `ind` is the index of the first ':' encountered after an '[', or -1 if such a sequence did not occur.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and characters [, ], :, |, with a length between 1 and 500000 (inclusive), `n` is an integer equal to the length of `s`, `i` is -1, `f` is `True` if `s` contains at least one `']'`, `ind` is -1, and `bind` is the index of the first `':'` encountered after a `']'` from the end of `s`, or -1 if no such sequence exists.
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
                
            #State of the program after the  for loop has been executed: `s` is a string of length `n` (1 to 500000) consisting of lowercase Latin letters and characters [, ], :, |, `n` is the length of `s`, `i` is `bind - 1` if the loop executes and -1 otherwise, `f` is `True` if `s` contains at least one `']'`, `ind` and `bind` are not -1 with `ind < bind`, and `ans` is 4 plus the number of '|' characters in the substring of `s` from `ind + 1` to `bind - 1`.
            print(ans)
        #State of the program after the if-else block has been executed: `s` is a string consisting of lowercase Latin letters and characters [, ], :, |, with a length between 1 and 500000 (inclusive), `n` is an integer equal to the length of `s`, `i` is either -1 or `bind - 1` if the loop executes, `f` is `True` if `s` contains at least one `']'`, `ind` and `bind` are not -1, and either the value -1 has been printed when `ind` is greater than or equal to `bind`, or the value 4 plus the number of '|' characters in the substring of `s` from `ind + 1` to `bind - 1` has been returned at the output when `ind` is less than `bind`.
    #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase Latin letters and characters [, ], :, |, with a length between 1 and 500000 (inclusive), `n` is an integer equal to the length of `s`, `f` is `True` if `s` contains at least one `']'`. If `ind` is -1 or `bind` is -1, the program outputs -1, `i` remains -1. If `ind` and `bind` are not -1, then `i` is either -1 or `bind - 1`, and the program either outputs -1 when `ind` is greater than or equal to `bind`, or returns 4 plus the number of '|' characters in the substring of `s` from `ind + 1` to `bind - 1` when `ind` is less than `bind`.
#Overall this is what the function does:The function reads a string of lowercase Latin letters and characters [, ], :, |, and returns the count of '|' characters between the first ':' after a '[' and the first ':' before a ']' from the end, plus 4, or -1 if the specified sequence is not found or if the indices do not meet the required conditions.

