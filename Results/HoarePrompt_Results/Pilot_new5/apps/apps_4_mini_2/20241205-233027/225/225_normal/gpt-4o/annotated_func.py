#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters with a length not exceeding 100.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string of capital English letters, `vowels` is {'A', 'E', 'I', 'O', 'U', 'Y'}, `max_jump` is the maximum distance between consecutive vowels in `s`, `prev_pos` is the index of the last vowel found in `s`, and `i` is equal to the length of `s` after all iterations of the loop.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns the maximum jump calculated as the maximum of the previous maximum jump and the difference between the length of the string `s` and the index of the last vowel found in `s`.
#Overall this is what the function does:The function accepts a non-empty string `s` consisting of capital English letters and calculates the maximum distance (or "jump") between consecutive vowels in the string. It also considers the distance from the last vowel to the end of the string. The function returns this maximum jump as an integer.

