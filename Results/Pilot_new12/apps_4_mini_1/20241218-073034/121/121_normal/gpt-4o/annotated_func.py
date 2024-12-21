#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 255, and s is a string of length n consisting of the characters 'A', 'C', 'G', 'T', and '?'.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program returns None since there is no value specified to return after 'return'
    #State of the program after the if block has been executed: *`n` is an integer equal to `int(data[0])` such that 4 ≤ `n` ≤ 255; `s` is equal to `data[1]`. The integer `n` is divisible by 4.
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer equal to `int(data[0])` such that 4 ≤ `n` ≤ 255 and `n` is divisible by 4; `s` is a string of length `len(s)`; `target_count` is equal to `n // 4`; `counts` contains the counts of 'A', 'C', 'G', and 'T' from the string `s`. If a character `char` in `s` is one of 'A', 'C', 'G', or 'T', then `counts[char]` will contain the number of occurrences of that character in `s`. If a character in `s` is not one of these, then `counts` remains unchanged for that character.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255 and divisible by 4, `s` is a string of length `len(s)`, `target_count` is equal to `n // 4`, and `counts` contains the keys 'A', 'C', 'G', and 'T' with `counts[char]` less than or equal to `target_count` for all characters `char` in the keys 'A', 'C', 'G', and 'T'.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 ≤ `n` ≤ 255 and divisible by 4; `s` is a string of length `len(s)`; `target_count` is equal to `n // 4`; each `counts['A'], counts['C'], counts['G'], and counts['T']` is equal to `target_count`; `result` contains characters 'A', 'C', 'G', and 'T' and all '?' have been replaced to ensure the counts meet the target requirement.
    print(''.join(result))
#Overall this is what the function does:The function reads an integer `n` (4 ≤ n ≤ 255) and a string `s` of length `n` containing the characters 'A', 'C', 'G', 'T', and '?'. If `n` is not divisible by 4, it prints '===' and exits. The function counts the occurrences of 'A', 'C', 'G', and 'T' in `s` and checks if any character appears more than `n // 4` times; if so, it prints '===' and exits. If all characters are within the limit, the function replaces any '?' in the string with the appropriate characters to ensure that each of 'A', 'C', 'G', and 'T' appears exactly `n // 4` times. Finally, it prints the modified string. The function does not return any value; instead, it prints outputs based on certain conditions. The missing functionality includes handling cases for invalid characters outside 'A', 'C', 'G', 'T', and '?' as well as a lack of error messages for invalid string compositions.

