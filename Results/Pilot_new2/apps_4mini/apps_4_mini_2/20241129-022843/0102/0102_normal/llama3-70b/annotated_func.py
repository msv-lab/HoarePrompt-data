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
        #State of the program after the if-else block has been executed: *`s` is an integer such that 10 ≤ `s` ≤ 99; if `s` is between 10 and 19, the output corresponds to the respective teen value from the `teens` array. If `s` is 20 or greater, the output is based on the individual tens and ones values derived from `s` using the `ones` and `teens` arrays.
    #State of the program after the if-else block has been executed: *`s` is an integer such that 0 ≤ `s` ≤ 99. If `s` is less than 10, the output is the string representation of `s` from the `ones` array. If `s` is between 10 and 19, the output corresponds to the respective value from the `teens` array. If `s` is 20 or greater, the output is derived from the individual tens and ones values using the `ones` and `teens` arrays.
#Overall this is what the function does:The function accepts an integer input `s` from the user (expected to be between 0 and 99) and prints its English word representation. For values from 0 to 9, it retrieves the corresponding string from the `ones` list; for values from 10 to 19, it retrieves the string from the `teens` list; for values from 20 to 99, it constructs the representation using the `tens` list and the `ones` list, separating tens and ones with a hyphen if necessary. The function does not handle input validation or cases where the input is outside the expected range.

