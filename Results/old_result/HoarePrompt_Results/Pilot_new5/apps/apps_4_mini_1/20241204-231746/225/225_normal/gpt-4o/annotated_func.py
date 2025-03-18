#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters, and the length of s does not exceed 100.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters; `vowels` is {'A', 'E', 'I', 'O', 'U', 'Y'}; `prev_pos` is the index of the last vowel found in `s` or -1 if no vowels are present; `max_jump` is the maximum distance between consecutive vowels found in `s` or 1 if there are no vowels.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns the maximum jump distance which is calculated as max(max_jump, len(s) - prev_pos), where len(s) is the length of the non-empty string 's' consisting of capital English letters and prev_pos is the index of the last vowel found in 's', or -1 if no vowels are present.
#Overall this is what the function does:The function accepts a non-empty string `s` consisting of capital English letters and returns the maximum distance (jump) between consecutive vowels in the string. If no vowels are found, it returns the length of the string since no maximum jump can be defined. The maximum jump is calculated based on the positions of vowels and the edges of the string. If there are no vowels in the string, the function will return the length of the string, which is not covered by the annotations.

