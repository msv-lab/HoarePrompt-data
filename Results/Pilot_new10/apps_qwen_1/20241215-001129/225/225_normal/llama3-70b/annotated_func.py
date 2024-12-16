#State of the program right berfore the function call: The input is a non-empty string consisting of capital English letters, and its length does not exceed 100. The string may contain the following vowels: 'A', 'E', 'I', 'O', 'U', and 'Y'.
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
        
    #State of the program after the  for loop has been executed: `s` is the user input string, `vowels` is 'AEIOUY', `n` is the length of `s`, `max_jump` is the maximum jump distance found in the string `s`, `last_vowel` is the index of the last vowel encountered in the string `s`.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is the user input string, `vowels` is 'AEIOUY', `n` is the length of `s`, `max_jump` is at least the maximum of its original value and 1, `last_vowel` is the index of the last vowel encountered in the string `s`. If `last_vowel` is not the last index of the string, `max_jump` is at least the maximum of its original value and the distance from the last vowel to the end of the string.
    print(max_jump)
#Overall this is what the function does:The function accepts a non-empty string consisting of capital English letters and calculates the maximum possible "jump" distance between vowels in the string. If no vowels are present, it calculates the distance from the last non-vowel position to the end of the string and prints the result.

