#State of the program right berfore the function call: password is a string consisting of exactly n characters, where each character is either a lowercase Latin letter or a digit, and n is an integer such that 1 ≤ n ≤ 20.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: `password` is a string consisting of exactly `n` characters, where each character is either a lowercase Latin letter or a digit, and `n` is an integer such that 1 ≤ n ≤ 20. `digits` is a list containing all the digits from the `password` string in the order they appear. `letters` is a list containing all the lowercase Latin letters from the `password` string in the order they appear.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: 'NO'
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns the string 'NO'
    #State: 'NO', `digits` is a list of elements that is sorted
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns the string 'NO'
    #State: 'NO', `digits` is a list of elements that is sorted, and `letters` is a list of elements that is sorted
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function checks if a given password string, consisting of lowercase Latin letters and digits, meets specific conditions: all digits must appear before any letters, and both digits and letters must be in non-decreasing order. If these conditions are met, it returns 'YES'; otherwise, it returns 'NO'.

