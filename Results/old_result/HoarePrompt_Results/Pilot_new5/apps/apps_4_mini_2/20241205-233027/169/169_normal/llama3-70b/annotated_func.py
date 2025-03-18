#State of the program right berfore the function call: n is a positive integer (1 <= n <= 100), and s is a string of length n consisting of the characters '+' and '-'.
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: *`n` is a positive integer (1 <= n <= 100), `s` is a string of length `n` consisting of characters '+' and '-', `minus_count` is the count of '-' in `s`, `plus_count` is the count of '+' in `s`. If `minus_count` is greater than `plus_count`, the output is 0. Otherwise, the result of `plus_count - minus_count` is printed.
#Overall this is what the function does:The function accepts a positive integer `n` (1 <= n <= 100) and a string `s` of length `n` consisting of the characters '+' and '-'. It counts the occurrences of '-' and '+' in the string. If the count of '-' exceeds that of '+', it prints 0. Otherwise, it prints the difference between the counts of '+' and '-'.

