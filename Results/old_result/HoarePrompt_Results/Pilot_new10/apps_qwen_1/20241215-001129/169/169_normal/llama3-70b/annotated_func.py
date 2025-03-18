#State of the program right berfore the function call: $n$ is a positive integer such that $1 \leq n \leq 100$, and $s$ is a string of length $n$ consisting of "-" and "+" symbols.
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100 (inclusive), `s` is a string of length `n` consisting of "-" and "+" symbols, `minus_count` is the count of '-' symbols in `s`, `plus_count` is the count of '+' symbols in `s`. If `minus_count` is greater than `plus_count`, the program does nothing. Otherwise, the output of the print statement is `plus_count - minus_count`.
#Overall this is what the function does:The function processes a string `s` of length `n`, counts the number of "+" symbols, and prints `0` if the number of "-" symbols is greater than the number of "+" symbols, otherwise it prints the count of "+" symbols.

