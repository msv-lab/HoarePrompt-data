#State of the program right berfore the function call: s is a non-empty string consisting of capital English letters, with a length not exceeding 100.
def func_1(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    max_jump = 1
    prev_pos = -1
    for i in range(len(s)):
        if s[i] in vowels:
            max_jump = max(max_jump, i - prev_pos)
            prev_pos = i
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters, `max_jump` is the maximum distance between consecutive vowels or 1 if no vowels are present, `prev_pos` is the index of the last vowel found or -1 if no vowels exist.
    max_jump = max(max_jump, len(s) - prev_pos)
    return max_jump
    #The program returns the maximum of its previous value and the length of the string 's' minus the index of the last vowel found or -1 if no vowels exist
#Overall this is what the function does:The function accepts a non-empty string `s` consisting of capital English letters and calculates the maximum distance between consecutive vowels within the string. If no vowels are found, the function returns 1. Otherwise, it returns the maximum distance either between vowels or from the last vowel to the end of the string. Notably, if the string contains no vowels, the return value does not reflect the length of the string minus the index of a last vowel (as stated in the return postconditions), but simply defaults to returning 1. The final state of the program thus includes returning this calculated maximum distance based on the presence and positions of vowels in the input string.

