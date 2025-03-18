#State of the program right berfore the function call: n is an integer such that 4 <= n <= 255, and s is a string of length n consisting of the characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 <= n <= 255, `s` is a string of length `n`, `count` is updated such that `count['A']` is the number of occurrences of 'A' in `s`, `count['C']` is the number of occurrences of 'C' in `s`, `count['G']` is the number of occurrences of 'G' in `s`, `count['T']` is the number of occurrences of 'T' in `s`, and `count['?']` remains 0.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 <= n <= 255, `s` is a string of length `n`, `count['A']` is `avg - count['A']`, `count['C']` is `avg - count['C']`, `count['G']` is `avg - count['G']`, `count['T']` is `avg - count['T']`, `count['?']` remains 0, `avg` is equal to `n // 4.`
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
        
    #State of the program after the  for loop has been executed: `res` is a string containing characters from `s` with '?' replaced by characters from 'A', 'C', 'G', 'T' based on their availability, `count['A']`, `count['C']`, `count['G']`, and `count['T']` reflect their final decremented values, `count['?']` remains 0, and `avg` is equal to `n // 4`.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`res` is a string containing characters from `s` with '?' replaced by 'A', 'C', 'G', 'T' based on their availability, and `count['A']`, `count['C']`, `count['G']`, and `count['T']` reflect their final decremented values while `count['?']` remains 0 and `avg` is equal to `n // 4`. If at least one of the counts in `count` is greater than 0, the replacements reflect this availability. Otherwise, if all values in `count` are 0, `res` is generated with '?' replaced accordingly, resulting in no characters available from 'A', 'C', 'G', and 'T'.
#Overall this is what the function does:The function accepts an integer `n` (between 4 and 255) and a string `s` of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'. It counts the occurrences of 'A', 'C', 'G', and 'T' in `s`, calculates the average number of each nucleotide that should be present (which is `n // 4`), and replaces '?' in the string with the appropriate nucleotides from 'A', 'C', 'G', and 'T' until the counts match the calculated average. If it is not possible to replace '?' such that all nucleotides are balanced, it prints '===', otherwise it prints the resulting string. Edge cases include scenarios where the input string `s` has too many '?' or where the counts of 'A', 'C', 'G', and 'T' cannot be balanced, leading to the output '===' instead of a valid string.

