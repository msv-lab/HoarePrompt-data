#State of the program right berfore the function call: The input is a non-empty string consisting of capital English letters, with a length not exceeding 100.
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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string of capital English letters, `n` is the length of `s`, `max_jump` is the maximum jump calculated based on the positions of vowels in `s`, `last_vowel` is the index of the last vowel found in `s`, if there are vowels in `s`, and it will remain -1 if there are no vowels.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is a non-empty string of capital English letters, `n` is the length of `s`, `max_jump` is updated to the maximum of its previous value and `((n - last_vowel) // 2 + 1)`, while `last_vowel` is the index of the last vowel found in `s` (if any) and remains -1 if there are no vowels, under the condition that `last_vowel` is not equal to `n - 1`.
    print(max_jump)
#Overall this is what the function does:The function reads a non-empty string of capital English letters from input and computes the maximum "jump" based on the positions of vowels within that string. If there are no vowels, the maximum jump will remain as 0. If vowels are present, it calculates the maximum distance between consecutive vowels and considers the distance from the start of the string to the first vowel, as well as from the last vowel to the end of the string. The computed maximum jump is then printed. The function does not return any value.

