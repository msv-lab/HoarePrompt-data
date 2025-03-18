#State of the program right berfore the function call: n, m, r, and k are integers such that 1 <= n, m <= 10^5, 1 <= r <= min(n, m), and 1 <= k <= min(n*m, 10^5).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function accepts four integer parameters (n, m, r, k) within specified ranges, calculates the minimum between k and the number of possible sub-grids of size r x r in an n x m grid, then prints the ratio of this minimum value to the total number of possible sub-grids of size r x r. The function's output represents the proportion of the grid's sub-grids that can be covered by k sub-grids, assuming each sub-grid can be of size r x r, and the sub-grids must be completely within the bounds of the larger grid. The function handles potential edge cases where k is greater than the total number of possible sub-grids, in which case it returns a value representing full coverage. The final state of the program after execution will be that the calculated ratio has been printed to the console, providing insight into how the given parameters (n, m, r, k) relate to the coverage of the grid's sub-grids.

