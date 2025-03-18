#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 255, and s is a string of length n consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program returns nothing, as indicated by the empty return statement.
    #State of the program after the if block has been executed: *`n` is the integer value of `data[0]` (4 ≤ n ≤ 255); `s` is equal to `data[1]`, which is a string of length `n`; `data` is a list of substrings derived from the input. The value of `n` is a multiple of 4.
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `n` is the integer value of `data[0]`, `s` is a string of length `n`, `counts` is a dictionary containing the count of characters 'A', 'C', 'G', and 'T' in `s`, where `counts['A']`, `counts['C']`, `counts['G']`, and `counts['T']` represent the total occurrences of these characters in `s`. If no characters from `s` were in counts, then `counts` remains {'A': 0, 'C': 0, 'G': 0, 'T': 0}.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `n` is the integer value of `data[0]`, `s` is a string of length `n`, `counts` is a dictionary containing counts for 'A', 'C', 'G', and 'T'. After the loop executes, if no counts exceeded `target_count`, the output will be that `counts['A']`, `counts['C']`, `counts['G']`, and `counts['T']` are all less than or equal to `target_count`. If `counts` contains only zeros, it remains {'A': 0, 'C': 0, 'G': 0, 'T': 0}.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `s` is a string of length `n`, `result` contains characters from `s` with '?' replaced by characters from `counts` that are less than `target_count`, `counts` reflects the final counts of 'A', 'C', 'G', and 'T' after all possible replacements, and each count in `counts` is less than or equal to `target_count`. If there were more '?' than available characters in `counts` that could be added, the remaining '?' in `result` will remain unchanged.
    print(''.join(result))
#Overall this is what the function does:The function accepts an integer `n` and a string `s` of length `n`, where `n` must be a multiple of 4. If `n` is not a multiple of 4, it outputs '===' and terminates without returning any value. It counts the occurrences of characters 'A', 'C', 'G', and 'T' in `s` and checks if any of these counts exceed `n // 4`; if they do, it outputs '===' and terminates. If the counts are within the allowed limit, it replaces any '?' in `s` with characters from 'A', 'C', 'G', or 'T' until each of these characters appears at most `n // 4` times. Finally, it prints the modified string. In cases where there are more '?' than needed characters, those '?' remain unchanged. The function does not return any value.

