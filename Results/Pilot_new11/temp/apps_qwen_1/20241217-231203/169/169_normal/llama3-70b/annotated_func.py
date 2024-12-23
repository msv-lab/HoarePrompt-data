#State of the program right berfore the function call: The input consists of two lines. The first line contains a positive integer n (1 ≤ n ≤ 100) representing the number of operations. The second line contains a string s of length n, where each character is either "-" (indicating removing a stone) or "+" (indicating adding a stone).
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: `n` is an integer between 1 and 100, inclusive; `s` is a string of length `n` consisting of characters "-" and "+"; `minus_count` is the count of '-' characters in `s`; `plus_count` is the count of '+' characters in `s`; the function prints `plus_count - minus_count` if `minus_count` is not greater than `plus_count`, and `minus_count` remains unchanged if `minus_count` is greater than `plus_count`.
#Overall this is what the function does:The function processes an input consisting of two lines: the first line is a positive integer \( n \) (1 ≤ \( n \) ≤ 100) representing the number of operations, and the second line is a string \( s \) of length \( n \) containing characters "-" and "+". The function counts the number of "+" and "-" characters in the string \( s \). It then compares the count of "-" characters to the count of "+" characters. If the count of "-" characters is greater than the count of "+" characters, the function prints 0. Otherwise, it prints the difference between the count of "+" characters and the count of "-" characters. This difference represents the net number of "+" characters in the string after considering the removals indicated by "-".

