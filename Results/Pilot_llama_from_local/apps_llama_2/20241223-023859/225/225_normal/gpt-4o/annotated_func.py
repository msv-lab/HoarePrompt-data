#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters, `vowels` is a set containing {'A', 'E', 'I', 'O', 'U', 'Y'}, `max_jump` is the maximum distance between any two consecutive vowels in `s`, and `prev_pos` is the index of the last vowel found in `s`.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns the maximum distance from the last vowel to the end of string `s`, where `s` is a non-empty string of capital English letters and the last vowel can be any of 'A', 'E', 'I', 'O', 'U', 'Y'.
#Overall this is what the function does:The function accepts a non-empty string `s` of capital English letters and returns the maximum distance between any two consecutive vowels in `s`, including the distance from the last vowel to the end of the string. The function considers the vowels 'A', 'E', 'I', 'O', 'U', 'Y' and handles edge cases where the string contains no vowels or only one vowel. In the case where the input string is empty or contains no capital English letters, the function may not behave as expected. The function's output will be the maximum distance between any two consecutive vowels in the input string, providing a measure of the spacing between vowels in the given string.

