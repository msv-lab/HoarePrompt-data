#State of the program right berfore the function call: # Precondition
**s is an integer such that 0 <= s <= 99.**
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
        #State of the program after the if-else block has been executed: *`s` is an integer such that 10 <= s <= 99, `ones` is a list containing strings from 'one' to 'nine', `teens` is a list containing strings from 'ten' to 'nineteen', `tens` is a list containing strings '' (empty string), '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety. If s < 20, the value at the index s-10 in the list `teens` is printed. If s >= 20, the result is the string representation of the number `s` in words.
    #State of the program after the if-else block has been executed: *`s` is an integer such that 0 <= s <= 99, `ones` is a list containing strings from 'one' to 'nine', `teens` is a list containing strings from 'ten' to 'nineteen', `tens` is a list containing strings '' (empty string), '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety. After the execution of the if else block, if `s` is less than 10, the output is the string representation of the integer `s` from the `ones` list. If `s` is between 10 and 19, the output is the string at the index `s-10` from the `teens` list. If `s` is 20 or greater, the output is the string representation of the number `s` in words.
#Overall this is what the function does:The function does not accept any parameters. It reads an integer `s` from the user input and converts it to its word representation. If `s` is less than 10, it prints the word representation from the `ones` list. If `s` is between 10 and 19, it prints the word representation from the `teens` list. If `s` is 20 or greater, it prints the word representation by combining the words from the `tens` and `ones` lists. The function covers the conversion of integers to words from 0 to 99.

