#State of the program right berfore the function call: The function operates on a string s that consists of lowercase Latin letters and characters [, ], :, |, and has a length between 1 and 500000 (inclusive).
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
        
    #State of the program after the  for loop has been executed: `s` is the input string of length between 1 and 500000 (inclusive), `n` is the integer equal to the length of `s` where 1 ≤ `n` ≤ 500000, `i` is equal to `n`, `f` is True if `s` contains at least one '[', and `ind` is the index of the first ':' after a '[' in `s`, or -1 if no such ':' is found.
    bind = -1
    f = False
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            f = True
        elif s[i] == ':':
            if f:
                bind = i
                break
        
    #State of the program after the  for loop has been executed: `s` is the input string of length between 1 and 500000 (inclusive), `n` is the integer equal to the length of `s` where 1 ≤ `n` ≤ 500000, `i` is -1, `f` is `True` if a ']' character is found in `s`, otherwise `f` is `False`, `bind` is the index of the ':' character if a ']' character is found before it, otherwise `bind` is -1, and `ind` is the index of the first ':' after a '[' in `s`, or -1 if no such ':' is found.
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
                
            #State of the program after the  for loop has been executed: `s` is the input string of length between 1 and 500000 (inclusive), `n` is the integer equal to the length of `s` where 1 ≤ `n` ≤ 500000, `ind` is the index of the first ':' after a '[' in `s`, `bind` is the index of the ':' character, `i` is `bind - 1`, `f` is `True`, and `ans` is 4 plus the number of '|' characters in `s` between indices `ind + 1` and `bind - 1`.
            print(ans)
        #State of the program after the if-else block has been executed: `s` is the input string of length between 1 and 500000 (inclusive), `n` is the integer equal to the length of `s` where 1 ≤ `n` ≤ 500000, `f` is `True`, `ind` and `bind` are the indices of the ':' characters and are not equal to -1. If `ind` is greater than or equal to `bind`, then the value -1 has been printed. Otherwise, `i` is `bind - 1` and the function returns `ans` which is 4 plus the number of '|' characters in `s` between indices `ind + 1` and `bind - 1`.
    #State of the program after the if-else block has been executed: *`s` is the input string of length between 1 and 500000 (inclusive), `n` is the integer equal to the length of `s`, `i` is either -1 or `bind - 1` if `ind` is less than `bind`, `f` is `True` if a ']' character is found in `s`, otherwise `f` is `False`, `bind` is either -1 or the index of the ':' character if a ']' character is found before it, `ind` is either -1 or the index of the first ':' after a '[' in `s`. If `ind` is -1 or `bind` is -1, the function returns -1. Otherwise, if `ind` is greater than or equal to `bind`, the function returns -1. If `ind` is less than `bind`, `i` is `bind - 1` and the function returns `ans` which is 4 plus the number of '|' characters in `s` between indices `ind + 1` and `bind - 1`.
#Overall this is what the function does:The function takes an input string `s` of length between 1 and 500000 (inclusive) consisting of lowercase Latin letters and characters [, ], :, |. It attempts to find the index of the first ':' after a '[' and the index of the first ':' before a ']'. If either of these indices is not found, or if the index of the first ':' after a '[' is greater than or equal to the index of the first ':' before a ']', the function prints -1. Otherwise, it counts the number of '|' characters between these two indices and prints 4 plus this count. The function does not handle any exceptions or edge cases outside of the specified string length and character set, and it does not return any value in the classical sense, but rather prints its result directly to the console.

