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
        
    #State of the program after the  for loop has been executed: `s` is an input string of capital English letters, `vowels` is 'AEIOUY', `n` is the length of `s`, `max_jump` is equal to the maximum distance between consecutive vowels in `s`, `last_vowel` is the index of the last vowel found in `s`, and if there are no vowels, `max_jump` is 0.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is a string of capital English letters, `vowels` is 'AEIOUY', `n` is the length of `s`, and `last_vowel` is the index of the last vowel found in `s`. If `last_vowel` is not equal to `n - 1`, `max_jump` is updated to the maximum of its current value and the value calculated as (n - last_vowel) // 2 + 1. If `last_vowel` is equal to `n - 1`, `max_jump` remains unchanged.
    print(max_jump)
#Overall this is what the function does:The function accepts a non-empty string consisting of capital English letters and calculates the maximum "jump" between consecutive vowels in the string. The jump is defined as half the distance between the indices of consecutive vowels, rounded up, plus one for the first vowel found. If there are no vowels, it returns 0. If the last character of the string is not a vowel, it updates the maximum jump based on the distance from the last vowel to the end of the string. The result is printed as an integer.

