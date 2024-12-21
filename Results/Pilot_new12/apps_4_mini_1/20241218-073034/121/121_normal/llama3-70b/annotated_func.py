#State of the program right berfore the function call: n is an integer between 4 and 255 (inclusive), and s is a string of length n consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `count` contains the counts of 'A', 'C', 'G', and 'T' in the string `s`, and the total number of '?' in `s` does not affect the counts in `count`. `n` is an integer between 4 and 255, and `s` is a string of length exactly `n`.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `count['A']` is `avg - original count['A']`, `count['C']` is `avg - original count['C']`, `count['G']` is `avg - original count['G']`, `count['T']` is `avg - original count['T']`, `n` is an integer between 4 and 255, `s` is a string of length exactly `n`, `avg` is an integer between 1 and 63 (equal to `n // 4`).
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
        
    #State of the program after the  for loop has been executed: `count['A']`, `count['C']`, `count['G']`, `count['T']` reflect the remaining counts of each nucleotide after processing all characters in `s`, `n` is the initial integer between 4 and 255, `s` is an empty string post-processing, and `res` contains the resulting string with all `?` replaced and original characters.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`count['A']`, `count['C']`, `count['G']`, `count['T']` reflect the remaining counts of each nucleotide after processing all characters in `s`, where `n` is an integer between 4 and 255, `s` is an empty string post-processing, and `res` contains the resulting string with all `?` replaced and original characters. If at least one nucleotide count in `count` is greater than 0, the counts and the resulting string are updated accordingly. If all nucleotide counts are 0, then `res` is printed with the original characters and all `?` replaced.
#Overall this is what the function does:The function processes a string `s` of length `n`, consisting of characters 'A', 'C', 'G', 'T', and '?', by counting occurrences of 'A', 'C', 'G', and 'T'. It computes the required counts for each nucleotide to achieve an equal distribution (one-fourth of `n`) and replaces each '?' in the string with the corresponding nucleotides, prioritizing those that still need counts. After processing, if any nucleotide count remains unmet (greater than 0), it prints '===', indicating that a balanced distribution is not possible; otherwise, it prints the newly formed string `res` which contains the original characters and all '?' replaced with the required nucleotides. Edge cases include the possibility of having too many '?' or not enough nucleotides to meet an equal distribution, which are handled by the checks on the final counts. The function does not return values; instead, it prints its outcomes directly.

