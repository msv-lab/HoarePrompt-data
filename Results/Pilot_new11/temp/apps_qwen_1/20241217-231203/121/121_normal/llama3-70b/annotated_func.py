#State of the program right berfore the function call: The input consists of two lines. The first line contains an integer n indicating the length of the genome string, and the second line contains a string s of length n consisting of characters 'A', 'C', 'G', 'T', and '?'. The value of n is between 4 and 255 inclusive.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `n` is the integer value of the first input line, `s` is an empty string, `count` is a dictionary with keys 'A', 'C', 'G', 'T' and values representing the count of corresponding characters 'A', 'C', 'G', 'T' in the original string `s`. If any character `c` in the string `s` is not '?', then `count[c]` is incremented by 1 for each occurrence of `c` in `s`.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `n` is the integer value of the first input line, `s` is an empty string, `count` is a dictionary with keys 'A', 'C', 'G', 'T' and values all equal to 0, `avg` is `n // 4`, and the string 'ACGT' is correctly defined.
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
        
    #State of the program after the  for loop has been executed: `s` is the input string, `count` is a dictionary with keys 'A', 'C', 'G', 'T' and values updated based on the characters in `s`, `avg` is `n // 4`, and `res` is the longest prefix of `s` that consists of 'A', 'C', 'G', and 'T' in the order 'ACGT' based on their counts in `count`.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: *`s` is the input string, `count` is a dictionary with keys 'A', 'C', 'G', 'T' and values updated based on the characters in `s`, `avg` is `n // 4`. If `any(count.values())` is `True`, `res` is the longest prefix of `s` that consists of 'A', 'C', 'G', and 'T' in the order 'ACGT' based on their counts in `count`, and the console output is '==='. Otherwise, `res` is an empty string, and `any(count.values())` is `False`.
#Overall this is what the function does:The function processes an input string `s` of length `n`, which consists of characters 'A', 'C', 'G', 'T', and '?'. It first counts the occurrences of 'A', 'C', 'G', and 'T' in `s`, excluding the '?' characters. Then, it adjusts these counts to ensure that each character 'A', 'C', 'G', and 'T' appears approximately `n // 4` times by either decrementing or incrementing their counts. After this adjustment, it constructs a new string `res` by replacing all '?' characters in `s` with 'A', 'C', 'G', or 'T' in the order 'ACGT' based on their adjusted counts. If the adjusted counts are not all zero, it prints '==='; otherwise, it prints the constructed string `res`. Potential edge cases include when `n` is 4 (the minimum length), and when the adjusted counts cannot perfectly match `n // 4`.

