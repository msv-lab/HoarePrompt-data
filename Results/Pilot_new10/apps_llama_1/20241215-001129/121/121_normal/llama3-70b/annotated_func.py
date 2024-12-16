#State of the program right berfore the function call: The function takes no explicit parameters, but it reads two inputs: an integer n and a string s of length n, where n is an integer such that 4 ≤ n ≤ 255, and s is a string consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255 (inclusive), `s` is the input string, `count` is a dictionary with keys 'A', 'C', 'G', 'T' where each value represents the count of the respective character in `s`.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255 (inclusive), `s` is the input string, `avg` is an integer between 1 and 63 (inclusive) equal to `n // 4`, and `count` is a dictionary with keys 'A', 'C', 'G', 'T' where each value `count[c]` is `n // 4 - count_original[c]`, with `count_original[c]` being the original count of character `c` before the loop execution.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255 (inclusive), `s` is the fully processed input string, `avg` is `n // 4`, `count` is a dictionary with keys 'A', 'C', 'G', 'T' and values decremented by the number of times each nucleotide was used to replace '?' in `s`, `res` is the resulting string after replacing all '?' in `s` with the available nucleotides from `count`.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: `n` is an integer between 4 and 255 (inclusive), `s` is the fully processed input string, `avg` is `n // 4`, `count` is a dictionary with keys 'A', 'C', 'G', 'T', `res` is the resulting string after replacing all '?' in `s` with the available nucleotides from `count`. If at least one of the values in the `count` dictionary is greater than 0, '===' has been printed to the console. Otherwise, the string `res` has been returned at the output, with all values in the `count` dictionary being 0, indicating that all available nucleotides have been used to replace '?' in `s`.
#Overall this is what the function does:The function reads an integer `n` and a string `s` of length `n`, where `n` is between 4 and 255 (inclusive), and `s` consists of the characters 'A', 'C', 'G', 'T', and '?', replaces '?' in `s` with 'A', 'C', 'G', 'T' to achieve a balance of `n // 4` for each character, and prints the resulting string if all available characters are used, or '===' if there are remaining characters; if the input does not meet the specified conditions, the function's behavior is undefined

