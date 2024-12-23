#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200) representing the length of string s, and s is a string consisting of both lowercase and uppercase Latin letters, with a length equal to n.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `s` is a string of length `n`, `max_count` is the maximum number of unique lowercase letters encountered consecutively in `s`, `current_set` is empty, and `current_count` is 0. If `s` contains no lowercase letters, `max_count` will be 0. If there are consecutive lowercase letters in `s`, `max_count` will be the largest number of distinct lowercase letters between non-lowercase characters.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function reads a positive integer `n` and a string `s` of length `n` composed of both lowercase and uppercase Latin letters. It determines the maximum number of unique lowercase letters that appear consecutively in `s`, resetting the count whenever a non-lowercase character is encountered. After processing, it prints this maximum count. If the string consists solely of non-lowercase characters, the output will be `0`. Additionally, there is no handling for invalid input or cases where the string may be empty, which could lead to unexpected behavior. The function does not accept parameters, it operates directly on user input.

