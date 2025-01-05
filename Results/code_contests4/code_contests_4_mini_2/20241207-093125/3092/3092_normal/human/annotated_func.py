#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100000, and s is a string of length n consisting only of lowercase English letters.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input())
        s = raw_input()
        if (n <= 26) :
            result = n - len(set(s))
        else :
            result = -1
        #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100000; `s` is the input string of length `n`. If `n` is less than or equal to 26, then `result` is calculated as the value of `n` minus the number of unique characters in `s`. If `n` is greater than 26, then `result` is set to -1.
        print(str(result))
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100000, and `s` is a string of length `n` consisting only of lowercase English letters. If the program is executed as the main module, `result` has been printed as a string. Otherwise, there are no actions taken.
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100000) and a string `s` of length `n` consisting only of lowercase English letters. If `n` is less than or equal to 26, it calculates the result as `n` minus the number of unique characters in `s` and prints this result. If `n` is greater than 26, it sets the result to -1 and prints it. The output is printed only when the function is executed as the main module.

