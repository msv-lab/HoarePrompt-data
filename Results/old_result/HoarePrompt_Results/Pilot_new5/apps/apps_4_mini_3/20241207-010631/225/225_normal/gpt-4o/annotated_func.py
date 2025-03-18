#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters, and the length of s does not exceed 100.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters, `max_jump` is the maximum jump between consecutive vowels or 1 if there are no vowels, `prev_pos` is the index of the last vowel found or -1 if no vowels were found.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns the maximum jump calculated as the maximum of its previous value and the length of the string 's' minus the index of the last vowel found, which is stored in 'prev_pos'.
#Overall this is what the function does:The function accepts a non-empty string `s` consisting of capital English letters and returns the maximum distance (jump) between consecutive vowels in the string. If there are no vowels, it returns the length of the string as the maximum jump. It calculates the maximum jump by considering the distance from the last vowel found to the end of the string as well.

