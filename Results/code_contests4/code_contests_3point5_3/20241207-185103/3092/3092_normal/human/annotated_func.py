#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100,000 and s is a string of length n consisting of only lowercase English letters.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input())
        s = raw_input()
        if (n <= 26) :
            result = n - len(set(s))
        else :
            result = -1
        #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100,000, `s` is a string of length `n` consisting of only lowercase English letters. If `n` is less than or equal to 26, then `result` is the difference between `n` and the number of unique characters in `s`. Otherwise, if `n` is greater than 26, then `result` is -1
        print(str(result))
    #State of the program after the if block has been executed: *`n` is an integer such that 1 <= n <= 100,000 and `s` is a string of length n consisting of only lowercase English letters. Depending on the values of `n` and the number of unique characters in `s`, the `result` will be computed accordingly and printed as a string.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `s` from the input. If the value of `n` is less than or equal to 26, it calculates the difference between `n` and the number of unique characters in the string `s` and prints the result. If `n` is greater than 26, it prints -1. The function does not have a return value. Edge cases to consider are when `n` is exactly 26 and when `s` contains all unique characters.

