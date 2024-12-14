#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 255, and s is a string of length n consisting only of the characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255, `s` is a string of length `n` consisting of 'A', 'C', 'G', 'T', and '?', `count` is {'A': the number of 'A's in `s`, 'C': the number of 'C's in `s`, 'G': the number of 'G's in `s`, 'T': the number of 'T's in `s'}. If `s` consists only of '?', then `count` remains {'A': 0, 'C': 0, 'G': 0, 'T': 0}.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255; `s` is a string of length `n` consisting of 'A', 'C', 'G', 'T', and '?'; `count` is updated as `count['A']` = `avg - count['A']`, `count['C']` = `avg - count['C']`, `count['G']` = `avg - count['G']`, `count['T']` = `avg - count['T']`, where `avg` is `n // 4`, and `c` has taken all values in the sequence 'A', 'C', 'G', 'T'.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255; `s` is a string of length `n` consisting of 'A', 'C', 'G', 'T', and '?'; `res` is a string containing all non-'?' characters from `s` along with characters from 'A', 'C', 'G', 'T' added in the order based on their presence in `count` where `count` maintains non-negative values for 'A', 'C', 'G', and 'T', reflecting the remaining occurrences after processing all '?' characters in `s`. If no '?' exists in `s`, `res` will be exactly `s`, while if `count` for 'A', 'C', 'G', and 'T' is exhausted, those characters will not appear in `res`.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 4 ≤ `n` ≤ 255; `s` is a string of length `n` consisting of 'A', 'C', 'G', 'T', and '?'; if there is at least one non-zero value in `count`, `res` contains all non-'?' characters from `s` along with characters from 'A', 'C', 'G', 'T' added in the order based on their presence in `count`, reflecting the remaining occurrences after processing all '?' characters in `s`. If all values for 'A', 'C', 'G', and 'T' in `count` are zero, then `res` consists solely of the non-'?' characters from `s` which are printed.
#Overall this is what the function does:The function accepts an integer `n` (where 4 ≤ n ≤ 255) and a string `s` of length `n` consisting solely of the characters 'A', 'C', 'G', 'T', and '?'. It counts the occurrences of each character and calculates the average number of 'A's, 'C's, 'G's, and 'T's that should ideally be present for balance. The function then replaces the '?' characters in `s` with the required characters ('A', 'C', 'G', 'T') to achieve this balance, in the order they are needed. If it is not possible to replace all '?' characters while satisfying the required counts, the function prints '===', otherwise, it prints the modified string `res`. Edge cases include handling scenarios where all characters in `s` are '?' or when the input string already has a balanced number of 'A's, 'C's, 'G's, and 'T's.

