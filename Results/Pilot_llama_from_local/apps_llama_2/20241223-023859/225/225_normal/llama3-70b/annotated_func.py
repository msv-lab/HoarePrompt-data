#State of the program right berfore the function call: the input is a non-empty string consisting of capital English letters, and its length does not exceed 100.
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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of capital English letters, `vowels` is 'AEIOUY', `n` is a positive integer not greater than 100 and is equal to the length of `s`, `i` is `n-1`, `last_vowel` is the index of the last vowel in `s` or `-1` if no vowel is found, and `max_jump` is the maximum possible jump between vowels in `s`.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is a non-empty string consisting of capital English letters, `vowels` is 'AEIOUY', `n` is a positive integer not greater than 100 and is equal to the length of `s`, `i` is `n-1`, if `last_vowel` is not equal to `n - 1`, then `max_jump` is the maximum of its previous value and `(n - last_vowel) // 2 + 1`.
    print(max_jump)
#Overall this is what the function does:The function accepts a non-empty string of capital English letters with a maximum length of 100 characters, calculates and prints the maximum possible jump between vowels in the string, where the jump is defined as the maximum of the distance from the start of the string to the first vowel, the distance between consecutive vowels divided by 2 plus 1, and the distance from the last vowel to the end of the string divided by 2 plus 1. If no vowels are found in the string, the function prints the maximum of the distance from the start to the end of the string divided by 2 plus 1. The function does not return any value, it only prints the result. The input string remains unchanged after the function execution.

