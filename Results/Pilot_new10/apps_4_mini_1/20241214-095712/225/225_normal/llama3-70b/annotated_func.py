#State of the program right berfore the function call: The input is a non-empty string consisting of capital English letters with a length not exceeding 100.
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
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of capital English letters, `vowels` is 'AEIOUY', `n` is the length of `s`, `last_vowel` is the index of the last vowel found in `s` or remains -1 if none found, and `max_jump` is the maximum jump calculated based on the positions of vowels in `s`.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is an input string consisting of capital English letters, `vowels` is 'AEIOUY', `n` is the length of `s`, and `last_vowel` is the index of the last vowel found in `s` or -1 if none is found. If `last_vowel` is not equal to `n - 1`, `max_jump` is updated to the maximum of its current value and half the distance from `last_vowel` to the end of the string plus one.
    print(max_jump)
#Overall this is what the function does:The function accepts a non-empty string of capital English letters, calculates and prints the maximum jump distance between vowels, and considers the distance from the last vowel to the end of the string.

