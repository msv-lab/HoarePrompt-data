#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 ≤ a, b, c, d < n, and n is a positive integer (2 ≤ n ≤ 10^4).
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: '? [a] [b] [c] [d]' (where [a], [b], [c], and [d] are the respective values of the variables a, b, c, and d, which are non-negative integers less than n)
    return input()
    #The program returns an input value, which is a non-negative integer within the range [0, n), where n is a positive integer (2 ≤ n ≤ 10^4).
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters \(a\), \(b\), \(c\), and \(d\) within the range \([0, n)\), where \(n\) is a positive integer between 2 and \(10^4\). It prints these parameters and then returns an input value provided by the user, which is also a non-negative integer within the same range \([0, n)\).

