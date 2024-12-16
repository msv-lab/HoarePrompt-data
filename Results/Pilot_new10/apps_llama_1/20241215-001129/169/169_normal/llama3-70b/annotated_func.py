#State of the program right berfore the function call: The function takes no arguments, but it is implied that it has access to two input variables: n, a positive integer from 1 to 100, and s, a string of length n consisting only of '+' and '-' characters.
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: `n` is an input integer, `s` is the input string, `minus_count` is the number of '-' characters in `s`, `plus_count` is the number of '+' characters in `s`. If `minus_count` is higher than `plus_count`, the value 0 has been returned to the console. Otherwise, the value `plus_count - minus_count` has been printed.
#Overall this is what the function does:The function reads an integer `n` and a string `s` from the user, counts the '+' and '-' characters in `s`, and then prints 0 if there are more '-' characters than '+' characters; otherwise, it prints the difference between the count of '+' and '-' characters, without validating `n` or `s` against the implied constraints.

