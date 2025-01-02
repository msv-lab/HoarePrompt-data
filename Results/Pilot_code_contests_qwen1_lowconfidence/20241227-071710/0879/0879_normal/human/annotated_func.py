#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 10^5. The list a contains n non-decreasing integers representing the x-coordinates of cities, and the list b contains m non-decreasing integers representing the x-coordinates of cellular towers.
def func():
    n, m = map(int, raw_input().split())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    min_r = 0
    for el in a:
        i = bisect_left(b, el)
        
        if i == 0:
            min_r = max(min_r, abs(el - b[0]))
        elif i == m:
            min_r = max(min_r, abs(el - b[m - 1]))
        elif i == m - 1:
            min_r = max(min_r, min(abs(el - b[m - 1]), abs(el - b[m - 2])))
        else:
            min_r = max(min_r, min(abs(el - b[i + 1]), abs(el - b[i - 1]), abs(el -
                b[i])))
        
    #State of the program after the  for loop has been executed: `n` is the first integer input, `m` is the second integer input, `a` is a list of integers, `b` is a list of integers, and `min_r` is the maximum of the absolute differences between elements in `a` and their nearest neighbors in `b` under the specified conditions.
    print(min_r)
#Overall this is what the function does:The function accepts two positive integers `n` and `m` (both such that \(1 \leq n, m \leq 10^5\)), and two lists `a` and `b` (where `a` contains `n` non-decreasing integers and `b` contains `m` non-decreasing integers). It calculates the minimum radius `r` such that every city represented by an element in `a` can be covered by a cellular tower represented by an element in `b`. Specifically, for each city `el` in `a`, it finds the nearest cellular tower in `b` and determines the maximum distance `r` among these nearest distances. If a city has no suitable tower (i.e., it is beyond the first or last tower), it considers the nearest available tower. The function then prints this minimum radius `r`.

