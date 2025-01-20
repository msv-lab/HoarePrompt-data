#State of the program right berfore the function call: The function takes no input parameters. The input is read from standard input, where the first line contains an integer n (1 ≤ n ≤ 200) representing the length of the string s, and the second line contains the string s consisting of lowercase and uppercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `max_count` is the maximum count of any character in the string `s`, `current_set` contains all unique lowercase characters from `s`, and `current_count` is 0.
    max_count = max(max_count, current_count)

print(max_count)
#Overall this is what the function does:The function reads an integer `n` and a string `s` from standard input, where `n` represents the length of `s` and `s` consists of lowercase and uppercase Latin letters. It then processes the string `s` to find the maximum count of consecutive lowercase characters, while ignoring uppercase characters. The function prints the maximum count of such consecutive lowercase characters. If there are no consecutive lowercase characters, the output will be 0.

