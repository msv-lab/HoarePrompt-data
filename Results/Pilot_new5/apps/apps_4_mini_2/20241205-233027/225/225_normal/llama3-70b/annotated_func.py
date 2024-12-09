#State of the program right berfore the function call: The input is a non-empty string consisting of capital English letters, and the length of the string does not exceed 100.
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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string of capital English letters, `vowels` is 'AEIOUY', `n` is a positive integer equal to the length of `s`, `max_jump` is the maximum jump distance between consecutive vowels or 0 if there are no vowels, `last_vowel` is the index of the last vowel found in `s` or -1 if no vowels were found.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is a non-empty string of capital English letters, `vowels` is 'AEIOUY', `n` is a positive integer equal to the length of `s`, if `last_vowel` is not equal to `n - 1`, then `max_jump` is updated to the maximum of its current value and `(n - last_vowel) // 2 + 1`, while `last_vowel` remains the index of the last vowel found in `s`.
    print(max_jump)
#Overall this is what the function does:The function accepts a non-empty string of capital English letters with a maximum length of 100, calculates the maximum "jump distance" between consecutive vowels, and prints this value. If there are no vowels in the string, it will return a maximum jump distance of 0. Additionally, if the last character of the string is not a vowel, it considers the distance from the last vowel to the end of the string when calculating the maximum jump.

