#State of the program right berfore the function call: n is an integer such that 4 <= n <= 255, and s is a string of length n consisting only of the characters 'A', 'C', 'G', 'T', and '?'.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program returns nothing as there is no value specified to return.
    #State of the program after the if block has been executed: *`n` is equal to the integer value of `data[0]`, `s` is a string equal to `data[1]` consisting only of the characters 'A', 'C', 'G', 'T', and '?'; `data` is a list created from splitting the input string `s` by whitespace, and `n` is a multiple of 4.
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `counts` is a dictionary containing the counts of 'A', 'C', 'G', and 'T' from string `s`; if `s` is empty, `counts` remains {'A': 0, 'C': 0, 'G': 0, 'T': 0}.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `counts` is a dictionary containing counts of 'A': [0 or more], 'C': [0 or more], 'G': [0 or more], 'T': [0 or more]; the loop will execute for each base, and if a count exceeds `target_count`, the function would have returned early. If none exceed, counts remain as counted from the string `s`.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `counts` is a dictionary with keys 'A', 'C', 'G', and 'T', each having values between 0 and `target_count`, inclusive. `result` is a list containing the characters assigned based on the respective counts, or it may still have '?' in places where counts have reached `target_count`. If `n` is greater than the number of '?' in the original `result`, the number of characters assigned equals the original number of '?' that were replaced before reaching the limit set by `target_count`. If there were no '?' characters in `result` or if counts for all characters reached `target_count`, then `result` remains unchanged.
    print(''.join(result))
#Overall this is what the function does:The function processes an input string of characters 'A', 'C', 'G', 'T', and '?' based on a specified integer length. It ensures that the number of each base does not exceed a target count derived from the input length, which must be a multiple of four. If the length is not a multiple of four or if any base exceeds its target count, the function outputs '===' and terminates. It replaces any '?' characters in the string with the corresponding base if their count is below the target. Finally, the function outputs the modified string. The function does not return values but may output warnings or the resulting string, and handles cases with insufficient '?' characters by not replacing them if the target count has been achieved. Edge cases include strings of different lengths, no '?' characters, or all bases reaching their target count.

