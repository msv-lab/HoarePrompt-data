#State of the program right berfore the function call: The input consists of the number of watchmen n (1 ≤ n ≤ 200 000) followed by n lines, each containing two integers xi and yi (|xi|, |yi| ≤ 109) representing the coordinates of the i-th watchman. Some positions may coincide.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `rows` is a dictionary where each key `x` maps to the number of times `x` appeared as the first coordinate, `cols` is a dictionary where each key `y` maps to the number of times `y` appeared as the second coordinate, `posi` is a dictionary where each key `(x, y)` maps to the number of times `(x, y)` appeared.
    ans = 0
    for t in rows.keys():
        ans = ans + (rows[t] - 1) * rows[t] / 2
        
    #State of the program after the  for loop has been executed: `ans` is the sum of \((\text{rows}[t] - 1) \times \text{rows}[t] / 2\) for all unique keys \(t\) in `rows`, `rows` is unchanged, `cols` is unchanged, and `posi` is unchanged.
    for t in cols.keys():
        ans = ans + (cols[t] - 1) * cols[t] / 2
        
    #State of the program after the  for loop has been executed: `ans` is the sum of \((\text{cols}[t] - 1) \times \text{cols}[t] / 2\) for all unique keys \(t\) in `cols`, `rows` remains unchanged, `cols` remains unchanged, `posi` remains unchanged.
    for t in posi.keys():
        if posi[t] > 1:
            ans -= (posi[t] - 1) * posi[t] / 2
        
    #State of the program after the  for loop has been executed: `ans` is the final value of `ans` after applying the adjustment for each key `t` in `posi.keys()` where `posi[t] > 1`, and `posi` is a dictionary where the value of each key `t` is decremented by 1 for every iteration where `posi[t] > 1`. If no iterations occur (i.e., all values in `posi` are initially <= 1), then `ans` remains unchanged and `posi` remains as the initial state.
    print(ans)
#Overall this is what the function does:The function reads the number of watchmen `n` and their coordinates `(xi, yi)` from the input. It then calculates the number of pairs of watchmen that can see each other horizontally and vertically, while also accounting for any watchmen that are positioned at the same coordinates. Specifically, the function:

1. Counts the occurrences of each horizontal and vertical position using dictionaries `rows` and `cols`.
2. Calculates the number of pairs of watchmen for each unique horizontal and vertical position using the formula \((\text{count} - 1) \times \text{count} / 2\).
3. Adjusts the count for positions where multiple watchmen are present, subtracting the overcounted pairs of watchmen that are positioned at the same coordinates.

After processing all watchmen, the function prints the total number of valid pairs of watchmen that can see each other either horizontally or vertically. The function handles the case where watchmen share the same coordinates by adjusting the count of such pairs.

