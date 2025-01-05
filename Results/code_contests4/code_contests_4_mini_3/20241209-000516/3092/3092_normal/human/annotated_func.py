#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and s is a string of length n consisting only of lowercase English letters.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input())
        s = raw_input()
        if (n <= 26) :
            result = n - len(set(s))
        else :
            result = -1
        #State of the program after the if-else block has been executed: *`n` is an integer within the range 1 to 100,000; if `n` is between 1 and 26, `result` is calculated as `n - len(set(s))`. Otherwise, for values of `n` greater than 26, `result` is set to -1.
        print(str(result))
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 100,000, and `s` is a string of length `n` consisting only of lowercase English letters. If `n` is between 1 and 26, the variable `result` is calculated as `n - len(set(s))`. If `n` is greater than 26, `result` is set to -1. The value of `result` is printed as a string.
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 100,000) and a string `s` of length `n` consisting only of lowercase English letters. If `n` is less than or equal to 26, it calculates and prints the difference between `n` and the number of unique characters in `s`. If `n` is greater than 26, it prints -1. The function does not handle cases where `n` is outside the specified range or where `s` contains characters outside the lowercase English letters.

