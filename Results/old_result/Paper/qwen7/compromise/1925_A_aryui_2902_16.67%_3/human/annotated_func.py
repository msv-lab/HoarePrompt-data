#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that is the substring of 's' from the start up to the k-th character, repeated n times.
#Overall this is what the function does:The function reads two integers \(n\) and \(k\) from standard input, where \(1 \leq n \leq 26\) and \(1 \leq k \leq 26\). It then constructs and returns a string consisting of the first \(k\) characters of the string 'abcdefghijklmnopqrstuvw', repeated \(n\) times.

