#State of the program right berfore the function call: n is a positive integer, 1 ≤ n ≤ 200, representing the length of string s; s is a string consisting of only lowercase and uppercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 200, `max_count` is the maximum number of distinct lowercase letters encountered in consecutive lowercase segments of `s`, `current_set` is empty, and `current_count` is 0 if `s` was empty or ended with an uppercase letter. If `s` consists only of lowercase letters, `current_set` contains all distinct lowercase letters in `s`, and `current_count` is equal to the number of distinct lowercase letters.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 ≤ n ≤ 200) and a string `s` consisting solely of lowercase and uppercase Latin letters. It analyzes `s` to determine the maximum count of distinct lowercase letters found within consecutive segments that contain only lowercase letters. If an uppercase letter is encountered, it resets the count of the distinct lowercase letters. The final output is the maximum count of distinct lowercase letters from any such segment, printed as a single integer. The function does not handle cases where `s` might be empty; however, based on the constraints, it is assumed that `n` will always be at least 1. If `s` consists entirely of uppercase letters, the output will be 0, as no lowercase letters would be counted.

