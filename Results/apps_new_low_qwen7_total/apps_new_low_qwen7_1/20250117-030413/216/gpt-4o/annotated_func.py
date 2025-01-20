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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 200, `s` is a non-empty string consisting only of lowercase and uppercase Latin letters, `max_count` is the maximum count of consecutive unique lowercase characters in `s`, `current_set` is a set containing all unique lowercase characters encountered in `s` up to the last iteration, and `current_count` is 0.
    max_count = max(max_count, current_count)

print(max_count)
#Overall this is what the function does:The function processes an integer `n` (1 ≤ n ≤ 200) and a string `s` (consisting only of lowercase and uppercase Latin letters). It determines the maximum count of consecutive unique lowercase characters in `s`. The function does not explicitly accept `n` and `s` as parameters; instead, it reads them from standard input. After reading `n` and `s`, the function iterates through each character in `s`. If a character is lowercase and not already in the `current_set`, it adds the character to `current_set` and increments `current_count`. If a character is uppercase, it updates `max_count` with the maximum of `max_count` and `current_count`, then resets `current_set` and `current_count`. Finally, it prints the value of `max_count`, which is the maximum count of consecutive unique lowercase characters in `s`.

