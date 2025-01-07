#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200) representing the length of string s, and s is a string consisting of lowercase and uppercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 200), `s` is a non-empty string of length `n`, `max_count` is the maximum count of unique lowercase letters encountered in contiguous segments of `s`, `current_set` is empty if the last character of `s` is uppercase or contains unique lowercase letters from the last contiguous segment, `current_count` is the count of unique lowercase letters from the last contiguous segment, which could be 0 if the last character is uppercase.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 200) and a string `s` of length `n` consisting of both lowercase and uppercase Latin letters. It calculates the maximum number of unique lowercase letters found in contiguous segments of the string, resetting the count whenever an uppercase letter is encountered, and prints this maximum count. If the string consists entirely of uppercase letters or contains no lowercase letters, the function will return 0.

