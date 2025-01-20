#State of the program right berfore the function call: The input is a string s consisting only of the uppercase English letters "V" and "K" with a length between 1 and 100, inclusive.
def func():
    s = input()

count_vk = 0
    for i in range(len(s) - 1):
        if s[i] == 'V' and s[i + 1] == 'K':
            count_vk += 1
        
    #State of the program after the  for loop has been executed: `s` is the input string, `count_vk` is the total number of occurrences where 'V' is immediately followed by 'K' in the string `s`, and `i` can take any value from 0 to `len(s) - 2` inclusive. The final value of `count_vk` is the sum of 1 for each such occurrence in the string `s`.
    max_vk = count_vk
    for i in range(len(s)):
        if s[i] == 'V':
            s_new = s[:i] + 'K' + s[i + 1:]
        elif s[i] == 'K':
            s_new = s[:i] + 'V' + s[i + 1:]
        else:
            continue
        
        new_count_vk = 0
        
        for j in range(len(s_new) - 1):
            if s_new[j] == 'V' and s_new[j + 1] == 'K':
                new_count_vk += 1
        
        max_vk = max(max_vk, new_count_vk)
        
    #State of the program after the  for loop has been executed: s
    print(max_vk)
#Overall this is what the function does:The function accepts a string `s` consisting only of the uppercase English letters "V" and "K" with a length between 1 and 100, inclusive. It calculates and prints the maximum number of occurrences where "VK" can be formed by performing the following operations:

1. It counts the initial number of "VK" pairs in the string `s`.
2. For each character in the string `s`, it generates a new string by replacing the current character with the other (i.e., "V" becomes "K" and "K" becomes "V").
3. It counts the number of "VK" pairs in each of these new strings.
4. It keeps track of the maximum count of "VK" pairs found among all generated strings.
5. Finally, it prints the maximum count of "VK" pairs.

