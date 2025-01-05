#State of the program right berfore the function call: the trump suit is a string that is one of "S", "H", "D", or "C"; the two cards are represented as strings in the format of two characters, where the first character is one of "6", "7", "8", "9", "T", "J", "Q", "K", "A" representing the rank, and the second character is one of "S", "H", "D", or "C" representing the suit; the two cards must be different.
def func():
    coz = raw_input()
    f, s = raw_input().split()
    d = {'6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
    'A': 14}
    if (f[1] == coz and s[1] != coz) :
        print('YES')
    else :
        if (f[1] != coz and s[1] == coz) :
            print('NO')
        else :
            if (f[1] == s[1] and [f[0]] > d[s[0]]) :
                print('YES')
            else :
                print('NO')
            #State of the program after the if-else block has been executed: *The trump suit is a string that is one of "S", "H", "D", or "C"; the two cards `f` and `s` are represented as strings in the format of two characters; the suits of cards `f` and `s` are equal to `coz`; the ranks of cards `f` and `s` are different; if the rank of card `f` is greater than the rank of card `s` as defined in dictionary `d`, then 'YES' has been printed. Otherwise, 'NO' has been printed.
        #State of the program after the if-else block has been executed: *The trump suit is a string that is one of "S", "H", "D", or "C"; the two cards `f` and `s` are represented as strings in the format of two characters; the two cards `f` and `s` are different; `coz` is an input string; the suit of card `f` is not equal to `coz` and the suit of card `s` is equal to `coz`; if the suit of card `f` is not equal to `coz`, 'NO' is printed. Otherwise, if the suits of cards `f` and `s` are equal to `coz` and their ranks are different, if the rank of card `f` is greater than the rank of card `s` as defined in dictionary `d`, then 'YES' is printed; otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *The trump suit is a string that is one of "S", "H", "D", or "C"; the two cards `f` and `s` are strings representing two different cards; `coz` is an input string. If the suit of card `f` is equal to `coz` and the suit of card `s` is not equal to `coz`, 'YES' is printed. Otherwise, if the suit of card `f` is not equal to `coz` and the suit of card `s` is equal to `coz`, 'NO' is printed. If the suits of cards `f` and `s` are both equal to `coz` and their ranks are different, then if the rank of card `f` is greater than the rank of card `s` as defined in dictionary `d`, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts a trump suit and two different cards represented as strings. It prints 'YES' if the first card's suit matches the trump suit and the second card's suit does not. It prints 'NO' if the first card's suit does not match the trump suit and the second card's suit does. If both cards have the same suit as the trump suit, it checks their ranks; if the rank of the first card is greater than the second's, it prints 'YES', otherwise it prints 'NO'. The function does not validate the inputs for correctness beyond ensuring the cards are different.

