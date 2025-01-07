#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and s is a string of length n consisting of only the characters "-" and "+".
def func():
    n = int(input())
    s = input()
    minus_count = s.count('-')
    plus_count = s.count('+')
    if (minus_count > plus_count) :
        print(0)
    else :
        print(plus_count - minus_count)
    #State of the program after the if-else block has been executed: *`s` is a string consisting of "-" and "+"; if the count of '-' in `s` is greater than the count of '+' in `s`, then the function proceeds with that condition. Otherwise, the printed value is the non-negative difference between the count of '+' and the count of '-' in `s` (i.e., `plus_count - minus_count`).
#Overall this is what the function does:The function accepts a positive integer `n` (1 <= n <= 100) and a string `s` of length `n` containing only the characters '-' and '+'. It counts the occurrences of each character and prints `0` if there are more '-' characters than '+' characters. If there are more or an equal number of '+' characters than '-', it prints the difference between the counts of '+' and '-'. The function does not return any value; it solely prints results based on the input string.

