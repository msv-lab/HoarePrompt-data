#State of the program right berfore the function call: The input is a non-empty string consisting of uppercase English letters (A-Z), and the length of the string does not exceed 100.
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
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of uppercase English letters (A-Z); `vowels` is 'AEIOUY'; `n` is greater than or equal to 0; `max_jump` is the maximum jump calculated based on the positions of the vowels in `s`; `last_vowel` is the index of the last vowel found in `s`.
    if (last_vowel != n - 1) :
        max_jump = max(max_jump, (n - last_vowel) // 2 + 1)
    #State of the program after the if block has been executed: *`s` is an input string consisting of uppercase English letters (A-Z); `vowels` is 'AEIOUY'; `n` is greater than or equal to 0; if the index of the last vowel (`last_vowel`) is not equal to `n - 1`, then `max_jump` is updated to the maximum of its previous value and `(n - last_vowel) // 2 + 1`.
    print(max_jump)
#Overall this is what the function does:The function calculates the maximum jump between consecutive vowels in a given non-empty string consisting exclusively of uppercase letters (A-Z), where the length of the string does not exceed 100 characters. It determines the maximum distance between any two vowels or from the start or end of the string to the nearest vowel. The final output is the maximum jump value, which is printed to the console. If no vowels are present, the function effectively defaults to a jump of 0 since it would not capture any legitimate vowel indices. The function does not return a value; it only prints the result.

