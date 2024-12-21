#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and s is a string of length n consisting of only the symbols "+" and "-".
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 <= `n` <= 100, `s` is a string of length `n` consisting of only the symbols "+" and "-". If `minus_count` is greater than `plus_count`, the value printed is 0. Otherwise, the printed value is the difference between `plus_count` and `minus_count`.
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 ≤ n ≤ 100) and a string `s` of length `n` consisting solely of the symbols "+" and "-". It counts the occurrences of the "-" symbols and the "+" symbols in the string `s`. If the count of "-" symbols (`minus_count`) exceeds the count of "+" symbols (`plus_count`), it prints 0. Otherwise, it prints the difference between the count of "+" and "-" symbols, (`plus_count - minus_count`). The function ultimately ensures that the output is either 0 (if "-" symbols are more) or a non-negative integer representing the surplus of "+" symbols over "-" symbols. Note that there is no return statement; the output is printed directly. Additionally, the function lacks handling for invalid input scenarios, such as when the input string contains characters other than "+" or "-".

