#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and s is a string of length n consisting only of the characters "-" and "+".
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 <= `n` <= 100, `s` is an input string of length `n` consisting only of the characters "-" and "+"; if the count of '-' in `s` is greater than the count of '+' in `s`, a value of 0 has been printed. Otherwise, the output value is `plus_count - minus_count`, where the count of '-' is less than or equal to the count of '+'.
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 <= n <= 100) and a string `s` of length `n` that consists only of the characters "-" and "+". It counts the occurrences of the "-" and "+" characters in the string. If the count of "-" is greater than the count of "+", it outputs 0. Otherwise, it outputs the difference between the count of "+" and the count of "-". The function does not return a value but prints the result directly. It does not handle cases where the input format is incorrect or where `n` does not match the length of `s`.

