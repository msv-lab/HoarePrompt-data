#State of the program right berfore the function call: n is a positive integer representing the length of the string s, and s is a string of length n consisting of only lowercase English letters.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input())
        s = raw_input()
        if (n <= 26) :
            result = n - len(set(s))
        else :
            result = -1
        #State of the program after the if-else block has been executed: *n is assigned the value of the input received from the user as an integer, s is a string of length n consisting of only lowercase English letters. If n is less than or equal to 26, result is a non-negative integer. If n is larger than 26, result is -1.
        print(str(result))
    #State of the program after the if block has been executed: *`n` is a positive integer representing the length of string `s`, `s` is a string of length `n` consisting of only lowercase English letters. If `n` is less than or equal to 26, the result is a non-negative integer. If `n` is larger than 26, the result is -1.
#Overall this is what the function does:The function `func` reads an integer `n` representing the length of a string `s` and the string `s` itself. If the length of `s` is less than or equal to 26, it calculates the difference between `n` and the number of unique characters in `s` and prints the result. If the length of `s` is greater than 26, it prints -1. The function does not return any value.

