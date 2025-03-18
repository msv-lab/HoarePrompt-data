#State of the program right berfore the function call: The input is a non-empty string consisting of capital English letters, with a length not exceeding 100. The string contains only the characters 'A', 'E', 'I', 'O', 'U', and 'Y' as vowels.
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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters with a length not exceeding 100, `vowels` is 'AEIOUY', `n` is the length of `s`, `max_jump` is the maximum value of `i - last_vowel` // 2 + 1 encountered during the loop (with `i - last_vowel` being even), `last_vowel` is the index of the last vowel found in the string, `i` is `n`. If no vowels are found in the string, `last_vowel` remains -1.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is a non-empty string consisting of capital English letters with a length not exceeding 100, `vowels` is 'AEIOUY', `n` is the length of `s`, `max_jump` is the maximum value of `i - last_vowel` // 2 + 1 encountered during the loop (with `i - last_vowel` being even), `last_vowel` is the index of the last vowel found in the string, `i` is `n`. If `last_vowel` is not equal to `n - 1`, `max_jump` is updated to the maximum value of `max(max_jump, (n - last_vowel) // 2 + 1)`. If `last_vowel` equals `n - 1`, no change is made to `max_jump`.
    print(max_jump)
#Overall this is what the function does:The function accepts a non-empty string consisting of capital English letters, with a length not exceeding 100, containing only the characters 'A', 'E', 'I', 'O', 'U', and 'Y' as vowels. It calculates and prints the maximum jump distance between consecutive vowels in the string. A "jump distance" is defined as half the number of characters between two vowels, rounded up. If there are no vowels in the string, the function prints 0. If the last character of the string is a vowel and there is no other vowel before it, the function correctly considers the distance from the start of the string to this vowel.

