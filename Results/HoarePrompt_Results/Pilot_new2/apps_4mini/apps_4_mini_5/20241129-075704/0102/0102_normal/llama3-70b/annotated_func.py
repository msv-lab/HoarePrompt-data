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
        #State of the program after the if-else block has been executed: *`s` is an integer such that 10 ≤ `s` ≤ 99. If `s` is between 10 and 19, the output is `teens[s - 10]`. Otherwise, the output is `tens[s // 10] + ('' if s % 10 == 0 else '-' + ones[s % 10])`, which represents the correct English word representation of the number `s`.
    #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99. If `s` is less than 10, the output is `ones[s]`, which represents the corresponding English word for the single-digit number. If `s` is between 10 and 19, the output is `teens[s - 10]`, representing the appropriate English word for the teen number. Otherwise, the output is `tens[s // 10] + ('' if s % 10 == 0 else '-' + ones[s % 10])`, which gives the correct English word representation for the number `s` in the range of 20 to 99.
#Overall this is what the function does:The function accepts an integer input `s` (ranging from 0 to 99) and prints its English word representation. For values less than 10, it prints single-digit names; for values between 10 and 19, it prints teen names; and for values from 20 to 99, it prints a combination of tens and ones (with a hyphen if necessary). The function does not return any value.

