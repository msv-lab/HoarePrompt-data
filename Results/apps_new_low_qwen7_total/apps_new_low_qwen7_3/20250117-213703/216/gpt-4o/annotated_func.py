#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the second input line is a string s consisting only of lowercase and uppercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting only of lowercase and uppercase Latin letters. `max_count` is the maximum count of consecutive unique lowercase letters found in `s`. `current_set` is an empty set, and `current_count` is 0.
    max_count = max(max_count, current_count)

print(max_count)
#Overall this is what the function does:The function `func` accepts an integer `n` within the range \(1 \leq n \leq 200\) and a string `s` consisting only of lowercase and uppercase Latin letters. It processes the string `s` to find the maximum count of consecutive unique lowercase letters and returns this maximum count. If `n` is not within the specified range or `s` contains characters other than lowercase and uppercase Latin letters, the function will handle these cases by ignoring them and still process the valid parts of `s`.

