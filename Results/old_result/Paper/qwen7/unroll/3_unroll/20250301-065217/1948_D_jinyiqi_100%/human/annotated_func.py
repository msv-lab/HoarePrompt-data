#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each testcase, s is a string consisting of lowercase Latin letters and/or question marks such that 1 ≤ |s| ≤ 5000. The total length of the strings over all testcases does not exceed 5000.
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
        
    #State: Output State: The output state depends on the input string `s`. The loop checks for substrings of length `j` where each character matches the corresponding character `j` positions ahead, allowing for '?' as a wildcard. If such a substring of length `j` is found, it prints `2 * j` and exits. Therefore, the output could be any even number between 2 and 2*n, depending on the input string, or nothing if no such substring exists.
    print(0)
    #This is printed: 0
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters and/or question marks. It checks for the longest substring where each character matches the character `j` positions ahead, allowing for '?' as a wildcard. If such a substring is found, it prints `2 * j` and exits. If no such substring exists, it prints `0`. The function does not return anything but prints the result directly.

