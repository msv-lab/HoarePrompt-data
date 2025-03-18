#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, m is an integer such that 1 ≤ m ≤ n, the second input line is a list of n integers each in the range {1, 2, ..., m}, and the third input line is a list of m integers k_1, k_2, ..., k_{m} such that 1 ≤ ∑_{i=1}^{m} k_{i} ≤ n.
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `m` is an integer such that 1 ≤ `m` ≤ `n`, `colors` is a list of colors, `color_counts` is a dictionary where each key is a unique color from the `colors` list and each value is the count of occurrences of that color in the `colors` list. If `colors` is empty, `color_counts` remains an empty dictionary.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `found` indicates whether a valid combination was found (True or False); `window_counts` contains the final counts of colors from the last checked range in the `colors` list.
    print('YES' if found else 'NO')
#Overall this is what the function does:The function accepts two integers `n` and `m`, along with a list of `n` integers representing colors and a list of `m` integers representing target counts for those colors. It checks if there exists a contiguous subsequence of colors that matches the specified counts of each unique color. If such a subsequence is found, it prints 'YES'; otherwise, it prints 'NO'. The function does not explicitly handle cases with invalid input ranges or empty lists, assuming inputs adhere to the constraints defined by the problem statement.

