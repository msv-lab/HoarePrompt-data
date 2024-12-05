#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 255, and s is a string of length n consisting of characters 'A', 'C', 'G', 'T', and '?'
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program does not return any value, it simply terminates the function.
    #State of the program after the if block has been executed: *`n` is the integer value of `int(data[0])`, `s` is the string value of `data[1]` of length `n`, `data` is a list of strings resulting from splitting the input. The value of `n` is a multiple of 4.
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer, `s` is a string of length `n`, `counts` contains the counts of 'A', 'C', 'G', and 'T' in `s`, and `target_count` is equal to `n // 4`.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `n` is an integer, `s` is a string of length `n`, `counts` contains exactly 4 elements corresponding to the counts of 'A', 'C', 'G', and 'T', `target_count` is equal to `n // 4`, and for all characters in `counts`, `counts[char]` is less than or equal to `target_count.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is an integer, `s` is a string of length `n`, `counts` reflects the counts of 'A', 'C', 'G', and 'T' such that each count is equal to `target_count`, and `result` contains characters from 'A', 'C', 'G', and 'T' with all '?' replaced accordingly, ensuring the character counts conform to the `target_count`.
    print(''.join(result))
#Overall this is what the function does:The function accepts an integer `n` (4 ≤ n ≤ 255) and a string `s` of length `n` containing the characters 'A', 'C', 'G', 'T', and '?'. It checks if `n` is a multiple of 4; if not, it terminates without returning any value. If `n` is valid, it counts the occurrences of 'A', 'C', 'G', and 'T' in `s` and ensures that each of these characters appears exactly `n // 4` times. If any character exceeds this count, it terminates without returning any value. It replaces '?' in `s` with the necessary characters to achieve the target counts, then prints the modified string. If it is not possible to achieve the required counts, the function also terminates without returning any value.

