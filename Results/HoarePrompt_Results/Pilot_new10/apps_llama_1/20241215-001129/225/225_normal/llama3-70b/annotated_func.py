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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters with a length not exceeding 100, `vowels` is 'AEIOUY', `n` is the length of `s`, `i` is `n-1`, `last_vowel` is the index of the last vowel in `s` or -1 if `s` does not contain any vowels, and `max_jump` is the maximum possible jump between two vowels in `s` or 0 if `s` does not contain any vowels.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: `s` is a non-empty string consisting of capital English letters with a length not exceeding 100, `vowels` is 'AEIOUY', `n` is the length of `s`, `i` is `n-1`. If the last character of `s` is not a vowel, then `last_vowel` is the index of the last vowel in `s` or -1 if `s` does not contain any vowels, and `max_jump` is the maximum of its previous value and `(n - last_vowel) // 2 + 1`. If the last character of `s` is a vowel, then `last_vowel` and `max_jump` retain their previous values.
    print(max_jump)
#Overall this is what the function does:The function takes a non-empty string of capital English letters with a length not exceeding 100 as input, calculates the maximum possible jump between two vowels in the string, and prints the result, considering the distance between the last vowel and the end of the string if the last character is not a vowel, or returns 0 if the string does not contain any vowels.

