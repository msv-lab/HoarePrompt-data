#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each testcase, s is a string consisting of lowercase Latin letters and/or question marks such that 1 ≤ |s| ≤ 5000. The total length of all strings s does not exceed 5000.
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
        
    #State: Output State: `count` is 0, `j` is 0, `n` is greater than `j`.
    #
    #In Natural Language: After all iterations of the loop have finished, the value of `count` remains 0 because it never reached the value of `j` during any iteration. The value of `j` becomes 0 after the loop completes since the loop starts with `j` as `n // 2` and decrements `j` by 1 in each iteration until it reaches 0. The value of `n` remains unchanged and is still greater than `j` (which is now 0).
    print(0)
    #This is printed: 0
#Overall this is what the function does:The function processes a string `s` consisting of lowercase Latin letters and/or question marks. It checks for pairs of characters that are either equal or both question marks, starting from the middle of the string and moving towards the beginning. If it finds such a pair, it prints twice the length of the longest such sequence found and exits. If no such sequence is found, it prints 0. The function does not accept any parameters and does not return any value.

