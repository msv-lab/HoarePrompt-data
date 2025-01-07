#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the string s consists only of lowercase and uppercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 200\), `s` is a non-empty string, `max_count` is the maximum count of any single lowercase character in `s` that meets the conditions in the if and else blocks, `current_set` is an empty set, and `current_count` is 0.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function processes an integer \(n\) (where \(1 \leq n \leq 200\)) and a string \(s\) consisting only of lowercase and uppercase Latin letters. It counts the maximum number of consecutive unique lowercase characters in \(s\). After processing, it prints the maximum count. The function does not return any value explicitly. If no lowercase characters are found, the printed value will be 0. The function handles the following cases:
1. Counts the number of unique consecutive lowercase characters starting from each lowercase character in the string \(s\).
2. Clears the set and resets the counter when encountering an uppercase character.
3. Updates the maximum count after processing the entire string.

