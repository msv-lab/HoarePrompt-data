#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and s is a string of length n consisting of symbols "-" and "+".
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: *`s` is a string consisting of symbols "-" and "+"; if the count of '-' in `s` is greater than the count of '+' in `s`, then `0` is printed. Otherwise, the result of `plus_count - minus_count` is printed.
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 <= n <= 100) and a string `s` of length `n` consisting of symbols "-" and "+". It counts the occurrences of each symbol and prints `0` if there are more "-" symbols than "+" symbols. If there are equal or more "+" symbols than "-", it prints the difference between the count of "+" and "-" symbols. The function does not return any value; it only prints the result.

