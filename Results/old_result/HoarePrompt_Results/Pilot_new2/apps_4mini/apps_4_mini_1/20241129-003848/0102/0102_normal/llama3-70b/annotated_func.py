#State of the program right berfore the function call: s is an integer such that 0 ≤ s ≤ 99.
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
        #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99 and `s` is greater than or equal to 10. If `s` is less than 20, the output is the string from `teens` corresponding to `s - 10`. Otherwise, if `s` is 20 or greater, the output is the string representation of `s`.
    #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99. If `s` is less than 10, the printed value is `ones[s]`. If `s` is between 10 and 19 inclusive, the output is the string from `teens` corresponding to `s - 10`. If `s` is 20 or greater, the output is the string representation of `s`.
#Overall this is what the function does:The function accepts no parameters and prompts the user for an integer input `s` in the range 0 to 99. It then prints the English word representation of the number. If `s` is less than 10, it prints the corresponding word from the `ones` list. If `s` is between 10 and 19, it prints the corresponding word from the `teens` list. If `s` is 20 or greater, it prints the word from the `tens` list followed by the word from the `ones` list if necessary (e.g., "twenty-one"). There is no return value from the function.

