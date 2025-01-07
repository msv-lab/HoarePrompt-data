#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and s is a string consisting of lowercase and uppercase Latin letters with length n.
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
        
    #State of the program after the  for loop has been executed: `max_count` is the maximum number of unique lowercase letters encountered in consecutive characters of `s`, `current_set` is empty, `current_count` is 0; `n` is an integer such that 1 ≤ `n` ≤ 200, `s` is a string of length `n`. If `s` contains no lowercase letters, then `max_count` is 0.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 200) and a string `s` consisting of lowercase and uppercase Latin letters of length `n`. It calculates the maximum number of unique lowercase letters found in consecutive segments of the string. The function then prints this maximum count, which may be zero if there are no lowercase letters present in the string.

