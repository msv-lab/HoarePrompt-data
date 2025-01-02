#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (2 ≤ n ≤ 1000), representing the number of mines. The following n lines each contain two integers xi and yi (-10^9 ≤ xi, yi ≤ 10^9), representing the coordinates of each mine. All coordinates are distinct.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer between 2 and 1000, `maxx` is the maximum value among all `a` values entered by the user, `minx` is the minimum value among all `a` values entered by the user, `miny` is the minimum value among all `b` values entered by the user, `maxy` is the maximum value among all `b` values entered by the user, `z` is `t-1`, `a` is an integer entered by the user, `b` is an integer entered by the user.
    print(max(maxx - minx, maxy - miny)) ** 2
#Overall this is what the function does:The function reads an integer \( n \) representing the number of mines and \( n \) pairs of integers representing the coordinates of each mine from the standard input. It then calculates the maximum difference between the maximum and minimum \( x \)-coordinates (\( maxx - minx \)) and the maximum difference between the maximum and minimum \( y \)-coordinates (\( maxy - miny \)). Finally, it prints the square of the larger of these two differences.

