#State of the program right berfore the function call: n is an integer such that 4 <= n <= 255, and s is a string of length n containing characters from the set {'A', 'C', 'G', 'T', '?'}.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program returns without any value as the return statement is empty.
    #State of the program after the if block has been executed: *`n` is an integer such that 4 <= n <= 255; `s` is a string of length `n` containing characters from the set {'A', 'C', 'G', 'T', '?'}, `data` is a list obtained from splitting the full input string into separate elements based on whitespace; `s` is now equal to `data[1]`, and `n` is a multiple of 4.
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 <= `n` <= 255; `s` is a string of length `n`; `data` is a list obtained from splitting the full input string; `s` is equal to `data[1]`; `target_count` is equal to `n // 4`; `counts` is a dictionary with counts of 'A', 'C', 'G', 'T' representing how many times each character appears in `s`.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 <= `n` <= 255, `s` is a string of length `n`, `data` is a list obtained from splitting the full input string, `target_count` is equal to `n // 4`, `counts` contains keys 'A', 'C', 'G', 'T' with all counts less than or equal to `target_count`.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 4 <= `n` <= 255; `s` is a string of length `n`; `data` is a list obtained from splitting the full input string; `target_count` is equal to `n // 4`; `counts` contains keys 'A', 'C', 'G', 'T' with each count equal to `target_count` if there were no '?', or all counts balanced such that the characters in `result` are filled appropriately, meeting the count target without exceeding. If there are still '?', they remain in `result` after all assignments.
    print(''.join(result))
#Overall this is what the function does:The function accepts an integer `n` (where 4 <= n <= 255) and a string `s` of length `n` containing characters from {'A', 'C', 'G', 'T', '?'}. It checks if `n` is a multiple of 4; if not, it prints '===' and returns nothing. It counts the occurrences of 'A', 'C', 'G', and 'T' in `s`, ensuring none exceed `n/4`. If any character does, it also prints '===' and returns nothing. The function replaces '?' in the string to balance counts of 'A', 'C', 'G', 'T' to be equal to `n/4`. Finally, it prints the modified string without returning a value. If there are still '?' left after all replacements, they remain unchanged. The function handles edge cases related to count validation and ensures constraints on input are followed before processing.

