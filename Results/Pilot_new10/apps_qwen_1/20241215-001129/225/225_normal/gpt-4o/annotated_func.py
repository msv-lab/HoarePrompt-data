#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters, and the length of s does not exceed 100. The string may contain the following vowels: 'A', 'E', 'I', 'O', 'U', and 'Y'.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a string, `i` is `len(s)`, `prev_pos` is the last index where a vowel was found in the string `s`, and `max_jump` is the maximum distance between any two consecutive vowels in the string `s`.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns max_jump which is the maximum value between its original value and i - prev_pos, where i is len(s) and prev_pos is the last index where a vowel was found in the string s
#Overall this is what the function does:The function accepts a string `s` and returns the maximum distance between any two consecutive vowels in the string. If no vowels are present, it returns the length of the string plus one.

