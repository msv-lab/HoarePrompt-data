#State of the program right berfore the function call: n is an integer between 4 and 255, and s is a string of length n consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `s` is a string of length `n`, `count` contains the counts of 'A', 'C', 'G', 'T' in `s`, and if `n` is greater than 0, `count` reflects the total number of occurrences of each character ignoring '?' characters.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `s` is a string of length `n`, `count` contains values `avg - original_count['A']`, `avg - original_count['C']`, `avg - original_count['G']`, `avg - original_count['T']`, and `avg` is equal to `n // 4`.
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
        
    #State of the program after the  for loop has been executed: `s` is a string of length `n`, where all '?' have been replaced by valid characters from 'A', 'C', 'G', 'T' such that the counts of these characters in `count` reflect the original counts minus those used to replace '?', and `res` contains the complete valid string formed from `s`, with `c` being the last character processed from `s` which can be either a replaced character or the last non-'?' character in `s`.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`s` is a string of length `n`, where all '?' have been replaced by valid characters from 'A', 'C', 'G', 'T'; `count` reflects the original counts minus those used to replace '?'; `res` contains the complete valid string formed from `s`; `c` is the last character processed from `s`. If at least one of the values in `count` is greater than 0, '===' has been printed. If all values of `count` are 0, the output of the print statement is `res`.
#Overall this is what the function does:The function accepts an integer `n` (between 4 and 255) and a string `s` of length `n` made up of the characters 'A', 'C', 'G', 'T', and '?'. It counts occurrences of 'A', 'C', 'G', and 'T' in the string while ignoring '?' characters. It calculates the average count of each valid character as `avg = n // 4`. Then, for each '?', it replaces it with a valid character from 'A', 'C', 'G', 'T' based on the required count calculated earlier. After processing, if any character still needs to be added (i.e., if `count` has any remaining values greater than zero), it prints '===', indicating an incomplete formation. Otherwise, it outputs the fully formed string `res`, which contains all '?' replaced. The function ensures that the resulting string contains characters distributed evenly as much as possible; however, there is no validation for the input beyond the expected format. The function doesn't handle scenarios where input is not as expected or where it cannot fully replace all '?' due to excess required characters.

