#State of the program right berfore the function call: s is an integer such that 0 ≤ s ≤ 99.**
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
        #State of the program after the if-else block has been executed: *s is an input integer such that 10 ≤ s ≤ 99; ones is a list containing string representations of numbers from zero to nine; teens is a list containing string representations of numbers from ten to nineteen; tens is a list containing string representations of the tens place values. If s is less than 20, the function returns the string representation of the number indexed by `s - 10` in the teens list. If s is larger or equal to 20, the function returns the concatenation of the string representation of the tens place value of s and the string representation of the ones place value of s if non-zero, separated by a hyphen if the ones place value is non-zero.
    #State of the program after the if-else block has been executed: *s is an input integer such that 0 ≤ s ≤ 99; ones is a list containing string representations of numbers from zero to nine; teens is a list containing string representations of numbers from ten to nineteen; tens is a list containing string representations of the tens place values. If s < 10, the function prints the string representation of the number indexed by s in the ones list. If s is between 10 and 19, the function returns the string representation of the number indexed by `s - 10` in the teens list. If s is 20 or greater, the function returns the concatenation of the string representation of the tens place value of s and the string representation of the ones place value of s if non-zero, separated by a hyphen if the ones place value is non-zero.
#Overall this is what the function does:The function accepts user input integer `s` in the range 0 to 99. It then prints the English word representation of the input number based on its digits. If `s` is less than 10, it prints the word representation from 'one' to 'nine'. If `s` is between 10 and 19, it prints the word representation of numbers 'ten' to 'nineteen'. For `s` greater than or equal to 20, it prints the word representation of tens place value followed by the ones place value if non-zero, with a hyphen in between.

