#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 10^5. The list ai contains n integers in non-decreasing order, representing the x-coordinates of cities. The list bj contains m integers in non-decreasing order, representing the x-coordinates of cellular towers.
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
        
    #State of the program after the  for loop has been executed: `a` is a non-empty list of integers in non-decreasing order, `b` is a list of integers in non-decreasing order that has been modified during the loop execution to include each element of `a` exactly once while maintaining the sorted order, `min_r` is the maximum absolute difference found during the loop execution between any element of `a` and its closest neighbors in `b`.
    print(min_r)
#Overall this is what the function does:The function accepts two positive integers `n` and `m` (with constraints 1 ≤ n, m ≤ 10^5), and two lists `a` and `b` containing `n` and `m` integers respectively, both in non-decreasing order. It calculates and prints the maximum absolute difference between any element in list `a` and its closest element in list `b`. The function iterates through each element in list `a`, finds the closest elements in list `b`, and updates the minimum radius (`min_r`) if a larger difference is found. If an element in `a` does not have a direct match in `b`, the function considers the nearest elements in `b` to calculate the difference.

