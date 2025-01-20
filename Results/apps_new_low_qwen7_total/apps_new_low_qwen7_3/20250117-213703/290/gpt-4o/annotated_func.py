#State of the program right berfore the function call: The input is a string s consisting only of the uppercase English letters "V" and "K" with a length between 1 and 100, inclusive.
def func():
    s = input()

count_vk = 0
    for i in range(len(s) - 1):
        if s[i] == 'V' and s[i + 1] == 'K':
            count_vk += 1
        
    #State of the program after the  for loop has been executed: The string `s` can be any valid string, `count_vk` is the total number of occurrences of the substring "VK" in `s`, and `i` is `len(s) - 2` if the loop executed at least once, otherwise `i` is 0.
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
        
    #State of the program after the  for loop has been executed: `s` is a valid string, `count_vk` is the total number of occurrences of the substring "VK" in `s`, `i` is 0, `max_vk` is the maximum value between the initial `count_vk` and all `new_count_vk` values calculated during each iteration of the loop, and `s_new` remains unchanged after all iterations.
    print(max_vk)
#Overall this is what the function does:The function `func()` accepts a string `s` consisting only of the uppercase English letters "V" and "K" with a length between 1 and 100, inclusive. It calculates the maximum number of non-overlapping "VK" substrings that can be achieved by swapping any "V" with a "K" or vice versa in the given string. After processing, it prints the maximum count of such substrings. Edge cases include strings without "VK", where the maximum count will be 0. If the string consists entirely of "V"s or "K"s, the maximum count will also be 0.

