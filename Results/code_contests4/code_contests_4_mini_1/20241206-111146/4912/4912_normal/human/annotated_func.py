#State of the program right berfore the function call: S is a string consisting of uppercase English letters, with a length between 9 and 50 characters, and S ends with 'FESTIVAL'.
def func():
    n = int(input())
    s = input()
    res = []
    count = 0
    if (s[0] == '1') :
        one = 1
    else :
        one = 0
    #State of the program after the if-else block has been executed: *`S` is a string consisting of uppercase English letters, ending with 'FESTIVAL'; `n` is an input integer; `s` is an input string from the user; if the first character of `s` is '1', then `one` is set to 1. Otherwise, if `s` does not start with '1', `one` is set to 0. `res` remains an empty list and `count` is 0 throughout.
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
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of uppercase English letters ending with 'FESTIVAL'; `n` is at least 3; `s` is an input string from the user; `one` is the count of consecutive '1's encountered before the last '0' after the last '101'; `res` is a list containing lists of counts of '1's collected after each occurrence of '101'; `count` remains 0; `temp` is an empty list if the loop ends without a trailing '0' after the last '101', otherwise it contains the last counted '1's; `tar` is 0 if the last processed character is not part of a '101' pattern or has not been set to 1 before.
    if (s[-1] == '1') :
        one += 1
    #State of the program after the if block has been executed: *`S` is a string consisting of uppercase English letters ending with 'FESTIVAL'; `n` is at least 3; `s` is an input string from the user. If the last character of `s` is '1', then `one` is increased by 1, `res` is updated to contain lists of counts of '1's collected after each occurrence of '101', `count` remains 0, and `temp` is either an empty list or contains the last counted '1's. If the last character is not '1', there are no changes made to `one`, `res`, `count`, or `temp`.
    if (tar == 1) :
        temp.append(one)
        res.append(temp.copy())
    #State of the program after the if block has been executed: *`S` is a string consisting of uppercase English letters ending with 'FESTIVAL'; `n` is at least 3; `s` is an input string from the user. If `tar` is equal to 1, `one` is increased by 1 if the last character of `s` is '1'; `res` is updated to contain lists of counts of '1's collected after each occurrence of '101'; `count` remains 0; `temp` is either an empty list or contains the last counted '1's; `temp` now contains the value of `one` appended to it; `res` now contains a copy of `temp`. If `tar` is not equal to 1, there are no changes made to `one`, `res`, `count`, or `temp`.
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
        
    #State of the program after the  for loop has been executed: If `res` is empty:
    print(count)
#Overall this is what the function does:The function accepts a string `s` consisting of uppercase English letters with a length between 9 and 50 characters, ending with 'FESTIVAL'. It counts occurrences of the pattern '101' in the string and sums the maximum counts of consecutive '1's that appear between these '101' patterns. The final count is printed. If the string does not contain the '101' pattern, the count remains 0. If the string ends with '1' after the last '101', this is also accounted for in the count.

