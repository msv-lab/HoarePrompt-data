#State of the program right berfore the function call: n is an integer such that 0 <= n <= 99.**
def func_1(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
    'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety']
    if (0 <= n <= 9) :
        return ones[n]
        #The program returns the string representation of the number 'n' where n is an integer between 0 and 9 as per the list 'ones'
    else :
        if (11 <= n <= 19) :
            return teens[n - 10]
            #The program returns the string representation of the number in the 'teens' list at index n - 10, where n is an integer between 11 and 19 inclusive
        else :
            if (10 <= n <= 99) :
                if (n % 10 == 0) :
                    return tens[n // 10]
                    #The program returns the string representing the tens place of the current value of n
                else :
                    return tens[n // 10] + '-' + ones[n % 10]
                    #The program returns the string representation of the given integer 'n' in words by concatenating the tens place value from the list 'tens' with the ones place value from the list 'ones' separated by a hyphen.
            #State of the program after the if block has been executed: *n is an integer such that 10 <= n <= 99; ones is a list of strings representing numbers from zero to nine; teens is a list of strings representing numbers from eleven to nineteen; tens is a list of strings representing numbers from zero to ninety. n is not between 11 and 19 inclusive, n is not between 10 and 99 inclusive
        #State of the program after the if-else block has been executed: *n is an integer such that 10 <= n <= 99; ones is a list of strings representing numbers from zero to nine; teens is a list of strings representing numbers from eleven to nineteen; tens is a list of strings representing numbers from zero to ninety. n is not between 11 and 19 inclusive, n is not between 10 and 99 inclusive
    #State of the program after the if-else block has been executed: *n is an integer such that 10 <= n <= 99; ones is a list of strings representing numbers from zero to nine; teens is a list of strings representing numbers from eleven to nineteen; tens is a list of strings representing numbers from zero to ninety. n is not between 11 and 19 inclusive, n is not between 10 and 99 inclusive
#Overall this is what the function does:The function `func_1` accepts an integer `n` where 0 <= n <= 99 and returns the string representation of that number based on different cases. It returns the string representation of the number 'n' if n is between 0 and 9, the string representation from the 'teens' list if n is between 11 and 19, the string representing the tens place if n is a multiple of 10, and the full string representation of a two-digit number by combining the tens and ones values with a hyphen for other cases.

