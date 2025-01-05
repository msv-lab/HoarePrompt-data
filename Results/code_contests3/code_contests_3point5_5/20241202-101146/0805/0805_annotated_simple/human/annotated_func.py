#State of the program right berfore the function call: **
def func():
    n = int(input())
    strings = input()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_strings = ''
    for s in strings:
        index = letters.index(s)
        
        added_index = index + n
        
        new_index = added_index % 26
        
        new_s = letters[new_index]
        
        new_strings += new_s
        
    #State of the program after the  for loop has been executed: Output State: `n` is an input integer, `strings` is a non-empty string from input, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` is a string with the updated characters based on the calculations from all iterations of the loop, `s` is the last character in `strings`, `index` is the index of `s` in `letters`, `added_index` is the result of `index + n` after all iterations, `new_index` is the calculated value between 0 and 25 after all iterations, `new_s` is assigned the value of the letter at index `new_index` in `letters` after all iterations.
    print(new_strings)
#Overall this is what the function does:The function `func` takes an integer input `n` and a string input `strings`. It then performs a series of calculations on each character of the input string based on the value of `n`, shifting the characters in the string according to the alphabetical order. The updated string `new_strings` is printed as the final output. The function does not return any value.

