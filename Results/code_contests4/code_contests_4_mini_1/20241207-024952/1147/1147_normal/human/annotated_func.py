#State of the program right berfore the function call: trump_suit is a string that is either "S", "H", "D", or "C"; card1 and card2 are strings representing cards formatted as two characters, where the first character is a rank ("6", "7", "8", "9", "T", "J", "Q", "K", or "A") and the second character is a suit ("S", "H", "D", or "C").
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
            #State of the program after the if-else block has been executed: *`trump_suit` is a string that is either "S", "H", "D", or "C"; `card1` and `card2` are strings representing cards; `f` and `s` are input strings split from `coz`; `d` is a dictionary mapping card values to integers; it is not the case that `f[1]` is not equal to `coz` or `s[1]` is equal to `coz`. If `f[1]` is equal to `s[1]` and the value of `f[0]` is greater than `d[s[0]]`, then 'YES' has been printed. Otherwise, if `f[1]` is not equal to `s[1]` or the value of `f[0]` is less than or equal to `d[s[0]]`, then 'NO' is printed.
        #State of the program after the if-else block has been executed: *`trump_suit` is a string that is either "S", "H", "D", or "C"; `card1` and `card2` are strings representing cards; `f` and `s` are input strings split from `coz`; `d` is a dictionary mapping card values to integers. If `f[1]` is not equal to `coz` and `s[1]` is equal to `coz`, 'NO' is printed. Otherwise, if `f[1]` is equal to `s[1]` and the value of `f[0]` is greater than `d[s[0]]`, then 'YES' is printed. If `f[1]` is not equal to `s[1]` or the value of `f[0]` is less than or equal to `d[s[0]]`, then 'NO' is printed.
    #State of the program after the if-else block has been executed: *`trump_suit` is a string that is either "S", "H", "D", or "C"; `card1` and `card2` are strings representing cards; `f` and `s` are input strings split from `coz`; `d` is a dictionary mapping card values to integers. If the second element of `f` is equal to `coz` and the second element of `s` is not equal to `coz`, then "YES" is printed. Otherwise, if the second element of `f` is not equal to `coz` and the second element of `s` is equal to `coz`, "NO" is printed. If the second elements of `f` and `s` are equal and the value of `f[0]` is greater than `d[s[0]]`, then "YES" is printed. If the second elements of `f` and `s` are not equal or the value of `f[0]` is less than or equal to `d[s[0]]`, then "NO" is printed.
#Overall this is what the function does:The function reads a trump suit and two cards from input, then determines the outcome based on the following rules: If the suit of the first card matches the trump suit and the suit of the second card does not, it prints "YES". If the suit of the first card does not match the trump suit and the suit of the second card does, it prints "NO". If both cards have the same suit and the rank of the first card is higher than the rank of the second card, it prints "YES"; otherwise, it prints "NO". The function does not accept any parameters directly, as it uses raw input to fetch its values.

