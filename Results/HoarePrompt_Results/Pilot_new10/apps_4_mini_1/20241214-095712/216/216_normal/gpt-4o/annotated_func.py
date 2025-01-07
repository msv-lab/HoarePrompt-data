#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200) representing the length of string s, and s is a string consisting only of uppercase and lowercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 200), `s` is the input string consisting of uppercase and lowercase Latin letters, `max_count` is the maximum count of unique lowercase letters found in any segment of `s`, `current_set` is empty, `current_count` is 0 if the last character was uppercase, or the number of unique lowercase letters in the final segment of `s` if the last character was lowercase.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 200) and a string `s` consisting of uppercase and lowercase Latin letters. It calculates the maximum number of unique lowercase letters found in contiguous segments of the string `s` that are terminated by uppercase letters, and prints that maximum count. If the string consists entirely of uppercase letters, the output will be 0. If the string consists entirely of lowercase letters, the maximum count will equal the total number of unique lowercase letters in the string. The function does not handle invalid inputs, such as non-integer values for `n` or strings longer than `n`.

