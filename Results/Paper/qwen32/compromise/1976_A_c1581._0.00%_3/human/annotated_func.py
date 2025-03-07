#State of the program right berfore the function call: password is a string consisting of exactly n characters, where n is an integer such that 1 ≤ n ≤ 20, and each character in the string is either a lowercase Latin letter or a digit.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: password is a string consisting of exactly n characters, where n is an integer such that 1 ≤ n ≤ 20, and each character in the string is either a lowercase Latin letter or a digit; `digits` is a list containing all the digit characters from the password; `letters` is a list containing all the lowercase Latin letter characters from the password.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: password is a string consisting of exactly n characters, where n is an integer such that 1 ≤ n ≤ 20, and each character in the string is either a lowercase Latin letter or a digit; digits is a list containing all the digit characters from the password; letters is a list containing all the lowercase Latin letter characters from the password; last_digit_index is the index of the last digit in the password if there are any digits, otherwise -1.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: password is a string consisting of exactly n characters, where n is an integer such that 1 ≤ n ≤ 20, and each character in the string is either a lowercase Latin letter or a digit; digits is a list containing all the digit characters from the password; letters is a list containing all the lowercase Latin letter characters from the password; last_digit_index is the index of the last digit in the password if there are any digits, otherwise -1; the list of digits is sorted.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: password is a string consisting of exactly n characters, where n is an integer such that 1 ≤ n ≤ 20, and each character in the string is either a lowercase Latin letter or a digit; digits is a list containing all the digit characters from the password; letters is a list containing all the lowercase Latin letter characters from the password; last_digit_index is the index of the last digit in the password if there are any digits, otherwise -1; the list of digits is sorted; the list of letters is sorted.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` checks if a given password string, consisting of lowercase Latin letters and digits, meets specific conditions. It returns 'NO' if there are lowercase letters after any digit or if the digits or letters are not in sorted order. Otherwise, it returns 'YES'.

