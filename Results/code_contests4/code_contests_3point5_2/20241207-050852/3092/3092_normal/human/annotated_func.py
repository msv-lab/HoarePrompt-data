#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100,000. s is a string of length n consisting of only lowercase English letters.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input())
        s = raw_input()
        if (n <= 26) :
            result = n - len(set(s))
        else :
            result = -1
        #State of the program after the if-else block has been executed: *`n` is an input integer such that 1 <= n <= 100,000, `s` is a string of length n consisting of only lowercase English letters. If n <= 26, `result` is the difference between the total number of characters in the string `s` and the number of unique characters in the string `s`. If n > 26, `result` is -1.
        print(str(result))
    #State of the program after the if block has been executed: *n is an integer between 1 and 100,000, s is a string of length n with only lowercase English letters. If the condition __name__ == '__main__' is satisfied, the value of `result` is printed. Otherwise, no action is taken.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `s`, where `n` is between 1 and 100,000, and `s` is a string of lowercase English letters of length `n`. If `n` is less than or equal to 26, it calculates the difference between the total number of characters in the string `s` and the number of unique characters in `s` and prints the result. If `n` is greater than 26, it prints -1. The function does not explicitly return a value but performs the calculations and prints the result.

