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
        #The program returns the string representing the integer value of n in the list 'ones'
    else :
        if (11 <= n <= 19) :
            return teens[n - 10]
            #The program returns the string from the 'teens' list at index n-10, where n is an integer such that 11 <= n <= 19
        else :
            if (10 <= n <= 99) :
                if (n % 10 == 0) :
                    return tens[n // 10]
                    #The program returns the string from the 'tens' list at the index n//10, where n is an integer between 10 and 99 inclusive and n % 10 equals 0
                else :
                    return tens[n // 10] + '-' + ones[n % 10]
                    #The program returns the combination of the string in the 'tens' list at index n // 10 and the string in the 'ones' list at index n % 10, separated by a hyphen '-'
            #State of the program after the if block has been executed: *n is an integer such that 10 <= n <= 99; ones is a list containing the strings 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'; teens is a list containing the strings 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'; tens is a list containing strings 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'. The value of n is not between 11 and 19, and n is not between 10 and 99
        #State of the program after the if-else block has been executed: *n is an integer such that 10 <= n <= 99; ones is a list containing the strings 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'; teens is a list containing the strings 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'; tens is a list containing strings 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'. The value of n is not between 11 and 19, and n is not between 10 and 99
    #State of the program after the if-else block has been executed: *n is an integer such that 10 <= n <= 99; ones is a list containing the strings 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'; teens is a list containing the strings 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'; tens is a list containing strings 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'. The value of n is not between 11 and 19, and n is not between 10 and 99
#Overall this is what the function does:The function `func_1` accepts an integer `n` between 0 and 99. It then returns different strings based on the value of `n` as follows: 
- If n is between 0 and 9, the function returns the string representing the integer value of n in the list 'ones'.
- If n is between 11 and 19, the function returns the string from the 'teens' list at index n-10.
- If n is between 10 and 99 inclusive and n % 10 equals 0, the function returns the string from the 'tens' list at the index n//10.
- If n is between 10 and 99 inclusive and n % 10 does not equal 0, the function returns the combination of the string in the 'tens' list at index n // 10 and the string in the 'ones' list at index n % 10, separated by a hyphen '-'.

