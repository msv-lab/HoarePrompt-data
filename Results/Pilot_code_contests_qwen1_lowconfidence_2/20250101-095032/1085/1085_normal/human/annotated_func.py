#State of the program right berfore the function call: The input is a list of points where each point is represented as a tuple (xi, yi) and consists of integers. The length of the list is n (1 ≤ n ≤ 200,000) and for each point, the coordinates xi and yi satisfy |xi|, |yi| ≤ 10^9.
def func():
    n = int(raw_input())
    rows = {}
    cols = {}
    posi = {}
    for i in range(n):
        x, y = [int(t) for t in raw_input().split(' ')]
        
        if x in rows:
            rows[x] += 1
        else:
            rows[x] = 1
        
        if y in cols:
            cols[y] += 1
        else:
            cols[y] = 1
        
        if (x, y) in posi:
            posi[x, y] += 1
        else:
            posi[x, y] = 1
        
    #State of the program after the  for loop has been executed: `n` must be greater than 0; `cols` is a dictionary where each key `y` is associated with a value that is the count of occurrences of `y` across all iterations of the loop; `rows` is a dictionary where each key `x` is associated with a value that is the count of occurrences of `x` across all iterations of the loop; `posi` is a dictionary where each key `(x, y)` is associated with a value that is the count of occurrences of the pair `(x, y)` across all iterations of the loop; `x` and `y` are integers from the input; `i` is equal to `n`.
    ans = 0
    for t in rows.keys():
        ans = ans + (rows[t] - 1) * rows[t] / 2
        
    #State of the program after the  for loop has been executed: Output State: `ans` is the sum of \((rows[t] - 1) * rows[t] / 2\) for all keys `t` in `rows`, `cols` is a dictionary where each key `y` is associated with a value that is the count of occurrences of `y` across all iterations of the loop, `rows` is a dictionary where each key `x` is associated with a value that is the count of occurrences of `x` across all iterations of the loop, `posi` is a dictionary where each key `(x, y)` is associated with a value that is the count of occurrences of the pair `(x, y)` across all iterations of the loop, `i` is 0.
    for t in cols.keys():
        ans = ans + (cols[t] - 1) * cols[t] / 2
        
    #State of the program after the  for loop has been executed: `ans` is the sum of \((cols[t] - 1) * cols[t] / 2\) for all keys `t` in `cols`, `cols` is an empty dictionary, `rows` is a dictionary where each key `x` is associated with a value that is the count of occurrences of `x` across all iterations of the loop, `posi` is a dictionary where each key `(x, y)` is associated with a value that is the count of occurrences of the pair `(x, y)` across all iterations of the loop, `i` is the number of times the loop has executed.
    for t in posi.keys():
        if posi[t] > 1:
            ans -= (posi[t] - 1) * posi[t] / 2
        
    #State of the program after the  for loop has been executed: `ans` is the sum of \(-(posi[t] - 1) * posi[t] / 2)\ for all keys `t` in `posi` where `posi[t] > 1`, `i` is the number of times the loop has executed, `cols` is an empty dictionary, `rows` is an empty dictionary, and `posi` is a dictionary containing pairs `(x, y)` with counts of occurrences of such pairs.
    print(ans)
#Overall this is what the function does:The function accepts a list of points where each point is a tuple (xi, yi) with integer coordinates. It calculates and returns the number of unique pairs of points that share either the same x-coordinate or the same y-coordinate, without double-counting pairs. Specifically, it first counts the occurrences of each x-coordinate and y-coordinate. Then, it calculates the number of unique pairs for each x-coordinate (using the combination formula \( \frac{n(n-1)}{2} \) where n is the count of occurrences) and adds these to the total count. It then does the same for each y-coordinate. Finally, it subtracts the overcounted pairs (pairs that have both the same x-coordinate and the same y-coordinate) from the total count. The function prints and returns the resulting count. Potential edge cases include when the input list is empty, which would result in no pairs being counted. Additionally, the function assumes that the input list contains valid tuples with integer coordinates and that the coordinates are within the specified bounds.

