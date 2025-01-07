#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and s is a string of length n consisting of the characters '+' and '-' only.
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 <= `n` <= 100; `s` is a string of length `n` consisting of the characters '+' and '-' only. If `minus_count` is greater than `plus_count`, then 0 has been printed. Otherwise, `plus_count - minus_count` is a non-negative integer.
#Overall this is what the function does:The function accepts an integer `n` (1 <= n <= 100) and a string `s` of length `n` consisting of characters '+' and '-'. It counts the number of '+' and '-' characters in the string. If the number of '-' characters exceeds the number of '+' characters, the function prints `0`. Otherwise, it prints the difference between the count of '+' and '-' characters, which will be a non-negative integer. The function does not return any value; it only prints the results.

