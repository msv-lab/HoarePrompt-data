#State of the program right berfore the function call: The function `func` is expected to take two inputs implicitly or through global variables: `n` and `m`. `n` is an integer where 0 ≤ n ≤ 10^9 without leading zeroes, and `m` is an integer where 0 ≤ m ≤ 10^9 which may include leading zeroes.
def func():
    I = raw_input
    n = I()
    m = I()
    n = sorted(list(n))
    for i in range(len(n)):
        if n[i] != '0':
            break
        
    #State of the program after the  for loop has been executed: `n` is a list of characters from the string value from `I()` in sorted order, `m` is a string value from `I()`, `i` is the index of the first character in `n` that is not '0'. If all characters in `n` are '0', `i` is `len(n)`.
    if (n[i] != '0') :
        n[0], n[i] = n[i], n[0]
    #State of the program after the if block has been executed: *`n` is a list of characters from the string value from `I()` in sorted order, `m` is a string value from `I()`, and `i` is the index of the first character in `n` that is not '0'. If all characters in `n` are '0', `i` is `len(n)`. If `n[i]` is not '0', `n[0]` is the character at index `i` before the swap, and `n[i]` is the character that was originally at `n[0]`. Otherwise, the list `n` remains unchanged.
    print['OK', 'WRONG_ANSWER'][n != list(m)]
#Overall this is what the function does:The function `func` reads two lines of input, where the first line represents an integer `n` (without leading zeroes) and the second line represents an integer `m` (which may have leading zeroes). It then processes `n` by converting it into a list of characters, sorting this list, and swapping the first non-zero character with the first character of the list if it is not already the first character. After processing, it compares the modified list of characters of `n` with the list of characters of `m`. If the lists match, it prints "OK"; otherwise, it prints "WRONG_ANSWER". The function does not return any value. Edge cases include when `n` consists entirely of zeros, in which case no swap occurs, and when `n` and `m` are identical strings, leading to "OK" being printed.

