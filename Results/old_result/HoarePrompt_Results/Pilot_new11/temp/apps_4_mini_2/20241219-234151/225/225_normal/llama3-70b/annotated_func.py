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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string of capital English letters; `n` is the length of `s`; `max_jump` is the maximum jump length calculated based on the positions of vowels; `last_vowel` is the index of the last vowel found in the string.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is a non-empty string of capital English letters, `n` is the length of `s`, `last_vowel` is the index of the last vowel found in the string. If `last_vowel` is not equal to `n - 1`, then `max_jump` is updated to `new_max_jump`, which is calculated as the maximum of `old_max_jump` and half of the distance from the last vowel to the end of the string plus one.
    print(max_jump)
#Overall this is what the function does:The function accepts a non-empty string consisting of capital English letters, with a length not exceeding 100 characters. It calculates the maximum jump length based on the positions of the vowels (A, E, I, O, U, Y) in the string. If the last vowel is not the last character in the string, it also considers the distance from the last vowel to the end of the string. The maximum jump length is then printed. The function does not handle cases where the string might contain no vowels, but it correctly handles scenarios where vowels are present and the last vowel occurs at various positions in the string. The final state of the program includes the printed maximum jump length that reflects the calculated jump based on the input string.

