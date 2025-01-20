#State of the program right berfore the function call: The input is a non-empty string s consisting of uppercase English letters, where the length of s does not exceed 100.
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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string of uppercase English letters with length `n`, `vowels` is 'AEIOUY', `n` is the length of `s`, `max_jump` is the maximum distance between any two consecutive vowels in `s` (or half the distance plus one if the distance is odd), `last_vowel` is the index of the last vowel in `s`. If no vowels are present in `s`, `max_jump` remains 0 and `last_vowel` remains -1.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is a non-empty string of uppercase English letters with length `n`, `vowels` is 'AEIOUY', `n` is the length of `s`, `last_vowel` is the index of the last vowel in `s`, if no vowels are present in `s`, `max_jump` remains 0 and `last_vowel` remains -1. If `last_vowel` is not equal to `n - 1`, `max_jump` is updated to the maximum of its original value and `(n - last_vowel) // 2 + 1`. Otherwise, `max_jump` remains unchanged.
    print(max_jump)
#Overall this is what the function does:The function reads a non-empty string `s` consisting of uppercase English letters (length ≤ 100) from user input. It calculates the maximum distance between any two consecutive vowels in the string, considering the distance to the start or end of the string if no preceding or following vowel is found, respectively. The function then prints this maximum distance. If the string contains no vowels, the function prints 0. The function does not return any value.

