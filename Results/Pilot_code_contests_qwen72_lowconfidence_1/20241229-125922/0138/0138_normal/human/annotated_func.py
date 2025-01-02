#State of the program right berfore the function call: s and t are non-empty strings consisting of lowercase Latin letters, and their lengths are between 1 and 5000 inclusive.
def func_1():
    s = list(raw_input())
    t = list(raw_input())
    scount = [0] * 26
    tcount = [0] * 26
    for char in s:
        scount[ord(char) - ord('a')] += 1
        
    #State of the program after the  for loop has been executed: `s` is a list of characters from the input string with at least 1 character, `t` is a list of characters from the new input string, `scount` is a list of 26 integers where each element at index `i` represents the count of the character `chr(i + ord('a'))` in `s`, `tcount` is a list of 26 zeros.
    for char in t:
        tcount[ord(char) - ord('a')] += 1
        
    #State of the program after the  for loop has been executed: `s` is a list of characters from the input string with at least 1 character, `t` is a list of characters from the new input string, `scount` is a list of 26 integers representing the count of each character in `s`, `tcount` is a list of 26 integers where each element at index `i` represents the count of the character `chr(i + ord('a'))` in `t`. If `t` is an empty list, `tcount` remains a list of 26 zeros.
    allgreater = True
    for i in range(26):
        if scount[i] < tcount[i]:
            allgreater = False
        
    #State of the program after the  for loop has been executed: `s` is a list of characters from the input string with at least 1 character, `t` is a list of characters from the new input string, `scount` is a list of 26 integers representing the count of each character in `s`, `tcount` is a list of 26 integers where each element at index `i` represents the count of the character `chr(i + ord('a'))` in `t`. If `t` is an empty list, `tcount` remains a list of 26 zeros. `allgreater` is `True` if for every character `c` in the alphabet, the count of `c` in `s` is greater than or equal to the count of `c` in `t`. Otherwise, `allgreater` is `False`.
    if allgreater :
        if (len(s) == len(t)) :
            return -1
            #The program returns -1
        #State of the program after the if block has been executed: *`s` is a list of characters from the input string with at least 1 character, `t` is a list of characters from the new input string, `scount` is a list of 26 integers representing the count of each character in `s`, `tcount` is a list of 26 integers where each element at index `i` represents the count of the character `chr(i + ord('a'))` in `t`. If `t` is an empty list, `tcount` remains a list of 26 zeros. `allgreater` is `True`, indicating that for every character `c` in the alphabet, the count of `c` in `s` is greater than or equal to the count of `c` in `t`. Additionally, the length of `s` is not equal to the length of `t`.
        for char in t:
            scount[ord(char) - ord('a')] -= 1
            
        #State of the program after the  for loop has been executed: `s` is a list of characters from the input string with at least 1 character, `t` is a list of characters from the new input string, `scount` is a list of 26 integers representing the count of each character in `s` minus the count of each corresponding character in `t`, `tcount` is a list of 26 integers where each element at index `i` represents the count of the character `chr(i + ord('a'))` in `t`, `allgreater` is `True`, and the length of `s` is not equal to the length of `t`.
        for i in range(26):
            while scount[i] > 0:
                t.append(chr(i + ord('a')))
                scount[i] -= 1
            
        #State of the program after the  for loop has been executed: `s` is a list of characters from the input string with at least 1 character, `t` is a list of characters from the new input string with characters appended such that the counts of each character in `s` and `t` are balanced (i.e., `scount` is a list of 26 integers all set to 0), `scount` is a list of 26 integers all set to 0, `tcount` is a list of 26 integers where each element at index `i` represents the count of the character `chr(i + ord('a'))` in `t`, `allgreater` is `True`, the length of `s` is not equal to the length of `t`.
        return ''.join(map(str, t))
        #The program returns a string formed by joining all characters in the list `t`. The list `t` contains characters appended to balance the counts of each character in `s` and `t`, ensuring that the counts of each character represented by the lists `scount` and `tcount` are balanced. The length of `s` is not equal to the length of `t`, and `allgreater` is `True`.
    #State of the program after the if block has been executed: `s` is a list of characters from the input string with at least 1 character, `t` is a list of characters from the new input string, `scount` is a list of 26 integers representing the count of each character in `s`, `tcount` is a list of 26 integers where each element at index `i` represents the count of the character `chr(i + ord('a'))` in `t`. If `t` is an empty list, `tcount` remains a list of 26 zeros. `allgreater` is `False` because there exists at least one character `c` in the alphabet for which the count of `c` in `s` is less than the count of `c` in `t`.
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
        
    #State of the program after the  for loop has been executed: Output State:
    if (works == -1) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: Output State, and `works` is not equal to -1
    res = list()
    for i in range(works):
        res.append(t[i])
        
        scount[ord(t[i]) - ord('a')] -= 1
        
    #State of the program after the  for loop has been executed: `works` is a positive integer, `res` is `[t[0], t[1], ..., t[works-1]]`, `scount[ord(t[i]) - ord('a')]` is decremented by 1 for each `i` from 0 to `works - 1`.
    for j in range(ord(t[works]) - ord('a') + 1, 26):
        if scount[j] > 0:
            res.append(chr(j + ord('a')))
            scount[j] -= 1
            break
        
    #State of the program after the  for loop has been executed: Output State: `works` is a positive integer less than the length of `t`, `t[works]` is a lowercase letter, `res` is the list initially containing the first `works` elements of `t` and possibly an additional character that is the next available character in the alphabet after `t[works]` with a positive count in `scount`, `scount[ord(t[works]) - ord('a') + k]` is decremented by 1 if a valid `k` was found, otherwise `scount` remains unchanged.
    for i in range(26):
        while scount[i] > 0:
            res.append(chr(i + ord('a')))
            scount[i] -= 1
        
    #State of the program after the  for loop has been executed: `works` is a positive integer less than the length of `t`, `t[works]` is a lowercase letter, `res` is the list initially containing the first `works` elements of `t` and possibly an additional character that is the next available character in the alphabet after `t[works]` with a positive count in `scount`, now including each character from `'a'` to `'z'` repeated according to their respective counts in `scount`, `scount[ord(t[works]) - ord('a') + k]` is decremented by 1 if a valid `k` was found, otherwise `scount` remains unchanged, and all elements in `scount` are 0.
    return ''.join(map(str, res))
    #The program returns a string that is the concatenation of the first `works` elements of `t` and possibly an additional character that is the next available character in the alphabet after `t[works]` with a positive count in `scount`, now including each character from `'a'` to `'z'` repeated according to their respective counts in `scount`. Since all elements in `scount` are 0, no additional characters are added, and the returned string consists only of the first `works` elements of `t`.
#Overall this is what the function does:The function `func_1` processes two input strings `s` and `t`, both of which are non-empty and consist of lowercase Latin letters with lengths between 1 and 5000. The function returns one of the following:

1.

