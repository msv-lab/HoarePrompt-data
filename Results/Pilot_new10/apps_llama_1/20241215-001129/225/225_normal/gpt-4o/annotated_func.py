#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters, with a length not exceeding 100.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters, with a length not exceeding 100, `vowels` is {'A', 'E', 'I', 'O', 'U', 'Y'}, `max_jump` is the maximum distance between any two vowels in `s` if `s` contains vowels, otherwise it is 1, and `prev_pos` is the position of the last vowel in `s` if `s` contains vowels, otherwise it is -1.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns max_jump, which is the maximum of its previous value and the difference between the length of string `s` and the position of the last vowel in `s` (or -1 if `s` does not contain vowels), reflecting the maximum jump considering the string's length and vowel positions.
#Overall this is what the function does:The function accepts a non-empty string `s` of capital English letters, with a length not exceeding 100, and returns the maximum distance between any two consecutive vowels in `s`, including the distance from the last vowel to the end of the string, or the length of `s` plus one if `s` does not contain any vowels.

