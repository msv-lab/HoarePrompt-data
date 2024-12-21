#State of the program right berfore the function call: The input consists of two lines, the first line contains an integer n (4 ≤ n ≤ 255) representing the length of the genome, and the second line contains a string s of length n consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255 (inclusive), `s` is a string, `c` is the last character in `s` if `s` is not empty, `count` is a dictionary with keys 'A', 'C', 'G', 'T' where the value of `count[c]` is the total count of each character 'A', 'C', 'G', 'T' in `s`, ignoring any '?' characters.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255 (inclusive), `s` is a string, `c` is 'T', `avg` is `n // 4`, `count` is a dictionary with keys 'A', 'C', 'G', 'T' where each value `count[c]` is `n // 4 - original_count[c]`.
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
        
    #State of the program after the  for loop has been executed: To determine the output state of the loop after all iterations have finished, let's analyze the loop's behavior based on the provided code and the pattern observed from the output states after executing the loop a few times.
    #
    #1. **Variable `n`**: This remains unchanged as it is not modified within the loop. It is an integer between 4 and 255 (inclusive).
    #
    #2. **Variable `s`**: This is a string, and its content does not change within the loop; it is the source of characters that the loop iterates over. The loop's execution does not alter `s` itself.
    #
    #3. **Variable `c`**: After the loop finishes executing, `c` will hold the last character of `s` that was processed, which could be either one of 'A', 'C', 'G', 'T', or '?' if `s` ends with it.
    #
    #4. **Variable `avg`**: Like `n`, `avg` remains unchanged throughout the execution of the loop. It was initialized to `n // 4`.
    #
    #5. **Variable `count`**: This dictionary initially contains keys 'A', 'C', 'G', 'T' with each value set to `n // 4 - original_count[c]`. During each iteration, if a character `c` from `s` is '?', the loop checks the `count` dictionary for any nucleotide ('A', 'C', 'G', 'T') that has a count greater than 0, appends the first such nucleotide found to `res`, and then decrements its count by 1. If `c` is not '?', it directly appends `c` to `res` without altering the `count` dictionary. After all iterations, the `count` dictionary will reflect the updated counts based on how many times each nucleotide was added to `res` in place of '?'.
    #
    #6. **Variable `res`**: This starts as an empty string. For each character in `s`, if the character is '?', the first available nucleotide ('A', 'C', 'G', 'T') based on the `count` dictionary (i.e., the one with a count greater than 0) is appended to `res`, and its count is decremented. If no nucleotide has a count greater than 0, `res` remains unchanged for that iteration. If the character from `s` is not '?', it is directly appended to `res`. After all iterations, `res` will be a string where all '?' in `s` have been replaced by the nucleotides 'A', 'C', 'G', 'T' based on availability in `count`, and all non-'?' characters from `s` have been appended as is.
    #
    #**Output State**: 
    #**`n` is an integer between 4 and 255 (inclusive), `s` is the original string, `avg` is `n // 4`, `c` is the last character of `s`, `count` is a dictionary with updated counts for 'A', 'C', 'G', 'T' based on replacements made for '?' in `s`, and `res` is a string where all '?' in `s` have been replaced by available nucleotides 'A', 'C', 'G', 'T' based on the `count` dictionary, and all non-'?' characters from `s` are appended as is.**
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`n` is an integer between 4 and 255 (inclusive), `s` is the original string, `avg` is `n // 4`, `c` is the last character of `s`, `count` is a dictionary with updated counts for 'A', 'C', 'G', 'T' based on replacements made for '?' in `s`, and `res` is a string where all '?' in `s` have been replaced by available nucleotides 'A', 'C', 'G', 'T' based on the `count` dictionary, and all non-'?' characters from `s` are appended as is. If there are any remaining nucleotides with counts greater than 0, '===' has been printed to the console. Otherwise, `res` has been printed to the console.
#Overall this is what the function does:The function accepts two lines of input, an integer n and a string s, where n represents the length of the genome and s is a string of length n consisting of the characters 'A', 'C', 'G', 'T', and '?'. It then processes this input to produce a string where all '?' in s have been replaced by the nucleotides 'A', 'C', 'G', 'T' in a way that each nucleotide appears as close to n/4 times as possible, while preserving the order of non-'?' characters. If there are any remaining nucleotides with counts greater than 0 after replacement, it prints '===', otherwise, it prints the resulting string. The function does not handle cases where the input may not match the expected format, such as non-integer values for n, strings of length not equal to n, or characters in s other than 'A', 'C', 'G', 'T', and '?'.

