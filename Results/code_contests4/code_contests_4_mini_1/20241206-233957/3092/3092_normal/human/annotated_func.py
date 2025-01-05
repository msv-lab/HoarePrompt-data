#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100000, and s is a string of length n consisting of only lowercase English letters.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input())
        s = raw_input()
        if (n <= 26) :
            result = n - len(set(s))
        else :
            result = -1
        #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100000, and `s` is a string of length `n` consisting of only lowercase English letters. If `n` is less than or equal to 26, `result` is calculated as `n - len(set(s))`, which represents the difference between the length of `s` and the number of unique characters in `s`. Otherwise, if `n` is greater than 26, `result` is set to -1.
        print(str(result))
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100000, and `s` is a string of length `n` consisting of only lowercase English letters. If `n` ≤ 26, `result` is calculated as `n - len(set(s))`; if `n` > 26, `result` is set to -1.
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100000) and a string `s` of length `n` consisting of lowercase English letters. If `n` is less than or equal to 26, it calculates and prints the difference between `n` and the number of unique characters in `s`. If `n` is greater than 26, it prints `-1`. The function does not return any value but prints the result directly to the output.

