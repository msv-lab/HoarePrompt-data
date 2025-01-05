#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 1000.**
def func():
    n, m = map(int, sys.stdin.readline().split())
    print(n * m) / 2
#Overall this is what the function does:The function reads two positive integers n and m from the standard input, then prints the result of (n * m) divided by 2. The function does not accept any parameters and does not return any value. However, the code has an issue with the print statement as it should be `print(n * m / 2)` instead of `print(n * m) / 2`.

