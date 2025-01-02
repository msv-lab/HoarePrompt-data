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
        
    #State of the program after the  for loop has been executed: `a` must contain at least one element, `min_r` is the maximum difference found between any element in `a` and its closest element in `b` (considering both sides of the insertion point), and `i` is the index where each element in `a` would be inserted in `b` to maintain sorted order.
    print(min_r)
#Overall this is what the function does:The function calculates the minimum possible radius \(r\) for cellular towers such that every city (represented by elements in list `a`) is within distance \(r\) from at least one tower (represented by elements in list `b`). It achieves this by iterating through each city coordinate in `a` and finding its closest tower in `b` using binary search (via `bisect_left`). For each city, it checks the distances to the nearest towers on either side and updates `min_r` with the maximum of these distances. The function ultimately prints the value of `min_r`, which represents the minimum radius required to ensure coverage of all cities by the towers. Potential edge cases include scenarios where a city is exactly on the boundary between two towers or when a city is farthest from any tower.

