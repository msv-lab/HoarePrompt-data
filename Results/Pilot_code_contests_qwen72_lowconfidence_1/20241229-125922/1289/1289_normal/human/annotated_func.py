#State of the program right berfore the function call: The function `func` is expected to take a list of tuples as input, where each tuple represents the (x, y) coordinates of a mine. The list has a length n (2 ≤ n ≤ 1000), and each coordinate xi, yi satisfies -10^9 ≤ xi, yi ≤ 10^9. All coordinates are distinct.
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
        
    #State of the program after the  for loop has been executed: `maxx` is the maximum x-coordinate from all inputs, `minx` is the minimum x-coordinate from all inputs, `maxy` is the maximum y-coordinate from all inputs, `miny` is the minimum y-coordinate from all inputs, `t` is the number of inputs provided, `z` is `t - 1` if `t > 0`, otherwise `z` is 0, `a` and `b` are the last input integers if `t > 0`, otherwise `a` and `b` are undefined, `maxx` is at least `-10`, `minx` is at most `10`, `miny` is at most \(10^{18}\).
    print(max(maxx - minx, maxy - miny)) ** 2
#Overall this is what the function does:The function reads a series of (x, y) coordinate pairs from the standard input, where the number of pairs is specified by the first input integer `t`. It calculates the maximum and minimum x and y coordinates from these pairs. After processing all the coordinates, it computes the square of the larger of the two differences: (maximum x - minimum x) and (maximum y - minimum y). This squared value is then printed to the standard output. The function does not return any value; it only prints the result. If no coordinates are provided (`t == 0`), the function will still execute without error, but the values of `maxx`, `minx`, `maxy`, and `miny` will remain at their initial extreme values, leading to a printed result of \( (10^{18} + 10^{18})^2 \).

