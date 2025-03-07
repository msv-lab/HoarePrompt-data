#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 ≤ a, b, c, d < n, and n is a positive integer (2 ≤ n ≤ 10^4).
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? ? ? ? (where the first question mark is replaced by the value of `a`, the second by `b`, the third by `c`, and the fourth by `d`)
    return input()
    #The program returns an input value, which is a non-negative integer between 0 and n-1.
#Overall this is what the function does:The function `func_1` accepts four parameters \(a\), \(b\), \(c\), and \(d\), all of which are non-negative integers less than \(n\), where \(n\) is a positive integer between 2 and \(10^4\). After printing these values, the function waits for user input and returns a non-negative integer between 0 and \(n-1\).

