#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 255, and s is a string of length n consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program returns None as nothing is specified for return.
    #State of the program after the if block has been executed: *`n` is equal to `int(data[0])`, where `4 ≤ n ≤ 255`; `s` is equal to `data[1]`, a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'; and `n` is a multiple of 4.
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `n` is equal to `int(data[0])`, `s` is equal to `data[1]`, `target_count` is equal to `n // 4`, and `counts` is {'A': count of 'A' in `s`, 'C': count of 'C' in `s`, 'G': count of 'G' in `s`, 'T': count of 'T' in `s`}. The counts of 'A', 'C', 'G', and 'T' will vary based on the distribution of these characters in `s`.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `n` is equal to `int(data[0])`, `s` is a non-empty string, `target_count` is equal to `n // 4`, `counts` contains at least one of 'A', 'C', 'G', 'T'. The loop will execute for each character in `counts`. If any `counts[char]` is greater than `target_count`, the loop exits early. If all characters have `counts[char]` less than or equal to `target_count`, then the loop will complete its iterations without returning, indicating that none of the counts exceed the target count.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `result` contains all characters from `s` with '?' replaced by valid characters from `counts` as necessary, `counts` will hold the counts of each character ('A', 'C', 'G', 'T') adjusted accordingly based on the replacements made, ensuring that for each character, its count is either equal to or not exceeding `target_count`. If there were no '?' characters in `s`, then `result` will be equal to `s`, and `counts` will remain unchanged.
    print(''.join(result))
#Overall this is what the function does:The function reads an integer `n` and a string `s` from standard input. `n` must be between 4 and 255 and `s` should contain the characters 'A', 'C', 'G', 'T', and '?'. If `n` is not a multiple of 4, the function outputs '===' and terminates. After confirming `n` is valid, it counts occurrences of 'A', 'C', 'G', and 'T' in `s`. If any of these counts exceed `n / 4`, it once again outputs '===' and terminates. The function then replaces each '?' in the string with characters 'A', 'C', 'G', or 'T' as necessary to ensure that none exceed the target count of `n / 4`. Finally, it prints the modified string. If `s` contains no '?', the output will be identical to `s`. The function always returns `None` as it terminates with print statements rather than return values.

