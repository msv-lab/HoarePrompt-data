#State of the program right berfore the function call: n is an integer such that 4 <= n <= 255, and s is a string of length n consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 <= `n` <= 255; `count` is {'A': x, 'C': y, 'G': z, 'T': w}, where x, y, z, and w are the counts of 'A', 'C', 'G', and 'T' characters in the string `s`, respectively. If `s` contains any '?' characters, they do not affect the counts. If `s` contains no characters other than '?', then `count` remains {'A': 0, 'C': 0, 'G': 0, 'T': 0}.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 <= `n` <= 255; `count` is {'A': avg - x, 'C': avg - y, 'G': avg - z, 'T': avg - w}; `avg` is `n // 4`.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 <= `n` <= 255, `avg` is `n // 4`, `count` is {'A': 0, 'C': 0, 'G': 0, 'T': 0}, and `res` contains the original string `s` with all occurrences of '?' replaced by characters from 'A', 'C', 'G', or 'T' according to the counts in `count`, if possible.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 4 <= `n` <= 255, `avg` is `n // 4`, and `count` is {'A': 0, 'C': 0, 'G': 0, 'T': 0}. If at least one value in `count` is greater than 0, then `res` contains the original string `s` with all occurrences of '?' replaced by characters from 'A', 'C', 'G', or 'T' according to the counts in `count`. If all values in `count` are 0, then `res` is the original string `s` since there are no characters to replace the '?'.
#Overall this is what the function does:The function accepts an integer `n` (where 4 <= n <= 255) and a string `s` of length `n` consisting of the characters 'A', 'C', 'G', 'T', and '?'. It counts the occurrences of 'A', 'C', 'G', and 'T' in `s`, calculates the average number of each nucleotide required to balance their counts, and attempts to replace '?' in `s` with the necessary characters. If it is not possible to balance the counts (i.e., if any nucleotide count remains positive after replacements), it prints '===', otherwise, it prints the modified string `res`. If `s` only contains '?' characters, `count` will not be able to zero out, resulting in '===' being printed.

