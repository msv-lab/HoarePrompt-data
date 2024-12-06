#State of the program right berfore the function call: n is an integer in the range 1 to 200, and s is a string consisting of both lowercase and uppercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer in the range 1 to 200; `s` is a non-empty string; `max_count` is the maximum count of unique lowercase letters found in any contiguous sequence of lowercase letters in `s`; `current_set` is empty; `current_count` is 0.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function accepts an integer `n` (which is read from input) and a string `s` (also read from input) consisting of both lowercase and uppercase Latin letters. It calculates the maximum number of unique lowercase letters found in any contiguous sequence of lowercase letters in `s` and prints this count. The function does not explicitly return a value, and it does not handle cases where `s` may be empty or contain no lowercase letters, potentially resulting in a maximum count of 0 being printed.

