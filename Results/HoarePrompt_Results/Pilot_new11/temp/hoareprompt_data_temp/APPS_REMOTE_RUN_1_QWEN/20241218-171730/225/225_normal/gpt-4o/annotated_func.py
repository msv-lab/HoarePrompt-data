#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters, and the length of s does not exceed 100. The string contains only the characters 'A', 'E', 'I', 'O', 'U', and 'Y' as vowels.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters, and the length of `s` does not exceed 100; `prev_pos` is the index of the last vowel in `s`, `max_jump` is the maximum gap between any two consecutive vowels in `s`, and `vowels` is a set containing {'A', 'E', 'I', 'O', 'U', 'Y'}.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #`max_jump` is the maximum of its current value and the length of the string `s` minus `prev_pos`; `s` is a non-empty string consisting of capital English letters with a length not exceeding 100; `prev_pos` is the index of the last vowel in `s`; `vowels` is a set containing {'A', 'E', 'I', 'O', 'U', 'Y'}. The program returns `max_jump`.
#Overall this is what the function does:The function `func_1` accepts a single parameter `s`, which is a non-empty string consisting of capital English letters (only vowels 'A', 'E', 'I', 'O', 'U', and 'Y' are allowed) with a length not exceeding 100. The function iterates through the string `s` to find the maximum gap (number of consonants) between any two consecutive vowels. It updates the variable `max_jump` to store this maximum gap. After the iteration, it ensures that `max_jump` is also updated to include the distance from the last vowel to the end of the string. The function then returns `max_jump`. Potential edge cases include strings with no vowels or with only one vowel. In such cases, `max_jump` would be the length of the string.

