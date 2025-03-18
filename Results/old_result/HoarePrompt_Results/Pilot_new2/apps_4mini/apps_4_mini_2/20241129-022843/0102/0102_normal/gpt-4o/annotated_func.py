#State of the program right berfore the function call: s is an integer such that 0 ≤ s ≤ 99.
def func_1(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
    'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety']
    if (0 <= n <= 9) :
        return ones[n]
        #The program returns the string representation of the integer `n` from the list `ones`, where `n` is an integer such that 0 ≤ n ≤ 9.
    else :
        if (11 <= n <= 19) :
            return teens[n - 10]
            #The program returns the string representation of the integer n, which is in the range of 11 to 19, corresponding to the 'teens' list where n - 10 gives the appropriate index.
        else :
            if (10 <= n <= 99) :
                if (n % 10 == 0) :
                    return tens[n // 10]
                    #The program returns the string corresponding to the tens place of the integer n, which is a multiple of 10 between 10 and 99 inclusive, using the tens list.
                else :
                    return tens[n // 10] + '-' + ones[n % 10]
                    #The program returns the English word representation of the integer n (between 10 and 99) by concatenating the corresponding value from the 'tens' list for the ten's place and the corresponding value from the 'ones' list for the unit's place, separated by a hyphen.
            #State of the program after the if block has been executed: *`s` is an integer such that 0 ≤ s ≤ 99; `ones` is a list containing ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']; `teens` is a list containing ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']; `tens` is a list containing ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']; `n` is an integer such that n is less than 10 or greater than 99, and n is in the range from 11 to 19 (inclusive).
        #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ s ≤ 99; `ones` is a list containing ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']; `teens` is a list containing ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']; `tens` is a list containing ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']; `n` is an integer such that n is less than 10 or greater than 99, and n is in the range from 11 to 19 (inclusive).
    #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ s ≤ 99; `ones` is a list containing ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']; `teens` is a list containing ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']; `tens` is a list containing ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']; `n` is an integer such that n is less than 10 or greater than 99, and n is in the range from 11 to 19 (inclusive).
#Overall this is what the function does:The function accepts an integer `n` (where 0 ≤ n ≤ 99) and returns its English word representation. If `n` is between 0 and 9, it returns the corresponding string from the 'ones' list. If `n` is between 11 and 19, it returns the corresponding string from the 'teens' list. For multiples of 10 between 10 and 99, it returns the corresponding string from the 'tens' list. For values between 10 and 99 that are not multiples of 10, it returns a string combining the appropriate entries from the 'tens' and 'ones' lists, separated by a hyphen. The function does not handle values outside the specified range of 0 to 99 and does not account for the case when `n` is exactly 10, which should return 'ten' but is instead falling into the 'teens' block.

