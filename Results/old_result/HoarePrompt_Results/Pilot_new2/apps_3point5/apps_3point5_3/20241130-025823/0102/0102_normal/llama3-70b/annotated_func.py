#State of the program right berfore the function call: The function takes no input arguments.
def func():
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety']
    s = int(input())
    if (s < 10) :
        print(ones[s])
    else :
        if (s < 20) :
            print(teens[s - 10])
        else :
            print(tens[s // 10] + ('' if s % 10 == 0 else '-' + ones[s % 10]))
        #State of the program after the if-else block has been executed: *`ones` is a list of strings from empty string to 'nine' representing the numbers from 0 to 9; `teens` is a list of strings representing the numbers from 10 to 19; `tens` is a list of strings representing the tens place values from empty string to 'ninety'; `s` is an input integer. s is greater than or equal to 10. If s < 20, the output string is the string at index s - 10 in the `teens` list. If s is 20 or greater, the output string is the concatenation of the string at index s//10 in the `tens` list and the string at index s%10 in the `ones` list, separated by a hyphen if the ones place value is not 0.
    #State of the program after the if-else block has been executed: *`ones`, `teens`, `tens` are lists of strings. `s` is an integer input. If `s` is less than 10, the string representation of the number corresponding to `s` is printed. If `s` is greater than or equal to 10, the output string is determined based on the value of `s`. If s is less than 20, the output string is taken from the `teens` list. If `s` is 20 or greater, the output string is a combination of the string at index s//10 in the `tens` list and the string at index s%10 in the `ones` list, separated by a hyphen if the ones place value is not 0.
#Overall this is what the function does:The function defines lists of strings representing numbers from 0 to 9, 10 to 19, and tens values. It then takes an integer input and prints the corresponding string representation based on the input value. If the input is less than 10, it prints the string from the `ones` list. If the input is between 10 and 19, it prints the string from the `teens` list. For inputs greater than or equal to 20, it prints the combination of the tens and ones strings. The function does not return any value but determines the string representation of the input number.

