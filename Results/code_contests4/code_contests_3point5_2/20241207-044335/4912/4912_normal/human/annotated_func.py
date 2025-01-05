#State of the program right berfore the function call: S is a string of length between 9 and 50, consisting of uppercase English letters and ending with `FESTIVAL`.
def func():
    n = int(input())
    s = input()
    res = []
    count = 0
    if (s[0] == '1') :
        one = 1
    else :
        one = 0
    #State of the program after the if-else block has been executed: *S is a string of length between 9 and 50, consisting of uppercase English letters and ending with `FESTIVAL`; n is an input integer; res is an empty list; count is 0. If the first character of S is '1', then one is assigned the value 1. If the first character of S is not '1', then one is assigned the value 0.
    temp = []
    tar = 0
    for i in range(1, n - 1):
        if s[i - 1:i + 2] == '101':
            tar = 1
            temp.append(one)
            one = 0
        else:
            if s[i] == '0' and tar == 1:
                temp.append(one)
                res.append(temp.copy())
                temp = []
                tar = 0
            if s[i] == '1':
                one += 1
            else:
                one = 0
        
    #State of the program after the  for loop has been executed: `S` is a string of length between 9 and 50, consisting of uppercase English letters and ending with `FESTIVAL`, `n` is at least 2, `res` is a list containing elements where `temp` has been copied, `count` may or may not be incremented, `one` is either incremented by `n-1` or 0, `temp` is an empty list, `tar` is 0, `i` is `n-1` for the loop to execute, and the substring starting at index `i` and ending at index `i + 3` of `S` may or may not be equal to '101'. If `S[i] == '0'` and `tar == 1`, then the program state remains the same as described. If `S[i] == '1'`, `one` is either incremented by `n-1` or `n-2`.
    if (s[-1] == '1') :
        one += 1
    #State of the program after the if block has been executed: *`S` is a string of length between 9 and 50, consisting of uppercase English letters and ending with `FESTIVAL`, `n` is at least 2, `res` is a list containing elements where `temp` has been copied, `count` may or may not be incremented, `one` is either incremented by `n` or `n-1`, `temp` is an empty list, `tar` is 0, `i` is `n-1` for the loop to execute, and the substring starting at index `i` and ending at index `i + 3` of `S` may or may not be equal to '101'. If `S[i] == '0'` and `tar == 1`, then the program state remains the same as described. If `S[i] == '1'`, `one` is either incremented by `n` or `n-1`. Additionally, if `S[-1]` is '1', then the program state is updated according to the if condition.
    if (tar == 1) :
        temp.append(one)
        res.append(temp.copy())
    #State of the program after the if block has been executed: *`S` is a string of length between 9 and 50, consisting of uppercase English letters and ending with `FESTIVAL`, `n` is at least 2, `res` contains the appended `temp` list, `count` may or may not be incremented, `one` is either incremented by `n` or `n-1`, `temp` contains the appended value of `one`, `tar` is either 0 or 1, `i` is `n-1` for the loop to execute, and the substring starting at index `i` and ending at index `i + 3` of `S` may or may not be equal to '101'. If `S[i] == '0'` and `tar == 1`, then the program state remains the same as described. If `S[i] == '1'`, `one` is either incremented by `n` or `n-1`. Additionally, if `S[-1]` is '1', then the program state is updated according to the if condition.
    for x in res:
        temp = 0
        
        m = len(x)
        
        f = []
        
        if m == 2:
            temp = max(x[0], x[1])
        
        if m == 3:
            temp = max(x[0], x[1], x[2])
        
        if m == 4:
            temp = max(x[0] + x[2], x[3] + max(x[0], x[1]))
        
        if m >= 5:
            f.append([x[0], x[1]])
            f.append([x[1], max(x[2], x[0])])
            f.append(x[0] + x[2], x[3] + f[0])
            for i in range(3, m - 1):
                f.append(x[i] + max(f[i - 2][0], f[i - 3][0]))
                f.append(x[i + 1] + max(f[i - 2][0], f[i - 2][1]))
            temp = max(f[-1][0], f[-1][1], f[-2][0])
        
        count += temp
        
    #State of the program after the  for loop has been executed: At the end of the loop execution, `S` is a string of length between 9 and 50, ending with `FESTIVAL`, `n` is at least 2, `res` contains the appended `temp` list and is non-empty, `count` is the sum of all `temp` values calculated in each iteration of the loop, `one` is either incremented by `n` or `n-1`, `tar` is either 0 or 1, `i` is `m - 2`, the substring starting at index `i` and ending at index `i + 3` of `S` may or may not be equal to '101', `temp` is assigned the maximum value between the last two elements and the second last element of list `f`, `m` depends on the length of `x`, and `f` contains the appended values based on the conditions within the loop.
    print(count)
#Overall this is what the function does:The function `func` reads an integer `n` and a string `s` from the user input. It then processes the string `s` based on certain conditions and calculates a final count. The function does not accept any parameters and operates on the constraints where `s` is a string of length between 9 and 50, consisting of uppercase English letters and ending with `FESTIVAL`. The functionality includes iterating over the characters of `s`, extracting specific substrings, and performing calculations to obtain a final count, which is then printed at the end.

