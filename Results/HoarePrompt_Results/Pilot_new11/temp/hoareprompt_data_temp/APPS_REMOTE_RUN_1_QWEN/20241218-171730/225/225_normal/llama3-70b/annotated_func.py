#State of the program right berfore the function call: The input is a non-empty string consisting of capital English letters, and its length does not exceed 100. The string contains only the characters 'A', 'E', 'I', 'O', 'U', and 'Y'.
def func():
    s = input()
    vowels = 'AEIOUY'
    n = len(s)
    max_jump = 0
    last_vowel = -1
    for i in range(n):
        if s[i] in vowels:
            if last_vowel == -1:
                max_jump = max(max_jump, i + 1)
            else:
                max_jump = max(max_jump, (i - last_vowel) // 2 + 1)
            last_vowel = i
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of capital English letters 'A', 'E', 'I', 'O', 'U', 'Y', with a length not exceeding 100; `vowels` is 'AEIOUY'; `n` is the length of `s`; `i` is the index of the last vowel encountered, `last_vowel` is the index of the last vowel encountered; `max_jump` is the maximum of its current value and the distance between consecutive vowels divided by 2 rounded up plus 1. If no vowels are present in `s`, `last_vowel` remains -1 and `max_jump` remains 0.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is a string consisting of capital English letters 'A', 'E', 'I', 'O', 'U', 'Y', with a length not exceeding 100; `vowels` is 'AEIOUY'; `n` is the length of `s`; `i` is the index of the last vowel encountered; `last_vowel` is the index of the last vowel encountered; `max_jump` is the maximum of its current value and the distance between consecutive vowels divided by 2 rounded up plus 1. If `last_vowel` is not equal to `n - 1`, `last_vowel` remains unchanged and `max_jump` remains unchanged. If no vowels are present in `s`, `last_vowel` remains -1 and `max_jump` remains 0.
    print(max_jump)
#Overall this is what the function does:The function `func` accepts a non-empty string consisting of capital English letters, and its length does not exceed 100. The string contains only the characters 'A', 'E', 'I', 'O', 'U', and 'Y'. The function calculates the maximum jump length possible by considering the distances between consecutive vowels in the string. A "jump" is defined as moving from one vowel to another vowel, where the distance is halved and then incremented by 1. If the string ends with a consonant ('Y'), the remaining distance from the last vowel to the end of the string is also considered as a jump. The function returns the maximum jump length found. If no vowels are present in the string, the function returns 0.

