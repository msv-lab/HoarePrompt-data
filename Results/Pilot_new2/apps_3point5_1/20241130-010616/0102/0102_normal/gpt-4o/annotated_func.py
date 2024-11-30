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
        #The program returns the word representation of the integer n between 0 and 9 from the list 'ones'
    else :
        if (11 <= n <= 19) :
            return teens[n - 10]
            #The program returns the corresponding value from the 'teens' list based on the index calculated as n - 10, where n is currently between 11 and 19
        else :
            if (10 <= n <= 99) :
                if (n % 10 == 0) :
                    return tens[n // 10]
                    #The program returns the string representation of the tens place digit of the number 'n' which is divisible by 10. The string representation is based on the 'tens' list provided in the initial state.
                else :
                    return tens[n // 10] + '-' + ones[n % 10]
                    #The program returns the concatenation of the word representing the tens place of integer n and the word representing the ones place of integer n separated by a hyphen.
            #State of the program after the if block has been executed: *n is an integer such that 10 <= n <= 99; ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']; teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']; tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']. n is not between 11 and 19. n is not between 10 and 99, or n is not an integer between 10 and 99.
        #State of the program after the if-else block has been executed: *n is an integer such that 10 <= n <= 99; ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']; teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']; tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']. n is not between 11 and 19. n is not between 10 and 99, or n is not an integer between 10 and 99.
    #State of the program after the if-else block has been executed: *n is an integer such that 10 <= n <= 99; ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']; teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']; tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']. n is not between 11 and 19. n is not between 10 and 99, or n is not an integer between 10 and 99.
#Overall this is what the function does:Functionality: The function `func_1` takes an integer `n` where 0 <= n <= 99 and returns the word representation of `n` based on the following conditions:
- If n is between 0 and 9, it returns the word representation from the 'ones' list.
- If n is between 11 and 19, it returns the corresponding value from the 'teens' list.
- If n is divisible by 10, it returns the string representation of the tens place digit from the 'tens' list.
- For all other cases, it concatenates the word representing the tens place of n and the word representing the ones place of n separated by a hyphen.

