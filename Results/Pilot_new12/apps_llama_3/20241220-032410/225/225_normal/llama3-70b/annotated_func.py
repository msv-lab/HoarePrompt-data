#State of the program right berfore the function call: the input is a non-empty string consisting of capital English letters with a length not exceeding 100.
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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters with a length not exceeding 100, `vowels` is 'AEIOUY', `n` is the length of `s` and is greater than 0, `i` is `n - 1`, `last_vowel` is the index of the last vowel in `s` or -1 if no vowel is found, `max_jump` is the maximum jump between any two vowels in `s` plus one, or the position of the first vowel plus one if only one vowel is present, or 0 if no vowels are present.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is a non-empty string consisting of capital English letters with a length not exceeding 100, `vowels` is 'AEIOUY', `n` is the length of `s` and is greater than 0, `i` is `n - 1`, `last_vowel` is the index of the last vowel in `s` or -1 if no vowel is found. If the last character of `s` is not a vowel, then `max_jump` is the maximum of its previous value and `(n - last_vowel) // 2 + 1`. Otherwise, `max_jump` remains unchanged.
    print(max_jump)
#Overall this is what the function does:The function calculates and prints the maximum jump between any two vowels in a given input string, where a jump is defined as half the distance between two vowels plus one. If the input string contains only one vowel, the maximum jump is the position of that vowel plus one. If the input string does not contain any vowels, the maximum jump is 0. Additionally, if the last character of the string is not a vowel, the function considers the distance from the last vowel to the end of the string as a potential maximum jump. The function does not accept any parameters, reads input from the user, and does not return any value, instead printing the calculated maximum jump to the console. The input string is expected to be a non-empty string consisting of capital English letters with a length not exceeding 100.

