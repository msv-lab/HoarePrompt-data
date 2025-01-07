#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and s is a string consisting only of lowercase and uppercase Latin letters.
def func():
    n = int(input())
    s = input()
    max_count = 0
    current_set = set()
    current_count = 0
    for char in s:
        if char.islower():
            if char not in current_set:
                current_set.add(char)
                current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_set.clear()
            current_count = 0
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(1 \leq n \leq 200\), `s` is a non-empty string, `max_count` is the maximum count of consecutive unique lowercase characters found in `s`, `current_set` is an empty set, and `current_count` is 0.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function processes a given string `s` to find the maximum number of consecutive unique lowercase characters. It reads an integer `n` (though `n` is not used in the function), then iterates through each character in `s`. If a character is lowercase and not already in the current set of characters, it is added to the set and the count of unique characters increases. If the character is uppercase, the function resets the count of unique characters and clears the set. After processing all characters, it prints the maximum count of consecutive unique lowercase characters found in the string `s`. The function does not accept any parameters and operates on the global variables `n` and `s`. Potential edge cases include an empty string `s` or `n` outside the specified range, although the code does not enforce these constraints.

