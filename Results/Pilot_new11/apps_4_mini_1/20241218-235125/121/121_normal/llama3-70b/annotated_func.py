#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 255, and s is a string of length n consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255, `s` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?', and `count` is a dictionary with the counts of 'A', 'C', 'G', and 'T' based on their occurrences in `s`. Characters in `s` that are '?' do not affect the counts, and therefore `count` only contains the total occurrences of 'A', 'C', 'G', and 'T' in `s`.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255; `s` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'; `count` is updated such that for each character 'c' in 'ACGT': `count[c]` is equal to \( (n // 4) - \text{original count}[c] \); `avg` is equal to \(n // 4`.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255, `s` has been fully processed, `res` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', `count` contains the remaining counts of 'A', 'C', 'G', and 'T' after replacing all '?' in `s`.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 4 ≤ `n` ≤ 255, `s` has been fully processed, and `res` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T'. If there is at least one character remaining in `count` with a non-zero value, the program continues processing. Otherwise, if all counts in `count` are zero, `res` is printed.
#Overall this is what the function does:The function processes input consisting of an integer `n` and a string `s` of length `n` containing the characters 'A', 'C', 'G', 'T', and '?'. It counts the occurrences of 'A', 'C', 'G', and 'T' in `s`. It then calculates the desired average count of each character as `n // 4` and determines how many of each character are still needed to balance the counts. It then replaces each '?' in `s` with the required characters from 'A', 'C', 'G', and 'T' based on their remaining counts. After processing the string, the function checks if there are any characters left that still need to be placed (indicated by non-zero counts). If there are remaining characters needed, it prints '===', signaling that it's not possible to create a balanced string. If all characters are filled appropriately, it prints the resultant string `res` which consists solely of characters 'A', 'C', 'G', and 'T'. The function ensures that the final output is either the balanced string or a specific indication that balancing could not be achieved.

