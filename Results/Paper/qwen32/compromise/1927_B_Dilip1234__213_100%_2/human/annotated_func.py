#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5) representing the length of the lost string, and a is a list of n integers (0 ≤ a_i < n) representing the trace of the string. It is guaranteed that the sum of n over all test cases does not exceed 2 · 10^5, and for each test case, a valid string s exists that corresponds to the given trace.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: s is 'abcdefghijklmnopqrstuvwxyz', char_count is [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], i is n.
    return s
    #The program returns the string 'abcdefghijklmnopqrstuvwxyz'
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the length of the lost string, and `a`, a list of `n` integers representing the trace of the string. Regardless of the input values, the function always returns the string 'abcdefghijklmnopqrstuvwxyz'.

