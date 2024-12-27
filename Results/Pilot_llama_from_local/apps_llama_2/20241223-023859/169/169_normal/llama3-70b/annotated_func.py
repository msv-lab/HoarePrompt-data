#State of the program right berfore the function call: The input to the function consists of an integer n (1 <= n <= 100) and a string s of length n, consisting of '+' and '-' characters, where '+' represents adding a stone to the pile and '-' represents taking a stone from the pile.
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: `n` is an integer between 1 and 100 (inclusive), `s` is a string of length `n`, consisting of '+' and '-' characters, `minus_count` is the number of '-' characters in `s`, `plus_count` is equal to `n - minus_count`. If `minus_count` is greater than `plus_count`, the value 0 has been printed and returned to the output. Otherwise, the value of `n - 2 * minus_count` has been returned and printed.
#Overall this is what the function does:The function calculates and prints the final number of stones in a pile, given an integer `n` and a string `s` of length `n`, where `s` consists of '+' and '-' characters representing adding or removing stones from the pile. The function accepts no explicit parameters but reads two inputs: an integer `n` and a string `s`. After execution, the program state reflects that it has processed the input string, counted the occurrences of '+' and '-' characters, and printed the resulting number of stones. If the number of '-' characters exceeds the number of '+' characters, the function prints 0, indicating an empty pile; otherwise, it prints the difference between the counts of '+' and '-' characters, which represents the final number of stones in the pile. The function handles all potential edge cases, including when `n` is at its minimum (1) or maximum (100), and when the string `s` is entirely composed of either '+' or '-' characters, or any combination thereof. The final state of the program includes the side effect of printing the outcome to the console, and the variables `n`, `s`, `minus_count`, and `plus_count` hold the respective input length, input string, and counts of '-' and '+' characters.

