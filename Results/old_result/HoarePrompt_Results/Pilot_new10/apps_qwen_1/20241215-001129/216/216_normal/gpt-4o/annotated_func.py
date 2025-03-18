#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 200) representing the length of the string s. The second line contains a string s consisting only of lowercase and uppercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 200, `s` is a non-empty string, `max_count` is the maximum number of consecutive lowercase characters seen in `s`, `current_set` is an empty set, and `current_count` is 0.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function reads an integer `n` followed by a string `s` as input, where `n` represents the length of `s`, and `s` consists only of lowercase and uppercase Latin letters. The function then iterates through each character in `s` and keeps track of the maximum count of consecutive lowercase characters. If an uppercase character is encountered, the current count of consecutive lowercase characters is reset. Finally, the function prints the maximum count of consecutive lowercase characters found in `s`.

