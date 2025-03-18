#State of the program right berfore the function call: n is an integer between 4 and 255, and s is a string of length n consisting of the characters 'A', 'C', 'G', 'T', and '?'.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program returns None, as there is no value specified to return.
    #State of the program after the if block has been executed: *`n` is equal to the integer value of `data[0]`, `s` is equal to `data[1]`, and `n` is divisible by 4.
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `n` is equal to the integer value of `data[0]`, `s` is a string of length equal to `n`, `target_count` is equal to `n // 4`, `counts` is a dictionary {'A': count of 'A' in `s`, 'C': count of 'C' in `s`, 'G': count of 'G' in `s`, 'T': count of 'T' in `s`}. The sum of `counts['A']`, `counts['C']`, `counts['G']`, and `counts['T']` is equal to `n`.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `n` is equal to the integer value of `data[0]`, `s` is a string of length equal to `n`, `target_count` is equal to `n // 4`, `counts` is a dictionary containing counts of 'A', 'C', 'G', and 'T' that are all less than or equal to `target_count`, `char` is the last key in `counts`.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `result` is a string of length `n` where all '?' are replaced by characters from `counts` such that each character in `counts` appears no more than `target_count` times, `counts` contains the final counts of 'A', 'C', 'G', and 'T' after filling `result`, and `target_count` is equal to `n // 4`.
    print(''.join(result))
#Overall this is what the function does:The function accepts an integer `n` (between 4 and 255) and a string `s` of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'. It verifies if `n` is divisible by 4; if not, it prints '===' and returns None. If `n` is divisible by 4, it counts the occurrences of 'A', 'C', 'G', and 'T' in `s` and ensures that none of these characters exceed `n // 4` in count. It then replaces any '?' in `s` with the characters 'A', 'C', 'G', or 'T' as needed to meet the count requirement, and finally prints the modified string. The function does not return any value but will print '===' if any character exceeds the allowed count or if `n` is not divisible by 4.

