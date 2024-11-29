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
        #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99 and `s` is greater than or equal to 10. If `s` is between 10 and 19, the string representation is `teens[s - 10]`. If `s` is greater than or equal to 20, the output is the string representation of `s` in tens and ones format.
    #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99. If `s` is less than 10, then the string representation of `s` is given by `ones[s]`. If `s` is between 10 and 19, the string representation is given by `teens[s - 10]`. If `s` is greater than or equal to 20, the output is the string representation of `s` in tens and ones format.
#Overall this is what the function does:The function accepts an integer input `s` (0 ≤ s ≤ 99) from the user and prints its English word representation. It handles numbers in three ranges: for `s` less than 10, it prints the corresponding word from the `ones` list; for `s` between 10 and 19, it prints the corresponding word from the `teens` list; and for `s` 20 or greater, it constructs the word representation using the `tens` list and the `ones` list. The function does not return any value; it only prints the result. However, it assumes that the input will always be within the specified range and does not handle invalid inputs (e.g., negative numbers or numbers greater than 99).

