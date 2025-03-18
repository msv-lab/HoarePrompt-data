#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each testcase, s is a string consisting of lowercase Latin letters and/or question marks such that 1 ≤ |s| ≤ 5000. The total length of all strings s does not exceed 5000.
def func_1():
    s = list(input())
    n = len(s)
    for j in range(n // 2, 0, -1):
        count = 0
        
        for k in range(0, n - j):
            if s[k] == '?' or s[k + j] == '?' or s[k] == s[k + j]:
                count += 1
            else:
                count = 0
            if count == j:
                print(count * 2)
                return
        
    #State: Output State: The loop has executed all its iterations, and the output state is as follows:
    #
    #- `n` remains the same as its initial value, `N`.
    #- `j` is set to `J - 1` after the last iteration of the outer loop.
    #- `count` reflects the total number of times the conditions `s[k] == '?'`, `s[k + j] == '?'`, or `s[k] == s[k + j]` were true across all iterations of the loop. It is reset to 0 whenever it reaches `j`, at which point `count * 2` is printed and the function returns, effectively stopping the loop.
    #- The list `s` and the initial value of `t` remain unchanged from their initial states.
    #
    #In simpler terms, after the loop has run through all possible values of `j` starting from `n // 2` down to 1, `count` will hold the maximum value it reached before the loop terminated, and this value will have been doubled and printed. The value of `j` will be one less than the final value it took during the last iteration of the loop.
    print(0)
    #This is printed: 0
#Overall this is what the function does:The function `func_1` takes no parameters and does not return any value. It processes a string `s` consisting of lowercase Latin letters and/or question marks. The function checks for pairs of characters in the string that are either equal or both question marks, starting from the middle of the string and moving towards the beginning. For each possible pair distance (from half the string length down to 1), it counts how many such valid pairs exist. If it finds a valid pair distance where the count equals the distance, it prints the count doubled and exits. If no such distance is found, it prints 0.

