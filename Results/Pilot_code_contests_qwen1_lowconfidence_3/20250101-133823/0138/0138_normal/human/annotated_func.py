#State of the program right berfore the function call: s and t are non-empty strings consisting of lowercase Latin letters, with lengths satisfying 1 ≤ |s|, |t| ≤ 5000.
def func_1():
    s = list(raw_input())
    t = list(raw_input())
    scount = [0] * 26
    tcount = [0] * 26
    for char in s:
        scount[ord(char) - ord('a')] += 1
        
    #State of the program after the  for loop has been executed: `scount` is a list of 26 integers where each integer represents the count of a corresponding character from 'a' to 'z' in the string `s`, `s` is a list of characters from the input, `t` is a list of characters from the input, `tcount` is a list of 26 zeros, `char` is the last character processed in the list `s` if the loop executed at least once. If the loop did not execute, `scount` remains a list of 26 zeros.
    for char in t:
        tcount[ord(char) - ord('a')] += 1
        
    #State of the program after the  for loop has been executed: `t` is a list of characters, `tcount` is a list of 26 integers where each integer represents the count of a corresponding character from 'a' to 'z' in the list `t`, and if the loop executed at least once, `char` is the last character processed in the list `t`. If the loop did not execute, `tcount` remains a list of 26 zeros.
    allgreater = True
    for i in range(26):
        if scount[i] < tcount[i]:
            allgreater = False
        
    #State of the program after the  for loop has been executed: `scount` and `tcount` are lists of integers, and `allgreater` is either `True` or `False`. `allgreater` is `True` if and only if `scount[i]` is not less than `tcount[i]` for all `i` from 0 to 25. Otherwise, `allgreater` is `False`.
    if allgreater :
        if (len(s) == len(t)) :
            return -1
            #The program returns -1
        #State of the program after the if block has been executed: *`scount` and `tcount` are lists of integers, and `allgreater` is either `True` or `False`. `allgreater` is `True` if and only if `scount[i]` is not less than `tcount[i]` for all `i` from 0 to 25. The lengths of `s` and `t` are not equal.
        for char in t:
            scount[ord(char) - ord('a')] -= 1
            
        #State of the program after the  for loop has been executed: `scount[ord(char) - ord('a')]` for each character `char` in `t` is decremented by 1, `tcount` and `allgreater` are unchanged.
        for i in range(26):
            while scount[i] > 0:
                t.append(chr(i + ord('a')))
                scount[i] -= 1
            
        #State of the program after the  for loop has been executed: 
        return ''.join(map(str, t))
        #The program returns a string obtained by joining the elements of list 't' converted to strings
    #State of the program after the if block has been executed: Postcondition: `scount` and `tcount` are lists of integers, and `allgreater` is either `True` or `False`. `allgreater` is `False` if and only if there exists at least one index `i` from 0 to 25 such that `scount[i]` is less than `tcount[i]`.
    works = -1
    scountcopy = list(scount)
    for i in range(len(s)):
        cando = False
        
        for j in range(ord(t[i]) - ord('a') + 1, 26):
            if scountcopy[j] > 0:
                cando = True
        
        if cando:
            works = i
        
        if scountcopy[ord(t[i]) - ord('a')] == 0:
            break
        
        scountcopy[ord(t[i]) - ord('a')] -= 1
        
    #State of the program after the  for loop has been executed: `scount` must have at least one element, `i` is the length of `s`, `tcount` is a list of integers, `allgreater` is either `True` or `False`, `cando` is `True` if there exists an index `j` such that `scountcopy[j] > 0` for any `j` in the range `ord(t[i]) - ord('a') + 1` to 25, otherwise `cando` remains `True`, `scountcopy` is a copy of `scount` with the value at index `ord(t[i]) - ord('a')` decreased by 1 for each character `t[i]` in `s` for which `scountcopy[ord(t[i]) - ord('a')] > 0`, `works` is the last index `i` for which the inner loop did not break, and the loop breaks if `scountcopy[ord(t[i]) - ord('a')] == 0` for any `i`.
    if (works == -1) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `scount` must have at least one element, `i` is the length of `s`, `tcount` is a list of integers, `allgreater` is either `True` or `False`, `cando` remains `True`, `scountcopy` is a copy of `scount` with the value at index `ord(t[i]) - ord('a')` decreased by 1 for each character `t[i]` in `s` for which `scountcopy[ord(t[i]) - ord('a')] > 0`, `works` is an index for which the inner loop did not break, and the loop breaks if `scountcopy[ord(t[i]) - ord('a')] == 0` for any `i`.
    res = list()
    for i in range(works):
        res.append(t[i])
        
        scount[ord(t[i]) - ord('a')] -= 1
        
    #State of the program after the  for loop has been executed: `res` is a list containing the first `works` characters from `t`, and for each character `t[i]` in `res`, `scount[ord(t[i]) - ord('a')]` is decreased by 1; otherwise, `scount` remains unchanged.
    for j in range(ord(t[works]) - ord('a') + 1, 26):
        if scount[j] > 0:
            res.append(chr(j + ord('a')))
            scount[j] -= 1
            break
        
    #State of the program after the  for loop has been executed: `res` is a list containing the first `works` characters from `t` plus an additional character `chr(j + ord('a'))` for each valid `j` (where `ord(t[works]) - ord('a') + 1 <= j < 26` and `scount[j] > 0`). For each such `j`, `scount[j]` is decreased by 1. `works` remains the same unless the loop is executed 26 - `ord(t[works]) - ord('a') + 1` times, in which case `works` will be incremented to 0.
    for i in range(26):
        while scount[i] > 0:
            res.append(chr(i + ord('a')))
            scount[i] -= 1
        
    #State of the program after the  for loop has been executed: `res` is the concatenation of all characters corresponding to the indices where `scount[i]` was originally greater than 0, `scount[i]` for all `i` is 0, and `i` ranges from 0 to 25.
    return ''.join(map(str, res))
    #The program returns an empty string since 'res' is the concatenation of all characters where 'scount[i]' was originally greater than 0, and 'scount[i]' for all i ranges from 0 to 25 is 0.
#Overall this is what the function does:The function `func_1` takes no explicit parameters but reads two strings `s` and `t` from the user input, then processes these strings to determine the result based on specific conditions. After reading the strings, it counts the occurrences of each character in both strings `s` and `t` using `scount` and `tcount` respectively. It then compares these counts to check if every character in `s` appears at least as many times as in `t`.

If `scount` is always greater than or equal to `tcount` for all characters, and the lengths of `s` and `t` are equal, the function returns `-1`.

If the above condition is not met but the lengths of `s` and `t` are equal, it attempts to remove characters from `s` to match `t` by decrementing the corresponding counts in `scount`. If successful, it appends the remaining characters to `t` and returns the result as a string. If unsuccessful, it returns `-1`.

If the initial comparison indicates that `scount` is not always greater than or equal to `tcount`, the function proceeds to a more complex algorithm involving a temporary copy of `scount` (`scountcopy`) to find a valid starting index `works`. This index represents the position in `s` where the first character in `t` cannot be found in sufficient quantity in `s`. If such an index is found, it constructs a result string by taking characters from `t` up to this index and appending any remaining valid characters from `scountcopy` in lexicographical order. If no such index exists, it returns `-1`.

In all cases, the function returns `-1` in certain scenarios and constructs and returns a string in others, based on the comparison and processing of the input strings.

