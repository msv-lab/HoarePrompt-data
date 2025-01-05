#State of the program right berfore the function call: n and m are integers representing the dimensions of a rectangular field, where 1 ≤ n, m ≤ 1000.
def func():
    n, m = map(int, sys.stdin.readline().split())
    print(n * m) / 2
#Overall this is what the function does:The function reads two integers `n` and `m` from input, which represent the dimensions of a rectangular field, and calculates half of the area of that field by computing `(n * m) / 2`. However, since the result of the calculation is printed without being returned, the function does not return any value. Additionally, the functionality does not handle any potential input errors or invalid values, and the output is simply printed rather than returned.

