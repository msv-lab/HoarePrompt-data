#State of the program right berfore the function call: The input consists of the number of mines n (2 ≤ n ≤ 1000) followed by n lines, each containing a pair of integers xi and yi representing the coordinates of a mine (-10^9 ≤ xi, yi ≤ 10^9). All coordinates are distinct.
def func():
    t = int(raw_input())
    maxx, maxy = -10 ** 18, -10 ** 18
    minx = 10 ** 18
    miny = 10 ** 18
    for z in xrange(t):
        a, b = map(int, raw_input().split())
        
        maxx = max(maxx, a)
        
        minx = min(minx, a)
        
        maxy = max(maxy, b)
        
        miny = min(miny, b)
        
    #State of the program after the  for loop has been executed: `n` is the number of mines (2 ≤ n ≤ 1000 and n > 0), `t` is equal to `n`, `maxx` is the maximum of `-10` and all the `a` values encountered, `minx` is the minimum of `10` and all the `a` values encountered, `miny` is the minimum of `10` and all the `b` values encountered, `a` and `b` are the last integer values from user input, `z` is `n - 1`.
    print(max(maxx - minx, maxy - miny)) ** 2
#Overall this is what the function does:The function processes the input consisting of the number of mines \( n \) (2 ≤ \( n \) ≤ 1000) followed by \( n \) lines, each containing a pair of integers \( x_i \) and \( y_i \) representing the coordinates of a mine (\(-10^9 \leq x_i, y_i \leq 10^9\)). The function calculates the maximum difference between the maximum and minimum \( x \)-coordinates and the maximum and minimum \( y \)-coordinates among the given mine coordinates. It then prints the square of the larger of these two differences. The function handles all valid inputs within the specified range and ensures that all coordinate pairs are distinct. However, it does not handle cases where the input format is incorrect or where the number of mines is outside the specified range.

