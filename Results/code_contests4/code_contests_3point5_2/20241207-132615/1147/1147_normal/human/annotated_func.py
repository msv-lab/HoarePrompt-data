#State of the program right berfore the function call: The input consists of a trump suit (one of "S", "H", "D" or "C") and two different cards described by two symbols each. The first symbol represents the rank ("6", "7", "8", "9", "T", "J", "Q", "K" and "A"), and the second symbol represents the suit ("S", "H", "D" and "C").**
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
            #State of the program after the if-else block has been executed: *The input consists of a trump suit, two different cards described by two symbols each. `coz` is assigned the user input. `f` and `s` are assigned the input values after splitting. `d` is a dictionary mapping card ranks to their respective values. The second symbol of `f` is not the same as `coz` or the second symbol of `s` is not the same as `coz`. If the second symbol of `f` is equal to the second symbol of `s` and the rank value of `f` is greater than the rank value of `s` based on the dictionary `d`, then the function returns 'YES'. Otherwise, the function returns 'NO'.
        #State of the program after the if-else block has been executed: *The input consists of a trump suit, two different cards described by two symbols each. `coz` is assigned the user input. `f` and `s` are assigned the input values after splitting. `d` is a dictionary mapping card ranks to their respective values. The second symbol of `f` is not the same as `coz` and the second symbol of `s` is the same as `coz`. If the second symbol of `f` is equal to the second symbol of `s` and the rank value of `f` is greater than the rank value of `s` based on the dictionary `d`, then the function returns 'YES'. Otherwise, the function returns 'NO'.
    #State of the program after the if-else block has been executed: *The input consists of a trump suit, two different cards described by two symbols each. `coz` is assigned the user input. `f` and `s` are assigned the input values after splitting. `d` is a dictionary mapping card ranks to their respective values. If the second symbol of `f` is equal to `coz` and the second symbol of `s` is not equal to `coz`, then 'YES' is printed. Otherwise, if the second symbol of `f` is not the same as `coz` and the second symbol of `s` is the same as `coz`, the function checks if the second symbol of `f` is equal to the second symbol of `s` and the rank value of `f` is greater than the rank value of `s` based on the dictionary `d`, then 'YES' is returned. Otherwise, 'NO' is returned.
#Overall this is what the function does:The function `func` takes user input for a trump suit and two cards, each described by two symbols representing rank and suit. It then compares the cards based on the trump suit and their ranks. If the second symbol of the first card matches the trump suit and the second symbol of the second card does not, it prints 'YES'. If the second symbol of the first card does not match the trump suit and the second symbol of the second card does, it prints 'NO'. If both cards have the same second symbol and the rank of the first card is greater than the rank of the second card, it prints 'YES'. Otherwise, it prints 'NO'. The function does not directly return any output.

