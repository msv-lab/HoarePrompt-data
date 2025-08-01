#State of the program right berfore the function call: There is an available input where the first line contains an integer n (4 ≤ n ≤ 255) representing the length of the genome, and the second line contains a string s of length n consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program returns None
    #State of the program after the if block has been executed: `n` is an integer and 4 ≤ `n` ≤ 255, `n` is a multiple of 4, `data` is a list where the first element is the string representation of `n` and the second element is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?', `s` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: To determine the output state after all iterations of the loop have finished, let's analyze the given information and the loop code step by step.
    #
    #1. **Initial State**: 
    #   - `n` is an integer and a multiple of 4 between 4 and 255.
    #   - `data` is a list where the first element is the string representation of `n` and the second element is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'.
    #   - `s` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'.
    #   - `target_count` is `n // 4`.
    #   - `counts` is a dictionary with keys 'A', 'C', 'G', 'T' and values 0.
    #
    #2. **Loop Code**:
    #   ```
    #   for char in s:
    #       if char in counts:
    #           counts[char] += 1
    #   ```
    #   This loop iterates over each character in string `s`. If the character is one of the keys in the `counts` dictionary ('A', 'C', 'G', 'T'), it increments the count for that character by 1.
    #
    #3. **Output State after Some Iterations**:
    #   - The output states after 1, 2, and 3 iterations give us hints about how the variables change. 
    #   - `n`, `data`, and `target_count` do not change because the loop does not modify them.
    #   - `s` must have at least as many characters as the number of iterations for the loop to execute that many times.
    #   - `counts` is updated based on the characters in `s` that match the keys in `counts`.
    #
    #4. **Final Output State**:
    #   - Since the loop iterates over all characters in `s` (which has a length of `n`), after all iterations, `counts` will contain the total count of 'A', 'C', 'G', 'T' characters in `s`.
    #   - The loop does not modify `n`, `data`, or `target_count`, so their values remain as in the initial state.
    #   - `s` is not modified by the loop, so its value remains the same.
    #
    #Given this analysis, if the loop executes (meaning `s` is not empty), the final state of `counts` will reflect the total counts of 'A', 'C', 'G', 'T' in `s`. If the loop does not execute (because `s` is empty), then `counts` remains unchanged with all values being 0. However, since `s` is defined as a string of length `n` and `n` is between 4 and 255, `s` cannot be empty, ensuring the loop will always execute.
    #
    #**Output State**: **`n` is an integer and a multiple of 4 between 4 and 255, `data` is a list where the first element is the string representation of `n` and the second element is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?', `s` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?', `target_count` is `n // 4`, and `counts` is a dictionary with keys 'A', 'C', 'G', 'T' where each value is the total count of the respective character in `s`.**
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: To determine the output state after all iterations of the loop have finished, let's analyze the given information and the loop code step by step.
    #
    #1. **Initial State**: 
    #   - `n` is an integer and a multiple of 4 between 4 and 255.
    #   - `data` is a list where the first element is the string representation of `n` and the second element is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'.
    #   - `s` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?'.
    #   - `target_count` is `n // 4`.
    #   - `counts` is a dictionary with keys 'A', 'C', 'G', 'T' and values 0.
    #
    #2. **Loop Code**:
    #   ```
    #   for char in counts:
    #       if counts[char] > target_count:
    #           print('===')
    #           return
    #   ```
    #   This loop iterates over each character in the `counts` dictionary ('A', 'C', 'G', 'T'). If the count of any character exceeds `target_count` (`n // 4`), it prints '===' and returns from the function.
    #
    #3. **Output State after Some Iterations**:
    #   - The output states after 1, 2, and 3 iterations give us hints about how the variables change. 
    #   - `n`, `data`, and `target_count` do not change because the loop does not modify them.
    #   - `s` must have at least as many characters as the number of iterations for the loop to execute that many times, but since the loop iterates over `counts`, not `s`, this condition is always met since `s`'s length is used to populate `counts` before this loop.
    #   - `counts` is updated based on the characters in `s` that match the keys in `counts`, but this happens in the previous loop (not shown in this snippet).
    #
    #4. **Final Output State**:
    #   - Since the loop checks each character in `counts`, after all iterations, if none of the counts exceed `target_count`, the function will not return and will continue execution beyond this loop.
    #   - If any count exceeds `target_count`, the function will return after printing '===', indicating that at least one of the character counts in `s` exceeds the target count.
    #   - `n`, `data`, `s`, and `target_count` retain their initial values because they are not modified within this loop.
    #   - `counts` retains its value as calculated from `s` before this loop, showing the total count of each character in `s`.
    #
    #Given this analysis, the output state after all iterations of the loop will depend on whether any character count exceeds `target_count`. However, since the loop's primary action is to check and potentially return, the variables' states are mostly determined by the previous loop that populated `counts`.
    #
    #- If the function does not return (meaning no count exceeds `target_count`), `n`, `data`, `s`, `target_count`, and `counts` will have the same values as after the previous loop that populated `counts`.
    #- If the function returns (meaning at least one count exceeds `target_count`), the state of the variables is frozen at the point of return, with `n`, `data`, `s`, and `target_count` unchanged, and `counts` reflecting the distribution of characters in `s`.
    #
    #Thus, the output state after all iterations will reflect whether the function continued beyond this loop or returned due to exceeding `target_count`. Since `counts` is the critical variable here, and its calculation happens before this snippet, we consider its state as determined by the previous loop.
    #
    #**Output State**: **`n` is an integer and a multiple of 4 between 4 and 255, `data` is a list where the first element is the string representation of `n` and the second element is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?', `s` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?`, `target_count` is `n // 4`, and `counts` is a dictionary with keys 'A', 'C', 'G', 'T' where each value is the total count of the respective character in `s`. If any value in `counts` exceeds `target_count`, the function returns after printing '===', otherwise, it continues execution.**
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is an integer and a multiple of 4 between 4 and 255, `data` is a list where the first element is the string representation of `n` and the second element is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?`, `s` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?`, `target_count` is `n // 4`, `counts` is a dictionary with keys 'A', 'C', 'G', 'T' where each value is the total count of the respective character in the original `s` plus the number of times each character was used to update `result`, and `result` is a list of characters where all '?' have been replaced with characters from 'A', 'C', 'G', 'T' that had counts less than `target_count` at the time of their assignment.
    print(''.join(result))
#Overall this is what the function does:The function processes two lines of input, the first containing an integer `n` (4 ≤ `n` ≤ 255) and the second a string `s` of length `n` with characters 'A', 'C', 'G', 'T', and '?'. It checks if `n` is a multiple of 4, counts nucleotides in `s`, and checks if any count exceeds `n // 4`. If `n` is not a multiple of 4 or any count exceeds `n // 4`, it prints '===' and returns None. Otherwise, it replaces '?' in `s` with nucleotides that have counts less than `n // 4` and prints the modified string. The function does not handle unexpected input formats and assumes replacement of '?' is always possible without exceeding target counts.

