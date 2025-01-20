#State of the program right berfore the function call: The input is a string s consisting of characters '-' and 'o', where 3 ≤ |s| ≤ 100, representing a necklace.
def func():
    s = input().strip()

pearl_count = s.count('o')

link_count = s.count('-')
    if (pearl_count == 0 or pearl_count == 1) :
        print('YES')
    else :
        if (link_count % pearl_count == 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`s` is a string of length between 3 and 100 consisting of characters '-' and 'o', `pearl_count` is the number of 'o' characters in `s`, and `link_count` is the number of '-' characters in `s`. `pearl_count` is greater than 1. If `link_count` is a multiple of `pearl_count`, no action is taken. Otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`s` is a string of length between 3 and 100 consisting of characters '-' and 'o', `pearl_count` is the number of 'o' characters in `s`, and `link_count` is the number of '-' characters in `s`. If `pearl_count` is 0 or 1, no action is taken. If `pearl_count` is greater than 1, and `link_count` is a multiple of `pearl_count`, no action is taken. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function `func` reads a string `s` from user input, which consists of characters '-' and 'o', where the length of `s` is between 3 and 100, inclusive. It then counts the number of 'o' characters (`pearl_count`) and the number of '-' characters (`link_count`). If `pearl_count` is 0 or 1, the function prints 'YES'. If `pearl_count` is greater than 1, the function checks if `link_count` is a multiple of `pearl_count`. If it is, the function prints 'YES'; otherwise, it prints 'NO'. After the function concludes, the string `s` remains unchanged, and the values of `pearl_count` and `link_count` are determined based on the input string.

