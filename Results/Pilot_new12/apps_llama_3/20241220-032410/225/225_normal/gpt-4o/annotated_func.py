#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters with a length not exceeding 100.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters with a length not exceeding 100, `vowels` is {'A', 'E', 'I', 'O', 'U', 'Y'}, `max_jump` is the maximum distance between any two consecutive vowels in `s` (or 1 if `s` contains less than two vowels), `prev_pos` is the index of the last vowel in `s` (or -1 if `s` does not contain any vowels).
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns the maximum jump value, which is the maximum of its previous value and the difference between the length of string `s` and the index of the last vowel in `s` (or `len(s) + 1` if `s` does not contain any vowels), where `s` is a non-empty string of capital English letters not exceeding 100 characters in length.
#Overall this is what the function does:The function calculates and returns the maximum distance between any two consecutive vowels in a given non-empty string `s` of capital English letters, not exceeding 100 characters in length, including the distance from the last vowel to the end of the string. It accepts a string `s` as input, where `s` only contains capital English letters and has a length between 1 and 100. The function considers 'A', 'E', 'I', 'O', 'U', and 'Y' as vowels. If the string contains less than two vowels, the function returns a minimum value of 1 for the maximum jump. If the string does not contain any vowels, the function returns the length of the string plus 1, effectively measuring the distance from the start of the string to the end, since there are no vowels to calculate distance between. The function does not modify the input string `s`.

