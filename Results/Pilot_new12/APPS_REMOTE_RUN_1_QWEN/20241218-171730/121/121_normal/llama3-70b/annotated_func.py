#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 255, and s is a string of length n consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255, `s` is a non-empty string consisting of characters 'A', 'C', 'G', 'T', and '?', `count` is a dictionary with keys 'A', 'C', 'G', 'T' and their values incremented by 1 for each occurrence of the corresponding character in `s` (excluding '?' characters). If no character other than '?' appears in `s`, the values in `count` remain 0.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255; `s` is a non-empty string containing at least one of the characters `'A', 'C', 'G', 'T'`; `count` is a dictionary with keys `'A', 'C', 'G', 'T'` and their values updated such that each key's value is `avg - count[key]` for all characters in the string `s`; `avg` is `n // 4`.
    res = ''
    for c in s:
        if c == '?':
            for nc in 'ACGT':
                if count[nc] > 0:
                    res += nc
                    count[nc] -= 1
                    break
        else:
            res += c
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255, `s` is a non-empty string consisting only of the characters `'A', 'C', 'G', 'T'` and possibly `'?'`, `count` is a dictionary with keys `'A', 'C', 'G', 'T'` and their values updated such that each key's value is `0` (since all counts will eventually be depleted), `avg` is `n // 4`, and `res` is a string formed by replacing each `'?'` in `s` with one of `'A', 'C', 'G', 'T'` while respecting the count constraints, or appending the corresponding character from `s` if it is not `'?'`.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`n` is an integer between 4 and 255, `s` is a non-empty string consisting only of the characters `'A', 'C', 'G', 'T'` and possibly `'?'`, `count` is a dictionary with keys `'A', 'C', 'G', 'T'` and their values updated such that either at least one key's value is greater than 0 or all values are `0`, `avg` is `n // 4`, and `res` is a string formed by replacing each `'?'` in `s` with one of `'A', 'C', 'G', 'T'` while respecting the count constraints, or appending the corresponding character from `s` if it is not `'?'`. Printed: `===` if any count value is greater than 0, otherwise the value of `res` is printed.
#Overall this is what the function does:The function `func()` accepts two parameters: an integer `n` such that 4 ≤ n ≤ 255, and a string `s` of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'. It processes the string `s` to replace all '?' characters with one of 'A', 'C', 'G', 'T' such that the counts of 'A', 'C', 'G', and 'T' in the resulting string are as close to equal as possible. If the original string `s` contains characters other than '?', these characters are appended to the result as-is. After processing, the function prints '===' if any count of 'A', 'C', 'G', or 'T' is greater than 0, otherwise it prints the resulting string `res`.

