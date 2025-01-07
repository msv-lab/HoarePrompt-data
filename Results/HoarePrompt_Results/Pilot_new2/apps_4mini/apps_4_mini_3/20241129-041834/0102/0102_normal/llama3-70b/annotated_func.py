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
        #State of the program after the if-else block has been executed: *`s` is an integer such that 10 ≤ `s` ≤ 99. If `s` is between 10 and 19, the word printed is `teens[s - 10]`. Otherwise, the output string is the string representation of `s`.
    #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99. If `s` is less than 10, the output is the string representation of `s` from the `ones` list. If `s` is between 10 and 19, the output is the corresponding word from the `teens` list. Otherwise, if `s` is 20 or greater, the output is the string representation of `s`, composed using the appropriate elements from the `tens` and `ones` lists.
#Overall this is what the function does:The function accepts an integer input `s` in the range of 0 to 99 and prints its English word representation. If `s` is less than 10, it prints the corresponding word from the `ones` list. If `s` is between 10 and 19, it prints the corresponding word from the `teens` list. For values 20 and above, it constructs the word representation by combining elements from the `tens` and `ones` lists, using a hyphen if necessary. The function does not return any value; it only prints the result.

