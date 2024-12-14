#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters, and the length of s does not exceed 100.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters, `vowels` is {'A', 'E', 'I', 'O', 'U', 'Y'}, `max_jump` is the maximum distance between consecutive vowels in `s` (considering the start of the string), `prev_pos` is the index of the last vowel found in `s`, which can be -1 if no vowels exist.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns max_jump, which is the maximum between the previous max_jump and the length of string 's' minus the index of the last vowel found (prev_pos), which can be -1 if no vowels exist.
#Overall this is what the function does:The function accepts a non-empty string `s` consisting of capital English letters and returns the largest distance ('jump') between consecutive vowels in `s`, including the distance from the beginning of the string to the first vowel and from the last vowel to the end of the string. If `s` contains no vowels, it returns the length of the string, since the `prev_pos` would be -1.

