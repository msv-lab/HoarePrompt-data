#State of the program right berfore the function call: The input to the function func will consist of a positive integer n followed by a string s of length n containing only '+' or '-' characters, representing the n operations performed by Vasya.
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: `n` is a positive integer, `s` is a string of length `n` containing only '+' or '-' characters, `minus_count` is the number of '-' characters in `s`, `plus_count` is `n - minus_count`. If `minus_count` is higher than `plus_count`, the value 0 has been printed. Otherwise, the value `2 * plus_count - n` or `n - 2 * minus_count` has been printed.
#Overall this is what the function does:The function accepts two inputs, a positive integer `n` and a string `s` of length `n` containing only '+' or '-' characters. It calculates the difference between the number of '+' and '-' characters in `s`. If the number of '-' characters is greater than the number of '+' characters, it prints 0. Otherwise, it prints the difference between the counts of '+' and '-' characters, which is equivalent to `2 * plus_count - n` or `n - 2 * minus_count`. The function does not return any value; instead, it prints the calculated difference or 0 to the console, and the state of the program after execution will be that the input variables `n` and `s` have been utilized to produce this output, with `n` being a positive integer and `s` being a string of length `n` containing only '+' or '-' characters. The function does not handle potential edge cases such as non-integer or non-positive inputs for `n`, or strings `s` longer or shorter than `n` or containing characters other than '+' or '-', and it does not provide any error messages or handling mechanisms for such cases.

