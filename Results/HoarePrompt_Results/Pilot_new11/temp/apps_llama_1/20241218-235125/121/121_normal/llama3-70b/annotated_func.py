#State of the program right berfore the function call: n is an integer greater than or equal to 4 and less than or equal to 255, and s is a string of length n consisting of characters 'A', 'C', 'G', 'T', and '?' such that the total count of 'A', 'C', 'G', and 'T' in s plus the count of '?' in s equals n.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `s` is an input string, `count` is a dictionary with keys 'A', 'C', 'G', 'T' where the value of each key is the count of the corresponding character in `s`.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `s` is an input string, `count` is a dictionary with keys 'A', 'C', 'G', 'T' where each key's value is `n // 4 - original_count[key]`, `avg` is `n // 4`, and `c` is 'T'
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `s` is the input string, `avg` is `n // 4`, `count` is a dictionary with keys 'A', 'C', 'G', 'T' where each key's value is adjusted based on replacements made for '?', `c` is the last character in `s`, and `res` contains the modified string from `s` with '?' replaced based on availability in `count` and 'ACGT'.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`n` is an input integer, `s` is the input string, `avg` is `n // 4`, `count` is a dictionary with keys 'A', 'C', 'G', 'T' where each key's value is adjusted based on replacements made for '?', `c` is the last character in `s`, and `res` contains the modified string from `s` with '?' replaced based on availability in `count` and 'ACGT'. If any value in `count` is greater than 0, '===' has been printed to the console. If all values in `count` are 0, the value of `res` has been printed.
#Overall this is what the function does:The function takes an integer `n` between 4 and 255, and a string `s` of length `n` containing characters 'A', 'C', 'G', 'T', and '?' as input. It calculates the count of each character 'A', 'C', 'G', and 'T' in `s` and then adjusts these counts to achieve a balanced distribution where each character's count is as close as possible to `n // 4`. If there are '?' characters in `s`, it replaces them with 'A', 'C', 'G', or 'T' based on which character's count is currently below its target distribution. The function then checks if all '?' characters have been replaced such that the counts of 'A', 'C', 'G', and 'T' are as close as possible to `n // 4`. If the counts are successfully balanced, the function prints the modified string `s` with all '?' replaced; otherwise, it prints '===' to indicate that not all '?' characters could be replaced to meet the target distribution.

