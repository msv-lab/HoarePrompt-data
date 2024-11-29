#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, m is an integer such that 1 ≤ m ≤ n, the second input line is a list of n integers where each integer is in the range {1, 2, ..., m}, and the third input line is a list of m integers k_1, k_2, ..., k_{m} such that 1 ≤ ∑_{i=1}^{m} k_{i} ≤ n.
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: If `colors` is empty, `color_counts` is an empty dictionary. If `colors` contains elements, `color_counts` contains keys representing unique colors and values representing the counts of those colors.
    found = False
    for i in range(n):
        window_counts = {}
        
        for j in range(i, n):
            color = colors[j]
            if color not in window_counts:
                window_counts[color] = 0
            window_counts[color] += 1
            if all(count == target for count, target in zip(sorted(window_counts.
                values()), counts)):
                found = True
                break
        
        if found:
            break
        
    #State of the program after the  for loop has been executed: `colors` remains either empty or contains elements; `color_counts` contains counts of colors; `found` is either True or False; `n` is the original value of `n`, `i` is at least 0 and less than `n`, `j` is at least `i` and less than `n`, and `window_counts` reflects the counts of colors from `colors[i]` to `colors[n-1]` for the last completed iteration, or remains unchanged if no matching counts were found. If `found` is True, it indicates that a matching count of colors was found during the iterations.
    print('YES' if found else 'NO')
#Overall this is what the function does:The function accepts two integers `n` and `m`, a list of `n` integers representing colors, and a list of `m` integers representing target counts of those colors. It checks if there exists a contiguous subarray of the color list that contains the exact count of colors specified in the counts list. If such a subarray is found, it prints 'YES'; otherwise, it prints 'NO'. The function assumes valid inputs based on specified constraints. However, it does not handle cases where the input lists are empty or do not conform to the specified integer ranges.

