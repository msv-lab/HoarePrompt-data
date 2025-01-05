#State of the program right berfore the function call: n and m are integers such that 1 <= n, m <= 10^3.**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function takes input for two integers n and m, prints a string of '10' repeated n//2 times followed by '1' if n is odd. The function does not accept any parameters explicitly and does not return any value.

