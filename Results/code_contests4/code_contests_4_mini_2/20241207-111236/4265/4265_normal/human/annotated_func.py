#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 1000.
def func():
    n, m = map(int, sys.stdin.readline().split())
    print(n * m) / 2
#Overall this is what the function does:The function accepts no parameters, reads two integers `n` and `m` from standard input, computes their product and divides it by 2, but incorrectly uses the print function which will lead to a TypeError. The intended output is the value of `(n * m) / 2`, but due to the erroneous print statement, the function does not return or print any usable result.

