#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and s is a string of length n consisting of lowercase and uppercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `max_count` is the maximum number of unique lowercase letters in any contiguous segment of lowercase letters in `s`; `current_set` is empty, and `current_count` is 0 after the last character has been processed. If `s` contains no lowercase letters, `max_count` will be 0.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function reads an integer `n` and a string `s` of length `n` consisting of letters in a case-sensitive manner. It calculates and prints the maximum number of unique lowercase letters found in any contiguous segment of `s` consisting solely of lowercase letters. If no lowercase letters are present in `s`, it will return 0. The function maintains a count of unique lowercase letters and resets this count whenever an uppercase letter is encountered, thus only counting segments of lowercase letters. The final output is the maximum count found across all segments processed.

