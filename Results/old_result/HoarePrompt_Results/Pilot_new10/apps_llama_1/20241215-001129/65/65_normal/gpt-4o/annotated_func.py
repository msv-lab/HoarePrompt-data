#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 100 and 1 <= k <= 100, and s is a string consisting of lowercase letters of the Latin alphabet, where n is the length of s.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: To determine the output state after all iterations of the loop have finished, let's analyze the given information and the loop code step by step.
    #
    #1. **Initial State**: 
    #   - `n` and `k` are integers where 1 <= `n` <= 100 and 1 <= `k` <= 100.
    #   - `s` is an input string of length `n`.
    #   - `color_count` is an empty dictionary.
    #
    #2. **Loop Code**:
    #   - The loop iterates over each character `color` in the string `s`.
    #   - If `color` is already a key in `color_count`, its count is incremented by 1.
    #   - If `color` is not a key in `color_count`, it is added as a key with a count of 1.
    #
    #3. **Output States after the loop executes some number of times**:
    #   - These output states indicate the conditions and variable values after executing the loop a certain number of times. They show how `color_count` is updated based on the characters encountered in `s`.
    #
    #Given the loop code and the output states after executing the loop a certain number of times, we can deduce the following:
    #
    #- The loop will iterate over each character in the string `s`.
    #- For each character, it checks if the character is already a key in `color_count`. If it is, the count for that character is incremented. If not, the character is added to `color_count` with a count of 1.
    #- The loop does not modify `n` or `k`; it only updates `color_count` based on the characters in `s`.
    #
    #**Final Output State**:
    #After all iterations of the loop have finished, `color_count` will contain each unique character from `s` as keys, with their respective counts as values. The values of `n` and `k` remain unchanged, as they are not modified by the loop. The string `s` also remains unchanged, as it is only iterated over and not modified.
    #
    #If the string `s` is empty (which contradicts the given condition that 1 <= `n` <= 100, implying `s` cannot be empty), the loop would not execute, and `color_count` would remain an empty dictionary.
    #
    #However, given that `n` and `k` are within specified ranges and `s` has a length of `n`, the loop will execute for each character in `s`, resulting in `color_count` containing the frequency of each character in `s`.
    #
    #**Output State**: **`n` is an integer such that 1 <= `n` <= 100, `k` is an integer such that 1 <= `k` <= 100, `s` is a string of length `n`, and `color_count` is a dictionary where each key is a unique character from `s` and its corresponding value is the frequency of that character in `s`.**
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100, `k` is an integer such that 1 <= `k` <= 100, `s` is a string of length `n`, `color_count` is a dictionary with key-value pairs representing character frequencies in `s`, and `can_distribute` is `True` if all frequencies in `color_count` are less than or equal to `k`, otherwise `can_distribute` is `False`.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an integer such that 1 <= `n` <= 100, `k` is an integer such that 1 <= `k` <= 100, `s` is a string of length `n`, `color_count` is a dictionary with key-value pairs representing character frequencies in `s`. If `can_distribute` is `True`, the string 'YES' has been printed. If `can_distribute` is `False`, the string 'NO' has been printed to the console.
#Overall this is what the function does:The function reads two integers `n` and `k`, and a string `s` of length `n`, then checks if the frequency of each character in `s` is less than or equal to `k`. If all frequencies are within the limit, it prints 'YES'; otherwise, it prints 'NO', covering all potential cases based on the actual code execution

