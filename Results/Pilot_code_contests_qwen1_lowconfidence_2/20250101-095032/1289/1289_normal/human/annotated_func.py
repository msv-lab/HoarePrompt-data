#State of the program right berfore the function call: The input is a list of pairs of integers representing the coordinates of the mines. The list has at least 2 elements and at most 1000 elements, and each coordinate (xi, yi) satisfies -10^9 ≤ xi, yi ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `maxx` is the maximum value of all `a` read from input, `maxy` is the maximum value of all `b` read from input, `minx` is the minimum value of all `a` read from input, `miny` is the minimum value of all `b` read from input, `z` is `t-1`, `t` must be greater than 0.
    print(max(maxx - minx, maxy - miny)) ** 2
#Overall this is what the function does:The function `func` accepts a list of pairs of integers representing the coordinates of the mines. It reads the number of pairs `t` and then iterates through each pair to find the maximum and minimum values of the x-coordinates and y-coordinates separately. After processing all pairs, it calculates the difference between the maximum and minimum values for both x-coordinates and y-coordinates, takes the larger of these two differences, squares it, and prints the result. The function does not return anything; instead, it outputs the calculated value directly. Potential edge cases include when the list of pairs is empty or contains only one pair, in which case the function should still process the input correctly.

