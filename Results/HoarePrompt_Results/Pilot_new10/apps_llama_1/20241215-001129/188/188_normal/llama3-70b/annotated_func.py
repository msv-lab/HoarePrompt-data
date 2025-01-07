#State of the program right berfore the function call: The function operates on a predefined set of input where the first input is an even integer n (2 ≤ n ≤ 100) representing the number of cards, and the subsequent n inputs are integers a_1, a_2,..., a_{n} (1 ≤ a_{i} ≤ 100) representing the numbers written on the cards.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100 (inclusive), `a` is a list containing `n` integer elements where each element is an input integer, `i` is `n-1`.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: To determine the final output state of the loop, let's analyze the given information and the loop code step by step.
    #
    #1. **Initial State**: 
    #   - `n` is an even integer between 2 and 100 (inclusive).
    #   - `a` is a list containing `n` integer elements.
    #   - `i` is `n-1`.
    #   - `d` is an empty dictionary.
    #
    #2. **Loop Code**:
    #   ```
    #   for i in a:
    #       if i in d:
    #           d[i] += 1
    #       else:
    #           d[i] = 1
    #   ```
    #   This loop iterates over each element `i` in list `a`. For each `i`, it checks if `i` is already a key in dictionary `d`. If `i` is in `d`, it increments the value associated with `i` by 1. If `i` is not in `d`, it adds `i` as a new key with a value of 1.
    #
    #3. **Output States after Few Iterations**:
    #   - After 1 iteration, `i` is the first element in `a`, and `d` contains this element as a key with a value indicating its frequency.
    #   - After 2 iterations, `i` equals the second element in `a`, and `d` contains at least the first two elements of `a` as keys.
    #   - After 3 iterations, `i` equals the third element in `a`, and `d` contains at least the first three elements of `a` as keys, with their respective frequencies updated.
    #
    #4. **Analyzing the Pattern**:
    #   - The loop will iterate `n` times because it iterates over each element in list `a`, which contains `n` elements.
    #   - After all iterations, `i` will be the last element in `a` because the loop iterates over `a` in order.
    #   - Dictionary `d` will contain each unique element from `a` as a key, with its corresponding value being the frequency of that element in `a`.
    #
    #5. **Final Output State**:
    #   - The loop will execute `n` times, where `n` is the number of elements in `a`.
    #   - `i` will be the last element in `a`.
    #   - `d` will be a dictionary where each key is a unique element from `a`, and its value is the frequency of that element in `a`.
    #   - Since `n` is an even integer between 2 and 100 (inclusive), and `a` contains `n` integer elements, the final state of `n` and `a` does not change; `n` remains an even integer between 2 and 100 (inclusive), and `a` remains a list containing `n` integer elements.
    #
    #**Output State: ** `n` is an even integer between 2 and 100 (inclusive), `a` is a list containing `n` integer elements, `i` is the last element in `a`, and `d` is a dictionary where each key is a unique element from `a` and its value is the frequency of that element in `a`.
    c = 0
    a1, a2 = -1, -1
    for i in d:
        if d[i] == n // 2:
            if c == 0:
                a1 = i
                c += 1
            else:
                a2 = i
                break
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100 (inclusive), `a` is a list containing `n` integer elements, `d` is a dictionary where each key is a unique element from `a` and its value is the frequency of that element in `a`, `i` is the last key in `d`, `c` is 0 or 1, `a1` is the first element in `a` with a frequency of `n // 2` or -1, and `a2` is the second element in `a` with a frequency of `n // 2` or -1.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100 (inclusive), `a` is a list containing `n` integer elements, `d` is a dictionary where each key is a unique element from `a` and its value is the frequency of that element in `a`, `i` is the last key in `d`, `c` is 0 or 1, if there are at least two elements in `a` with a frequency of `n // 2`, then `a1` and `a2` are the first and second elements in `a` with a frequency of `n // 2`, 'YES' has been printed to the console, and `a1` and `a2` have been printed to the console. Otherwise, `a1` is the first element in `a` with a frequency of `n // 2` or -1, `a2` is the second element in `a` with a frequency of `n // 2` or -1, and 'NO' has been printed to the console, indicating that either `a1` is -1 or `a2` is -1, or both are -1.
#Overall this is what the function does:The function reads an even integer `n` and `n` integers, counts the frequency of each integer, and prints 'YES' followed by the first two integers that appear exactly `n // 2` times if such integers exist, otherwise prints 'NO', assuming the input meets certain criteria, but does not perform error checking on the input.

