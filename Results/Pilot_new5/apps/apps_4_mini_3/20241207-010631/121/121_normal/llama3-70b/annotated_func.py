#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 255, and s is a string of length n consisting of the characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255, `s` is a string of length `n` consisting of the characters 'A', 'C', 'G', 'T', and '?', `count` is updated such that it contains the counts of 'A', 'C', 'G', and 'T' in the string `s`, with `count['A']`, `count['C']`, `count['G']`, and `count['T']` representing the total occurrences of each respective character, while `count['?']` remains 0 as '?' characters do not affect the counts.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255; `s` is a string of length `n` consisting of the characters 'A', 'C', 'G', 'T', and '?'; `avg` is `n // 4`; `count[c]` for each character 'A', 'C', 'G', and 'T' is updated to `n // 4 - count[c]`.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255; `s` is a string of length `n`; `res` contains the original characters of `s`, with each '?' replaced by characters from 'A', 'C', 'G', and 'T' up to their required counts; `count['A']`, `count['C']`, `count['G']`, and `count['T']` will be equal to 0, indicating that all characters have been used as needed to balance the '?' characters.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 4 ≤ `n` ≤ 255; `s` is a string of length `n`; if any characters from 'A', 'C', 'G', or 'T' are needed to balance the '?' characters, then those characters remain unassigned in `res`. Otherwise, if all character counts are zero, indicating all '?' characters have been appropriately replaced, `res` is printed with no remaining unassigned characters.
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` (4 ≤ n ≤ 255) and a string `s` of length `n` consisting of the characters 'A', 'C', 'G', 'T', and '?'. It counts the occurrences of 'A', 'C', 'G', and 'T' in the string and calculates the average number of each character needed (n // 4). The function then attempts to replace all '?' characters in `s` with 'A', 'C', 'G', or 'T' to achieve a balanced count of each character. If there are any characters ('A', 'C', 'G', 'T') that are still needed after replacement, it prints '==='; otherwise, it prints the modified string `res`. If the string has more '?' than can be replaced while maintaining the balance, the output will not be valid.

