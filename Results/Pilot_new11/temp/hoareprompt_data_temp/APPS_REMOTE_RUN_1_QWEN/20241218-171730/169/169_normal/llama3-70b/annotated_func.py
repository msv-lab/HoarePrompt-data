#State of the program right berfore the function call: The variable n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n consisting only of '-' and '+' characters.
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: *`s` is a string entered by the user, `n` is the length of the string `s`, `minus_count` is the number of hyphens in the string `s`, `plus_count` is the number of plus signs in the string `s`. If the number of hyphens is greater than the number of plus signs, the function does not return anything (implying the value of `minus_count` remains unchanged). Otherwise, the value of `plus_count - minus_count` is printed.
#Overall this is what the function does:The function reads a positive integer \( n \) and a string \( s \) of length \( n \) consisting only of '-' and '+' characters. It then counts the number of hyphens and plus signs in the string. If the number of hyphens is greater than the number of plus signs, the function does not return anything. Otherwise, it prints the difference between the number of plus signs and the number of hyphens. The function accepts no parameters and does not modify the input string \( s \). Potential edge cases include when \( n \) is 1, where the function will either print 0 (if the character is '-'), or 1 (if the character is '+'). The function also ensures that \( n \) is within the range 1 to 100.

