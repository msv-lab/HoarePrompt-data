#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that is the concatenation of the substring of 's' from index 0 to k (inclusive) repeated n times.
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from standard input, where \( 1 \leq n \leq 26 \) and \( 1 \leq k \leq 26 \). It then constructs and returns a string consisting of the substring of the predefined string \( s = 'abcdefghijklmnopqrstuvw' \) from index 0 to \( k \) (inclusive), repeated \( n \) times.

