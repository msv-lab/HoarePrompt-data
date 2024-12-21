#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters, with a length not exceeding 100.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters, `prev_pos` is the index of the last vowel in `s` (or -1 if no vowels), `max_jump` is the maximum jump between consecutive vowels, which is at least 1.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns the maximum jump, which is the maximum of its previous value and the length of the string 's' minus the index of the last vowel (prev_pos), where 's' is a non-empty string consisting of capital English letters and 'prev_pos' is the index of the last vowel in 's' (or -1 if no vowels).
#Overall this is what the function does:The function accepts a non-empty string `s` consisting of capital English letters. It calculates the maximum 'jump' between consecutive vowels in the string, where a 'jump' is defined as the number of characters between two vowels (inclusive of the first vowel and exclusive of the second). If there are no vowels in the string, the function will return 1, as the initial value of `max_jump` is set to 1. The function finally returns the maximum of the jumps calculated between consecutive vowels and the jump from the last vowel to the end of the string. Therefore, it returns the largest distance encountered between the last vowel and the beginning of the string or between two vowels. The result effectively measures the maximum possible distance one could 'jump' in the string while adhering to the vowel constraints. Edge cases that it handles include strings with no vowels, where it returns 1, and strings where all characters are vowels, which may yield a maximum jump equal to the length of the string.

