#State of the program right berfore the function call: The input consists of two lines: the first line contains a positive integer n (1 ≤ n ≤ 200), and the second line contains a string s of length n consisting only of lowercase and uppercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 200, `s` is a string of length `n`, `max_count` is the maximum count of unique lowercase letters in any segment of `s` separated by non-lowercase characters, `current_set` is either empty (if the last character of `s` is not a lowercase letter) or contains the unique lowercase letters from the last segment of `s` (if the last character is a lowercase letter), and `current_count` is either 0 (if the last character of `s` is not a lowercase letter) or represents the count of unique lowercase letters in the last segment of `s` (if the last character is a lowercase letter).
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function reads a positive integer n and a string s of length n, finds the maximum count of unique lowercase letters in any segment of s separated by non-lowercase characters, and prints this maximum count, handling various edge cases including strings with no lowercase letters, strings with a single segment of lowercase letters, and strings where the last character is a lowercase letter.

