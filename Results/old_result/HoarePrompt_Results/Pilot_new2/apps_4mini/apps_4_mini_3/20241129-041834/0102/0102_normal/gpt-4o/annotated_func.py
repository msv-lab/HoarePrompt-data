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
        #The program returns the word corresponding to the integer `n` from the list `ones`, where `n` is an integer such that 0 ≤ `n` ≤ 9.
    else :
        if (11 <= n <= 19) :
            return teens[n - 10]
            #The program returns the word corresponding to the integer n, which is in the teens list for values between 11 and 19, specifically teens[n - 10] where n is the current integer between 11 and 19.
        else :
            if (10 <= n <= 99) :
                if (n % 10 == 0) :
                    return tens[n // 10]
                    #The program returns the string corresponding to the tens place of the integer `n`, where `n` is a multiple of 10 and ranges from 10 to 99, inclusive.
                else :
                    return tens[n // 10] + '-' + ones[n % 10]
                    #The program returns the string representation of the integer `n` in the format of "tens" followed by a hyphen and "ones", where `tens[n // 10]` gives the tens place name and `ones[n % 10]` gives the ones place name for the integer `n`
            #State of the program after the if block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99; `ones` is a list containing ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']; `teens` is a list containing ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']; `tens` is a list containing ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']; `n` is an integer such that `n` is less than 10 or greater than 99, and `n` is not in the range from 11 to 19 (inclusive).
        #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99; `ones` is a list containing ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']; `teens` is a list containing ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']; `tens` is a list containing ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']; `n` is an integer such that `n` is less than 10 or greater than 99, and `n` is not in the range from 11 to 19 (inclusive).
    #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99; `ones` is a list containing ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']; `teens` is a list containing ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']; `tens` is a list containing ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']; `n` is an integer such that `n` is less than 10 or greater than 99, and `n` is not in the range from 11 to 19 (inclusive).
#Overall this is what the function does:The function accepts an integer `n` (where 0 ≤ n ≤ 99) and returns its English word representation. It covers the following cases: it returns 'zero' through 'nine' for values 0-9; 'eleven' through 'nineteen' for values 11-19; for multiples of ten from 10 to 90 it returns 'ten', 'twenty', etc.; and for other numbers between 10 and 99 it returns a combination of the tens and ones place (e.g., 'twenty-one'). The function does not handle the case for the number 10, which is missing from the logic, as it falls under the teens and should return 'ten' instead of being omitted.

