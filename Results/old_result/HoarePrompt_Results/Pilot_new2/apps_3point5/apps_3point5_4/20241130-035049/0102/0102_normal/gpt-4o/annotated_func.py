#State of the program right berfore the function call: n is an integer such that 0 ≤ n ≤ 99.**
def func_1(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
    'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety']
    if (0 <= n <= 9) :
        return ones[n]
        #The program returns the string representation of the number 'n' where n is an integer between 0 and 9 represented by the list 'ones'
    else :
        if (11 <= n <= 19) :
            return teens[n - 10]
            #The program returns the string value representing the number n from the 'teens' list, where n is between 11 and 19.
        else :
            if (10 <= n <= 99) :
                if (n % 10 == 0) :
                    return tens[n // 10]
                    #The program returns the element at index n // 10 in the list 'tens', where n is an integer between 10 and 99 divisible by 10
                else :
                    return tens[n // 10] + '-' + ones[n % 10]
                    #The program returns the string representation of the number 'n' between 10 and 99 using the 'tens' and 'ones' lists.
            #State of the program after the if block has been executed: *n is an integer such that 10 ≤ n ≤ 99; ones is a list of strings representing numbers from 'zero' to 'nine'; teens is a list of strings representing numbers from 'eleven' to 'nineteen'; tens is a list of strings representing numbers from 'twenty' to 'ninety'. n is not in the range of 11 to 19, and n is either less than 10 or greater than 99
        #State of the program after the if-else block has been executed: *n is an integer such that 10 ≤ n ≤ 99; ones is a list of strings representing numbers from 'zero' to 'nine'; teens is a list of strings representing numbers from 'eleven' to 'nineteen'; tens is a list of strings representing numbers from 'twenty' to 'ninety'. n is not in the range of 11 to 19, and n is either less than 10 or greater than 99
    #State of the program after the if-else block has been executed: *n is an integer such that 10 ≤ n ≤ 99; ones is a list of strings representing numbers from 'zero' to 'nine'; teens is a list of strings representing numbers from 'eleven' to 'nineteen'; tens is a list of strings representing numbers from 'twenty' to 'ninety'. n is not in the range of 11 to 19, and n is either less than 10 or greater than 99
#Overall this is what the function does:The function `func_1` takes an integer parameter `n` in the range 0 to 99 and returns a string representation of that number based on specific cases:
- If `n` is between 0 and 9, it returns the string representation of `n` from the 'ones' list.
- If `n` is between 11 and 19, it returns the string value representing that number from the 'teens' list.
- If `n` is between 10 and 99 and divisible by 10, it returns the element at index `n // 10` from the 'tens' list.
- If `n` is between 10 and 99 but does not fall into the above cases, it returns the string representation of `n` using the 'tens' and 'ones' lists.
The function provides a textual representation of the input number based on these conditions.

